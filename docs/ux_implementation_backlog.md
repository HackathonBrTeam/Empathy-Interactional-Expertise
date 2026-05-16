# Pendencias De Implementacao UX - EmpathyAI

Backlog derivado da analise cirurgica da interface atual. A ordem considera impacto em usabilidade, acessibilidade, clareza do fluxo e viabilidade de implementacao para demo/hackathon.

## P0 - Correcoes Criticas De UX E Acessibilidade

- [x] Garantir rotulos visiveis e persistentes em todos os campos do Mapa de Alteridade.
- [x] Remover dependencia de placeholders como instrucao principal dos campos.
- [x] Revisar contraste de placeholders, captions, textos secundarios e alertas para atender WCAG.
- [x] Adicionar icones ou semantica visual em mensagens de sucesso, alerta e erro.
- [x] Eliminar mistura EN/PT-BR na interface, resultados, diario e mensagens geradas pelo LLM.
- [x] Garantir que a ponte sugerida seja exibida somente no idioma selecionado ou detectado.

## P1 - Reorganizacao Do Fluxo Principal

- [x] Linearizar o formulario em uma sequencia vertical clara:
  - [x] Contexto do usuario.
  - [x] Contexto da outra pessoa.
  - [x] Fatores sensoriais ou contextuais.
  - [x] Interacao ou mensagem para analisar.
  - [x] Opcao de salvar no diario e feedback.
  - [x] Acao de analisar.
- [x] Reduzir a carga cognitiva do Mapa de Alteridade.
- [x] Tornar o botao "Analisar interacao" sempre facil de encontrar.
- [x] Avaliar botao fixo/sticky no rodape do formulario.
- [x] Evitar layout em duas colunas para campos que exigem preenchimento reflexivo.

## P2 - Melhor Experiencia Dos Resultados

- [x] Transformar "Ponte sugerida" no elemento principal da resposta.
- [x] Exibir a ponte em card destacado.
- [x] Aumentar a hierarquia visual da ponte sugerida.
- [x] Adicionar botao "Copiar resposta".
- [x] Separar claramente:
  - [x] Contexto percebido.
  - [x] Traducao de perspectiva.
  - [x] Ponte sugerida.
  - [x] Insight de aprendizagem.
  - [x] Status de privacidade ou diario.
- [x] Evitar blocos longos de texto sem escaneabilidade.

## P3 - Diario De Aprendizado Mutuo

- [x] Melhorar nome ou titulo automatico das entradas do diario.
- [x] Permitir busca ou filtro no diario.
- [x] Exibir resumo curto da interacao.
- [x] Exibir data e hora em formato local e amigavel.
- [x] Permitir exclusao de entrada diretamente no diario.
- [x] Deixar claro quando uma analise sera salva antes do envio.
- [x] Considerar etapa pos-analise: "Salvar esta ponte no diario".

## P4 - Entrada Por Audio / Wow Factor

- [x] Adicionar botao "Desabafar via audio" como entrada opcional na demo Streamlit.
- [x] Gravar audio no navegador com `st.audio_input`.
- [ ] Enviar audio para backend.
- [ ] Transcrever audio.
- [ ] Extrair automaticamente:
  - [ ] Interacao principal.
  - [ ] Perfil do usuario.
  - [ ] Possivel perfil da outra pessoa.
  - [ ] Fatores contextuais.
  - [ ] Apoios de reparacao.
- [ ] Preencher o Mapa de Alteridade automaticamente com os dados extraidos.
- [ ] Permitir revisao manual antes da analise.
- [x] Definir politica de privacidade especifica para audio. Ver `docs/audio_privacy_policy.md`.

## P5 - Evolucao Tecnica Da Interface

- [x] Avaliar limitacoes do Streamlit para experiencia mobile-first.
- [x] Decidir se o front-end continuara em Streamlit ou migrara.
- [ ] Se houver migracao:
  - [ ] Criar API Python com FastAPI.
  - [ ] Criar front-end Vite + React.
  - [ ] Usar TailwindCSS.
  - [ ] Usar Shadcn/ui ou Chakra UI.
  - [ ] Hospedar front-end na Vercel.
- [ ] Separar definitivamente UI, API e engine de analise.
- [x] Criar contrato HTTP para analise de interacao. Ver `docs/http_api_contracts.md`.
- [x] Criar contrato HTTP para diario. Ver `docs/http_api_contracts.md`.
- [x] Criar contrato HTTP para audio/transcricao. Ver `docs/http_api_contracts.md`.

## P6 - Acessibilidade Formal

- [ ] Revisar navegacao por teclado.
- [x] Garantir foco visivel nos campos e botoes.
- [x] Adicionar labels acessiveis em todos os inputs.
- [x] Evitar status comunicado apenas por cor.
- [x] Testar contraste minimo. Validado por `python scripts/check_ux_accessibility.py`.
- [ ] Validar leitura por screen reader.
- [ ] Revisar ordem de tabulacao.
- [ ] Garantir responsividade em telas pequenas.

Referencia de validacao manual: `docs/accessibility_validation.md`.

## P7 - Produto E Demo

- [x] Reduzir aparencia de formulario academico.
- [x] Aproximar a experiencia de uma ferramenta de produtividade.
- [x] Priorizar fluxo rapido: escrever ou desabafar, revisar, analisar, copiar ponte e salvar no diario.
- [x] Criar demo roteirizada com cenario corporativo.
- [x] Criar exemplos pre-preenchidos para apresentacao.
- [x] Documentar limitacoes conhecidas da versao Streamlit.
