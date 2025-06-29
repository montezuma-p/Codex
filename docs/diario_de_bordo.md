# Diário de Bordo do Projeto Codex

> **Sumário das Mudanças Recentes (2025)**
> - Modularização total do código em `src/` (core, integrações, sugestões, banco, etc).
> - Logging estruturado e centralizado em todos os módulos (`src/log_config.py`).
> - Testes automatizados com pytest e mocks para integrações externas.
> - Automação de build, testes e documentação via Makefile/scripts.
> - Onboarding e documentação didática revisados para novos contribuidores.
> - Sistema de plugins/extensões em desenvolvimento.
> - Exemplos e instruções atualizados para CLI e novas ferramentas.
> - Personalização dinâmica das respostas do agente.
> - Guia expandido com troubleshooting, integração contínua e dicas avançadas.

---

## Sobre este Diário
Este documento registra avanços, decisões, aprendizados, bugs, troubleshooting e próximos passos do desenvolvimento do Codex. Serve como referência histórica e onboarding para novos contribuidores.

- Consulte sempre antes de propor mudanças estruturais.
- Registre problemas, soluções e decisões de arquitetura.
- Use datas e tópicos claros para facilitar buscas futuras.

---

## Troubleshooting e Dicas
- Consulte o [roadmap](roadmap.md) para visão geral e próximos passos.
- Veja exemplos de integração e testes em [guia_didatico/como_escrever_testes.md](guia_didatico/como_escrever_testes.md).
- Para dúvidas sobre plugins/extensões, veja o README e a documentação de integrações.

---

## Onboarding para Novos Contribuidores
1. Leia este diário para entender o histórico e decisões do projeto.
2. Registre aqui qualquer bug, solução, aprendizado ou decisão relevante.
3. Siga os padrões de modularização, logging e testes descritos nos guias.
4. Em caso de dúvida, abra uma issue ou peça revisão no PR.

---

## 28/06/2025
- Migramos a interface do projeto de Flask (web) para CLI (linha de comando), tornando o Codex mais simples, multiplataforma e fácil de automatizar.
- Atualizamos o README explicando a decisão e removendo instruções relacionadas ao Flask.
- Testamos a nova CLI, que já permite conversar com a IA, criar arquivos e buscar no histórico.
- Iniciamos o planejamento para adicionar testes automatizados com pytest e evoluir as ferramentas do Codex.

---

## 28/06/2025 (continuação)
- Implementada funcionalidade de sugestão inteligente no CLI: agora, ao iniciar uma nova interação, o Codex analisa o histórico e sugere automaticamente a pergunta ou comando mais frequente do usuário. Se o usuário pressionar Enter sem digitar nada, a sugestão é repetida automaticamente. Isso torna o uso mais prático e personalizado, aproveitando o aprendizado contínuo do agente.
- Adicionado teste automatizado para garantir o funcionamento da sugestão inteligente.

---

## 28/06/2025 (continuação 2)
- Adicionada a ferramenta `listar_arquivos` ao Codex CLI, permitindo ao agente perceber e listar arquivos e pastas do diretório do projeto. Agora o Codex pode responder perguntas como "liste os arquivos da pasta docs" e mostrar o conteúdo real do sistema de arquivos.
- Criado conteúdo didático em `docs/guia_didatico/percepcao_arquivos.md` explicando como funciona a percepção de arquivos e exemplos de uso.
- Testes automatizados garantem que a listagem funciona corretamente e de forma segura.

---

## 28/06/2025 (continuação 3)
- Adicionada a ferramenta `ler_arquivo` ao Codex CLI, permitindo ao agente ler e mostrar o conteúdo de arquivos de texto do projeto. Documentação didática criada em `docs/guia_didatico/ler_arquivo.md`.
- Testes automatizados garantem o funcionamento correto e seguro da leitura de arquivos.

---

