# Issue Draft: Registrar implementacoes de UX da branch ux-demo-readiness-streamlit

## Contexto

Esta issue registra o pacote de implementacoes realizado na branch `ux-demo-readiness-streamlit`, focado em deixar a demo Streamlit mais clara, apresentavel, acessivel e coerente com o fluxo do EmpathyAI.

Branch local de registro: `ux-demo-readiness-streamlit`

Commits locais:

- `4fd7bdc` - `Prepare Streamlit UX demo readiness`
- `a58b9f1` - `Add public demo issue draft`
- `b2f30ac` - `Document GitHub issue creation command`

## Implementacoes registradas

- Front-end Streamlit reorganizado para fluxo vertical e menor carga cognitiva.
- Mapa de Alteridade com rotulos persistentes e exemplos em placeholders.
- Cenarios de demo pre-preenchidos para acelerar apresentacao.
- Diario de aprendizado mutuo com busca, titulos amigaveis, data/hora local, exclusao e exibicao localizada.
- Correcoes de idioma para reduzir mistura EN/PT-BR/ES na interface e no diario.
- Ponte sugerida destacada como resultado principal, com botao de copiar.
- Entrada opcional de audio com `st.audio_input`, sinalizada como recurso de demo sem transcricao automatica.
- Melhorias de acessibilidade: contraste, foco visivel, feedback nao dependente apenas de cor e script de checagem.
- Documentacao criada para backlog UX, validacao de acessibilidade, contratos HTTP futuros, privacidade de audio, roteiro de demo e decisao de evolucao do front-end.

## Arquivos principais

- `app/streamlit_app.py`
- `empathy_engine/presentation/alterity_map.py`
- `empathy_engine/presentation/demo_scenarios.py`
- `empathy_engine/presentation/learning_diary.py`
- `empathy_engine/i18n/language.py`
- `empathy_engine/i18n/locales/en.py`
- `empathy_engine/i18n/locales/pt_br.py`
- `empathy_engine/i18n/locales/es.py`
- `scripts/check_ux_accessibility.py`
- `docs/ux_implementation_backlog.md`
- `docs/accessibility_validation.md`
- `docs/audio_privacy_policy.md`
- `docs/demo_script.md`
- `docs/frontend_evolution_decision.md`
- `docs/http_api_contracts.md`

## Validacoes executadas

- `python -m pytest`: 50 passed.
- `python scripts/smoke_test.py`: 3 cenarios ok.
- `python scripts/check_ux_accessibility.py`: ok.
- `python scripts/check_streamlit.py`: ok em `http://localhost:8501`.

## Como criar esta issue no GitHub

Depois de reautenticar o GitHub CLI:

```powershell
gh auth login -h github.com
gh issue create --repo HackathonBrTeam/Empathy-Interactional-Expertise --title "Registrar implementacoes de UX da branch ux-demo-readiness-streamlit" --body-file docs/issue_ux_demo_readiness_streamlit.md
```

Opcionalmente, publique a branch antes:

```powershell
git push -u origin ux-demo-readiness-streamlit
```

