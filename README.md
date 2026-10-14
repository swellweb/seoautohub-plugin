# SEO Automation Hub for AI IDEs

Use [SEO Automation Hub](https://seoautohub.com) from Claude Code, Cursor, Codex and OpenCode.

Other SEO connectors give your agent data to read. This one lets it close the loop on **your own site**:

1. read the prioritised title / H1 / meta suggestions from your audit;
2. change them in your code;
3. mark them done: the hub re-reads the **live page** to verify;
4. read the **measured** click change from your Search Console, with a verdict.

## Install

See `connect/` for your client. Short version for Claude Code:

```
/plugin marketplace add seoautohub/seoautohub-plugin
/plugin install seoautohub@seoautohub
```

You need a token (Settings → IDE and AI agent access) and a **Professional plan or higher** (trials included). The plugin is free and open source; access to your data is not.

## Tools

| Tool | Scope | What it does |
|---|---|---|
| `list_sites` | read | Your sites and audit status |
| `list_suggestions` | read | What to change, with reasoning and Search Console numbers |
| `get_results` | read | Clicks before/after, verdict per action |
| `run_audit` | write | Starts a fresh audit (one at a time per site) |
| `mark_suggestion_done` | write | Declares a change applied; verified on the live page |

## Skills

`audit-and-fix`, `find-ctr-opportunities`, `what-worked`, `ai-readiness`.

---

## Italiano

Usa SEO Automation Hub da Claude Code, Cursor, Codex e OpenCode. L'agente legge i consigli del tuo audit, modifica il codice, segna "fatto" (il hub verifica sulla pagina online) e legge l'effetto misurato sui tuoi click di Search Console.

Serve un token (Impostazioni → Accesso per IDE e agenti AI) e il piano Professional o superiore (prova inclusa). Guide in `connect/`.

## License

MIT
