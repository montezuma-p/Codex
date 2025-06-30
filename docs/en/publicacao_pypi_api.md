# PyPI/API Publication

1. **Install the required tools:**
   ```bash
   pip install build twine
   ```
2. **Generate the distribution files:**
   ```bash
   python -m build
   ```
   This will create the `.whl` and `.tar.gz` files in the `dist/` folder.
3. **Upload to PyPI:**
   - For the official PyPI:
     ```bash
     twine upload dist/*
     ```
   - To test on TestPyPI:
     ```bash
     twine upload --repository testpypi dist/*
     ```
   - You will be prompted for your PyPI username and password.

4. **Install the published package:**
   ```bash
   pip install codex-cli
   ```

---

## Using as a Service/API (Example with FastAPI)

You can expose Codex as an HTTP API using FastAPI:

```python
from fastapi import FastAPI, Request
from codex.cli_agent import main as codex_main

app = FastAPI()

@app.post("/codex/")
async def codex_endpoint(request: Request):
    data = await request.json()
    # Example: pass arguments to Codex CLI
    resposta = codex_main(**data)
    return {"resposta": resposta}
```

- Install FastAPI and the Uvicorn server:
  ```bash
  pip install fastapi uvicorn
  ```
- Run the server:
  ```bash
  uvicorn your_file_name:app --reload
  ```

Adapt as needed! See the official FastAPI documentation for more details.

---
