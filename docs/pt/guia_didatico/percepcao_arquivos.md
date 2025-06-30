# Como o Codex percebe e manipula arquivos e pastas

> **Sumário das Mudanças Recentes (2025)**
> - Ferramenta `listar_arquivos` modularizada em `src/` com logging estruturado.
> - Testes automatizados e exemplos revisados conforme nova CLI.
> - Documentação e onboarding atualizados para novos contribuidores.
> - Integrações externas padronizadas e exemplos expandidos.
> - Guia expandido com troubleshooting, integração contínua e dicas avançadas.

---

## Sobre este Guia
Este documento apresenta exemplos práticos, dicas e troubleshooting para uso da ferramenta `listar_arquivos` do Codex CLI. Serve como referência rápida e onboarding para desenvolvedores e usuários avançados.

- Consulte sempre após modificar a ferramenta ou exemplos de uso.
- Siga os padrões de modularização, logging e testes para garantir robustez.

---

## Troubleshooting e Dicas
- Se a listagem falhar, verifique permissões da pasta e se está no diretório do projeto.
- Para dúvidas sobre testes, consulte [como_escrever_testes.md](como_escrever_testes.md).
- Para integração contínua, veja o Makefile e scripts de automação.

---

## Onboarding para Novos Contribuidores
1. Sempre documente melhorias ou mudanças na ferramenta neste guia.
2. Rode os testes automatizados para garantir cobertura e robustez.
3. Consulte este guia para exemplos de argumentos e chamadas.
4. Em caso de dúvida, abra uma issue ou peça revisão no PR.

---

## O que a ferramenta faz?
- Permite listar o conteúdo de qualquer pasta do projeto, por exemplo: `docs`, `templates`, ou mesmo a raiz do projeto.
- Retorna os nomes dos arquivos e subpastas presentes no diretório solicitado.
- Informa se a pasta está vazia ou se não existe.

## Exemplos de uso
- **Usuário:** "Codex, liste os arquivos da pasta docs"
- **Codex:**
  ```
  Conteúdo de 'docs':
  diario_de_bordo.md
  guia_didatico
  proxima_missao.md
  roadmap.md
  ```

- **Usuário:** "Quais arquivos existem na raiz do projeto?"
- **Codex:**
  ```
  Conteúdo de '.':
  cli_agent.py
  database.py
  README.md
  ...
  ```
