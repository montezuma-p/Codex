# How to use the `ler_arquivo` tool in Codex

> **Summary of Recent Changes (2025)**
> - `ler_arquivo` tool modularized in `src/` with structured logging.
> - Automated tests and revised examples according to the new CLI.
> - Documentation and onboarding updated for new contributors.
> - Guide expanded with troubleshooting, continuous integration, and advanced tips.

---

## About this Guide
This document presents practical examples, tips, and troubleshooting for using the `ler_arquivo` tool in Codex CLI. It serves as a quick reference and onboarding for developers and advanced users.

- Always consult after modifying the tool or usage examples.
- Follow modularization, logging, and testing standards to ensure robustness.

---

## Troubleshooting and Tips
- If reading fails, check file permissions and if you are in the project directory.
- For questions about tests, see [como_escrever_testes.md](../pt/guia_didatico/como_escrever_testes.md).
- For continuous integration, see the Makefile and automation scripts.

---

## Onboarding for New Contributors
1. Always document improvements or changes to the tool in this guide.
2. Run automated tests to ensure coverage and robustness.
3. Consult this guide for examples of arguments and calls.
4. If in doubt, open an issue or request a PR review.

---

## What does it do?
- Reads text files (e.g., `.txt`, `.md`, `.py`, etc.) present in the project folder.
- Returns the file content safely, limiting the response to avoid huge prints.
- Informs if the file is empty or does not exist.

## Usage examples
- **User:** "Codex, read the file README.md"
- **Codex:**
  ```
  Content of 'README.md':
  # Codex – Learning with APIs, AI, and Project Automation
  ...
  ```

- **User:** "Show the content of teste_codex.txt"
- **Codex:**
  ```
  Content of 'teste_codex.txt':
  this is a Codex test
  ```

- **User:** "Read the file that does not exist"
- **Codex:**
  ```
  [ERROR]: File 'arquivo_que_nao_existe.txt' not found.
  ```
