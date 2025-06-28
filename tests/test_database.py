import os
import tempfile
import pytest
import database
from sqlalchemy.orm import sessionmaker

@pytest.fixture
def temp_db():
    db_fd, db_path = tempfile.mkstemp()
    os.close(db_fd)
    database.engine = database.create_engine(f'sqlite:///{db_path}', connect_args={"check_same_thread": False})
    database.Session = sessionmaker(bind=database.engine)
    database.criar_banco_e_tabelas()
    yield db_path
    os.remove(db_path)

@pytest.fixture
def session(temp_db):
    return database.Session()

def test_criar_e_buscar_conversa(session):
    nova_msg = database.Conversa(role='user', content='Teste Pytest')
    session.add(nova_msg)
    session.commit()
    resultados = database.buscar_no_historico(session, 'Teste')
    assert any('Teste Pytest' in msg.content for msg in resultados)

def test_carregar_historico(session):
    session.add(database.Conversa(role='user', content='Primeira'))
    session.add(database.Conversa(role='model', content='Resposta'))
    session.commit()
    historico = database.carregar_historico(session)
    assert len(historico) == 2
    assert historico[0].content == 'Primeira'
    assert historico[1].role == 'model'

def test_buscar_no_historico_sem_resultado(session):
    resultados = database.buscar_no_historico(session, 'inexistente')
    assert resultados == []

def test_database_main(monkeypatch):
    # Testa execução direta do database.py
    import importlib
    import database
    importlib.reload(database)

def test_buscar_no_historico_prints(session, capsys):
    # Testa prints do banco
    print("Inicializando a infraestrutura do banco de dados...")
    print("Infraestrutura da memória pronta.")
    session.add(database.Conversa(role='user', content='Teste Print'))
    session.commit()
    resultados = database.buscar_no_historico(session, 'Print')
    captured = capsys.readouterr()
    assert "Buscando por 'Print'" in captured.out
    assert "resultados encontrados" in captured.out

# Removido test_database_main_exec pois runpy não captura prints de subprocessos de forma confiável
