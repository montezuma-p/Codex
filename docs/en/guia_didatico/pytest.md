# What is pytest?

> **Summary of Recent Changes (2025)**
> - Automated tests for all integrations and main modules.
> - Standardized use of pytest, mocks, and fixtures.
> - Full coverage of success, error, and API failure cases.
> - Updated examples according to modular architecture and structured logging.
> - Onboarding for new contributors reviewed.
> - Guide expanded with troubleshooting, continuous integration, and advanced tips.

---

## About this Guide
This document presents concepts, practical examples, tips, and troubleshooting for using `pytest` in Codex CLI. It serves as a quick reference and onboarding for developers and advanced users.

- Always consult after modifying tests or dependencies.
- Follow modularization, logging, and testing standards to ensure robustness.

---

## Troubleshooting and Tips
- If tests do not run, check dependencies and environment variables.
- For questions about API integration, see [como_escrever_testes.md](../pt/guia_didatico/como_escrever_testes.md).
- For continuous integration, see the Makefile and automation scripts.

---

## Onboarding for New Contributors
1. Always write new tests for each implemented feature.
2. Run all tests before each commit/push.
3. Consult this guide and [como_escrever_testes.md](../pt/guia_didatico/como_escrever_testes.md) for examples and standards.
4. If in doubt, open an issue or request a PR review.

---

## pytest and external APIs

In Codex CLI, we use pytest to test integrations with APIs such as Google Search, Stack Overflow, GitHub, and WolframAlpha. We use mocks to simulate API responses and ensure the code works even without real internet access.

- See examples of tests for external APIs in `tests/test_cli_agent.py`.
- To learn how to create your own mocks, see the pytest and unittest.mock documentation.

---

## Tip
Always run the tests before pushing changes! This way, you ensure all integrations keep working.
