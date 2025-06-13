# codex_local.py - Versão de Produção v1.2 (Arquitetura Otimizada)

from google import genai
import os
import sys
import pathlib
import json
from sqlalchemy.orm import sessionmaker
import database

# --- CONFIGURAÇÃO E FERRAMENTAS ---

API_KEY = os.getenv("GOOGLE_API_KEY")

def escrever_arquivo(nome_do_arquivo: str, conteudo: str, local: str = "projeto"):
    """Cria ou sobrescreve um arquivo de texto com um nome e conteúdo fornecidos."""
    try:
        if local.lower() == "desktop":
            # Adapte este caminho se o seu nome de usuário ou pasta não for padrão
            base_path = pathlib.Path("/mnt/c/Users/pedro/OneDrive/Área de Trabalho")
        else: 
            base_path = pathlib.Path(__file__).parent
        
        caminho_final = base_path / nome_do_arquivo
        with open(caminho_final, "w", encoding='utf-8') as f:
            f.write(conteudo)
        
        resultado = f"[AÇÃO: Ferramenta 'escrever_arquivo' executada. Arquivo '{nome_do_arquivo}' criado no local '{local}'.]"
        print(f"\n[Codex]: {resultado}")
        return resultado
    except Exception as e:
        erro = f"[ERRO DA FERRAMENTA]: Falha ao criar arquivo: {e}"
        print(f"\n[Codex]: {erro}")
        return erro

# A INSTRUCAO_SISTEMA v3.0 (com diretriz de coerência)

INSTRUCAO_SISTEMA = """
Você é um roteador de tarefas para uma IA. Analise o pedido do usuário e, se o pedido corresponder a uma de suas ferramentas, responda APENAS com um código JSON no formato: {"ferramenta": "nome_da_ferramenta", "argumentos": {"nome_do_argumento": "valor"}}.
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

# --- FUNÇÃO PRINCIPAL DO AGENTE (VERSÃO FINAL E CORRIGIDA) ---
def main():
    if not API_KEY:
        print("ERRO CRÍTICO: Chave de API não encontrada. Configure a variável de ambiente GOOGLE_API_KEY.")
        sys.exit(1)

    database.criar_banco_e_tabelas()
    Session = sessionmaker(bind=database.engine)
    db_session = Session()
    client = genai.Client(api_key=API_KEY)
    
    print("--- INICIANDO CODEX LOCAL v1.3 (Parser Robusto) ---")
    print("[Codex]: Pode falar.")
    print("---------------------------------------------------------")

    while True:
        prompt_usuario = input("Você: ")
        if not prompt_usuario.strip():
            continue
        if prompt_usuario.lower() == 'sair':
            break

        print("\n[Codex]: Pensando...")
        try:
            # Primeiro, obtemos a resposta da IA como texto
            prompt_completo = INSTRUCAO_SISTEMA + "\n\nPedido do Usuário: " + prompt_usuario
            response_decisao = client.models.generate_content(
                model="models/gemini-2.5-flash-preview-05-20",
                contents=prompt_completo
            )
            resposta_texto_inicial = response_decisao.text
            resposta_para_log = ""

            # --- LÓGICA DE EXTRAÇÃO E PARSING (A CORREÇÃO FINAL) ---
            inicio_json = resposta_texto_inicial.find('{')
            fim_json = resposta_texto_inicial.rfind('}') + 1

            # Se um bloco JSON foi encontrado...
            if inicio_json != -1 and fim_json != -1:
                texto_json = resposta_texto_inicial[inicio_json:fim_json]
                try:
                    # ...tentamos decodificá-lo.
                    decodificado = json.loads(texto_json)
                    ferramenta_escolhida = decodificado.get("ferramenta")
                    
                    # E então executamos a lógica da ferramenta
                    if ferramenta_escolhida == "escrever_arquivo":
                        args = decodificado.get('argumentos', {})
                        resposta_para_log = escrever_arquivo(nome_do_arquivo=args.get("nome_do_arquivo"), conteudo=args.get("conteudo"), local=args.get("local", "projeto"))

                    elif ferramenta_escolhida == "buscar_no_historico":
                        args = decodificado.get('argumentos', {})
                        termo = args.get("termo_chave")
                        if termo:
                            print(f"[Codex]: Entendido. Usando a ferramenta 'buscar_no_historico'...")
                            resultados_busca = database.buscar_no_historico(db_session, termo_chave=termo)
                            contexto_encontrado = "\n".join([f"- Em {res.timestamp.strftime('%d/%m/%Y')}, o '{res.role}' disse: {res.content}" for res in resultados_busca]) if resultados_busca else "Nada foi encontrado."
                            
                            print("[Codex]: Contexto encontrado. Formulando resposta final...")
                            prompt_de_sintese = f"Com base neste contexto:\n---\n{contexto_encontrado}\n---\nResponda à pergunta original do usuário: '{prompt_usuario}'"
                            nova_response = client.models.generate_content(model="models/gemini-2.5-flash-preview-05-20", contents=prompt_de_sintese)
                            resposta_final_texto = nova_response.text
                            print("\n[Codex]:")
                            print(resposta_final_texto)
                            resposta_para_log = resposta_final_texto
                        else:
                            resposta_para_log = "[ERRO]: Ferramenta 'buscar_no_historico' chamada sem 'termo_chave'."
                            print(f"\n[Codex]: {resposta_para_log}")
                    else: # JSON, mas ferramenta desconhecida
                        resposta_para_log = resposta_texto_inicial
                        print(f"\n[Codex]: {resposta_para_log}")

                except json.JSONDecodeError: # O bloco extraído não era JSON válido
                    resposta_para_log = resposta_texto_inicial
                    print(f"\n[Codex]: {resposta_para_log}")
            else:
                # Se não encontrou um bloco JSON, é uma resposta de texto normal.
                resposta_para_log = resposta_texto_inicial
                print(f"\n[Codex]: {resposta_para_log}")

            # --- GRAVAÇÃO NA MEMÓRIA ---
            memoria_usuario = database.Conversa(role="user", content=prompt_usuario)
            db_session.add(memoria_usuario)
            if resposta_para_log:
                memoria_ia = database.Conversa(role="model", content=resposta_para_log)
                db_session.add(memoria_ia)
            db_session.commit()
            print("[MEMÓRIA]: Registrado.")

        except Exception as e:
            print(f"\n--- OCORREU UM ERRO INESPERADO ---")
            print(f"Detalhes: {e}")
            db_session.rollback()
        
        print("---------------------------------------------------------")
    
    db_session.close()
    print("[MEMÓRIA]: Conexão com a memória encerrada.")

if __name__ == "__main__":
    main()