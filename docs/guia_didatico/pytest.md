# O que é pytest?

O `pytest` é uma ferramenta poderosa e popular para testar código Python de forma automática. Ele permite que você escreva testes simples e também testes mais avançados, garantindo que seu código funcione como esperado mesmo após mudanças.

## Por que usar pytest?
- **Confiança:** Ajuda a garantir que novas funcionalidades não quebrem o que já existe.
- **Automação:** Permite rodar todos os testes de uma vez, economizando tempo.
- **Facilidade:** A sintaxe é simples e os relatórios de erro são claros.
- **Comunidade:** É o framework de testes mais usado na comunidade Python.

## Por que colocamos pytest no Codex?
- Para garantir que as funções principais do projeto funcionem corretamente.
- Para facilitar a evolução do projeto sem medo de quebrar nada.
- Para permitir que qualquer pessoa contribua com segurança.

## Como instalar o pytest?
Você pode instalar o pytest facilmente usando o pip:

```bash
pip install pytest
```

No Codex, também adicionamos o `pytest` no arquivo `requirements-dev.txt`, então basta rodar:

```bash
pip install -r requirements-dev.txt
```

## Como rodar os testes?
No terminal, dentro da pasta do projeto, digite:

```bash
pytest
```

Ou, para ver a cobertura de código:

```bash
pytest --cov=.
```

Assim você garante que tudo está funcionando e pode evoluir o projeto com tranquilidade!

---

## pytest e APIs externas

No Codex CLI, usamos pytest para testar integrações com APIs como Google Search, Stack Overflow, GitHub e WolframAlpha. Utilizamos mocks para simular respostas das APIs e garantir que o código funcione mesmo sem acesso real à internet.

- Veja exemplos de testes para APIs externas em `tests/test_cli_agent.py`.
- Para aprender a criar seus próprios mocks, consulte a documentação do pytest e do unittest.mock.

---

## Dica
Sempre rode os testes antes de subir mudanças! Assim, você garante que todas as integrações continuam funcionando.
