# LinkedIn evidence workflow

## Stage 1 — Gather
- Read user supplied data if present; never demand a PDF when a valid pasted About/experience is already available.
- Follow `browser-import.md` for opt-in access to own authenticated session when tooling supports it.
- Try exact public URL once using available web tools, not curl loops or spoofed headers. Tool output `Failed to fetch` is **not** evidence the profile contains no information.
- If blocked, use search tools if available. Query exact profile URL / name + verifiable associated organization. Prefer official speaker, employer, certifications and personal site. Resolve same-name ambiguity before attributing.
- Do not infer current headline/experience from snippets or external bio. These are evidence only for `PUBLIC_PRESENCE_REPORT`.

## Stage 2 — Coverage and evidence ledger
Create a compact matrix for Headline, About, Experience, Skills, Featured, Education, Languages. Each row: `observed via LinkedIn` / `user-provided` / `external only` / `unavailable`, date/source, and uncertainty.

## Stage 3 — Decide output
- `FULL_AUDIT`: headline + About + substantive experience from profile or user export. Audit, three headlines, About rewrite, job bullets grounded in facts, prioritized skills, featured/photo guidance, outreach, 7-day plan.
- `PARTIAL_AUDIT`: audit observed portions, rewrites ONLY for sections supported; highlight absent sections.
- `PUBLIC_PRESENCE_REPORT`: offer useful external professional positioning report, with verified strengths and keyword hypotheses. State clearly that it is NOT an audit of LinkedIn fields. Ask for profile text/PDF to finish.
- `INSUFFICIENT`: explain missing access/tools and ask for minimal input; can still give actionable checklist.

Do not create precise subjective scores or fabricated metrics. If citing sources, cite actual URLs or provided file references in host's format.

## Stage 4 — Deliver
Follow `templates/audit.md`. Do not make up any access capability or claim successful reading of pages not read.
