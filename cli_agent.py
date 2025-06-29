import os
import sys
import pathlib
import json
import requests
from google import genai
import database

def checar_api_key():
    API_KEY = os.getenv("GOOGLE_API_KEY")
    if not API_KEY:
        print("ERRO CRÍTICO: Chave de API não encontrada.")
        sys.exit(1)
    return API_KEY

client = None
API_KEY = os.getenv("GOOGLE_API_KEY")
if API_KEY:
    client = genai.Client(api_key=API_KEY)
MODELO_IA = "models/gemini-2.5-flash-preview-05-20"
PROMPT_MESTRA = """
Você é Codex, um agente de IA parceiro de programação do Montezuma.
Seu papel é ajudar de forma prática, objetiva e imersiva, sempre mantendo o contexto da conversa.

Ferramentas disponíveis:
- escrever_arquivo: cria ou sobrescreve arquivos de texto no projeto.
- buscar_no_historico: busca informações em conversas anteriores.
- listar_arquivos: mostra arquivos e pastas de um diretório do projeto.
- ler_arquivo: lê e mostra o conteúdo de um arquivo de texto do projeto.
- consultar_wikipedia: busca um resumo de um termo na Wikipedia em português.
- consultar_stackoverflow: busca perguntas e respostas relacionadas no Stack Overflow.
- consultar_google: busca resultados no Google Search (3 primeiros links e resumos).
- consultar_github: busca repositórios no GitHub relacionados ao termo.
- consultar_wolframalpha: faz perguntas matemáticas/científicas ao WolframAlpha.

Quando identificar que o usuário quer usar uma dessas ferramentas, responda apenas com um JSON no formato:
{"ferramenta": "nome_da_ferramenta", "argumentos": {"nome_do_argumento": "valor"}}

Se não for caso de ferramenta, responda normalmente, sempre mantendo a naturalidade e o contexto.

Imersão: nunca perca o contexto da conversa, mesmo após usar ferramentas.
"""

def escrever_arquivo(**kwargs):
    nome_do_arquivo = kwargs.get("nome_do_arquivo")
    conteudo = kwargs.get("conteudo")
    # Sempre salva na pasta do projeto
    base_path = pathlib.Path(__file__).parent
    try:
        caminho_final = base_path / nome_do_arquivo
        with open(caminho_final, "w", encoding='utf-8') as f:
            f.write(conteudo)
        return f"[AÇÃO: Arquivo '{nome_do_arquivo}' criado na pasta do projeto.]"
    except Exception as e:
        return f"[ERRO DA FERRAMENTA]: {e}"

def listar_arquivos(**kwargs):
    """
    Lista arquivos e pastas do diretório informado (relativo ao projeto).
    Parâmetro extra 'base_path' (Path) para facilitar testes.
    """
    caminho = kwargs.get("caminho", ".")
    base_path = kwargs.get("base_path", pathlib.Path(__file__).parent)
    dir_path = (base_path / caminho).resolve()
    if not dir_path.exists() or not dir_path.is_dir():
        return f"[ERRO]: Diretório '{caminho}' não encontrado."
    itens = sorted(os.listdir(dir_path))
    if not itens:
        return f"[INFO]: Diretório '{caminho}' está vazio."
    return f"Conteúdo de '{caminho}':\n" + "\n".join(itens)

def ler_arquivo(**kwargs):
    """
    Lê e retorna o conteúdo de um arquivo de texto de projeto.
    Parâmetro extra 'base_path' (Path) para facilitar testes.
    """
    nome_do_arquivo = kwargs.get("nome_do_arquivo")
    base_path = kwargs.get("base_path", pathlib.Path(__file__).parent)
    if not nome_do_arquivo:
        return "[ERRO]: Nome do arquivo não informado."
    caminho_final = (base_path / nome_do_arquivo).resolve()
    try:
        if not caminho_final.exists() or not caminho_final.is_file():
            return f"[ERRO]: Arquivo '{nome_do_arquivo}' não encontrado."
        with open(caminho_final, "r", encoding='utf-8') as f:
            conteudo = f.read()
        if not conteudo.strip():
            return f"[INFO]: Arquivo '{nome_do_arquivo}' está vazio."
        # Limita a resposta para evitar prints gigantes
        if len(conteudo) > 2000:
            return f"[INFO]: Arquivo muito grande, mostrando as primeiras 2000 letras:\n{conteudo[:2000]}..."
        return f"Conteúdo de '{nome_do_arquivo}':\n{conteudo}"
    except Exception as e:
        return f"[ERRO DA FERRAMENTA]: {e}"

def _extrair_termo(kwargs):
    termo = kwargs.get("termo")
    if termo is None:
        return None
    if isinstance(termo, str):
        termo = termo.strip()
        if not termo:
            return None
    return termo

