# Documentação automática das ferramentas do Codex CLI

## escrever_arquivo

(Sem descrição)

**Exemplo de chamada:**
`{"ferramenta": "escrever_arquivo", "argumentos": {...}}`

## listar_arquivos

Lista arquivos e pastas do diretório informado (relativo ao projeto).
    Parâmetro extra 'base_path' (Path) para facilitar testes.

**Exemplo de chamada:**
`{"ferramenta": "listar_arquivos", "argumentos": {...}}`

## ler_arquivo

Lê e retorna o conteúdo de um arquivo de texto de projeto.
    Parâmetro extra 'base_path' (Path) para facilitar testes.

**Exemplo de chamada:**
`{"ferramenta": "ler_arquivo", "argumentos": {...}}`

## consultar_wikipedia

Consulta um termo na Wikipedia e retorna o resumo.

**Exemplo de chamada:**
`{"ferramenta": "consultar_wikipedia", "argumentos": {...}}`

## consultar_stackoverflow

Consulta o Stack Overflow por perguntas e respostas relacionadas a um termo.
    Retorna o título, link e resposta mais votada (se houver).

**Exemplo de chamada:**
`{"ferramenta": "consultar_stackoverflow", "argumentos": {...}}`

## consultar_google

Consulta o Google Search e retorna os 3 primeiros resultados (título, link e snippet).
    Requer a variável de ambiente GOOGLE_SEARCH_API_KEY e GOOGLE_SEARCH_CX.

**Exemplo de chamada:**
`{"ferramenta": "consultar_google", "argumentos": {...}}`

## consultar_github

Busca repositórios ou issues no GitHub relacionados a um termo.
    Retorna os 3 primeiros resultados (nome, link, descrição).

**Exemplo de chamada:**
`{"ferramenta": "consultar_github", "argumentos": {...}}`

## consultar_wolframalpha

Consulta o WolframAlpha para perguntas matemáticas, científicas ou gerais.
    Requer a variável de ambiente WOLFRAMALPHA_APPID.

**Exemplo de chamada:**
`{"ferramenta": "consultar_wolframalpha", "argumentos": {...}}`
