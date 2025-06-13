# database.py - Módulo de gerenciamento da memória da IA

from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
from sqlalchemy.orm import declarative_base, sessionmaker
import datetime

# Define o "endereço" do nosso banco de dados.
DATABASE_URL = "sqlite:///memoria_codex.db"

# Cria o "motor" do SQLAlchemy. É o ponto de entrada principal para o nosso banco de dados.
engine = create_engine(DATABASE_URL)

# Cria uma 'Base' declarativa. Nossas tabelas (Classes Python) vão herdar dela.
Base = declarative_base()

# Esta é a nossa "planta" da tabela 'conversas', traduzida para uma Classe Python.
class Conversa(Base):
    __tablename__ = 'conversas' # O nome oficial da tabela no arquivo do banco de dados.

    id = Column(Integer, primary_key=True) # A chave primária, única e automática.
    timestamp = Column(DateTime, default=datetime.datetime.now) # A data e hora. O valor padrão é o momento da criação.
    role = Column(String(50)) # O papel ('user' ou 'model').
    content = Column(Text) # O conteúdo da mensagem.

    def __repr__(self):
        return f"<Conversa(id={self.id}, role='{self.role}', content='{self.content[:30]}...')>"

def criar_banco_e_tabelas():
    """Verifica se o banco de dados e as tabelas existem e, se não, os cria."""
    Base.metadata.create_all(bind=engine)

def carregar_historico(session, n_mensagens: int = 10):
    """Carrega as 'n' últimas mensagens do banco de dados para usar como contexto."""
    # print(f"[MEMÓRIA]: Carregando as últimas {n_mensagens} interações do histórico...")
    historico = session.query(Conversa).order_by(Conversa.id.desc()).limit(n_mensagens).all()
    return list(reversed(historico))

def buscar_no_historico(session, termo_chave: str):
    """Busca no histórico completo de conversas por um termo ou palavra-chave."""
    print(f"[MEMÓRIA]: Buscando pelo termo '{termo_chave}' no histórico completo...")
    termo_para_busca = f"%{termo_chave}%"
    resultados = session.query(Conversa).filter(Conversa.content.like(termo_para_busca)).all()
    print(f"[MEMÓRIA]: {len(resultados)} resultados encontrados.")
    return resultados

# Se rodarmos este arquivo diretamente, ele cria a infraestrutura.
if __name__ == "__main__":
    print("Inicializando a infraestrutura do banco de dados...")
    criar_banco_e_tabelas()
    print("Infraestrutura da memória pronta.")