# Cursor

Add to `~/.cursor/mcp.json` (or the project's `.cursor/mcp.json`):

```json
{
  "mcpServers": {
    "seoautohub": {
      "url": "https://seoautohub.com/api/mcp",
      "headers": { "Authorization": "Bearer ${env:SEOAUTOHUB_TOKEN}" }
    }
  }
}
```

Create the token in **Settings → IDE and AI agent access** and export `SEOAUTOHUB_TOKEN`. Then ask: "list my SEO Automation Hub sites".
