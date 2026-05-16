# Roteiro De Demo - EmpathyAI

## Objetivo Da Demo

Mostrar como o EmpathyAI transforma um conflito comunicacional corporativo em uma ponte de conversa segura, acionavel e registrada no diario de aprendizado mutuo.

## Cenario Principal

Use o cenario pre-preenchido "Projeto com informacoes confusas".

Mensagem base:

> Minha colega de trabalho esta passando informacoes sobre o projeto de forma confusa e desorganizada.

## Passo A Passo

1. Abrir a aplicacao em `http://localhost:8501`.
2. Confirmar que a interface esta em `Portugues (Brasil)`.
3. Em "Cenario de demo", selecionar `Projeto com informacoes confusas`.
4. Clicar em `Carregar cenario`.
5. Mostrar que o Mapa de Alteridade foi preenchido automaticamente com:
   - contexto do usuario;
   - contexto da outra pessoa;
   - fatores da situacao;
   - apoios para reparacao.
6. Marcar `Salvar esta analise no diario de aprendizado mutuo`.
7. Selecionar um feedback, por exemplo `Util e segura`.
8. Clicar em `Analisar interacao`.
9. Apresentar a `Ponte sugerida` como valor principal.
10. Clicar em `Copiar resposta` para demonstrar uso imediato.
11. Abrir as abas:
    - `Contexto`;
    - `Perspectivas`;
    - `Aprendizagem`;
    - `Privacidade`.
12. Mostrar que a analise foi salva no diario.
13. No diario, demonstrar busca por `projeto` ou `prioridade`.

## Narrativa Sugerida

"Em vez de obrigar a pessoa a decidir quem esta certo ou errado, o EmpathyAI ajuda a transformar uma tensao comunicacional em uma ponte de entendimento. O Mapa de Alteridade registra contexto dos dois lados, a analise evita diagnostico ou culpa, e a ponte final pode ser copiada para uso imediato."

## Pontos De Atencao

- Evitar usar nomes reais, e-mails, telefones ou dados sensiveis.
- Explicar que a demo usa armazenamento local consentido.
- Explicar que a solucao nao substitui suporte clinico, juridico, de RH ou educacional especializado.
- Se o modelo local nao responder, demonstrar o fallback seguro.

## Plano B

Se houver instabilidade do LLM local:

1. Usar `python scripts/smoke_test.py` para validar o fluxo.
2. Demonstrar o resultado com fallback seguro.
3. Explicar que a arquitetura preserva privacidade local e tolera indisponibilidade do modelo.
