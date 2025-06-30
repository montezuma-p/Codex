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
