# Roadmap e Visão do Projeto

> **Sumário das Mudanças Recentes (2025)**
> - Modularização total do código em `src/` (core, integrações, sugestões, banco, etc) visando PERFEIÇÃO arquitetural.
> - Logging estruturado e centralizado em todos os módulos (`src/log_config.py`) para rastreabilidade perfeita.
> - Testes automatizados com pytest e mocks para integrações externas, buscando cobertura e confiabilidade máximas.
> - Automação de build, testes e documentação via Makefile/scripts para garantir excelência contínua.
> - Onboarding e documentação didática revisados para novos contribuidores, com foco em clareza e perfeição no aprendizado.
> - Sistema de plugins/extensões em desenvolvimento para flexibilidade e integração perfeita.
> - Exemplos e instruções atualizados para CLI e novas ferramentas, sempre com foco em usabilidade perfeita.
> - Personalização dinâmica das respostas do agente, adaptando-se perfeitamente ao perfil do usuário.

---

## Visão Geral
O roadmap do Codex orienta a evolução do projeto, priorizando PERFEIÇÃO, qualidade máxima, modularidade, automação e experiência do usuário/contribuidor como referência no ecossistema open source.

- **Foco em arquitetura perfeita:** Separação clara de responsabilidades, modularização e extensibilidade de excelência.
- **Automação e testes de referência:** Build, testes e documentação automatizados garantem qualidade e robustez contínuas.
- **Onboarding e comunidade exemplar:** Documentação didática, exemplos e guias para facilitar contribuições e elevar o padrão da comunidade.

---

## O que já faz
- Armazena conversas entre usuário e IA em um banco SQLite, com histórico consultável de forma perfeita.
- Permite busca por palavras-chave no histórico de interações com precisão e velocidade.
- Interface de linha de comando (CLI) robusta, didática e referência em usabilidade.
- Integração com modelo Gemini da Google para respostas inteligentes e perfeitas.
- Ferramentas customizadas: escrita de arquivos, busca no histórico, listagem e leitura de arquivos, todas com foco em excelência.
- Integração com APIs externas:
  - Google Search (consultar_google)
  - Stack Overflow (consultar_stackoverflow)
  - Wikipedia (consultar_wikipedia)
  - GitHub (consultar_github)
  - WolframAlpha (consultar_wolframalpha)
- Testes automatizados com alta cobertura para todas as ferramentas e integrações, buscando perfeição.
- Documentação didática e exemplos de uso para cada ferramenta, sempre atualizados e claros.
- Respostas do agente agora podem ser personalizadas dinamicamente conforme o perfil do usuário (tom, exemplos, dicas), garantindo adaptação perfeita.

---

## Próximos Passos
- [ ] Adicionar argumento `--base-path` para customizar o local do banco de dados/histórico com flexibilidade perfeita
- [ ] Suporte a plugins e integrações customizadas, com arquitetura de referência
- [ ] Melhorias de segurança (criptografia do histórico, proteção por senha) para privacidade perfeita
- [ ] Automatizar publicação no PyPI via GitHub Actions, garantindo fluxo CI/CD de excelência
- [ ] Adicionar badges de build/testes para transparência e referência de qualidade
- [ ] Melhorar exemplos de uso como API (FastAPI), tornando o projeto referência em integração
- [ ] Internacionalização (i18n) para experiência perfeita em qualquer idioma
- [ ] Permitir manipulação avançada de arquivos (deletar, mover, renomear) com segurança e perfeição
- [ ] Aprimorar CLI com autocomplete, histórico navegável e comandos inteligentes, buscando usabilidade perfeita
- [ ] Estruturar o código para facilitar adição de novas integrações externas de forma exemplar
- [ ] Aprimorar onboarding e dicas interativas para novos usuários, tornando o início de jornada perfeito
- [ ] Permitir integração com outros serviços (Docker, Trello, Notion, etc) de forma transparente e perfeita
- [ ] Implementar aprendizado contínuo e sugestões proativas baseadas no uso, elevando a experiência à perfeição
- [ ] Gerar relatórios automáticos de produtividade e evolução dos projetos, com visualização perfeita
- [ ] Implementar personalização dinâmica das respostas do agente com base no perfil do usuário (adaptação de tom, exemplos e dicas) para interação perfeita
- [ ] (Opcional) Interface web ou GUI desktop expansível, com experiência de uso perfeita

---

## Troubleshooting e Dicas
- Consulte o [diário de bordo](diario_de_bordo.md) para histórico de decisões e problemas resolvidos com transparência e perfeição.
- Veja exemplos de uso e integração em [guia_didatico/auto_documentacao_ferramentas.md](guia_didatico/auto_documentacao_ferramentas.md), referência de auto-documentação perfeita.
- Para dúvidas sobre testes, consulte [guia_didatico/como_escrever_testes.md](guia_didatico/como_escrever_testes.md) e siga o padrão de excelência.

---

## Onboarding para Novos Contribuidores
1. Leia o README e este roadmap para entender a visão de PERFEIÇÃO do projeto.
2. Veja os exemplos e padrões em `src/` e `tests/`, buscando sempre excelência.
3. Siga as boas práticas de modularização, logging e testes, elevando o padrão à perfeição.
4. Em caso de dúvida, registre no diário de bordo ou abra uma issue para manter a evolução perfeita do projeto.

---

Este documento será atualizado conforme o projeto evoluir rumo à perfeição.
