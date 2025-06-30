# How Codex Perceives and Handles Files and Folders

> **Summary of Recent Changes (2025)**
> - `listar_arquivos` tool modularized in `src/` with structured logging.
> - Automated tests and revised examples according to the new CLI.
> - Documentation and onboarding updated for new contributors.
> - Standardized external integrations and expanded examples.
> - Guide expanded with troubleshooting, continuous integration, and advanced tips.

---

## About this Guide
This document presents practical examples, tips, and troubleshooting for using the `listar_arquivos` tool in Codex CLI. It serves as a quick reference and onboarding for developers and advanced users.

- Always consult after modifying the tool or usage examples.
- Follow modularization, logging, and testing standards to ensure robustness.

---

## Troubleshooting and Tips
- If listing fails, check folder permissions and if you are in the project directory.
- For questions about tests, see [como_escrever_testes.md](../pt/guia_didatico/como_escrever_testes.md).
- For continuous integration, see the Makefile and automation scripts.

---

## Onboarding for New Contributors
1. Always document improvements or changes to the tool in this guide.
2. Run automated tests to ensure coverage and robustness.
3. Consult this guide for examples of arguments and calls.
4. If in doubt, open an issue or request a PR review.

---

## What does the tool do?
- Allows listing the contents of any project folder, e.g.: `docs`, `templates`, or even the project root.
- Returns the names of files and subfolders present in the requested directory.
- Informs if the folder is empty or does not exist.

## Usage examples
- **User:** "Codex, list the files in the docs folder"
- **Codex:**
  ```
  Contents of 'docs':
  diario_de_bordo.md
  guia_didatico
  proxima_missao.md
  roadmap.md
  ```

- **User:** "What files exist in the project root?"
- **Codex:**
  ```
  Contents of '.':
  cli_agent.py
  database.py
  README.md
  ...
  ```
