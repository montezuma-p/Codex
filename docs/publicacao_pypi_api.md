## Publicação no PyPI

1. **Instale as ferramentas necessárias:**
   ```bash
   pip install build twine
   ```
2. **Gere os arquivos de distribuição:**
   ```bash
   python -m build
   ```
   Isso criará os arquivos `.whl` e `.tar.gz` na pasta `dist/`.
3. **Faça upload para o PyPI:**
   - Para o PyPI oficial:
     ```bash
     twine upload dist/*
     ```
   - Para testar no TestPyPI:
     ```bash
     twine upload --repository testpypi dist/*
     ```
   - Será solicitado seu usuário e senha do PyPI.

4. **Instale o pacote publicado:**
   ```bash
   pip install codex-cli
   ```

---

## Uso como Serviço/API (Exemplo com FastAPI)

Você pode expor o Codex como uma API HTTP usando FastAPI:

```python
from fastapi import FastAPI, Request
from codex.cli_agent import main as codex_main

app = FastAPI()

@app.post("/codex/")
async def codex_endpoint(request: Request):
    data = await request.json()
    # Exemplo: repasse argumentos para o Codex CLI
    resposta = codex_main(**data)
    return {"resposta": resposta}
```

- Instale o FastAPI e o servidor Uvicorn:
  ```bash
  pip install fastapi uvicorn
  ```
- Rode o servidor:
  ```bash
  uvicorn nome_do_arquivo:app --reload
  ```

Adapte conforme sua necessidade! Consulte a documentação oficial do FastAPI para mais detalhes.

---

## Referências
- [Publicando no PyPI (oficial)](https://packaging.python.org/pt_BR/latest/tutorials/packaging-projects/)
- [TestPyPI (ambiente de testes)](https://test.pypi.org/)
- [FastAPI Docs](https://fastapi.tiangolo.com/pt/)
