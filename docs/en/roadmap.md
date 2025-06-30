# Roadmap and Project Vision

> **Summary of Recent Changes (2025)**
> - Complete code modularization in `src/` (core, integrations, suggestions, database, etc) aiming for architectural PERFECTION.
> - Structured and centralized logging in all modules (`src/log_config.py`) for perfect traceability.
> - Automated tests with pytest and mocks for external integrations, seeking maximum coverage and reliability.
> - Build, test, and documentation automation via Makefile/scripts to ensure continuous excellence.
> - Onboarding and didactic documentation reviewed for new contributors, focusing on clarity and perfect learning.
> - Plugin/extension system in development for flexibility and perfect integration.
> - Updated examples and instructions for CLI and new tools, always focusing on perfect usability.
> - Dynamic agent response customization, perfectly adapting to the user's profile.

---

## Overview
The Codex roadmap guides the project's evolution, prioritizing PERFECTION, maximum quality, modularity, automation, and user/contributor experience as a reference in the open source ecosystem.

- **Focus on perfect architecture:** Clear separation of responsibilities, modularization, and excellence in extensibility.
- **Reference automation and testing:** Automated build, tests, and documentation ensure continuous quality and robustness.
- **Exemplary onboarding and community:** Didactic documentation, examples, and guides to facilitate contributions and raise the community standard.

---

## Current Features
- Stores conversations between user and AI in a SQLite database, with perfectly searchable history.
- Allows keyword search in the interaction history with precision and speed.
- Robust, didactic command-line interface (CLI), a reference in usability.
- Integration with Google's Gemini model for smart and perfect answers.
- Custom tools: file writing, history search, file listing and reading, all focused on excellence.
- Integration with external APIs:
  - Google Search (consultar_google)
  - Stack Overflow (consultar_stackoverflow)
  - Wikipedia (consultar_wikipedia)
  - GitHub (consultar_github)
  - WolframAlpha (consultar_wolframalpha)
- Automated tests with high coverage for all tools and integrations, seeking perfection.
- Didactic documentation and usage examples for each tool, always updated and clear.
- Agent responses can now be dynamically customized according to the user's profile (tone, examples, tips), ensuring perfect adaptation.

---

## Next Steps
- [ ] Add `--base-path` argument to customize the database/history location with perfect flexibility
- [ ] Support for plugins and custom integrations, with reference architecture
- [ ] Security improvements (history encryption, password protection) for perfect privacy
- [ ] Automate PyPI publication via GitHub Actions, ensuring an excellent CI/CD flow
- [ ] Add build/test badges for transparency and quality reference
- [ ] Improve usage examples as an API (FastAPI), making the project a reference in integration
- [ ] Internationalization (i18n) for a perfect experience in any language
- [ ] Allow advanced file manipulation (delete, move, rename) with security and perfection
- [ ] Enhance CLI with autocomplete, navigable history, and smart commands, seeking perfect usability
- [ ] Structure the code to facilitate the addition of new external integrations in an exemplary way
- [ ] Improve onboarding and interactive tips for new users, making the onboarding journey perfect
- [ ] Allow integration with other services (Docker, Trello, Notion, etc) transparently and perfectly
- [ ] Implement continuous learning and proactive suggestions based on usage, elevating the experience to perfection
- [ ] Generate automatic productivity and project evolution reports, with perfect visualization
- [ ] Implement dynamic agent response customization based on user profile (tone, examples, tips) for perfect interaction
- [ ] (Optional) Expandable web interface or desktop GUI, with a perfect user experience

---

## Troubleshooting and Tips
- See the [logbook](diario_de_bordo.md) for a history of decisions and problems solved with transparency and perfection.
- See usage and integration examples in [guia_didatico/auto_documentacao_ferramentas.md](guia_didatico/auto_documentacao_ferramentas.md), a reference for perfect auto-documentation.
- For questions about tests, see [guia_didatico/como_escrever_testes.md](guia_didatico/como_escrever_testes.md) and follow the standard of excellence.

---

## Onboarding for New Contributors
1. Read the README and this roadmap to understand the project's vision of PERFECTION.
2. See the examples and standards in `src/` and `tests/`, always seeking excellence.
3. Follow best practices for modularization, logging, and testing, raising the standard to perfection.
4. If in doubt, record it in the logbook or open an issue to keep the project's evolution perfect.

---

This document will be updated as the project evolves towards perfection.