## 28/06/2025 (sessão de evolução e integração)
- Adicionadas e integradas as ferramentas externas: `consultar_stackoverflow`, `consultar_google`, `consultar_github`, `consultar_wolframalpha` ao Codex CLI, seguindo padrão modular.
- Atualizado o prompt mestre e toda a documentação para refletir as novas integrações.
- Criados testes automatizados para todas as ferramentas externas, cobrindo casos de sucesso, erro, falta de parâmetro e falha de API.
- Atualizados guias didáticos (`percepcao_arquivos.md`, `como_escrever_testes.md`, `pytest.md`, `ferramentas_externas.md`) para incluir exemplos e dicas de uso das novas integrações.
- Implementada função de documentação automática das ferramentas, gerando o arquivo `auto_documentacao_ferramentas.md` a partir do código.
- Automatizada a geração da documentação via comando CLI (`python cli_agent.py --doc-ferramentas`) e Makefile (`make doc-ferramentas`).
- Estruturado o código para facilitar futuras expansões, centralizando as ferramentas no dicionário `FERRAMENTAS`.
- Roadmap atualizado para refletir o novo escopo, próximos passos e visão de futuro do projeto.

---

## 28/06/2025 (sessão de padronização e testes práticos)
- Padronizado o tratamento de argumentos e erros em todas as integrações externas (Google, Stack Overflow, Wikipedia, GitHub, WolframAlpha):
    - Uso da função `_extrair_termo` para validar argumentos.
    - Mensagens uniformes para ausência de termo e timeouts.
    - Tratamento explícito de exceções e respostas de erro.
- Rodados todos os testes automatizados com sucesso (100% de aprovação).
- Testada a aplicação na prática, validando prompts e respostas para todos os fluxos principais e de erro.
- Confirmado que todas as interações (perguntas e respostas) são salvas no histórico do banco de dados.
- Pronto para push e próximos avanços.

---

## 28/06/2025 (alerta de má funcionabilidade)
- Identificadas falhas de funcionamento em algumas integrações externas:
    - Google Search, Stack Overflow e WolframAlpha podem retornar `[ERRO]: Nenhum termo informado para consulta` mesmo quando o termo é informado, dependendo do parsing do prompt ou resposta da IA.
    - Wikipedia pode retornar `[ERRO DA FERRAMENTA]: ... Read timed out ...` devido a instabilidades de rede ou limitação da API.
- Esses problemas serão tratados e corrigidos na próxima sessão. Fica registrado o alerta para acompanhamento.

---

## 28/06/2025 (alerta de má funcionabilidade resolvido)
- Problemas de parsing e timeouts nas integrações externas (Google, Stack Overflow, Wikipedia, GitHub, WolframAlpha) foram corrigidos:
    - Argumentos agora são validados e tratados de forma padronizada.
    - Mensagens de erro e timeout uniformizadas.
    - Testes práticos e automatizados confirmam a resolução.
- Issue correspondente marcada como resolvida no repositório.

---

## 29/06/2025 (personalização dinâmica e aprendizado contínuo)
- Implementada personalização dinâmica das respostas do agente: agora o Codex adapta o tom, exemplos e dicas conforme o perfil do usuário (temas, horários, volume de perguntas, preferências extraídas do histórico).
- Adicionada geração automática de perfil resumido do usuário via comando `python cli_agent.py --perfil-usuario`.
- Implementada exportação do histórico de interações em formato JSONL para fine-tuning futuro (`python cli_agent.py --exportar-jsonl`).
- Adicionada geração de relatório automático de uso/aprendizado (`python cli_agent.py --relatorio-uso`), mostrando perguntas mais frequentes, palavras recorrentes, horários de maior uso e total de interações.
- Aprimorada sugestão inteligente contextual: agora considera frequência, horário do dia e temas recentes do histórico, exibindo múltiplas sugestões ao usuário.
- Implementado resgate automático de contexto relevante do histórico para enriquecer as respostas do agente.
- Atualizados README, roadmap e documentação para refletir todas as novas funcionalidades de personalização e aprendizado contínuo.
- Todas as funções novas testadas e validadas em uso prático.

---

## Como usar este diário
- Registre aqui cada avanço, decisão importante, bug resolvido ou ideia para o futuro.
- Use datas para organizar as entradas.
- Isso ajuda a manter o histórico do projeto e facilita revisões e colaborações.

---

