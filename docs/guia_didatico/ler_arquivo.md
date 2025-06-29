# Como usar a ferramenta `ler_arquivo` no Codex

> **Sumário das Mudanças Recentes (2025)**
> - Ferramenta `ler_arquivo` modularizada em `src/` com logging estruturado.
> - Testes automatizados e exemplos revisados conforme nova CLI.
> - Documentação e onboarding atualizados para novos contribuidores.
> - Guia expandido com troubleshooting, integração contínua e dicas avançadas.

---

## Sobre este Guia
Este documento apresenta exemplos práticos, dicas e troubleshooting para uso da ferramenta `ler_arquivo` do Codex CLI. Serve como referência rápida e onboarding para desenvolvedores e usuários avançados.

- Consulte sempre após modificar a ferramenta ou exemplos de uso.
- Siga os padrões de modularização, logging e testes para garantir robustez.

---

## Troubleshooting e Dicas
- Se a leitura falhar, verifique permissões do arquivo e se está no diretório do projeto.
- Para dúvidas sobre testes, consulte [como_escrever_testes.md](como_escrever_testes.md).
- Para integração contínua, veja o Makefile e scripts de automação.

---

## Onboarding para Novos Contribuidores
1. Sempre documente melhorias ou mudanças na ferramenta neste guia.
2. Rode os testes automatizados para garantir cobertura e robustez.
3. Consulte este guia para exemplos de argumentos e chamadas.
4. Em caso de dúvida, abra uma issue ou peça revisão no PR.

---

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
