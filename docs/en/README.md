# Codex CLI – AI Tools, APIs and Automation

[![PyPI](https://img.shields.io/pypi/v/codex-cli-montezuma)](https://pypi.org/project/codex-cli-montezuma/)

> **Quick Documentation Index**
> - [Visual Index](indice_visual.md)
> - [Global Contribution Guide](guia_contribuicao.md)
> - [General Index](indice_geral.md)
> - [PR Checklist](checklist_pr.md)
> - [Roadmap](roadmap.md)
> - [Logbook](diario_de_bordo.md)
> - [Next Mission](proxima_missao.md)
> - [Testing Guide](guia_didatico/como_escrever_testes.md)
> - [External Tools](guia_didatico/ferramentas_externas.md)
> - [Automatic Documentation](guia_didatico/auto_documentacao_ferramentas.md)
> - [File Reading](guia_didatico/ler_arquivo.md)
> - [File Perception](guia_didatico/percepcao_arquivos.md)
> - [pytest](guia_didatico/pytest.md)

## Quick Installation

```bash
pip install codex-cli-montezuma
```

Access the package on PyPI: https://pypi.org/project/codex-cli-montezuma/

> **Note:** For a full installation with all development dependencies, use:
> 
> ```bash
> pip install -r requirements-dev.txt
> ```

## Main Features
- Stores conversations and history in SQLite.
- Keyword search in history.
- Interact with Gemini AI (Google) via CLI.
- Integrated tools:
  - **escrever_arquivo**: creates/overwrites text files.
  - **listar_arquivos**: lists project files and folders.
  - **ler_arquivo**: reads project text files.
  - **consultar_wikipedia**: fetches summaries from Wikipedia.
  - **consultar_stackoverflow**: fetches technical Q&A.
  - **consultar_google**: returns the top 3 Google Search results.
  - **consultar_github**: shows popular repositories for a term.
  - **consultar_wolframalpha**: answers math/science questions.
- **Dynamic response customization**: the agent adapts tone, examples, and tips according to the user's profile, making answers more relevant and aligned to their style and needs.

## How to Use
1. Install dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```
2. Set the required environment variables:
   ```bash
   export GOOGLE_API_KEY='your-gemini-api-key'
   export GOOGLE_SEARCH_API_KEY='your-google-search-api-key'
   export GOOGLE_SEARCH_CX='your-google-search-cx'
   export GITHUB_TOKEN='your-github-token'  # (optional, for more requests)
   export WOLFRAMALPHA_APPID='your-wolframalpha-appid'
   ```
3. Initialize the database:
   ```bash
   python database.py
   ```
4. Run the CLI:
   ```bash
   python cli_agent.py
   ```

## Usage Examples
- "Codex, create a file called 'example.txt' with the content 'hello world'"
- "List the files in the docs folder"
- "Read the README.md file"
- "Search Google for 'Python asyncio'"
- "Find repositories about 'machine learning' on GitHub"
- "What is the square root of 144 on WolframAlpha?"
- "What does API mean according to Wikipedia?"
- "How do I make an HTTP request in Python? (Stack Overflow)"
- "Codex, give me personalized tips to study Python at night."

See more examples and tips in `guia_didatico/ferramentas_externas.md`.

## Dynamic Customization
Codex analyzes your usage history, frequent topics, times, and preferences to adapt:
- The tone of responses (more formal, objective, motivational, etc.)
- Practical examples aligned to your profile
- Contextual tips and suggestions

You can view your profile with:
```bash
python cli_agent.py --perfil-usuario
```
And export the history for future fine-tuning:
```bash
python cli_agent.py --exportar-jsonl
```

## Roadmap
See the [full roadmap](roadmap.md) for next steps, future vision, and project evolution.
