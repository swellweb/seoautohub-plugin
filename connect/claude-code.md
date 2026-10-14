# Claude Code

1. In SEO Automation Hub open **Settings → IDE and AI agent access**, create a token. Pick "Read and actions" if you want the agent to mark changes done and start audits.
2. Export it:

```bash
export SEOAUTOHUB_TOKEN="paste-your-token"
```

3. Install the plugin (skills + MCP together):

```
/plugin marketplace add seoautohub/seoautohub-plugin
/plugin install seoautohub@seoautohub
```

Or MCP only:

```bash
claude mcp add --transport http seoautohub https://seoautohub.com/api/mcp \
  --header "Authorization: Bearer $SEOAUTOHUB_TOKEN"
```

Requires the Professional plan or higher (or an active trial).
