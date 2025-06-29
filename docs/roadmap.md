# Roadmap e Visão do Projeto

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

## O que quero fazer (próximos passos)
- Permitir manipulação avançada de arquivos (deletar, mover, renomear).
- Aprimorar CLI com autocomplete, histórico navegável e comandos inteligentes.
- Estruturar o código para facilitar adição de novas integrações externas.
- Aprimorar onboarding e dicas interativas para novos usuários.
- Permitir integração com outros serviços (Docker, Trello, Notion, etc).
- Implementar aprendizado contínuo e sugestões proativas baseadas no uso.
- Gerar relatórios automáticos de produtividade e evolução dos projetos.
- (Opcional) Interface web ou GUI desktop expansível.

## [RESOLVIDO] Problemas de parsing e timeouts nas integrações externas
- As integrações com Google Search, Stack Overflow, Wikipedia, GitHub e WolframAlpha foram padronizadas e corrigidas.
- Argumentos validados, mensagens de erro e timeout uniformizadas.
- Testes práticos e automatizados confirmam a estabilidade.

## Visão de Futuro
O agente será uma espécie de "parceiro de pair programming", capaz de:
- Automatizar tarefas repetitivas e pesquisas técnicas.
- Gerenciar backlog e roadmap dos projetos.
- Ajudar a pesquisar soluções, integrar bibliotecas e resolver bugs.
- Gerar documentação técnica e exemplos de uso.
- Adaptar-se ao estilo de trabalho do usuário, aprendendo com o uso.

---

Este documento será atualizado conforme o projeto evoluir.
