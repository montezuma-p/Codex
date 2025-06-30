#!/bin/bash
# Script para automatizar releases do projeto

set -e

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Função para print colorido
print_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Verificar se estamos no branch correto
current_branch=$(git branch --show-current)
if [[ "$current_branch" != "master" && "$current_branch" != "main" ]]; then
    print_error "Você deve estar no branch master ou main para fazer um release"
    exit 1
fi

# Verificar se há mudanças não commitadas
if [[ -n $(git status --porcelain) ]]; then
    print_error "Há mudanças não commitadas. Faça commit antes do release."
    exit 1
fi

# Pedir a nova versão
echo "Versão atual no pyproject.toml:"
grep "version =" pyproject.toml

echo ""
read -p "Digite a nova versão (ex: 1.2.0): " NEW_VERSION

if [[ -z "$NEW_VERSION" ]]; then
    print_error "Versão não pode estar vazia"
    exit 1
fi

# Atualizar versão no pyproject.toml
print_info "Atualizando versão no pyproject.toml..."
sed -i "s/version = \".*\"/version = \"$NEW_VERSION\"/" pyproject.toml

# Executar testes
print_info "Executando testes..."
pytest --cov=src/codex --cov-report=term-missing -v

if [[ $? -ne 0 ]]; then
    print_error "Testes falharam! Abortando release."
    exit 1
fi

# Commit da nova versão
print_info "Commitando nova versão..."
git add pyproject.toml
git commit -m "chore: bump version to $NEW_VERSION"

# Criar tag
print_info "Criando tag v$NEW_VERSION..."
git tag -a "v$NEW_VERSION" -m "Release version $NEW_VERSION"

# Push
print_info "Enviando commits e tags..."
git push origin "$current_branch"
git push origin "v$NEW_VERSION"

print_info "✅ Release v$NEW_VERSION criado com sucesso!"
print_info "🚀 O GitHub Actions irá automaticamente:"
print_info "   - Executar todos os testes"
print_info "   - Buildar o pacote"
print_info "   - Publicar no PyPI"
print_info "   - Atualizar a documentação"
print_info "   - Criar o release no GitHub"

print_warning "⚠️  Certifique-se de que o PYPI_API_TOKEN está configurado nos secrets do GitHub!"
