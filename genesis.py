from google import genai 
import os
import sys
API_KEY = os.getenv("GOOGLE_API_KEY")
def main():
    """
    Função principal que organiza e executa a lógica da IA.
    """
    print("--- INICIANDO CODEX LOCAL vM2.0 (Corrigido) ---")
    if not API_KEY:
        print("\nERRO CRÍTICO: Chave de API não foi configurada.")
        print("Verifique a variável GOOGLE_API_KEY no seu arquivo .bashrc")
        sys.exit(1)
    try:
        client = genai.Client(api_key=API_KEY)
        print("\n[Codex v2.0]: FINALMENTE CARALHO, BORA TRABALHAR!!!.")
        print("Agora que eu to aqui dentro do teu PC, me diz ai. VAMO FAZER OQ?.")
        print("---------------------------------------------------------")       
        while True:
            prompt = input("Você: ")
            if prompt.lower() == 'sair':
                print("[Codex]: Encerrando sessão. Até a próxima, Engenheiro.")
                break
            print("\n[Codex]: Pensando...")            
            response = client.models.generate_content(
                model="models/gemini-2.5-flash-preview-05-20", 
                contents=prompt
            )      
            print("\n[Codex]:")
            print(response.text)
            print("---------------------------------------------------------")
    except Exception as e:
        print(f"\n--- OCORREU UM ERRO INESPERADO ---")
        print(f"Detalhes: {e}")
if __name__ == "__main__":
    main()