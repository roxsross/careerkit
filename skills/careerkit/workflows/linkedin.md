# LinkedIn — source-based audit

Follow the source-first protocol in `../SKILL.md` and the decision matrix in `../references/source-policy.md`.

## Intake
Record target role, country, language, experience, source files/URL. Do NOT delay an audit asking for role goals when evidence is already enough: state assumptions and proceed.

## Retrieval failure — mandatory graceful fallback
If opening the supplied URL returns **Failed to fetch**, 403, 429, a login gate, a CAPTCHA, or an empty page:
1. Report exactly that the URL could not be retrieved. **Do not retry indefinitely**, bypass restrictions, ask for cookies, or silently switch to an unrelated profile.
2. If available and permitted, try **one** ordinary public web search with the exact profile URL or person's name to locate an official portfolio or other authoritative public pages. Record those as **external corroboration only**, never as proof of what LinkedIn displays. If search tools are unavailable, skip this step.
3. Look for profile material the user already attached or pasted (PDF, screenshot, résumé, LinkedIn headline/About/Experience). If found, use it, labeling it **user-provided**.
4. If headline, About and experience are still missing, set readiness to **INSUFFICIENT**. Do not run a fake complete audit, make up scores, or reconstruct the LinkedIn profile from search snippets.
5. Return a short and actionable handoff, in the user's language, with the intake block below. Do not claim LinkedIn itself is broken; the current agent's retrieval failed.

**Fallback answer template (Spanish):**
> No pude abrir tu LinkedIn desde este agente (`Failed to fetch`). El skill está cargado, pero no tengo suficiente contenido del perfil para auditarlo correctamente. Podés adjuntar el PDF que descargues de tu propio LinkedIn, pegar el texto o enviar capturas. No necesito tu contraseña ni tus cookies. Si querés empezar por lo esencial, compartí:
>
> - Titular actual:
> - Acerca de / About:
> - Experiencia reciente (cargo, empresa, período y logros):
> - Rol al que apuntás (opcional):
>
> Con eso puedo hacer la auditoría; identificaré las secciones que sigan sin estar disponibles.

## Evidence checks
- If URL available and web access possible, attempt actual retrieval; record visible sections, not snippets alone.
- With PDF, extract text, inspect document pages if text is incomplete, and note sections absent from the export.
- With user-supplied content, mark `user-provided`; it is sufficient for rewriting the text even if unverified externally.
- Check each notable factual assertion against provided text/source.

## Tiers
**FULL:** Headline + About + relevant experience visible. Deliver scoped full review and three headline variations, About, experience, prioritized skills if provided or suggestions clearly labeled, featured, recruiter inbound/outbound, 7-day plan.
**PARTIAL:** Only review observed parts; include coverage table. Draft only grounded content; ask for missing core sections once. Do not assign numerical SEO/recruiter scores.
**INSUFFICIENT:** Stop at useful triage. Explain retrieval limitations and exactly how to supply missing information. Provide a short copy-paste intake template; no fabricated complete About.

## Evidence-based writing
Use action → scope → outcome. No fake metrics. Avoid claims about opaque LinkedIn algorithm, exact keyword ranking, or predicted recruiting conversions. Label suggestions as proposed.
