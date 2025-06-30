# Next Mission

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

## Vision and Objective
This document details the next missions for Codex, prioritizing automation, AI, continuous integration, and user/contributor experience.

- Always consult the [roadmap](roadmap.md) for a macro view.
- Record ideas, experiments, and evolution plans here.

---

## Troubleshooting and Tips
- See integration and testing examples in [guia_didatico/como_escrever_testes.md](guia_didatico/como_escrever_testes.md).
- For questions about plugins/extensions, see the README and integration documentation.

---

## Onboarding for New Contributors
1. Read this document to understand the priorities and future vision.
2. Propose new missions aligned with the project's architecture and culture.
3. Follow the modularization, logging, and testing standards described in the guides.
4. If in doubt, open an issue or request a PR review.

---

## General Objective
Create a personal AI agent that acts as a programming assistant, automating tasks, managing projects, and learning from usage.

## Priority Steps

### 1. Improve Data Persistence
- **Task:** Expand the SQLite data model to include:
  - History of executed commands.
  - Logs of errors and actions performed.
- **Justification:** Allow the agent to learn from past interactions and improve its efficiency.

### 2. Expand Available Tools
- **Task:** Add new tools, such as:
  - Python script execution.
  - GitHub integration for automatic versioning.
  - Technical documentation generation.
- **Justification:** Make the agent more useful in the development cycle.

### 3. Enhance the Web Interface
- **Task:**
  - Add support for multiple users.
  - Create dashboards for viewing history and progress.
- **Justification:** Improve user experience and facilitate collaborative use.

### 4. Implement Continuous Learning
- **Task:**
  - Create a learning module that analyzes usage patterns and suggests improvements.
  - Integrate machine learning models for personalization.
- **Justification:** Make the agent smarter and more adaptable over time.

### 5. Integrate with External Services
- **Task:**
  - Connect the agent to APIs such as Docker, Jenkins, and CI/CD services.
  - Allow automated project deployment.
- **Justification:** Expand the agent's scope beyond the local environment.

## Short-Term Goals
- Complete implementation of file writing tools, history search, listing, and file reading.
- Ensure the agent maintains context between interactions.
- Document existing code and create detailed usage examples.

## Long-Term Goals
- Transform the agent into a complete pair programming partner.
- Automate repetitive tasks and manage project backlogs.
- Build a community around the project to receive feedback and contributions.

---

**Note:** This document will be updated as the project evolves.
