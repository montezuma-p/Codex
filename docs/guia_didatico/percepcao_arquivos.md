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

## Segurança e testes
- O Codex só lista arquivos dentro do diretório do projeto, nunca acessa pastas do sistema.
- Nos testes automatizados, a função aceita um parâmetro especial para garantir que só o ambiente de teste seja manipulado.

## Outras ferramentas externas

O Codex CLI também integra APIs externas para potencializar sua experiência:

- **consultar_google**: Retorna os 3 primeiros resultados do Google Search para qualquer termo.
- **consultar_stackoverflow**: Busca perguntas e respostas técnicas diretamente do Stack Overflow.
- **consultar_github**: Mostra os repositórios mais populares sobre um termo no GitHub.
- **consultar_wolframalpha**: Responde perguntas matemáticas, científicas ou gerais usando o WolframAlpha.

### Exemplos de uso
- "Codex, pesquise no Google por 'Python asyncio'"
- "Como faço um request HTTP em Python? (Stack Overflow)"
- "Mostre repositórios sobre 'machine learning' no GitHub"
- "Quanto é a raiz quadrada de 144 no WolframAlpha?"

Veja exemplos detalhados em `ferramentas_externas.md`.

---

## Dica
Você pode pedir para o Codex listar qualquer pasta do projeto, facilitando a navegação, automação e integração com outras ferramentas!

Veja também: [Como usar a ferramenta ler_arquivo](ler_arquivo.md) para ler o conteúdo de arquivos de texto do projeto.