def consultar_wikipedia(**kwargs):
    """
    Consulta um termo na Wikipedia e retorna o resumo.
    """
    termo = _extrair_termo(kwargs)
    if not termo:
        return "[ERRO]: Nenhum termo informado para consulta."
    url = f"https://pt.wikipedia.org/api/rest_v1/page/summary/{termo.replace(' ', '_')}"
    try:
        resp = requests.get(url, timeout=5)
        if resp.status_code == 404:
            return f"[INFO]: Não encontrado na Wikipedia: '{termo}'"
        resp.raise_for_status()
        data = resp.json()
        resumo = data.get("extract")
        if not resumo:
            return f"[INFO]: Nenhum resumo disponível para '{termo}'"
        if len(resumo) > 1500:
            return f"[INFO]: Resumo muito grande, mostrando as primeiras 1500 letras:\n{resumo[:1500]}..."
        return f"Wikipedia – {termo}:\n{resumo}"
    except requests.exceptions.Timeout:
        return "[ERRO DA FERRAMENTA]: Timeout ao consultar a Wikipedia. Tente novamente mais tarde."
    except Exception as e:
        return f"[ERRO DA FERRAMENTA]: {e}"

def consultar_stackoverflow(**kwargs):
    """
    Consulta o Stack Overflow por perguntas e respostas relacionadas a um termo.
    Retorna o título, link e resposta mais votada (se houver).
    """
    termo = _extrair_termo(kwargs)
    if not termo:
        return "[ERRO]: Nenhum termo informado para consulta."
    url = (
        f"https://api.stackexchange.com/2.3/search/advanced?order=desc&sort=relevance&q={termo}&site=stackoverflow&filter=!9_bDDxJY5"
    )
    try:
        resp = requests.get(url, timeout=7)
        resp.raise_for_status()
        data = resp.json()
        if not data.get("items"):
            return f"[INFO]: Nenhuma pergunta encontrada para '{termo}' no Stack Overflow."
        pergunta = data["items"][0]
        titulo = pergunta.get("title")
        link = pergunta.get("link")
        # Buscar resposta mais votada para a pergunta
        id_pergunta = pergunta.get("question_id")
        url_respostas = f"https://api.stackexchange.com/2.3/questions/{id_pergunta}/answers?order=desc&sort=votes&site=stackoverflow&filter=withbody"
        try:
            resp2 = requests.get(url_respostas, timeout=7)
            resp2.raise_for_status()
            respostas = resp2.json().get("items", [])
            if respostas:
                resposta = respostas[0].get("body", "[Sem resposta]")
                import re
                resposta_limpa = re.sub(r'<.*?>', '', resposta)
                if len(resposta_limpa) > 1200:
                    resposta_limpa = resposta_limpa[:1200] + '...'
            else:
                resposta_limpa = "[Sem resposta disponível]"
        except requests.exceptions.Timeout:
            resposta_limpa = "[ERRO DA FERRAMENTA]: Timeout ao buscar resposta no Stack Overflow."
        except Exception as e:
            resposta_limpa = f"[ERRO DA FERRAMENTA]: {e}"
        return f"Stack Overflow – {titulo}\n{link}\nResposta mais votada:\n{resposta_limpa}"
    except requests.exceptions.Timeout:
        return "[ERRO DA FERRAMENTA]: Timeout ao consultar o Stack Overflow. Tente novamente mais tarde."
    except Exception as e:
        return f"[ERRO DA FERRAMENTA]: {e}"

def consultar_google(**kwargs):
    """
    Consulta o Google Search e retorna os 3 primeiros resultados (título, link e snippet).
    Requer a variável de ambiente GOOGLE_SEARCH_API_KEY e GOOGLE_SEARCH_CX.
    """
    termo = _extrair_termo(kwargs)
    api_key = os.getenv("GOOGLE_SEARCH_API_KEY")
    cx = os.getenv("GOOGLE_SEARCH_CX")
    if not termo:
        return "[ERRO]: Nenhum termo informado para consulta."
    if not api_key or not cx:
        return "[ERRO]: GOOGLE_SEARCH_API_KEY ou GOOGLE_SEARCH_CX não configurados."
    url = (
        f"https://www.googleapis.com/customsearch/v1?q={termo}&key={api_key}&cx={cx}&num=3&hl=pt"
    )
    try:
        resp = requests.get(url, timeout=7)
        resp.raise_for_status()
        data = resp.json()
        items = data.get("items", [])
        if not items:
            return f"[INFO]: Nenhum resultado encontrado para '{termo}' no Google."
        resultados = []
        for item in items:
            titulo = item.get("title", "[Sem título]")
            link = item.get("link", "[Sem link]")
            snippet = item.get("snippet", "[Sem resumo]")
            if len(snippet) > 400:
                snippet = snippet[:400] + '...'
            resultados.append(f"- {titulo}\n{link}\n{snippet}")
        return f"Google Search – Resultados para '{termo}':\n" + "\n\n".join(resultados)
    except requests.exceptions.Timeout:
        return "[ERRO DA FERRAMENTA]: Timeout ao consultar o Google Search. Tente novamente mais tarde."
    except Exception as e:
        return f"[ERRO DA FERRAMENTA]: {e}"

