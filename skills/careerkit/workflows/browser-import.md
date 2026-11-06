# Browser-assisted import (optional, opt-in)

The recommended route is the profile PDF (`pdf-import.md`). Offer the browser only as an alternative when the user prefers it and a connected browser tool actually exists.

For a user's **own profile**, offer a session-aware browser route when available. This is a strategy using host capabilities, **not** an embedded browser or a LinkedIn API.

1. Probe for a connected browser tool without inventing tool names. In Claude Code, suggest `/chrome` to check connectivity and `claude --chrome` if extension isn't enabled; Chrome integration has specific platform and account prerequisites. In Codex use whichever interactive browser/computer-use tools are actually installed; do not assume parity.
2. Before entering an authenticated LinkedIn tab, ask the user to authorize viewing their own profile through their current browser session. Do not request passwords, cookies, session tokens or control of another person's account.
3. Navigate to exact supplied URL in visible session. Read **only profile fields needed** (headline, About, employment titles/descriptions, skills, Featured, education, language). Expand 'see more' or scroll only if permitted; don't click send, connect, edit, apply, export contacts or message.
4. Capture field text and section coverage; log that source is `AUTH_BROWSER` and the access date. Read-only actions are the default.
5. If browser connection is absent, refuses access, CAPTCHA appears, or content is truncated, stop. Report what happened and switch to public discovery/PDF; never retry in a loop or suggest bypassing protection.
6. Do not persist complete profile contents, screenshots or personal information to repo/workspace unless user explicitly asks; redact when producing saved reports.

## Example diagnostic
- `AUTH_BROWSER AVAILABLE`: offer browser import with user permission.
- `AUTH_BROWSER UNAVAILABLE`: continue public fetch or document import.
- `AUTH_BROWSER FAILED`: explain reason and choose authorized fallback.
