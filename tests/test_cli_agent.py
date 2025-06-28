import pytest
import sys
import os
from unittest.mock import patch, MagicMock
from cli_agent import main as cli_main, escrever_arquivo, checar_api_key

def test_cli_agent_runs(monkeypatch):
    # Simula uma sequência de entradas do usuário e captura as saídas
    inputs = iter(["olá Codex!", "sair"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    # Não testamos a integração com a IA real aqui, só o fluxo CLI
    try:
        cli_main()
    except SystemExit:
        pass  # Permite sair normalmente

def test_cli_agent_input_vazio(monkeypatch):
    inputs = iter(["", "sair"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    try:
        cli_main()
    except SystemExit:
        pass

def test_cli_agent_comando_invalido(monkeypatch):
    inputs = iter(["/comando_invalido", "sair"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    try:
        cli_main()
    except SystemExit:
        pass

def test_checar_api_key_ausente(monkeypatch):
    # Remove a variável de ambiente para simular erro
    old_key = os.environ.pop("GOOGLE_API_KEY", None)
    try:
        with pytest.raises(SystemExit):
            checar_api_key()
    finally:
        if old_key:
            os.environ["GOOGLE_API_KEY"] = old_key

def test_escrever_arquivo_erro_json():
    # Simula erro de JSON na resposta da IA
    resposta = escrever_arquivo(nome_do_arquivo=None, conteudo=None)
    assert "ERRO" in resposta

@patch("cli_agent.client")
def test_cli_agent_branch_buscar_no_historico(mock_client, monkeypatch):
    # Simula resposta da IA para buscar_no_historico
    mock_response = MagicMock()
    mock_response.text = '{"ferramenta": "buscar_no_historico", "argumentos": {"termo_chave": "Quantum"}}'
    mock_client.models.generate_content.return_value = mock_response
    inputs = iter(["o que nós conversamos sobre o projeto Quantum?", "sair"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    try:
        cli_main()
    except SystemExit:
        pass

@patch("cli_agent.client")
def test_cli_agent_branch_escrever_arquivo(mock_client, monkeypatch):
    # Simula resposta da IA para escrever_arquivo
    mock_response = MagicMock()
    mock_response.text = '{"ferramenta": "escrever_arquivo", "argumentos": {"nome_do_arquivo": "mock.txt", "conteudo": "mock"}}'
    mock_client.models.generate_content.return_value = mock_response
    inputs = iter(["crie um arquivo chamado 'mock.txt' com o conteúdo 'mock'", "sair"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    try:
        cli_main()
    except SystemExit:
        pass

@patch("cli_agent.client")
def test_cli_agent_branch_resposta_padrao(mock_client, monkeypatch):
    # Simula resposta da IA para branch padrão
    mock_response = MagicMock()
    mock_response.text = 'Olá, esta é uma resposta padrão.'
    mock_client.models.generate_content.return_value = mock_response
    inputs = iter(["me conte uma piada", "sair"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    try:
        cli_main()
    except SystemExit:
        pass

def test_cli_agent_print_saida(monkeypatch, capsys):
    from unittest.mock import patch, MagicMock
    with patch("cli_agent.client") as mock_client:
        mock_response = MagicMock()
        mock_response.text = 'Olá, esta é uma resposta padrão.'
        mock_client.models.generate_content.return_value = mock_response
        inputs = iter(["me conte uma piada", "sair"])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        try:
            cli_main()
        except SystemExit:
            pass
        captured = capsys.readouterr()
        assert "Codex: Olá, esta é uma resposta padrão." in captured.out

def test_cli_agent_print_saida(monkeypatch):
    # Simula resposta inválida para forçar JSONDecodeError
    from cli_agent import client
    mock_response = type('Mock', (), {'text': 'resposta inválida'})()
    monkeypatch.setattr(client.models, 'generate_content', lambda *a, **kw: mock_response)
    inputs = iter(["forçar erro json", "sair"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    try:
        cli_main()
    except SystemExit:
        pass

@patch("cli_agent.client")
def test_cli_agent_branch_else(mock_client, monkeypatch):
    # Simula resposta da IA para branch else
    mock_response = MagicMock()
    mock_response.text = '{"ferramenta": "outra_ferramenta", "argumentos": {}}'
    mock_client.models.generate_content.return_value = mock_response
    inputs = iter(["comando desconhecido", "sair"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    try:
        cli_main()
    except SystemExit:
        pass

def test_sugerir_pergunta_frequente(monkeypatch):
    from cli_agent import sugerir_pergunta_frequente
    class DummySession:
        def query(self, *a, **kw):
            class DummyQuery:
                def filter(self, *a, **kw): return self
                def group_by(self, *a, **kw): return self
                def order_by(self, *a, **kw): return self
                def limit(self, n): return self
                def all(self): return [("pergunta frequente", 5)]
            return DummyQuery()
    session = DummySession()
    # Deve sugerir a pergunta frequente
    assert sugerir_pergunta_frequente(session) == "pergunta frequente"

def test_listar_arquivos(tmp_path):
    from cli_agent import listar_arquivos
    # Cria estrutura de diretório temporária
    pasta = tmp_path / "docs"
    pasta.mkdir()
    (pasta / "arquivo1.txt").write_text("abc")
    (pasta / "arquivo2.txt").write_text("def")
    # Testa listagem
    resultado = listar_arquivos(caminho="docs", base_path=tmp_path)
    assert "arquivo1.txt" in resultado and "arquivo2.txt" in resultado
    # Testa diretório vazio
    pasta_vazia = tmp_path / "vazio"
    pasta_vazia.mkdir()
    resultado_vazio = listar_arquivos(caminho="vazio", base_path=tmp_path)
    assert "está vazio" in resultado_vazio
    # Testa diretório inexistente
    resultado_erro = listar_arquivos(caminho="nao_existe", base_path=tmp_path)
    assert "não encontrado" in resultado_erro
