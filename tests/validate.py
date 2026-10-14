"""Valida il repo plugin: manifest JSON coerenti, .mcp.json, skill con frontmatter,
nessun segreto, ogni tool citato nelle skill esiste davvero nel server MCP."""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
MCP_URL = "https://seoautohub.com/api/mcp"
# Fonte: hub-backend/app/Http/Controllers/Api/V1/McpController.php
TOOLS = {"list_sites", "list_suggestions", "get_results", "run_audit", "mark_suggestion_done"}
errors = []


def need(cond, msg):
    if not cond:
        errors.append(msg)


def load(rel):
    p = ROOT / rel
    need(p.exists(), f"manca {rel}")
    return json.loads(p.read_text()) if p.exists() else {}


names = set()
for rel in (".claude-plugin/plugin.json", ".codex-plugin/plugin.json", ".cursor-plugin/plugin.json"):
    m = load(rel)
    need(m.get("name") == "seoautohub", f"{rel}: name deve essere seoautohub")
    need(re.fullmatch(r"\d+\.\d+\.\d+", m.get("version", "")), f"{rel}: version semver")
    need(m.get("license") == "MIT", f"{rel}: license MIT")
    names.add(m.get("version"))
need(len(names) == 1, f"versioni diverse tra manifest: {names}")

mk = load(".claude-plugin/marketplace.json")
need(any(p.get("name") == "seoautohub" for p in mk.get("plugins", [])), "marketplace: manca il plugin seoautohub")

mcp = load(".mcp.json")
srv = mcp.get("mcpServers", {}).get("seoautohub", {})
need(srv.get("url") == MCP_URL, ".mcp.json: url errato")
need("${SEOAUTOHUB_TOKEN}" in json.dumps(srv.get("headers", {})), ".mcp.json: il token deve venire da SEOAUTOHUB_TOKEN")

skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
need(len(skills) >= 4, f"servono almeno 4 skill, trovate {len(skills)}")
for s in skills:
    txt = s.read_text()
    fm = re.match(r"---\nname: (.+)\ndescription: (.+)\n---\n", txt)
    need(fm is not None, f"{s}: frontmatter name/description")
    if fm:
        need(fm.group(1) == s.parent.name, f"{s}: name != cartella")
    used = set(re.findall(r"`([a-z_]+)`", txt)) & {t for t in re.findall(r"`([a-z_]+)`", txt) if "_" in t}
    unknown = used - TOOLS - {"site_id", "suggestion_id", "focus_query", "suggested_title", "suggested_h1", "suggested_meta_description", "status", "processed_pages", "total_pages", "ai_pages"}
    need(not unknown, f"{s}: tool/campi sconosciuti {unknown}")
    need(re.search(r"mark_suggestion_done", txt) is None or "write" in txt, f"{s}: cita azioni senza spiegare lo scope write")

for rel in ("README.md", "LICENSE", "AGENTS.md", "connect/claude-code.md", "connect/cursor.md", "connect/codex.md", "connect/opencode.md"):
    need((ROOT / rel).exists(), f"manca {rel}")

for p in ROOT.rglob("*"):
    if p.is_file() and ".git" not in p.parts and p.name != "validate.py":
        need(not re.search(r"\b\d+\|[A-Za-z0-9]{30,}", p.read_text(errors="ignore")), f"{p}: sembra un token Sanctum")

if errors:
    print("\n".join("FAIL " + e for e in errors))
    sys.exit(1)
print(f"OK: {len(skills)} skill, 3 manifest, mcp.json")
