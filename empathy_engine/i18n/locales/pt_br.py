UI_TRANSLATIONS = {
    "product_kicker": "Mediador cognitivo",
    "subtitle": "Mediação de comunicação com IA e controles locais de privacidade",
    "intro": (
        "Descreva um desencontro de comunicação. O sistema anonimiza o texto, "
        "processa em inglês e mostra uma possível ponte de entendimento."
    ),
    "notice": (
        "Esta ferramenta oferece apenas apoio de comunicação. Ela não fornece "
        "aconselhamento clínico, jurídico, de RH ou educacional especializado."
    ),
    "demo_scenario_heading": "Cenario de demo",
    "demo_scenario_intro": "Carregue um cenario corporativo preparado para apresentar o fluxo completo com mais rapidez.",
    "demo_scenario_select": "Cenario",
    "load_demo_scenario": "Carregar cenario",
    "demo_scenario_loaded": "Cenario de demo carregado. Revise os campos antes de analisar.",
    "alterity_heading": "Mapa de alteridade",
    "alterity_intro": (
        "Cadastre um contexto opcional sobre as duas pessoas antes da analise. "
        "Use papeis ou iniciais em vez de dados pessoais reais."
    ),
    "alterity_user_profile": "Seu perfil de comunicacao",
    "alterity_user_profile_placeholder": (
        "Exemplo: costumo ser direto, literal e breve quando estou sob pressao."
    ),
    "alterity_other_profile": "Possivel perfil de comunicacao da outra pessoa",
    "alterity_other_profile_placeholder": (
        "Exemplo: ela pode esperar mais acolhimento, contexto ou pistas emocionais."
    ),
    "alterity_context_factors": "Fatores sensoriais ou contextuais",
    "alterity_context_factors_placeholder": (
        "Exemplo: sala barulhenta, reuniao atrasada, cansaco, mensagem escrita sem tom."
    ),
    "alterity_repair_supports": "Apoios que podem reparar a troca",
    "alterity_repair_supports_placeholder": (
        "Exemplo: esclarecer a intencao, perguntar preferencia, oferecer proximo passo concreto."
    ),
    "alterity_help": (
        "Opcional. Estas notas entram na analise e seguem as mesmas regras de "
        "anonimizacao e armazenamento local da interacao."
    ),
    "step_user_context": "Etapa 1 - Seu contexto",
    "step_other_context": "Etapa 2 - Contexto da outra pessoa",
    "step_context_factors": "Etapa 3 - Situacao e apoios",
    "step_interaction": "Etapa 4 - Mensagem para analisar",
    "audio_input_heading": "Nota de voz opcional",
    "audio_input_intro": (
        "Grave um desabafo curto para ensaiar o futuro fluxo de audio para insight. "
        "Nesta demo, revise a gravacao e escreva a interacao abaixo antes de analisar."
    ),
    "audio_input_label": "Desabafar via audio",
    "audio_input_help": (
        "O navegador grava o audio e envia para esta sessao local do Streamlit. "
        "Transcricao automatica e extracao do mapa ficam planejadas para a API pos-demo."
    ),
    "audio_input_received": (
        "Audio recebido localmente. A transcricao automatica nao esta ativa nesta demo; "
        "use a gravacao como referencia e escreva a interacao abaixo."
    ),
    "local_status": "Status local",
    "status_model": "Modelo",
    "status_available": "disponivel",
    "status_unavailable": "indisponivel",
    "status_processing_language": "Idioma de processamento",
    "status_database": "Banco de dados",
    "learning_diary_heading": "Diario de aprendizado mutuo",
    "learning_diary_intro": (
        "Revise registros locais consentidos e as perguntas de reflexao geradas "
        "a partir de trocas anteriores."
    ),
    "learning_diary_count": "Registros exibidos no diario: {count}",
    "learning_diary_empty": (
        "Ainda nao ha entradas no diario. Ative o consentimento de armazenamento "
        "local antes de analisar uma interacao para salvar registros anonimizados."
    ),
    "learning_diary_record_title": "Entrada #{record_id} - {created_at}",
    "learning_diary_privacy_note": "Somente conteudo anonimizado e consentido aparece aqui.",
    "learning_diary_interaction": "Interacao anonimizada:",
    "learning_diary_bridge": "Ponte sugerida:",
    "learning_diary_reflection": "Pergunta de reflexao:",
    "learning_diary_feedback": "Feedback: {feedback}",
    "learning_diary_search": "Buscar no diario",
    "learning_diary_search_placeholder": "Busque por interacao, ponte ou reflexao",
    "learning_diary_no_results": "Nenhuma entrada do diario corresponde a esta busca.",
    "delete_diary_entry": "Excluir esta entrada",
    "diary_entry_deleted": "Entrada do diario excluida.",
    "no_feedback": "sem feedback",
    "delete_record_id": "ID do registro para excluir",
    "delete_selected_record": "Excluir registro local selecionado",
    "delete_all_records": "Excluir todos os registros locais",
    "deleted_records": "Registros excluidos: {count}",
    "ui_language": "Idioma da interface",
    "interaction_label": "Interação para analisar",
    "interaction_placeholder": (
        "Exemplo: Meu colega achou minha mensagem curta grosseira, mas eu "
        "estava tentando ser claro porque a reunião estava atrasada."
    ),
    "interaction_help": (
        "Evite usar dados pessoais reais em demos. Se incluir nomes, e-mails, "
        "telefones ou endereços, o workflow tentará mascará-los."
    ),
    "save_to_diary_heading": "Diario e feedback",
    "save_to_diary": "Salvar esta analise no diario de aprendizado mutuo",
    "save_to_diary_help": (
        "Com esta opcao marcada, a analise e salva localmente em versao anonimizada."
    ),
    "save_to_diary_note": (
        "O diario guarda apenas registros anonimizados e consentidos neste computador."
    ),
    "consent": "Salvar esta analise no diario de aprendizado mutuo",
    "consent_help": "Quando desmarcado, nenhuma interacao e salva no diario local.",
    "feedback": "Feedback da resposta",
    "feedback_options": ["Útil e segura", "Parcialmente útil", "Não útil"],
    "feedback_help": (
        "O feedback opcional só é armazenado se o consentimento local estiver marcado."
    ),
    "analyze": "Analisar interação",
    "missing_interaction": "Descreva uma interação antes de analisar.",
    "spinner": "Executando análise multiagente de empatia...",
    "success": "Possível ponte de empatia identificada.",
    "context_heading": "### Contexto",
    "context_text": (
        "O workflow encontrou um possível desencontro de expectativas de tom "
        "e pistas de comunicação."
    ),
    "language_note": (
        "Idioma detectado do usuário: {user_language}. Idioma de processamento: inglês."
    ),
    "translation_heading": "### Tradução de perspectiva",
    "for_user": "Para o usuário:",
    "for_other": "Para a outra pessoa:",
    "bridge_heading": "### Ponte sugerida",
    "bridge_card_label": "Ponte pronta para usar",
    "copy_response": "Copiar resposta",
    "result_tab_context": "Contexto",
    "result_tab_perspectives": "Perspectivas",
    "result_tab_learning": "Aprendizagem",
    "result_tab_privacy": "Privacidade",
    "learning_heading": "### Insight de aprendizagem",
    "privacy_heading": "### Privacidade",
    "stored": "Analise anonimizada salva no diario como entrada {record_id}.",
    "not_stored": "Esta analise nao foi salva no diario.",
    "save_after_analysis": "Salvar esta analise no diario",
    "saved_after_analysis": "Analise salva no diario como entrada {record_id}.",
}


