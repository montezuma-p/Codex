# 🔑 Configuração de Chaves API para Integração Completa

Este documento explica como configurar as chaves de API necessárias para que todas as integrações do Codex CLI funcionem perfeitamente.

## 🚀 Como Configurar

### 1. Google API Key (Para Google Search)

#### 1.1. Criar Projeto no Google Cloud
1. Acesse [Google Cloud Console](https://console.cloud.google.com/)
2. Faça login com sua conta Google
3. Clique em **Novo Projeto** ou selecione um projeto existente
4. Dê um nome ao projeto (ex: "codex-cli-integrations")

#### 1.2. Habilitar Custom Search API
1. No painel, vá para **APIs e Serviços** → **Biblioteca**
2. Procure por "Custom Search API"
3. Clique em **Habilitar**

#### 1.3. Criar Credenciais
1. Vá para **APIs e Serviços** → **Credenciais**
2. Clique em **+ Criar Credenciais** → **Chave de API**
3. Copie a chave gerada

#### 1.4. Criar Search Engine
1. Acesse [Google Custom Search Engine](https://cse.google.com/)
2. Clique em **Adicionar**
3. Em "Sites a pesquisar", digite: `*` (para pesquisar toda a web)
4. Clique em **Criar**
5. Copie o **ID do mecanismo de pesquisa** (Search engine ID)

#### 1.5. Configurar Variáveis de Ambiente
```bash
export GOOGLE_API_KEY="sua_chave_api_aqui"
export GOOGLE_SEARCH_API_KEY="sua_chave_api_aqui"  # Mesma chave
export GOOGLE_SEARCH_CX="seu_search_engine_id_aqui"
```

### 2. WolframAlpha APP ID (Para Consultas Matemáticas/Científicas)

#### 2.1. Criar Conta
1. Acesse [WolframAlpha Developer Portal](https://products.wolframalpha.com/api/)
2. Clique em **Get Started for Free**
3. Crie uma conta gratuita

#### 2.2. Obter APP ID
1. Após login, vá para **My Apps**
2. Clique em **Get an AppID**
3. Escolha o plano gratuito (2000 consultas/mês)
4. Preencha os dados da aplicação:
   - **Application name**: "Codex CLI"
   - **Description**: "Personal AI assistant with mathematical capabilities"
5. Copie o **AppID** gerado

#### 2.3. Configurar Variável de Ambiente
```bash
export WOLFRAMALPHA_APPID="seu_app_id_aqui"
```

### 3. GitHub Token (Opcional - Para Maior Limite de API)

#### 3.1. Criar Personal Access Token
1. Vá para [GitHub Settings](https://github.com/settings/tokens)
2. Clique em **Generate new token** → **Generate new token (classic)**
3. Configure:
   - **Note**: "Codex CLI Integration"
   - **Expiration**: Escolha o período desejado
   - **Scopes**: Selecione apenas **public_repo** (para repositórios públicos)
4. Clique em **Generate token**
5. Copie o token gerado (você só verá uma vez!)

#### 3.2. Configurar Variável de Ambiente
```bash
export GITHUB_TOKEN="seu_token_aqui"
```

## 🔧 Configuração Permanente

### Linux/macOS
Adicione as variáveis ao seu arquivo `~/.bashrc` ou `~/.zshrc`:

```bash
# Codex CLI API Keys
export GOOGLE_API_KEY="sua_chave_aqui"
export GOOGLE_SEARCH_API_KEY="sua_chave_aqui"
export GOOGLE_SEARCH_CX="seu_cx_aqui"
export WOLFRAMALPHA_APPID="seu_appid_aqui"
export GITHUB_TOKEN="seu_token_aqui"  # Opcional
```

Depois execute:
```bash
source ~/.bashrc  # ou ~/.zshrc
```

### Windows
Usando Command Prompt:
```cmd
setx GOOGLE_API_KEY "sua_chave_aqui"
setx GOOGLE_SEARCH_API_KEY "sua_chave_aqui"
setx GOOGLE_SEARCH_CX "seu_cx_aqui"
setx WOLFRAMALPHA_APPID "seu_appid_aqui"
setx GITHUB_TOKEN "seu_token_aqui"
```

### Usando .env (Desenvolvimento)
Crie um arquivo `.env` na raiz do projeto:
```env
GOOGLE_API_KEY=sua_chave_aqui
GOOGLE_SEARCH_API_KEY=sua_chave_aqui
GOOGLE_SEARCH_CX=seu_cx_aqui
WOLFRAMALPHA_APPID=seu_appid_aqui
GITHUB_TOKEN=seu_token_aqui
```

## ✅ Verificar Configuração

Execute o Codex CLI e teste cada integração:

```bash
# Teste Google Search
python -m codex
# Digite: "pesquise sobre Python no Google"

# Teste WolframAlpha
# Digite: "qual é a derivada de x²+3x?"

# Teste GitHub
# Digite: "encontre repositórios sobre machine learning"

# Teste Wikipedia (não precisa de API)
# Digite: "o que é inteligência artificial?"
```

## 📊 Limites das APIs Gratuitas

| Serviço | Limite Gratuito | Limite com Token/Key |
|---------|-----------------|---------------------|
| **Google Search** | - | 100 pesquisas/dia |
| **WolframAlpha** | - | 2000 consultas/mês |
| **GitHub** | 60 req/hora | 5000 req/hora |
| **Wikipedia** | Ilimitado | Ilimitado |
| **StackOverflow** | Ilimitado | Ilimitado |

## 🚨 Segurança

- ⚠️ **Nunca** commite chaves de API no código
- 🔒 Use variáveis de ambiente ou arquivos `.env`
- 🗂️ Adicione `.env` ao `.gitignore`
- 🔄 Rotacione as chaves periodicamente
- 👥 Para projetos em equipe, use GitHub Secrets ou similar

## 🔍 Resolução de Problemas

### Erro: "API key not found"
- Verifique se a variável de ambiente está configurada corretamente
- Execute `echo $NOME_DA_VARIAVEL` para verificar

### Erro: "403 Forbidden"
- Sua chave pode estar inválida ou expirada
- Verifique se habilitou a API correta no Google Cloud

### Erro: "Quota exceeded"
- Você atingiu o limite da API gratuita
- Considere upgrade para plano pago ou aguarde reset do limite

### Erro: "Invalid search engine ID"
- Verifique se copiou o CX correto do Google Custom Search
- O ID deve ter formato similar a: `017576662512468239146:omuauf_lfve`
