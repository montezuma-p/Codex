# Como Escrever Testes Automatizados no Codex

Testes automatizados são pequenos programas que verificam se o seu código está funcionando corretamente. No Codex, usamos o framework `pytest` para isso. Veja como criar seus próprios testes!

---

## Estrutura dos Testes
- Todos os testes ficam na pasta `tests/`.
- Cada arquivo de teste começa com `test_` (ex: `test_database.py`).
- Cada função de teste também começa com `test_`.
- Usamos funções e fixtures do pytest para preparar o ambiente de teste.

---

## Exemplo Básico
```python
def test_soma():
    assert 1 + 1 == 2
```
Esse teste verifica se a soma está correta. Se não estiver, o pytest mostra um erro.

---

## Testando Funções do Projeto
Veja um exemplo real do Codex:
```python
def test_criar_e_buscar_conversa(session):
    nova_msg = database.Conversa(role='user', content='Teste Pytest')
    session.add(nova_msg)
    session.commit()
    resultados = database.buscar_no_historico(session, 'Teste')
    assert any('Teste Pytest' in msg.content for msg in resultados)
```
- **O que faz?** Cria uma mensagem no banco e testa se ela pode ser encontrada.
- **Por que é útil?** Garante que salvar e buscar no banco funcionam.

---

## Lógica dos Testes
1. **Preparação:** Crie o que precisa (ex: uma mensagem, um arquivo, etc).
2. **Ação:** Execute a função que quer testar.
3. **Verificação:** Use `assert` para checar se o resultado está certo.
4. **Limpeza:** (Opcional) Remova arquivos ou dados temporários.

---

## Dicas para Escrever Bons Testes
- Teste casos normais e casos de erro.
- Use nomes claros para as funções de teste.
- Separe os testes por arquivo conforme o módulo (ex: banco, ferramentas, CLI).
- Use fixtures do pytest para preparar ambientes temporários (ex: banco de dados em memória).

---

## Rodando os Testes
No terminal, digite:
```bash
pytest
```
Ou para ver a cobertura:
```bash
pytest --cov=.
```

Assim você garante que tudo está funcionando e pode evoluir o projeto com segurança!
