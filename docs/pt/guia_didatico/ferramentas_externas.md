# Ferramentas externas do Codex CLI: exemplos de uso

> **Sumário das Mudanças Recentes (2025)**
> - Todas as integrações externas migradas para módulos próprios em `src/integrations/`.
> - Logging estruturado e tratamento de erros padronizado em todas as ferramentas.
> - Exemplos e instruções revisados conforme nova CLI e onboarding.
> - Testes automatizados com mocks para todas as integrações.
> - Documentação e dicas atualizadas para onboarding de novos contribuidores.
> - Guia expandido com troubleshooting, integração contínua e dicas avançadas.

---

## Sobre este Guia
Este documento apresenta exemplos práticos, dicas e troubleshooting para uso das integrações externas do Codex CLI. Serve como referência rápida e onboarding para desenvolvedores e usuários avançados.

- Consulte sempre após adicionar ou modificar integrações.
- Exemplos refletem o comportamento real da CLI e das APIs.
- Siga os padrões de modularização, logging e testes para garantir integração consistente.

---

## Troubleshooting e Dicas
- Se uma ferramenta não funcionar, verifique variáveis de ambiente e dependências no README.
- Para dúvidas sobre testes, consulte [como_escrever_testes.md](como_escrever_testes.md).
- Para integração contínua, veja o Makefile e scripts de automação.

---

## Onboarding para Novos Contribuidores
1. Sempre documente novas integrações seguindo o padrão dos exemplos abaixo.
2. Rode os testes automatizados para garantir cobertura e robustez.
3. Consulte este guia para exemplos de argumentos e chamadas.
4. Em caso de dúvida, abra uma issue ou peça revisão no PR.

---

## consultar_google
Busca os 3 primeiros resultados do Google Search para um termo.

**Exemplo:**
- Usuário: "Codex, pesquise no Google por 'Python asyncio'"
- Codex:
  ```
  Google Search – Resultados para 'Python asyncio':
  - Python 3 asyncio documentation
  https://docs.python.org/3/library/asyncio.html
  ...
  - ...
  ```

## consultar_stackoverflow
Busca a pergunta mais relevante e a resposta mais votada no Stack Overflow.

**Exemplo:**
- Usuário: "Como faço um request HTTP em Python?"
- Codex:
  ```
  Stack Overflow – How to make an HTTP request in Python?
  https://stackoverflow.com/q/123456
  Resposta mais votada:
  ...
  ```

## consultar_github
Busca repositórios e issues relevantes no GitHub.

**Exemplo:**
- Usuário: "Codex, busque repositórios sobre 'machine learning'"
- Codex:
  ```
  GitHub – Repositórios encontrados:
  - scikit-learn
  - tensorflow
  ...
  ```

## consultar_wikipedia
Busca o resumo de um termo na Wikipedia.

**Exemplo:**
- Usuário: "Codex, resuma 'Inteligência Artificial'"
- Codex:
  ```
  Wikipedia – Inteligência Artificial:
  ...
  ```

## consultar_wolframalpha
Responde perguntas matemáticas e científicas usando WolframAlpha.

**Exemplo:**
- Usuário: "Codex, calcule a integral de x^2"
- Codex:
  ```
  WolframAlpha – Resultado:
  ...
  ```