def consultar_github(**kwargs):
    """
    Busca repositórios ou issues no GitHub relacionados a um termo.
    Retorna os 3 primeiros resultados (nome, link, descrição).
    """
    termo = _extrair_termo(kwargs)
    if not termo:
        return "[ERRO]: Nenhum termo informado para consulta."
    url = f"https://api.github.com/search/repositories?q={termo}&sort=stars&order=desc&per_page=3"
    headers = {"Accept": "application/vnd.github+json"}
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    try:
        resp = requests.get(url, headers=headers, timeout=7)
        resp.raise_for_status()
        data = resp.json()
        items = data.get("items", [])
        if not items:
            return f"[INFO]: Nenhum repositório encontrado para '{termo}' no GitHub."
        resultados = []
        for item in items:
            nome = item.get("full_name", "[Sem nome]")
            link = item.get("html_url", "[Sem link]")
            desc = item.get("description", "[Sem descrição]")
            if desc and len(desc) > 300:
                desc = desc[:300] + '...'
            resultados.append(f"- {nome}\n{link}\n{desc}")
        return f"GitHub – Repositórios para '{termo}':\n" + "\n\n".join(resultados)
    except requests.exceptions.Timeout:
        return "[ERRO DA FERRAMENTA]: Timeout ao consultar o GitHub. Tente novamente mais tarde."
    except Exception as e:
        return f"[ERRO DA FERRAMENTA]: {e}"

def consultar_wolframalpha(**kwargs):
    """
    Consulta o WolframAlpha para perguntas matemáticas, científicas ou gerais.
    Requer a variável de ambiente WOLFRAMALPHA_APPID.
    """
    termo = _extrair_termo(kwargs)
    appid = os.getenv("WOLFRAMALPHA_APPID")
    if not termo:
        return "[ERRO]: Nenhum termo informado para consulta."
    if not appid:
        return "[ERRO]: WOLFRAMALPHA_APPID não configurado."
    url = f"https://api.wolframalpha.com/v1/result?i={requests.utils.quote(termo)}&appid={appid}"
    try:
        resp = requests.get(url, timeout=7)
        if resp.status_code == 501:
            return f"[INFO]: WolframAlpha não sabe responder a '{termo}'."
        resp.raise_for_status()
        resposta = resp.text
        if len(resposta) > 1200:
            resposta = resposta[:1200] + '...'
        return f"WolframAlpha – Resposta para '{termo}':\n{resposta}"
    except requests.exceptions.Timeout:
        return "[ERRO DA FERRAMENTA]: Timeout ao consultar o WolframAlpha. Tente novamente mais tarde."
    except Exception as e:
        return f"[ERRO DA FERRAMENTA]: {e}"

def sugerir_pergunta_frequente(session):
    """
    Sugere ao usuário uma das perguntas/comandos mais frequentes do histórico.
    """
    sugestoes = database.perguntas_mais_frequentes(session, limite=1)
    if sugestoes:
        print(f"[Sugestão Codex] Você costuma perguntar: '{sugestoes[0]}' (pressione Enter para repetir)")
        return sugestoes[0]
    return None

FERRAMENTAS = {
    "escrever_arquivo": escrever_arquivo,
    "listar_arquivos": listar_arquivos,
    "ler_arquivo": ler_arquivo,
    "consultar_wikipedia": consultar_wikipedia,
    "consultar_stackoverflow": consultar_stackoverflow,
    "consultar_google": consultar_google,
    "consultar_github": consultar_github,
    "consultar_wolframalpha": consultar_wolframalpha,
    # Adicione novas ferramentas aqui
}

def gerar_documentacao_ferramentas():
    """
    Gera documentação automática das ferramentas registradas no dicionário FERRAMENTAS.
    Retorna uma string formatada com nome, docstring e exemplo de chamada.
    """
    doc = ["# Documentação automática das ferramentas do Codex CLI\n"]
    for nome, func in FERRAMENTAS.items():
        doc.append(f"## {nome}\n")
        docstring = func.__doc__ or "(Sem descrição)"
        doc.append(docstring.strip() + "\n")
        doc.append(f"**Exemplo de chamada:**\n`{{\"ferramenta\": \"{nome}\", \"argumentos\": {{...}}}}`\n")
    return "\n".join(doc)

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--doc-ferramentas":
        doc = gerar_documentacao_ferramentas()
        doc_path = pathlib.Path(__file__).parent / "docs/guia_didatico/auto_documentacao_ferramentas.md"
        with open(doc_path, "w", encoding="utf-8") as f:
            f.write(doc)
        print(f"Documentação das ferramentas atualizada em {doc_path}")
        return
    checar_api_key()
    database.criar_banco_e_tabelas()
    session = database.Session()
    print("Bem-vindo ao Codex CLI! Digite 'sair' para encerrar.")
    while True:
        sugestao = sugerir_pergunta_frequente(session)
        prompt_usuario = input("Você: ")
        if prompt_usuario.strip() == '' and sugestao:
            prompt_usuario = sugestao
            print(f"(Repetindo pergunta frequente: {prompt_usuario})")
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
            elif ferramenta in FERRAMENTAS:
                resposta_ia = FERRAMENTAS[ferramenta](**decodificado.get('argumentos', {}))
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
