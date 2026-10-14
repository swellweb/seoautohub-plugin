---
name: ai-readiness
description: Check whether AI assistants can read and cite a site, from the latest SEO Automation Hub audit, and apply the fixes in the project (robots, llms.txt, structured data). Use for "GEO", "AI search", "can ChatGPT cite my site". Risponde nella lingua dell'utente.
---

# AI readiness

Reply in the user's language.

1. `list_sites`, pick the site. If it was never audited, offer `run_audit` first (write token).
2. `list_suggestions` with `status: all` and look for items about AI crawlers, `llms.txt`, structured data or robots rules.
3. Explain what is blocking AI assistants and where in the project the fix lives (robots.txt, headers, a plugin or security layer such as Cloudflare or a WAF can block crawlers even when robots.txt is open).
4. Apply only what the user confirms. After deploy, `run_audit` again and compare.
