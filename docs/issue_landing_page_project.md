# Issue Draft: Create project landing page

## Context

Create a public-facing landing page for EmpathyAI that explains the project, shows the value proposition, and directs visitors to the controlled demo flow.

Branch: `landing-page-project`

## Goal

Build a concise, credible landing page that presents EmpathyAI as an AI-assisted communication mediation tool for transforming communication friction into safer, more actionable bridges of understanding.

The page should support the next deployment step: a protected public demo using VM + Ollama/Gemma4 + Streamlit.

## Proposed Scope

- Create a landing page entry point for the project.
- Present the project clearly in English first, with room for PT-BR/ES later.
- Explain the core idea without sounding academic or overloaded.
- Highlight:
  - communication mediation;
  - Alterity Map;
  - local-first/privacy-aware approach;
  - AI-assisted suggested bridge;
  - mutual learning diary;
  - controlled demo availability.
- Add a clear call to action for the protected demo.
- Link to project documentation or repository where appropriate.
- Keep the visual language aligned with the current EmpathyAI identity and Streamlit UX direction.

## UX Direction

- First viewport should make the product name and purpose immediately clear.
- Avoid a generic marketing page.
- Use the actual project/product as the hero signal.
- Keep content scannable and calm, suitable for people evaluating a communication-support tool.
- Avoid overpromising clinical, legal, HR, or educational advice.
- Make privacy boundaries visible but not alarming.

## Suggested Sections

- Hero: `EmpathyAI` + concise positioning.
- How it works: describe the flow in 3-4 steps.
- Core capabilities:
  - Alterity Map.
  - Suggested bridge.
  - Mutual learning diary.
  - Local/privacy controls.
- Demo status: explain controlled demo availability.
- Responsible-use note: communication support only, not specialized advice.
- CTA: request/access protected demo.

## Acceptance Criteria

- [ ] Landing page can be opened locally.
- [ ] Page has a clear hero with `EmpathyAI` as first-viewport signal.
- [ ] Page explains the product in plain English.
- [ ] Page includes a visible CTA for the controlled demo.
- [ ] Page includes responsible-use/privacy note.
- [ ] Page is responsive on desktop and mobile widths.
- [ ] Page avoids placeholder-only content.
- [ ] Page reuses or aligns with the existing visual identity.
- [ ] Basic accessibility checks pass: contrast, readable hierarchy, keyboard reachable CTA.

## Open Decisions

- [ ] Decide whether landing page is static HTML, Streamlit page, or future React/Vite page.
- [ ] Decide whether to include the current logo/assets.
- [ ] Decide destination for CTA: Streamlit demo URL, waitlist/contact, or GitHub repo.
- [ ] Decide whether PT-BR/ES translations are in scope for the first version.

## Validation

- [ ] Run local page/server.
- [ ] Check desktop viewport.
- [ ] Check mobile viewport.
- [ ] Check CTA behavior.
- [ ] Run available automated checks if implemented.

## How To Create This Issue On GitHub

After re-authenticating the GitHub CLI:

```powershell
gh auth login -h github.com
gh issue create --repo HackathonBrTeam/Empathy-Interactional-Expertise --title "Create project landing page" --body-file docs/issue_landing_page_project.md
```

Publish the branch when ready:

```powershell
git push -u origin landing-page-project
```

