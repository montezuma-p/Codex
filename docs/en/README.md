# Codex CLI: Your AI and Automation Assistant in the Terminal

**Codex CLI** is a powerful command-line tool designed for developers, data engineers, and automation enthusiasts. Integrate Google Gemini's artificial intelligence directly into your workflow, automate repetitive tasks, and query a variety of information sources without leaving the terminal.

With an extensible architecture and a focus on productivity, Codex CLI stores your interaction history, allows you to search past conversations, and provides a suite of built-in tools to interact with your file system and external APIs.

## Key Features

*   **Integrated Artificial Intelligence:** Chat with the **Google Gemini** language model to generate code, get explanations, translate text, and much more.
*   **Conversation History:** All your interactions are saved locally in an SQLite database, allowing you to review and search for important information at any time.
*   **Extensible Tool System:**
    *   `escrever_arquivo` (write_file): Create or modify files in your project.
    *   `listar_arquivos` (list_files): Navigate the directory structure.
    *   `ler_arquivo` (read_file): Read the content of text files.
    *   `consultar_wikipedia` (query_wikipedia): Get quick summaries from Wikipedia.
    *   `consultar_stackoverflow` (query_stackoverflow): Find solutions to programming problems.
    *   `consultar_google` (query_google): Perform web searches.
    *   And much more!
*   **Multilingual Support:** The interface and documentation are available in Portuguese and English.
*   **Task Automation:** Use Codex to automate scripts, generate reports, and interact with your development environment.

## Installation

To install Codex CLI, simply use `pip`:

```bash
pip install codex-cli-montezuma
```

## How to Use Codex CLI (Step-by-Step)

### 1. API Key Configuration

To allow Codex to use Google Gemini AI and other search tools, you need to provide your API keys.

**Why is this necessary?**
*   **`GOOGLE_API_KEY`**: Authenticates your requests to the Gemini API, enabling Codex to send your questions and receive AI responses.
*   **`GOOGLE_SEARCH_CX`**: This is your Google Custom Search Engine ID, required for the `consultar_google` (google_search) tool.

**How to configure:**

You have two options:

*   **(Recommended) Setup Script:** If you cloned the repository, you can use our interactive script:
    ```bash
    ./scripts/setup-api-keys.sh
    ```
    It will guide you and create a `.env` file automatically.

*   **Manually (`.env` file):** Create a file named `.env` in the directory where you will run the `codex` command and add the following lines, replacing with your values:
    ```
    GOOGLE_API_KEY="YOUR_GEMINI_API_KEY"
    GOOGLE_SEARCH_CX="YOUR_CUSTOM_SEARCH_ENGINE_ID"
    ```

> For a detailed guide on **how to obtain** these keys, please refer to our [API key setup guide](secrets-configuration.md).

### 2. Running Codex CLI

With everything installed and configured, you can interact with Codex in several ways:

**a) Interactive Mode (Chat)**

This is the main mode, where you chat with the AI. To start, simply run:
```bash
codex
```
From there, you can ask questions, request tasks, or use the available tools. To exit, type `sair` or `exit`.

**Example Interaction:**
```
You: Create a file named 'app.py' with a "Hello, World" in Python.

Codex: Sure, using the 'write_file' tool.

(The app.py file is created in your directory)
```

**b) Direct Commands (Arguments)**

You can execute specific commands directly from the command line without entering chat mode.

*   **Search History:**
    ```bash
    codex --buscar "your search term"
    ```

*   **Generate Usage Report:**
    ```bash
    codex --relatorio-uso
    ```

*   **Export History to JSONL:**
    ```bash
    codex --exportar-jsonl
    ```

*   **Generate Tool Documentation:**
    ```bash
    codex --doc-ferramentas
    ```

*   **View Usage Profile:**
    ```bash
    codex --perfil
    ```

## Full Documentation

To explore all features, contribution guides, and tutorials, browse the links in the side menu or visit the [General Index](indice_geral.md).
