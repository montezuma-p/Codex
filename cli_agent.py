import os
import sys
import pathlib
import json
from google import genai
import database

API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    print("ERRO CRÍTICO: Chave de API não encontrada.")
    sys.exit(1)

client = genai.Client(api_key=API_KEY)
MODELO_IA = "models/gemini-2.5-flash-preview-05-20"
PROMPT_MESTRA = """
Você é Codex, uma IA projetada pelo Montezuma. Seu papel é agir como mentor dele. Analise o pedido do usuário. Se corresponder a uma ferramenta, responda APENAS com um código JSON no formato: {"ferramenta": "nome_da_ferramenta", "argumentos": {"nome_do_argumento": "valor"}}.
Se nenhuma ferramenta for aplicável, responda normalmente mantendo a naturalidade.

PROTOCOLO DE IMERSÃO:
após o uso de uma ferramenta, vc DEVE manter o contexto. Vc é proíbido de ter amnésia.

### EXEMPLOS DE EXECUÇÃO:
- Pedido do Usuário: "crie um arquivo chamado 'ideias.txt' no desktop com a ideia 'construir um novo mundo'"
- Sua Resposta: {"ferramenta": "escrever_arquivo", "argumentos": {"nome_do_arquivo": "ideias.txt", "conteudo": "construir um novo mundo", "local": "desktop"}}

- Pedido do Usuário: "o que nós conversamos sobre o projeto Quantum Leap?"
- Sua Resposta: {"ferramenta": "buscar_no_historico", "argumentos": {"termo_chave": "Quantum Leap"}}

---

### Ferramentas disponíveis:
1. `escrever_arquivo`: Usada para criar ou sobrescrever arquivos de texto.
2. `buscar_no_historico`: Usada para responder perguntas sobre o que já foi conversado no passado.
"""

def escrever_arquivo(**kwargs):
    nome_do_arquivo = kwargs.get("nome_do_arquivo")
    conteudo = kwargs.get("conteudo")
    local = kwargs.get("local", "projeto")
    try:
        if local.lower() == "desktop":
            base_path = pathlib.Path.home() / "Área de Trabalho"
        else:
            base_path = pathlib.Path(__file__).parent
        caminho_final = base_path / nome_do_arquivo
        with open(caminho_final, "w", encoding='utf-8') as f:
            f.write(conteudo)
        return f"[AÇÃO: Arquivo '{nome_do_arquivo}' criado no local '{local}'.]"
    except Exception as e:
        return f"[ERRO DA FERRAMENTA]: {e}"

def main():
    database.criar_banco_e_tabelas()
    session = database.Session()
    print("Bem-vindo ao Codex CLI! Digite 'sair' para encerrar.")
    while True:
        prompt_usuario = input("Você: ")
        if prompt_usuario.strip().lower() == 'sair':
            print("Até logo!")
            break
        prompt_para_decidir = PROMPT_MESTRA + "\n\nPedido do Usuário: " + prompt_usuario
        response_decisao = client.models.generate_content(model=MODELO_IA, contents=prompt_para_decidir)
        resposta_ia = ""
        try:
            decodificado = json.loads(response_decisao.text)
            ferramenta = decodificado.get("ferramenta")
            if ferramenta == "buscar_no_historico":
                termo = decodificado.get('argumentos', {}).get('termo_chave')
                resultados = database.buscar_no_historico(session, termo_chave=termo)
                contexto = "\n".join([f"- {res.role}: {res.content}" for res in resultados])
                prompt_sintese = f"Contexto de conversas passadas:\n{contexto}\n\nBaseado nesse contexto, responda à pergunta original: '{prompt_usuario}'"
                nova_response = client.models.generate_content(model=MODELO_IA, contents=prompt_sintese)
                resposta_ia = nova_response.text
            elif ferramenta == "escrever_arquivo":
                resposta_ia = escrever_arquivo(**decodificado.get('argumentos', {}))
            else:
                historico = database.carregar_historico(session)
                historico_formatado = "\n".join([f"- {msg.role}: {msg.content}" for msg in historico])
                prompt_conversa = f"Você é Codex, um mentor de IA. Histórico da conversa:\n{historico_formatado}\n\nResponda ao usuário: {prompt_usuario}"
                nova_response = client.models.generate_content(model=MODELO_IA, contents=prompt_conversa)
                resposta_ia = nova_response.text
        except (json.JSONDecodeError, TypeError):
            resposta_ia = response_decisao.text
        print(f"Codex: {resposta_ia}")
        # Salva a interação no banco de dados
        session.add(database.Conversa(role="user", content=prompt_usuario))
        session.add(database.Conversa(role="model", content=resposta_ia))
        session.commit()

if __name__ == "__main__":
    main()
