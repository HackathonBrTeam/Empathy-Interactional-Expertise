# Decisao De Evolucao Do Front-End

## Estado Atual

A interface atual permanece em Streamlit para a versao demonstrativa local. O Streamlit continua adequado para iteracao rapida, validacao do fluxo multiagente, diario local consentido e demonstracao do Mapa de Alteridade.

## Limitacoes Observadas

- Controle limitado sobre mobile-first e comportamento sticky fino.
- Componentes de formulario menos flexiveis para experiencias altamente guiadas.
- Customizacao de acessibilidade depende de CSS e convencoes internas do Streamlit.
- Experiencias avancadas, como gravacao de audio no navegador e preenchimento automatico do Mapa de Alteridade, exigem componentes customizados ou outro front-end.
- Layout e interacoes ainda podem parecer mais proximos de prototipo de dados do que de ferramenta SaaS de produtividade.

## Decisao

Manter Streamlit para a demo atual e adiar a migracao completa de front-end para uma fase pos-demo.

## Direcao Recomendada Para Pos-Demo

- Criar uma API Python com FastAPI para expor:
  - analise de interacao;
  - leitura, busca e exclusao do diario;
  - transcricao e extracao de contexto por audio.
- Criar front-end Vite + React.
- Usar TailwindCSS com Shadcn/ui ou Chakra UI.
- Hospedar o front-end em Vercel.
- Manter a engine de analise em Python como nucleo independente.

## Criterio Para Migrar

Migrar quando pelo menos um destes requisitos for prioritario:

- experiencia mobile-first polida;
- gravacao de audio nativa no navegador;
- componentes acessiveis com foco, ARIA e navegacao por teclado mais previsiveis;
- fluxo visual mais proximo de produto SaaS do que de prototipo;
- deploy web publico com front-end desacoplado.
