# Diário de Bordo do Projeto Codex

Este documento serve para registrar os avanços, decisões, aprendizados e próximos passos do desenvolvimento do Codex.

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

## Como usar este diário
- Registre aqui cada avanço, decisão importante, bug resolvido ou ideia para o futuro.
- Use datas para organizar as entradas.
- Isso ajuda a manter o histórico do projeto e facilita revisões e colaborações.

---

