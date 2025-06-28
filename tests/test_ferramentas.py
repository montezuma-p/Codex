import os
import pathlib
import pytest
from cli_agent import escrever_arquivo

def test_escrever_arquivo_projeto(tmp_path):
    nome = "teste_pytest.txt"
    conteudo = "Arquivo de teste para pytest."
    # Redireciona o path para tmp_path
    original_parent = pathlib.Path.parent
    try:
        pathlib.Path.parent = property(lambda self: tmp_path)
        resposta = escrever_arquivo(nome_do_arquivo=nome, conteudo=conteudo)
        arquivo = tmp_path / nome
        assert arquivo.exists()
        assert arquivo.read_text(encoding='utf-8') == conteudo
        assert "criado" in resposta
    finally:
        pathlib.Path.parent = original_parent

def test_escrever_arquivo_erro(tmp_path):
    # Tenta salvar em um diretório inexistente (simula erro)
    nome = "invalido/teste.txt"
    conteudo = "erro"
    resposta = escrever_arquivo(nome_do_arquivo=nome, conteudo=conteudo)
    assert "ERRO" in resposta
