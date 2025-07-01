#!/bin/bash

# 🔧 Script de Configuração das APIs do Codex CLI
# Este script te ajuda a configurar as variáveis de ambiente necessárias

echo "🔑 Configuração das APIs do Codex CLI"
echo "====================================="
echo

# Função para adicionar variável ao .bashrc
add_to_bashrc() {
    local var_name=$1
    local var_value=$2
    
    # Remove a variável se já existir
    sed -i "/^export $var_name=/d" ~/.bashrc
    
    # Adiciona a nova variável
    echo "export $var_name=\"$var_value\"" >> ~/.bashrc
    
    echo "✅ $var_name adicionada ao ~/.bashrc"
}

# Verifica se já existe configuração
check_existing() {
    local var_name=$1
    local current_value=$(printenv $var_name)
    
    if [ -n "$current_value" ]; then
        echo "⚠️  $var_name já está configurada: ${current_value:0:20}..."
        read -p "Deseja sobrescrever? (s/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Ss]$ ]]; then
            return 1
        fi
    fi
    return 0
}

echo "1. 🤖 Google Gemini API (OBRIGATÓRIO)"
echo "   Obtenha em: https://aistudio.google.com/app/apikey"
echo

if check_existing "GOOGLE_API_KEY"; then
    read -p "Cole sua chave do Gemini: " gemini_key
    if [ -n "$gemini_key" ]; then
        add_to_bashrc "GOOGLE_API_KEY" "$gemini_key"
    fi
fi

echo
echo "2. 🔍 Google Search API (OPCIONAL)"
echo "   Obtenha em: https://console.cloud.google.com/"
echo

read -p "Deseja configurar Google Search? (s/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Ss]$ ]]; then
    if check_existing "GOOGLE_SEARCH_API_KEY"; then
        read -p "Cole sua API Key do Google Search: " search_key
        if [ -n "$search_key" ]; then
            add_to_bashrc "GOOGLE_SEARCH_API_KEY" "$search_key"
        fi
    fi
    
    if check_existing "GOOGLE_SEARCH_CX"; then
        read -p "Cole seu Search Engine ID (CX): " search_cx
        if [ -n "$search_cx" ]; then
            add_to_bashrc "GOOGLE_SEARCH_CX" "$search_cx"
        fi
    fi
fi

echo
echo "3. 🧮 WolframAlpha API (OPCIONAL)"
echo "   Obtenha em: https://products.wolframalpha.com/api/"
echo

read -p "Deseja configurar WolframAlpha? (s/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Ss]$ ]]; then
    if check_existing "WOLFRAMALPHA_APPID"; then
        read -p "Cole seu APP ID do WolframAlpha: " wolfram_id
        if [ -n "$wolfram_id" ]; then
            add_to_bashrc "WOLFRAMALPHA_APPID" "$wolfram_id"
        fi
    fi
fi

echo
echo "4. 🐙 GitHub Token (OPCIONAL)"
echo "   Obtenha em: https://github.com/settings/tokens"
echo

read -p "Deseja configurar GitHub Token? (s/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Ss]$ ]]; then
    if check_existing "GITHUB_TOKEN"; then
        read -p "Cole seu GitHub Token: " github_token
        if [ -n "$github_token" ]; then
            add_to_bashrc "GITHUB_TOKEN" "$github_token"
        fi
    fi
fi

echo
echo "🔄 Recarregando configurações..."
source ~/.bashrc

echo
echo "✅ Configuração concluída!"
echo
echo "📋 Variáveis configuradas:"
[ -n "$GOOGLE_API_KEY" ] && echo "   ✅ GOOGLE_API_KEY"
[ -n "$GOOGLE_SEARCH_API_KEY" ] && echo "   ✅ GOOGLE_SEARCH_API_KEY"
[ -n "$GOOGLE_SEARCH_CX" ] && echo "   ✅ GOOGLE_SEARCH_CX"
[ -n "$WOLFRAMALPHA_APPID" ] && echo "   ✅ WOLFRAMALPHA_APPID"
[ -n "$GITHUB_TOKEN" ] && echo "   ✅ GITHUB_TOKEN"

echo
echo "🚀 Agora você pode testar o Codex CLI:"
echo "   python -m codex"
echo
echo "📖 Para mais detalhes, consulte: docs/guia_apis.md"
