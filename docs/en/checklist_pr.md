# PR Checklist

Use this checklist to ensure every PR maintains the project's standards of excellence, integration, and clarity in both documentation and code.

---

## General Checklist
- [ ] Does the code follow the modularization standard (`src/`, integrations, core, etc)?
- [ ] Do all methods/functions have type hints and docstrings?
- [ ] Is logging implemented as in `src/log_config.py`?
- [ ] Are automated tests created/updated for the new feature/fix?
- [ ] Are the Makefile/automation scripts updated if necessary?
- [ ] Are the README.md and relevant guides updated?
- [ ] Is the change summary incremented in the affected documents?
- [ ] Are there usage examples/documentation for new tools or integrations?
- [ ] Is onboarding for new contributors clear and up to date?
- [ ] Have troubleshooting and tips been reviewed/added?
- [ ] Are cross-links between guides/documents verified?
- [ ] Is the logbook updated with relevant decisions?

## Documentation-Specific Checklist
- [ ] Is the general index (`docs/indice_geral.md`) updated?
- [ ] Is the corresponding didactic guide reviewed?
- [ ] Do examples and instructions reflect the current architecture and CLI?
- [ ] Is the change summary present and updated?

## Integrations/Plugins-Specific Checklist
- [ ] Is the new integration in `src/integrations/`?
- [ ] Registered in the `FERRAMENTAS` dictionary?
- [ ] Documented in `auto_documentacao_ferramentas.md`?
- [ ] Tests with mocks covering success, error, and failure cases?

---

> **Tip:** Before approving a PR, request cross-review and ensure all items above are checked.
