# Global Contribution Guide – Codex CLI

Welcome! This guide brings together best practices, standards, and tips for contributing with excellence to Codex CLI.

---

## 1. Getting Started
- Read the [README.md](../README.en.md) and the [General Index](indice_geral.md) to understand the project's architecture and culture.
- Install dependencies:
  ```bash
  pip install -r requirements-dev.txt
  ```
- Run the tests:
  ```bash
  pytest
  ```

## 2. Code Standards
- Use type hints and docstrings in all functions/methods.
- Implement structured logging as in `src/log_config.py`.
- Separate code into clear modules: core, integrations, database, suggestions, etc.
- Follow modularization and extensibility standards.

## 3. Testing and Automation
- Create/update automated tests for every new feature or fix.
- Use mocks for external integrations.
- Run `make test` and check coverage.
- See the [Testing Guide](guia_didatico/como_escrever_testes.md).

## 4. Documentation
- Update the change summary in each affected document.
- Add examples and instructions in relevant guides.
- Update the [General Index](indice_geral.md) and [Visual Index](indice_visual.md) if necessary.
- Check the [PR Checklist](checklist_pr.md) before submitting.

## 5. Onboarding and Review
- Follow the onboarding in each guide.
- Request cross-review and use the PR checklist.
- Record decisions and learnings in the [Logbook](diario_de_bordo.md).

## 6. Integration with External Documentation Tools
- Use [MkDocs](https://www.mkdocs.org/) or [Sphinx](https://www.sphinx-doc.org/) to generate navigable documentation from markdown files.
- Generate automatic documentation for tools with:
  ```bash
  python cli_agent.py --doc-ferramentas
  ```
- Consider publishing the documentation on [Read the Docs](https://readthedocs.org/) or [GitHub Pages](https://pages.github.com/).

## 7. Final Tips
- Always check the visual index and PR checklist.
- Keep examples and instructions aligned with the current CLI and architecture.
- If in doubt, open an issue or request a review.

---

> **Contribute, learn, and help keep Codex CLI a reference in excellence, integration, and didactics!**
