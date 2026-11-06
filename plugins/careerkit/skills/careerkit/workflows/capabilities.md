# CareerKit check — capability diagnostic

Describe tooling, do not simulate it. Check only tools actually exposed to the agent.

| Capability | Report |
|---|---|
| Public URL fetch | available / unavailable / failed |
| Public web search | available / unavailable |
| Visible authenticated browser | available / unavailable / needs user authorization |
| Local PDF read | available / unavailable |
| Images/screenshots | available / unavailable |
| File output | available / unavailable |

For Chrome with Claude Code: `/chrome` can diagnose extension connection; `claude --chrome` starts Chrome-enabled session if prerequisites are met. Do not promise these work in other hosts. A diagnostic must not open private pages without permission. End with best route for the user.
