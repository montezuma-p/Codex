# Como Escrever Testes Automatizados no Codex

> **Sumário das Mudanças Recentes (2025)**
> - Testes automatizados para todas as integrações e módulos principais.
> - Uso de pytest, mocks e fixtures padronizados.
> - Cobertura total de casos de sucesso, erro e falha de API.
> - Exemplos atualizados conforme arquitetura modular e logging estruturado.
> - Onboarding para novos contribuidores revisado.
> - Guia expandido com troubleshooting, integração contínua e dicas avançadas.

---

## Por que Testar? (Cultura de Qualidade)
Testes automatizados garantem que o Codex evolua com segurança, facilitando refatorações, novas features e contribuições externas. Eles:
- Evitam regressões e bugs silenciosos.
- Permitem evoluir o projeto sem medo.
- Facilitam onboarding de novos desenvolvedores.
- Servem como documentação viva do comportamento esperado.

---

## Estrutura dos Testes no Projeto
- Todos os testes ficam na pasta `tests/`.
- Cada arquivo de teste começa com `test_` (ex: `test_database.py`).
- Cada função de teste também começa com `test_`.
- Use type hints e docstrings em funções de teste para clareza.
- Logging pode ser usado em testes para depuração avançada.
- Separe os testes por domínio: banco, integrações, CLI, sugestões, etc.

---

## Exemplo Básico
```python
def test_soma() -> None:
    """Testa se a soma básica funciona."""
    assert 1 + 1 == 2
```
Esse teste verifica se a soma está correta. Se não estiver, o pytest mostra um erro.

---

## Testando Funções do Projeto
Veja um exemplo real do Codex:
```python
def test_criar_e_buscar_conversa(session):
    """Testa criação e busca de mensagem no banco."""
    nova_msg = database.Conversa(role='user', content='Teste Pytest')
    session.add(nova_msg)
    session.commit()
    resultados = database.buscar_no_historico(session, 'Teste')
    assert any('Teste Pytest' in msg.content for msg in resultados)
```
- **O que faz?** Cria uma mensagem no banco e testa se ela pode ser encontrada.
- **Por que é útil?** Garante que salvar e buscar no banco funcionam.

---

## Testando Ferramentas Externas (com Mocks)
O Codex CLI possui testes automatizados para todas as integrações com APIs externas:
- Google Search
- Stack Overflow
- GitHub
- WolframAlpha

### Exemplo de teste para API externa
```python
from unittest.mock import patch, MagicMock

@patch("cli_agent.requests.get")
def test_consultar_google_sucesso(mock_get, monkeypatch):
    """Testa integração com Google Search usando mock."""
    from cli_agent import consultar_google
    mock_resp = MagicMock()
    mock_resp.json.return_value = {"items": [{"title": "Python", "link": "https://python.org", "snippet": "..."}]}
    mock_resp.status_code = 200
    mock_get.return_value = mock_resp
    monkeypatch.setenv("GOOGLE_SEARCH_API_KEY", "fake-key")
    monkeypatch.setenv("GOOGLE_SEARCH_CX", "fake-cx")
    resultado = consultar_google(termo="python")
    assert "Python" in resultado
```
- Use mocks para simular respostas das APIs e garantir testes rápidos e confiáveis.

---

## Parametrização e Fixtures Avançadas
Use `@pytest.mark.parametrize` para testar múltiplos casos:
```python
import pytest
@pytest.mark.parametrize("entrada,esperado", [(1,2), (2,3), (3,4)])
def test_incrementa(entrada, esperado):
    assert entrada + 1 == esperado
```
Crie fixtures customizadas para preparar ambientes temporários:
```python
import pytest
@pytest.fixture
def arquivo_temp(tmp_path):
    arquivo = tmp_path / "exemplo.txt"
    arquivo.write_text("conteúdo de teste")
    return arquivo
```

---

## Lógica dos Testes
1. **Preparação:** Crie o que precisa (ex: uma mensagem, um arquivo, etc).
2. **Ação:** Execute a função que quer testar.
3. **Verificação:** Use `assert` para checar se o resultado está certo.
4. **Limpeza:** (Opcional) Remova arquivos ou dados temporários.

---

## Boas Práticas e Dicas
- Sempre cubra casos de sucesso, erro, falta de parâmetro e falha de API.
- Use nomes claros e docstrings nas funções de teste.
- Separe os testes por arquivo conforme o módulo (ex: banco, ferramentas, CLI).
- Use fixtures do pytest para preparar ambientes temporários (ex: banco de dados em memória).
- Use logging para depuração em testes complexos.
- Veja exemplos completos em `tests/test_cli_agent.py`.

---

## Integração Contínua e Automação
- Rode todos os testes antes de cada commit/push.
- Use o Makefile: `make test` para rodar todos os testes.
- Gere relatórios de cobertura: `pytest --cov=.`
- Integre com CI/CD (ex: GitHub Actions) para garantir qualidade contínua.

---

## Troubleshooting (Erros Comuns)
- **ImportError:** Verifique se o PYTHONPATH inclui a raiz do projeto.
- **Falha em mocks:** Confirme o nome do patch e o caminho do import.
- **Banco de dados não limpo:** Use fixtures para isolar testes.
- **Timeouts em APIs:** Sempre use mocks para integrações externas.

---

## Onboarding para Novos Contribuidores
1. Instale as dependências de desenvolvimento:
   ```bash
   pip install -r requirements-dev.txt
   ```
2. Rode todos os testes:
   ```bash
   pytest
   ```
3. Crie novos testes seguindo os exemplos deste guia.
4. Use type hints, docstrings e logging em testes complexos.
5. Consulte os arquivos `tests/` e este guia para referência.
6. Em caso de dúvida, abra uma issue ou peça revisão no PR.

---

## Recursos e Referências
- [Documentação oficial do pytest](https://docs.pytest.org/)
- [Guia de mocks do unittest](https://docs.python.org/3/library/unittest.mock.html)
- [Cobertura de código com pytest-cov](https://pytest-cov.readthedocs.io/)
- Veja também: [guia_didatico/pytest.md](pytest.md), [guia_didatico/auto_documentacao_ferramentas.md](auto_documentacao_ferramentas.md)

Assim você garante que tudo está funcionando e pode evoluir o projeto com segurança!
