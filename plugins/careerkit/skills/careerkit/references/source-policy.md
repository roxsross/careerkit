# Evidence & access policy

| Source | What it proves | What it does not prove |
|---|---|---|
| Visible LinkedIn page | Fields actually rendered during access | Hidden About, jobs, skills, current private profile |
| User-provided PDF | Text contained in this snapshot | Unexported Featured/Skills or changes since export |
| User-supplied copy | What user says their profile contains | Independent validation of job outcomes |
| Employer/public talk pages | Specific corroborated awards, talks, work | Exact text or layout of LinkedIn profile |
| Search snippet | A short publicly indexed excerpt | Full section contents |

For profile sections label `visible`, `partial`, `not accessible`, `not provided` or `user supplied`. A lack of visibility is NOT evidence of absence. Record extraction time when possible.

Suggested user prompt if insufficient:
"Pude ver [fields], pero no [fields]. Para una auditoría completa, compartime el PDF de tu perfil desde LinkedIn en escritorio (Más/Recursos → Guardar en PDF, si aparece) o pegá Titular, Acerca de y Experiencia. Podés ocultar datos privados. Mientras tanto puedo revisar solo lo que sí veo." 

Never request secrets, cookies, headless-login scripts, browser session exports, or unauthorized profile scraping. Prefer user-controlled exports and explicit consent.

## Failed-to-fetch behavior
A failed URL request proves only that the agent could not retrieve it during this attempt. It does not mean the LinkedIn profile is deleted, private, incomplete, or invalid. Do not scrape via third-party mirrors or unauthorized APIs. Ordinary search results may be used to corroborate a public credential, but must never be passed off as live LinkedIn fields. Use user-supplied PDF or pasted sections for the substantive profile audit.
