# Politica De Privacidade Para Entrada Por Audio

A entrada por audio e um recurso pos-demo. A politica abaixo define o comportamento esperado antes de qualquer implementacao de gravacao, transcricao ou preenchimento automatico do Mapa de Alteridade.

## Estado Na Demo Streamlit

- A interface permite gravar uma nota de voz opcional com `st.audio_input`.
- O audio fica disponivel apenas na sessao local do Streamlit durante a interacao.
- A demo nao transcreve, nao persiste e nao usa o audio para analise automaticamente.
- O usuario deve revisar a gravacao e escrever a interacao no campo de texto antes de analisar.

## Principios

- Audio bruto nao deve ser salvo por padrao.
- O usuario precisa acionar a gravacao explicitamente.
- O usuario precisa revisar a transcricao antes da analise.
- A transcricao deve passar pelo mesmo fluxo de anonimizacao usado em texto.
- O diario deve armazenar apenas conteudo anonimizado e consentido.
- A interface deve explicar quando audio, transcricao e analise ficam apenas locais ou quando passam por API externa.

## Fluxo Esperado

1. Usuario clica em `Desabafar via audio`.
2. Navegador solicita permissao de microfone.
3. Usuario grava e encerra manualmente.
4. Backend transcreve o audio.
5. Audio bruto e descartado depois da transcricao, salvo se houver consentimento separado e finalidade explicita.
6. Usuario revisa a transcricao e os campos extraidos.
7. Somente depois da revisao o usuario executa a analise.
8. O diario salva apenas dados anonimizados quando houver consentimento local.

## Aviso De Interface Recomendado

`O audio sera usado apenas para gerar uma transcricao revisavel. Nao grave dados pessoais sensiveis. O diario salva somente conteudo anonimizado quando voce autorizar.`
