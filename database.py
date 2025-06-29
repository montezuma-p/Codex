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

def perguntas_mais_frequentes(db_session, limite=3):
    """
    Retorna as perguntas/comandos do usuário mais frequentes no histórico.
    """
    from sqlalchemy import func
    resultados = (
        db_session.query(Conversa.content, func.count(Conversa.content).label('freq'))
        .filter(Conversa.role == 'user')
        .group_by(Conversa.content)
        .order_by(func.count(Conversa.content).desc())
        .limit(limite)
        .all()
    )
    return [r[0] for r in resultados]

def gerar_relatorio_uso(db_session, n_mensagens=100):
    """
    Gera um relatório automático de uso e aprendizado do Codex CLI.
    """
    from collections import Counter
    historico = db_session.query(Conversa).order_by(Conversa.id).limit(n_mensagens).all()
    total = len(historico)
    perguntas = [msg.content for msg in historico if msg.role == 'user']
    respostas = [msg.content for msg in historico if msg.role == 'model']
    horarios = [msg.timestamp.hour for msg in historico]
    palavras = []
    for p in perguntas:
        palavras.extend(p.lower().split())
    freq_perguntas = Counter(perguntas).most_common(5)
    freq_palavras = Counter(palavras).most_common(5)
    freq_horarios = Counter(horarios).most_common(3)
    relatorio = [
        f"Total de interações: {total}",
        f"Perguntas mais frequentes: {[p for p, _ in freq_perguntas]}",
        f"Palavras mais recorrentes: {[w for w, _ in freq_palavras]}",
        f"Horários de maior uso: {[h for h, _ in freq_horarios]}",
    ]
    return "\n".join(relatorio)

def exportar_historico_jsonl(db_session, caminho_arquivo="historico_codex.jsonl", n_mensagens=1000):
    """
    Exporta o histórico de interações (prompt/resposta) em formato JSONL para fine-tuning futuro.
    Cada linha: {"prompt": ..., "completion": ...}
    """
    historico = db_session.query(Conversa).order_by(Conversa.id).limit(n_mensagens).all()
    pares = []
    buffer = None
    for msg in historico:
        if msg.role == 'user':
            buffer = msg.content
        elif msg.role == 'model' and buffer:
            pares.append({"prompt": buffer, "completion": msg.content})
            buffer = None
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        for par in pares:
            import json
            f.write(json.dumps(par, ensure_ascii=False) + "\n")
    return f"Exportação concluída: {len(pares)} pares salvos em {caminho_arquivo}"

def perfil_usuario(db_session, n_mensagens=200):
    """
    Analisa o histórico e retorna um perfil resumido do usuário: temas, tom, horários, etc.
    """
    from collections import Counter
    historico = db_session.query(Conversa).order_by(Conversa.id).limit(n_mensagens).all()
    perguntas = [msg.content for msg in historico if msg.role == 'user']
    palavras = []
    for p in perguntas:
        palavras.extend(p.lower().split())
    temas = Counter([w for w in palavras if len(w) > 4]).most_common(5)
    horarios = [msg.timestamp.hour for msg in historico if msg.role == 'user']
    freq_horarios = Counter(horarios).most_common(2)
    perfil = {
        "temas_mais_frequentes": [t for t, _ in temas],
        "horarios_mais_ativos": [h for h, _ in freq_horarios],
        "total_perguntas": len(perguntas)
    }
    return perfil

if __name__ == "__main__":
    print("Inicializando a infraestrutura do banco de dados...")
    criar_banco_e_tabelas()
    print("Infraestrutura da memória pronta.")