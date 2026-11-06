# Changelog

## [1.3.0] - 2026-11-06
- PDF export is now the default, recommended LinkedIn route (`workflows/pdf-import.md`).
- First reply includes PDF export steps when no profile content is provided.
- Public URL tried at most once per conversation; no retries after a failure.
- Public-presence preview while waiting for the PDF.
- Sections missing from the PDF (Featured, photo, banner) marked as "not in PDF", not empty.
- Authenticated browser import kept as an optional alternative.
- `.gitignore` excludes profile PDFs and LinkedIn data exports.

## [1.2.0] - 2026-11-06
- Browser-assisted import opt-in using available host tools; no bundled browser.
- Capability diagnosis `careerkit check`.
- Source labels and separate `PUBLIC_PRESENCE_REPORT` output.
- Clear LinkedIn fetch fallback, permission, privacy and evidence rules.
- Marketplace and Codex copy synchronization tests.
- Photo and career-transition workflows, guides and templates from 1.1.1 now live in `skills/careerkit/`.

## [1.1.1]
- Added fallback instructions for inaccessible LinkedIn URLs.
