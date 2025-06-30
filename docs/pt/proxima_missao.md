# Próxima Missão

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

## Visão e Objetivo
Este documento detalha as próximas missões do Codex, priorizando automação, IA, integração contínua e experiência do usuário/contribuidor.

- Consulte sempre o [roadmap](roadmap.md) para visão macro.
- Registre aqui ideias, experimentos e planos de evolução.

---

## Troubleshooting e Dicas
- Veja exemplos de integração e testes em [guia_didatico/como_escrever_testes.md](guia_didatico/como_escrever_testes.md).
- Para dúvidas sobre plugins/extensões, veja o README e a documentação de integrações.

---

## Onboarding para Novos Contribuidores
1. Leia este documento para entender as prioridades e visão de futuro.
2. Proponha novas missões alinhadas à arquitetura e cultura do projeto.
3. Siga os padrões de modularização, logging e testes descritos nos guias.
4. Em caso de dúvida, abra uma issue ou peça revisão no PR.

---

## Objetivo Geral
Criar um agente de IA pessoal que atue como assistente de programação, automatizando tarefas, gerenciando projetos e aprendendo com o uso.

## Passos Prioritários

### 1. Melhorar a Persistência de Dados
- **Tarefa:** Expandir o modelo de dados no SQLite para incluir:
  - Histórico de comandos executados.
  - Logs de erros e ações realizadas.
- **Justificativa:** Permitir que o agente aprenda com interações passadas e melhore sua eficiência.

### 2. Ampliar as Ferramentas Disponíveis
- **Tarefa:** Adicionar novas ferramentas, como:
  - Execução de scripts Python.
  - Integração com GitHub para versionamento automático.
  - Geração de documentação técnica.
- **Justificativa:** Tornar o agente mais útil no ciclo de desenvolvimento.

### 3. Aprimorar a Interface Web
- **Tarefa:**
  - Adicionar suporte a múltiplos usuários.
  - Criar dashboards para visualização de histórico e progresso.
- **Justificativa:** Melhorar a experiência do usuário e facilitar o uso colaborativo.

### 4. Implementar Aprendizado Contínuo
- **Tarefa:**
  - Criar um módulo de aprendizado que analise padrões de uso e sugira melhorias.
  - Integrar modelos de machine learning para personalização.
- **Justificativa:** Tornar o agente mais inteligente e adaptável ao longo do tempo.

### 5. Integração com Serviços Externos
- **Tarefa:**
  - Conectar o agente a APIs como Docker, Jenkins e serviços de CI/CD.
  - Permitir deploy automatizado de projetos.
- **Justificativa:** Expandir o escopo de atuação do agente para além do ambiente local.

## Metas de Curto Prazo
- Finalizar a implementação das ferramentas de escrita de arquivos, busca no histórico, listagem e leitura de arquivos.
- Garantir que o agente mantenha contexto entre interações.
- Documentar o código existente e criar exemplos de uso detalhados.

## Metas de Longo Prazo
- Transformar o agente em um parceiro de pair programming completo.
- Automatizar tarefas repetitivas e gerenciar backlog de projetos.
- Criar uma comunidade em torno do projeto para receber feedback e contribuições.

---

**Nota:** Este documento será atualizado conforme o projeto evoluir.
