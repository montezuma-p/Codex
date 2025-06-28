# Como usar a ferramenta `ler_arquivo` no Codex

A ferramenta `ler_arquivo` permite que o Codex leia e mostre o conteúdo de qualquer arquivo de texto do projeto diretamente pelo CLI.

## O que faz?
- Lê arquivos de texto (ex: `.txt`, `.md`, `.py`, etc) presentes na pasta do projeto.
- Retorna o conteúdo do arquivo de forma segura, limitando a resposta para evitar prints gigantes.
- Informa se o arquivo está vazio ou não existe.

## Exemplos de uso
- **Usuário:** "Codex, leia o arquivo README.md"
- **Codex:**
  ```
  Conteúdo de 'README.md':
  # Codex – Aprendizado com APIs, IA e Automação de Projetos
  ...
  ```

- **Usuário:** "Mostre o conteúdo de teste_codex.txt"
- **Codex:**
  ```
  Conteúdo de 'teste_codex.txt':
  isso é um teste do Codex
  ```

- **Usuário:** "Leia o arquivo que não existe"
- **Codex:**
  ```
  [ERRO]: Arquivo 'arquivo_que_nao_existe.txt' não encontrado.
  ```

## Observações
- O Codex só lê arquivos dentro do diretório do projeto.
- Arquivos muito grandes têm a resposta truncada para evitar excesso de texto.
- Para arquivos binários ou não-texto, a ferramenta pode retornar erro ou conteúdo ilegível.

Aproveite para explorar, revisar e automatizar tarefas lendo arquivos direto pelo Codex CLI!
