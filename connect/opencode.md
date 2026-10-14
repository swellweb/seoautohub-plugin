# OpenCode

Add to `opencode.json`:

```json
{
  "mcp": {
    "seoautohub": {
      "type": "remote",
      "url": "https://seoautohub.com/api/mcp",
      "headers": { "Authorization": "Bearer {env:SEOAUTOHUB_TOKEN}" }
    }
  }
}
```

Export `SEOAUTOHUB_TOKEN` with a token from **Settings → IDE and AI agent access**.
