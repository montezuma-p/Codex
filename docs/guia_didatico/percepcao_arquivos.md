# Como o Codex percebe e manipula arquivos e pastas

O Codex CLI agora possui uma ferramenta chamada `listar_arquivos`, que permite ao agente perceber e listar arquivos e pastas do diretório onde está instalado. Isso torna o Codex mais "agente" de verdade, pois ele pode interagir com o sistema de arquivos do projeto.

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

## Dica
Você pode pedir para o Codex listar qualquer pasta do projeto, facilitando a navegação, automação e integração com outras ferramentas!
