import os
import sys
import pathlib
import json
import requests
from google import genai
from google.genai import types
from codex import database
from codex.integrations.wikipedia import consultar_wikipedia
from codex.integrations.stackoverflow import consultar_stackoverflow
from codex.integrations.google import consultar_google
from codex.integrations.github import consultar_github
from codex.integrations.wolframalpha import consultar_wolframalpha
from codex.cli_commands import executar_comando_cli
from codex.suggestions import buscar_contexto_relevante
from codex.cli_core import FERRAMENTAS, gerar_documentacao_ferramentas
from locales.i18n import _

def checar_api_key():
    API_KEY = os.getenv("GOOGLE_API_KEY")
    if not API_KEY:
        print(_("CRITICAL ERROR: API key not found. Please set GOOGLE_API_KEY environment variable."))
        sys.exit(1)
    return API_KEY

def main():
    """Entry point for Codex global CLI."""
    API_KEY = checar_api_key()
    client = genai.Client(api_key=API_KEY)
    MODELO_IA = "gemini-2.5-flash"  # ou o modelo correto para seu uso
    executar_comando_cli(sys.argv, client, MODELO_IA)

if __name__ == "__main__":
    main()
