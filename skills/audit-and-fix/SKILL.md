---
name: audit-and-fix
description: Run or read a SEO Automation Hub audit for a site, then apply the prioritised title/H1/meta changes directly in the project's code and mark them done so the hub verifies them on the live page. Use when the user says "audit my site", "fix the SEO suggestions", "apply the hub advice". Risponde nella lingua dell'utente.
---

# Audit and fix

Reply in the user's language.

1. Call `list_sites`. If several, ask which one; match the project's domain when obvious.
2. If the site has never been audited or the user asked for a fresh one, call `run_audit` (needs a `write` token). Audits can take from minutes to about an hour on large sites: re-check `list_sites` every few minutes, report `progress` (percent) and `processed_pages`/`total_pages` to the user, and continue only when `status` is no longer `processing`. If it returns "already running", just wait; never start a second one.
3. Call `list_suggestions` with `status: pending`. Work through them by `impressions`, highest first.
4. For each suggestion: find the page in the project (route, template, CMS field, or markdown front matter matching `url`). Show the user the current vs `suggested_title`, `suggested_h1`, `suggested_meta_description` and the `reasoning`. Apply the change only after the user agrees, or when they said to apply all.
5. Never invent text beyond the suggestion. If the suggestion does not fit the page's real content, say so and skip it.
6. After the change is deployed (not merely edited locally), call `mark_suggestion_done` with `suggestion_id`. The hub re-reads the live page: `detected` means confirmed, `unchanged` means the page online still shows the old text (deploy or cache), `unreachable` means retry later. Report the verdict honestly.

Do not call `mark_suggestion_done` for changes that are not live. It is a claim the hub will check.
