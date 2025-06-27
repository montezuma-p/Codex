# database.py - Módulo de gerenciamento da memória da IA

import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
from sqlalchemy.orm import declarative_base, sessionmaker

# Adicionamos 'check_same_thread=False' para compatibilidade com o Flask
DATABASE_URL = "sqlite:///memoria_codex.db?check_same_thread=False" 
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Conversa(Base):
    __tablename__ = 'conversas'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.datetime.now)
    role = Column(String(50))
    content = Column(Text)

def criar_banco_e_tabelas():
    Base.metadata.create_all(bind=engine)

def carregar_historico(db_session, n_mensagens: int = 50):
    historico = db_session.query(Conversa).order_by(Conversa.id.desc()).limit(n_mensagens).all()
    return list(reversed(historico))

def buscar_no_historico(db_session, termo_chave: str):
    print(f"[MEMÓRIA]: Buscando por '{termo_chave}'...")
    termo_para_busca = f"%{termo_chave}%"
    resultados = db_session.query(Conversa).filter(Conversa.content.like(termo_para_busca)).all()
    print(f"[MEMÓRIA]: {len(resultados)} resultados encontrados.")
    return resultados

if __name__ == "__main__":
    print("Inicializando a infraestrutura do banco de dados...")
    criar_banco_e_tabelas()
    print("Infraestrutura da memória pronta.")