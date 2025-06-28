# Ferramentas externas do Codex CLI: exemplos de uso

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
  Use o pacote requests: requests.get('url')
  ...
  ```

## consultar_github
Busca os 3 repositórios mais populares relacionados ao termo.

**Exemplo:**
- Usuário: "Codex, mostre repositórios sobre 'machine learning' no GitHub"
- Codex:
  ```
  GitHub – Repositórios para 'machine learning':
  - scikit-learn
  https://github.com/scikit-learn/scikit-learn
  ...
  - ...
  ```

## consultar_wolframalpha
Pergunta matemática, científica ou geral ao WolframAlpha.

**Exemplo:**
- Usuário: "Codex, quanto é a raiz quadrada de 144?"
- Codex:
  ```
  WolframAlpha – Resposta para 'raiz quadrada de 144':
  12
  ```

---

**Dica:** Para cada ferramenta, basta pedir de forma natural. O Codex identifica o contexto e aciona a API correta!
