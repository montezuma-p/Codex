# Codex CLI – Ferramentas de IA, APIs e Automação

Bem-vindo(a) ao Codex! Este projeto é um laboratório de integração de IA, automação e APIs para desenvolvedores.

## Funcionalidades Principais
- Armazena conversas e histórico em SQLite.
- Busca por palavras-chave no histórico.
- Interação com IA Gemini (Google) via CLI.
- Ferramentas integradas:
  - **escrever_arquivo**: cria/sobrescreve arquivos de texto.
  - **listar_arquivos**: lista arquivos e pastas do projeto.
  - **ler_arquivo**: lê arquivos de texto do projeto.
  - **consultar_wikipedia**: busca resumos na Wikipedia.
  - **consultar_stackoverflow**: busca perguntas e respostas técnicas.
  - **consultar_google**: retorna os 3 primeiros resultados do Google Search.
  - **consultar_github**: mostra repositórios populares sobre um termo.
  - **consultar_wolframalpha**: responde perguntas matemáticas/científicas.

## Como Usar
1. Instale as dependências:
   ```bash
   pip install -r requirements-dev.txt
   ```
2. Configure as variáveis de ambiente necessárias:
   ```bash
   export GOOGLE_API_KEY='sua-api-key-gemini'
   export GOOGLE_SEARCH_API_KEY='sua-api-key-google-search'
   export GOOGLE_SEARCH_CX='seu-cx-google-search'
   export GITHUB_TOKEN='seu-token-github'  # (opcional, para mais requisições)
   export WOLFRAMALPHA_APPID='seu-appid-wolframalpha'
   ```
3. Inicialize o banco de dados:
   ```bash
   python database.py
   ```
4. Rode o CLI:
   ```bash
   python cli_agent.py
   ```

## Exemplos de Uso
- "Codex, crie um arquivo chamado 'exemplo.txt' com o conteúdo 'olá mundo'"
- "Liste os arquivos da pasta docs"
- "Leia o arquivo README.md"
- "Pesquise no Google por 'Python asyncio'"
- "Busque repositórios sobre 'machine learning' no GitHub"
- "Qual a raiz quadrada de 144 no WolframAlpha?"
- "O que significa API segundo a Wikipedia?"
- "Como faço um request HTTP em Python? (Stack Overflow)"

Veja mais exemplos e dicas em `docs/guia_didatico/ferramentas_externas.md`.

## Roadmap
Consulte `docs/roadmap.md` para próximos passos e visão de futuro.

## Licença
MIT

## ✅ FUNCIONALIDADE RESTABELECIDA (28/06/2025)

As integrações externas (Google Search, Stack Overflow, WolframAlpha, Wikipedia, GitHub) foram corrigidas e padronizadas:

- Argumentos validados e tratados de forma uniforme.
- Mensagens de erro e timeout padronizadas.
- Testes práticos e automatizados confirmam a resolução.

Se encontrar qualquer novo problema, por favor abra uma issue ou consulte o diário de bordo para atualizações.

---

Projeto didático, aberto a sugestões e contribuições!
