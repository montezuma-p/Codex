# Codex CLI External Tools: Usage Examples

> **Summary of Recent Changes (2025)**
> - All external integrations migrated to dedicated modules in `src/integrations/`.
> - Structured logging and standardized error handling in all tools.
> - Examples and instructions revised according to the new CLI and onboarding.
> - Automated tests with mocks for all integrations.
> - Documentation and tips updated for new contributor onboarding.
> - Guide expanded with troubleshooting, continuous integration, and advanced tips.

---

## About this Guide
This document presents practical examples, tips, and troubleshooting for using Codex CLI's external integrations. It serves as a quick reference and onboarding for developers and advanced users.

- Always consult after adding or modifying integrations.
- Examples reflect the real behavior of the CLI and APIs.
- Follow modularization, logging, and testing standards to ensure consistent integration.

---

## Troubleshooting and Tips
- If a tool does not work, check environment variables and dependencies in the README.
- For questions about tests, see [como_escrever_testes.md](../pt/guia_didatico/como_escrever_testes.md).
- For continuous integration, see the Makefile and automation scripts.

---

## Onboarding for New Contributors
1. Always document new integrations following the standard of the examples below.
2. Run automated tests to ensure coverage and robustness.
3. Consult this guide for examples of arguments and calls.
4. If in doubt, open an issue or request a PR review.

---

## consultar_google
Fetches the top 3 Google Search results for a term.

**Example:**
- User: "Codex, search Google for 'Python asyncio'"
- Codex:
  ```
  Google Search – Results for 'Python asyncio':
  - Python 3 asyncio documentation
  https://docs.python.org/3/library/asyncio.html
  ...
  - ...
  ```

## consultar_stackoverflow
Fetches the most relevant question and top-voted answer from Stack Overflow.

**Example:**
- User: "How do I make an HTTP request in Python?"
- Codex:
  ```
  Stack Overflow – How to make an HTTP request in Python?
  https://stackoverflow.com/q/123456
  Top-voted answer:
  ...
  ```

## consultar_github
Fetches relevant repositories and issues from GitHub.

**Example:**
- User: "Codex, search for repositories about 'machine learning'"
- Codex:
  ```
  GitHub – Found repositories:
  - scikit-learn
  - tensorflow
  ...
  ```

## consultar_wikipedia
Fetches the summary of a term from Wikipedia.

**Example:**
- User: "Codex, summarize 'Artificial Intelligence'"
- Codex:
  ```
  Wikipedia – Artificial Intelligence:
  ...
  ```

## consultar_wolframalpha
Answers math and science questions using WolframAlpha.

**Example:**
- User: "Codex, calculate the integral of x^2"
- Codex:
  ```
  WolframAlpha – Result:
  ...
  ```
