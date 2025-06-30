# How to Write Automated Tests in Codex

> **Summary of Recent Changes (2025)**
> - Automated tests for all integrations and main modules.
> - Standardized use of pytest, mocks, and fixtures.
> - Full coverage of success, error, and API failure cases.
> - Updated examples according to modular architecture and structured logging.
> - Onboarding for new contributors reviewed.
> - Guide expanded with troubleshooting, continuous integration, and advanced tips.

---

## Why Test? (Quality Culture)
Automated tests ensure Codex evolves safely, making refactoring, new features, and external contributions easier. They:
- Prevent regressions and silent bugs.
- Allow the project to evolve without fear.
- Facilitate onboarding of new developers.
- Serve as living documentation of expected behavior.

---

## Test Structure in the Project
- All tests are in the `tests/` folder.
- Each test file starts with `test_` (e.g., `test_database.py`).
- Each test function also starts with `test_`.
- Use type hints and docstrings in test functions for clarity.
- Logging can be used in tests for advanced debugging.
- Separate tests by domain: database, integrations, CLI, suggestions, etc.

---

## Basic Example
```python
def test_sum() -> None:
    """Tests if basic sum works."""
    assert 1 + 1 == 2
```
This test checks if the sum is correct. If not, pytest shows an error.

---

## Testing Project Functions
See a real Codex example:
```python
def test_create_and_search_conversation(session):
    """Tests creation and search of a message in the database."""
    new_msg = database.Conversa(role='user', content='Pytest Test')
    session.add(new_msg)
    session.commit()
    results = database.buscar_no_historico(session, 'Test')
    assert any('Pytest Test' in msg.content for msg in results)
```
- **What does it do?** Creates a message in the database and tests if it can be found.
- **Why is it useful?** Ensures saving and searching in the database work.

---

## Testing External Tools (with Mocks)
Codex CLI has automated tests for all integrations with external APIs:
- Google Search
- Stack Overflow
- GitHub
- Wikipedia
- WolframAlpha

Use mocks to simulate API responses and ensure the code works even without real internet access.

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

> Well-written tests ensure the project's quality and safe evolution.
