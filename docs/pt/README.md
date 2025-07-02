# Codex CLI: Seu Assistente de IA e Automação no Terminal

**Codex CLI** é uma poderosa ferramenta de linha de comando projetada para desenvolvedores, engenheiros de dados e entusiastas de automação. Integre a inteligência artificial do Google Gemini diretamente no seu fluxo de trabalho, automatize tarefas repetitivas e consulte uma variedade de fontes de informação sem sair do terminal.

Com uma arquitetura extensível e foco na produtividade, o Codex CLI armazena seu histórico de interações, permite a busca por conversas passadas e oferece um conjunto de ferramentas integradas para interagir com seu sistema de arquivos e APIs externas.

## Principais Funcionalidades

*   **Inteligência Artificial Integrada:** Converse com o modelo de linguagem **Google Gemini** para gerar código, obter explicações, traduzir textos e muito mais.
*   **Histórico de Conversas:** Todas as suas interações são salvas localmente em um banco de dados SQLite, permitindo que você revise e busque por informações importantes a qualquer momento.
*   **Sistema de Ferramentas Extensível:**
    *   `escrever_arquivo`: Crie ou modifique arquivos no seu projeto.
    *   `listar_arquivos`: Navegue pela estrutura de diretórios.
    *   `ler_arquivo`: Leia o conteúdo de arquivos de texto.
    *   `consultar_wikipedia`: Obtenha resumos rápidos da Wikipedia.
    *   `consultar_stackoverflow`: Encontre soluções para problemas de programação.
    *   `consultar_google`: Realize buscas na web.
    *   E muito mais!
*   **Suporte Multilíngue:** A interface e a documentação estão disponíveis em Português e Inglês.
*   **Automação de Tarefas:** Use o Codex para automatizar scripts, gerar relatórios e interagir com seu ambiente de desenvolvimento.

## Instalação

Para instalar o Codex CLI, basta usar o `pip`:

```bash
pip install codex-cli-montezuma
```

## Como Usar o Codex CLI (Passo a Passo)

### 1. Configuração das Chaves de API

Para que o Codex possa usar a IA do Google Gemini e outras ferramentas de busca, você precisa fornecer suas chaves de API.

**Por que isso é necessário?**
*   **`GOOGLE_API_KEY`**: Autentica suas requisições à API do Gemini, permitindo que o Codex envie suas perguntas e receba respostas da IA.
*   **`GOOGLE_SEARCH_CX`**: É o ID do seu Mecanismo de Busca Personalizada do Google, necessário para a ferramenta `consultar_google`.

**Como configurar:**

Você tem duas opções:

*   **(Recomendado) Script de Configuração:** Se você clonou o repositório, pode usar nosso script interativo:
    ```bash
    ./scripts/setup-api-keys.sh
    ```
    Ele irá guiá-lo e criar um arquivo `.env` automaticamente.

*   **Manualmente (Arquivo `.env`):** Crie um arquivo chamado `.env` na pasta onde você executará o comando `codex` e adicione as seguintes linhas, substituindo pelos seus valores:
    ```
    GOOGLE_API_KEY="SUA_CHAVE_DE_API_DO_GEMINI"
    GOOGLE_SEARCH_CX="SEU_ID_DE_MECANISMO_DE_BUSCA_PERSONALIZADA"
    ```

> Para um guia detalhado sobre **como obter** essas chaves, consulte nosso [guia de configuração de API Keys](configuracao-api-keys.md).

### 2. Executando o Codex CLI

Com tudo instalado e configurado, você pode interagir com o Codex de várias maneiras:

**a) Modo Interativo (Chat)**

Este é o modo principal, onde você conversa com a IA. Para iniciar, simplesmente execute:
```bash
codex
```
A partir daí, você pode fazer perguntas, pedir para executar tarefas ou usar as ferramentas disponíveis. Para sair, digite `sair` ou `exit`.

**Exemplo de Interação:**
```
Você: Crie um arquivo chamado 'app.py' com um "Hello, World" em Python.

Codex: Claro, usando a ferramenta 'escrever_arquivo'.

(O arquivo app.py é criado no seu diretório)
```

**b) Comandos Diretos (Argumentos)**

Você pode executar comandos específicos diretamente da linha de comando, sem entrar no modo de chat.

*   **Buscar no Histórico:**
    ```bash
    codex --buscar "termo de busca"
    ```

*   **Gerar Relatório de Uso:**
    ```bash
    codex --relatorio-uso
    ```

*   **Exportar Histórico para JSONL:**
    ```bash
    codex --exportar-jsonl
    ```

*   **Gerar Documentação das Ferramentas:**
    ```bash
    codex --doc-ferramentas
    ```

*   **Ver Perfil de Uso:**
    ```bash
    codex --perfil
    ```

## Documentação Completa

Para explorar todas as funcionalidades, guias de contribuição e tutoriais, navegue pelos links no menu lateral ou acesse o [Índice Geral](indice_geral.md).
