#!/bin/bash

# 🔑 Codex CLI - Script de Configuração de API Keys
# Este script ajuda a configurar as variáveis de ambiente necessárias

echo "🔑 Configuração de API Keys para Codex CLI"
echo "=========================================="
echo ""

# Função para validar entrada não vazia
validate_input() {
    while [ -z "$1" ]; do
        echo "❌ Entrada não pode estar vazia. Tente novamente:"
        read -p "$2" input
        eval "$3='$input'"
        set -- "$input" "$2" "$3"
    done
}

# Verificar se .env já existe
if [ -f ".env" ]; then
    echo "⚠️  Arquivo .env já existe. Deseja sobrescrever? (y/N)"
    read -r response
    if [[ ! "$response" =~ ^[Yy]$ ]]; then
        echo "❌ Operação cancelada."
        exit 0
    fi
fi

echo "📝 Configuração das chaves de API:"
echo ""

# Google API Key
echo "1️⃣  Google API Key (para Google Search)"
echo "   Obtenha em: https://console.cloud.google.com/"
read -p "   Digite sua Google API Key: " google_api_key
validate_input "$google_api_key" "   Digite sua Google API Key: " google_api_key

echo ""
echo "2️⃣  Google Custom Search Engine ID"
echo "   Obtenha em: https://cse.google.com/"
read -p "   Digite seu Search Engine ID: " google_cx
validate_input "$google_cx" "   Digite seu Search Engine ID: " google_cx

echo ""
echo "3️⃣  WolframAlpha APP ID (opcional)"
echo "   Obtenha em: https://products.wolframalpha.com/api/"
read -p "   Digite seu WolframAlpha APP ID (ou ENTER para pular): " wolfram_appid

echo ""
echo "4️⃣  GitHub Token (opcional)"
echo "   Obtenha em: https://github.com/settings/tokens"
read -p "   Digite seu GitHub Token (ou ENTER para pular): " github_token

# Criar arquivo .env
echo "💾 Criando arquivo .env..."
cat > .env << EOF
# Codex CLI API Keys
# Configurado em $(date)

# Google Search (obrigatório para busca no Google)
GOOGLE_API_KEY=$google_api_key
GOOGLE_SEARCH_API_KEY=$google_api_key
GOOGLE_SEARCH_CX=$google_cx

EOF

# Adicionar WolframAlpha se fornecido
if [ ! -z "$wolfram_appid" ]; then
    echo "# WolframAlpha (opcional - para consultas matemáticas/científicas)" >> .env
    echo "WOLFRAMALPHA_APPID=$wolfram_appid" >> .env
    echo "" >> .env
fi

# Adicionar GitHub se fornecido
if [ ! -z "$github_token" ]; then
    echo "# GitHub (opcional - para maior limite de API)" >> .env
    echo "GITHUB_TOKEN=$github_token" >> .env
    echo "" >> .env
fi

# Adicionar ao .gitignore se não existir
if ! grep -q "^\.env$" .gitignore 2>/dev/null; then
    echo "🔒 Adicionando .env ao .gitignore para segurança..."
    echo ".env" >> .gitignore
fi

echo "✅ Configuração concluída!"
echo ""
echo "📋 Próximos passos:"
echo "   1. Execute: source .env"
echo "   2. Ou reinicie o terminal"
echo "   3. Teste o CLI: python -m codex"
echo ""
echo "🔍 Para verificar se funcionou:"
echo "   echo \$GOOGLE_API_KEY"
echo ""
echo "📚 Para mais informações, consulte:"
echo "   docs/pt/configuracao-api-keys.md"

# Tornar o script executável
chmod +x "$0" 2>/dev/null
