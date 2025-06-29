# Roadmap e Visão do Projeto

> **Sumário das Mudanças Recentes (2025)**
> - Modularização total do código em `src/` (core, integrações, sugestões, banco, etc).
> - Logging estruturado e centralizado em todos os módulos (`src/log_config.py`).
> - Testes automatizados com pytest e mocks para integrações externas.
> - Automação de build, testes e documentação via Makefile/scripts.
> - Onboarding e documentação didática revisados para novos contribuidores.
> - Sistema de plugins/extensões em desenvolvimento.
> - Exemplos e instruções atualizados para CLI e novas ferramentas.
> - Personalização dinâmica das respostas do agente.

---

## Visão Geral
O roadmap do Codex orienta a evolução do projeto, priorizando qualidade, modularidade, automação e experiência do usuário/contribuidor.

- **Foco em arquitetura limpa:** Separação clara de responsabilidades, modularização e extensibilidade.
- **Automação e testes:** Build, testes e documentação automatizados garantem qualidade contínua.
- **Onboarding e comunidade:** Documentação didática, exemplos e guias para facilitar contribuições.

---

## O que já faz
- Armazena conversas entre usuário e IA em um banco SQLite, com histórico consultável.
- Permite busca por palavras-chave no histórico de interações.
- Interface de linha de comando (CLI) robusta e didática.
- Integração com modelo Gemini da Google para respostas inteligentes.
- Ferramentas customizadas: escrita de arquivos, busca no histórico, listagem e leitura de arquivos.
- Integração com APIs externas:
  - Google Search (consultar_google)
  - Stack Overflow (consultar_stackoverflow)
  - Wikipedia (consultar_wikipedia)
  - GitHub (consultar_github)
  - WolframAlpha (consultar_wolframalpha)
- Testes automatizados com alta cobertura para todas as ferramentas e integrações.
- Documentação didática e exemplos de uso para cada ferramenta.
- Respostas do agente agora podem ser personalizadas dinamicamente conforme o perfil do usuário (tom, exemplos, dicas).

---

## Próximos Passos
- Permitir manipulação avançada de arquivos (deletar, mover, renomear).
- Aprimorar CLI com autocomplete, histórico navegável e comandos inteligentes.
- Estruturar o código para facilitar adição de novas integrações externas.
- Aprimorar onboarding e dicas interativas para novos usuários.
- Permitir integração com outros serviços (Docker, Trello, Notion, etc).
- Implementar aprendizado contínuo e sugestões proativas baseadas no uso.
- Gerar relatórios automáticos de produtividade e evolução dos projetos.
- Implementar personalização dinâmica das respostas do agente com base no perfil do usuário (adaptação de tom, exemplos e dicas).
- (Opcional) Interface web ou GUI desktop expansível.

---

## Troubleshooting e Dicas
- Consulte o [diário de bordo](diario_de_bordo.md) para histórico de decisões e problemas resolvidos.
- Veja exemplos de uso e integração em [guia_didatico/auto_documentacao_ferramentas.md](guia_didatico/auto_documentacao_ferramentas.md).
- Para dúvidas sobre testes, consulte [guia_didatico/como_escrever_testes.md](guia_didatico/como_escrever_testes.md).

---

## Onboarding para Novos Contribuidores
1. Leia o README e este roadmap para entender a visão do projeto.
2. Veja os exemplos e padrões em `src/` e `tests/`.
3. Siga as boas práticas de modularização, logging e testes.
4. Em caso de dúvida, registre no diário de bordo ou abra uma issue.

---

Este documento será atualizado conforme o projeto evoluir.
