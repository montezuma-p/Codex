# Project Codex Logbook

> **Summary of Recent Changes (2025)**
> - Complete code modularization in `src/` (core, integrations, suggestions, database, etc).
> - Structured and centralized logging in all modules (`src/log_config.py`).
> - Automated tests with pytest and mocks for external integrations.
> - Build, test, and documentation automation via Makefile/scripts.
> - Onboarding and didactic documentation reviewed for new contributors.
> - Plugin/extension system in development.
> - Updated examples and instructions for CLI and new tools.
> - Dynamic agent response customization.
> - Expanded guide with troubleshooting, continuous integration, and advanced tips.

---

## About this Logbook
This document records progress, decisions, learnings, bugs, troubleshooting, and next steps in Codex development. It serves as a historical reference and onboarding for new contributors.

- Always consult before proposing structural changes.
- Record problems, solutions, and architectural decisions.
- Use dates and clear topics to facilitate future searches.

---

## Troubleshooting and Tips
- See the [roadmap](roadmap.md) for an overview and next steps.
- See integration and testing examples in [guia_didatico/como_escrever_testes.md](guia_didatico/como_escrever_testes.md).
- For questions about plugins/extensions, see the README and integration documentation.

---

## Onboarding for New Contributors
1. Read this logbook to understand the project's history and decisions.
2. Record any bug, solution, learning, or relevant decision here.
3. Follow the modularization, logging, and testing standards described in the guides.
4. If in doubt, open an issue or request a PR review.

---

## 2025-06-28
- We migrated the project interface from Flask (web) to CLI (command line), making Codex simpler, multiplatform, and easier to automate.
- Updated the README explaining the decision and removed Flask-related instructions.
- Tested the new CLI, which already allows conversations with the AI, file creation, and history search.
- Started planning to add automated tests with pytest and evolve Codex tools.

---

## 2025-06-28 (continued)
- Implemented smart suggestion functionality in the CLI: now, when starting a new interaction, Codex analyzes the history and automatically suggests the user's most frequent question or command. If the user presses Enter without typing anything, the suggestion is repeated automatically. This makes usage more practical and personalized, leveraging the agent's continuous learning.
- Added automated test to ensure the smart suggestion works.

---

## 2025-06-28 (continued 2)
- Added the `listar_arquivos` tool to Codex CLI, allowing the agent to perceive and list files and folders in the project directory. Now Codex can answer questions like "list the files in the docs folder" and show the actual file system content.
- Created didactic content in `docs/guia_didatico/percepcao_arquivos.md` explaining how file perception works and usage examples.
- Automated tests ensure the listing works correctly and safely.

---
