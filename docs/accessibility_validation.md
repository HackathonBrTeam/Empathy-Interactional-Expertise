# Validacao De Acessibilidade Para Demo

Este registro consolida a revisao de acessibilidade do front-end Streamlit para a demo local. Ele nao substitui uma auditoria WCAG completa com ferramentas assistivas reais, mas define o que ja foi coberto e o que ainda precisa ser validado manualmente.

## Coberto Na Interface Atual

- Rotulos persistentes em todos os campos principais; placeholders ficam apenas como exemplos.
- Fluxo principal linear, com ordem de leitura vertical.
- Botao principal de analise visivel ao final do formulario e com comportamento sticky.
- Mensagens de sucesso com icone, evitando depender apenas da cor.
- Texto secundario e placeholders com contraste reforcado via `#595959`.
- Botao principal com gradiente escurecido para manter texto branco acima de 4.5:1 nas duas pontas.
- Estados de foco visiveis em campos de texto e seletores.
- Estados de foco ampliados para botoes, busca, radio, checkbox, expansores e entrada de audio.
- Resultados organizados em abas, com a ponte sugerida destacada primeiro.
- Diario com busca, titulos amigaveis, data local e acao de exclusao por entrada.

## Checklist Manual Antes Da Apresentacao

1. Navegar do seletor de idioma ate o botao `Analisar interacao` usando apenas `Tab` e `Shift+Tab`.
2. Confirmar que a ordem de foco acompanha a ordem visual: idioma, status local, cenario, campos do mapa, interacao, diario/feedback e acao principal.
3. Executar `python scripts/check_ux_accessibility.py` para validar tokens de contraste e invariantes basicos de layout.
4. Verificar que nenhum controle essencial fica oculto atras do botao sticky em telas pequenas.
5. Conferir a tela em largura reduzida, aproximadamente 390 px, para validar que os textos nao sobrepoem campos ou botoes.
6. Ler pelo menos o fluxo principal com NVDA, Narrator ou VoiceOver.
7. Confirmar que o botao `Copiar resposta` e anunciado como botao e que a ponte sugerida aparece antes dos detalhes.

## Riscos Restantes

- Streamlit controla parte do HTML interno; ARIA fino e ordem de tabulacao podem variar entre versoes.
- O componente HTML do botao de copiar depende da API do navegador para area de transferencia.
- A validacao de contraste cobre tokens criticos por script local, mas ainda nao substitui uma auditoria com captura real da pagina.
- A experiencia mobile-first continua limitada pelo Streamlit; uma migracao futura para React/Shadcn ou Chakra daria mais controle.
