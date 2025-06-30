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
- Wikipedia
- WolframAlpha

Utilize mocks para simular respostas das APIs e garantir que o código funcione mesmo sem acesso real à internet.

---

## Troubleshooting e Dicas
- Se os testes não rodarem, verifique dependências e variáveis de ambiente.
- Para dúvidas sobre integração de APIs, consulte [como_escrever_testes.md](como_escrever_testes.md).
- Para integração contínua, veja o Makefile e scripts de automação.

---

## Onboarding para Novos Contribuidores
1. Sempre escreva novos testes para cada funcionalidade implementada.
2. Rode todos os testes antes de cada commit/push.
3. Consulte este guia e [como_escrever_testes.md](como_escrever_testes.md) para exemplos e padrões.
4. Em caso de dúvida, abra uma issue ou peça revisão no PR.

---

> Testes bem escritos garantem a qualidade e evolução segura do projeto.
