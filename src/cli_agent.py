import os
import sys
import pathlib
import json
import requests
from google import genai
from src import database
from src.integrations.wikipedia import consultar_wikipedia
from src.integrations.stackoverflow import consultar_stackoverflow
from src.integrations.google import consultar_google
from src.integrations.github import consultar_github
from src.integrations.wolframalpha import consultar_wolframalpha
import datetime
from src.cli_commands import executar_comando_cli
from src.suggestions import buscar_contexto_relevante
from src.cli_core import PROMPT_MESTRA, FERRAMENTAS, gerar_documentacao_ferramentas

def checar_api_key():
    API_KEY = os.getenv("GOOGLE_API_KEY")
    if not API_KEY:
        print("ERRO CRÍTICO: Chave de API não encontrada.")
        sys.exit(1)
    return API_KEY

def main():
    checar_api_key()
    API_KEY = os.getenv("GOOGLE_API_KEY")
    client = genai.Client(api_key=API_KEY)
    MODELO_IA = "models/gemini-2.5-flash-preview-05-20"
    executar_comando_cli(sys.argv, client, MODELO_IA)

if __name__ == "__main__":
    main()
