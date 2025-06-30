# Checklist de Revisão para Pull Requests (PR) – Codex CLI

Utilize este checklist para garantir que cada PR mantém o padrão de excelência, integração e clareza da documentação e do código do projeto.

---

## Checklist Geral
- [ ] O código segue o padrão de modularização (`src/`, integrações, core, etc)?
- [ ] Todos os métodos/funções possuem type hints e docstrings?
- [ ] O logging está implementado conforme `src/log_config.py`?
- [ ] Foram criados/atualizados testes automatizados para a nova feature/correção?
- [ ] O Makefile/scripts de automação foram atualizados se necessário?
- [ ] O README.md e os guias relevantes foram atualizados?
- [ ] O sumário de mudanças foi incrementado nos documentos afetados?
- [ ] Há exemplos de uso/documentação para novas ferramentas ou integrações?
- [ ] O onboarding para novos contribuidores está claro e atualizado?
- [ ] Troubleshooting e dicas foram revisados/adicionados?
- [ ] Links cruzados entre os guias/documentos foram verificados?
- [ ] O diário de bordo foi atualizado com decisões relevantes?

## Checklist Específico para Documentação
- [ ] O índice geral (`docs/indice_geral.md`) foi atualizado?
- [ ] O guia didático correspondente foi revisado?
- [ ] Exemplos e instruções refletem a arquitetura e CLI atuais?
- [ ] O sumário de mudanças está presente e atualizado?

## Checklist Específico para Integrações/Plugins
- [ ] Nova integração está em `src/integrations/`?
- [ ] Registrada no dicionário `FERRAMENTAS`?
- [ ] Documentada em `auto_documentacao_ferramentas.md`?
- [ ] Testes com mocks cobrindo casos de sucesso, erro e falha?

---

> **Dica:** Antes de aprovar um PR, peça revisão cruzada e garanta que todos os itens acima estejam marcados.