OUTPUT_TRANSLATIONS = {
    (
        "The exchange is about project information that the user "
        "experiences as confusing or disorganized."
    ): (
        "A troca envolve informacoes de projeto que o usuario percebe como "
        "confusas ou desorganizadas."
    ),
    (
        "The other person may not realize which project details feel "
        "unclear, incomplete, or out of order."
    ): (
        "A outra pessoa talvez nao perceba quais detalhes do projeto parecem "
        "pouco claros, incompletos ou fora de ordem."
    ),
    (
        "The user may need the project information organized into "
        "clear points, priorities, and next steps."
    ): (
        "O usuario pode precisar que as informacoes do projeto sejam organizadas "
        "em pontos claros, prioridades e proximos passos."
    ),
    (
        "Which project information needs to be clarified first: "
        "priority, deadline, responsibility, or next step?"
    ): (
        "Qual informacao do projeto precisa ser esclarecida primeiro: "
        "prioridade, prazo, responsabilidade ou proximo passo?"
    ),
    "The other person may expect more emotional cues.": (
        "A outra pessoa pode esperar mais pistas emocionais."
    ),
    "Direct language may reflect efficiency, not hostility.": (
        "Linguagem direta pode refletir eficiência, não hostilidade."
    ),
    "What assumptions existed in this interaction?": (
        "Quais pressupostos existiam nesta interação?"
    ),
    (
        "Clarify intention, name the possible mismatch, and ask what "
        "would make the exchange easier for both people."
    ): (
        "Esclareça a intenção, nomeie o possível desencontro e pergunte "
        "o que tornaria a conversa mais fácil para ambas as pessoas."
    ),
    (
        "Frame outputs as possible interpretations, not diagnosis, "
        "fault, or behavioral normalization."
    ): (
        "Formule as saídas como interpretações possíveis, não como "
        "diagnóstico, culpa ou normalização comportamental."
    ),
    (
        "Frame outputs as possible interpretations, not diagnosis, fault, "
        "or behavioral normalization. For abuse, risk, legal, medical, or HR "
        "questions, state that the case needs appropriate human support."
    ): (
        "Formule as saídas como interpretações possíveis, não como diagnóstico, "
        "culpa ou normalização comportamental. Em casos de abuso, risco ou "
        "questões jurídicas, médicas ou de RH, indique que o caso precisa "
        "de apoio humano apropriado."
    ),
}
