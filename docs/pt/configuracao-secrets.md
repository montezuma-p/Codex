# 🔐 Configuração de Secrets para Automação Completa

Este documento explica como configurar os secrets necessários para que toda a automação funcione perfeitamente.

## 🚀 Como Configurar

### 1. Acesse as Configurações do Repositório
1. Vá para seu repositório no GitHub
2. Clique em **Settings** (Configurações)
3. No menu lateral, clique em **Secrets and variables** → **Actions**

### 2. Configurar PyPI Token (Obrigatório para publicação automática)

#### 2.1. Criar Token no PyPI
1. Acesse [pypi.org](https://pypi.org)
2. Faça login na sua conta
3. Vá em **Account settings** → **API tokens**
4. Clique em **Add API token**
5. Defina:
   - **Token name**: `github-actions-codex` (ou outro nome)
   - **Scope**: **Entire account** (para simplicidade) ou **Specific project** (mais seguro)
6. Clique em **Add token**
7. **COPIE O TOKEN** (só aparece uma vez!)

#### 2.2. Adicionar no GitHub
1. No GitHub, em **Secrets and variables** → **Actions**
2. Clique em **New repository secret**
3. Configure:
   - **Name**: `PYPI_API_TOKEN`
   - **Secret**: Cole o token do PyPI (começa com `pypi-`)
4. Clique em **Add secret**

### 3. Configurar Environment (Recomendado)

Para maior segurança, configure um environment chamado `pypi`:

1. Vá em **Settings** → **Environments**
2. Clique em **New environment**
3. Nome: `pypi`
4. Configure:
   - **Required reviewers**: Adicione você mesmo (opcional)
   - **Deployment branches**: Apenas `master` e `main`
5. Em **Environment secrets**, adicione:
   - **Name**: `PYPI_API_TOKEN`
   - **Value**: Seu token do PyPI

## 🔧 Secrets Necessários

| Secret | Descrição | Obrigatório |
|--------|-----------|-------------|
| `PYPI_API_TOKEN` | Token para publicar no PyPI | ✅ Sim |
| `GITHUB_TOKEN` | Automático do GitHub | ✅ Automático |

## 🧪 Testando a Configuração

Para testar se tudo está funcionando:

```bash
# 1. Faça uma mudança pequena
echo "# Test" >> README.md

# 2. Commit e push
git add README.md
git commit -m "test: verificar automação"
git push

# 3. Acompanhe em GitHub → Actions
```

## 🚀 Fazendo um Release

Duas opções:

### Opção 1: Script Automatizado (Recomendado)
```bash
make release
```

### Opção 2: Manual
```bash
# 1. Atualizar versão no pyproject.toml
# 2. Commit
git add pyproject.toml
git commit -m "chore: bump version to 1.2.0"

# 3. Criar tag
git tag -a "v1.2.0" -m "Release version 1.2.0"

# 4. Push
git push origin master
git push origin v1.2.0
```

## 🔍 Monitoramento

Acompanhe os workflows em:
- **GitHub → Actions** (para ver execuções)
- **PyPI → Your projects** (para ver publicações)
- **GitHub Pages** (para ver documentação)

## ❗ Troubleshooting

### Erro: "PYPI_API_TOKEN not found"
- Verifique se o secret está configurado corretamente
- Confirme o nome: `PYPI_API_TOKEN` (case-sensitive)

### Erro: "Authentication failed"
- Regenere o token no PyPI
- Atualize o secret no GitHub

### Workflow não executa
- Verifique se está no branch `master` ou `main`
- Confirme que o arquivo `.github/workflows/*.yml` está commitado

## 🎉 Resultado Final

Com tudo configurado, **cada push para master** automaticamente:

1. ✅ **Executa testes** em múltiplas versões do Python
2. ✅ **Faz linting** do código
3. ✅ **Gera cobertura** de testes
4. ✅ **Builda o pacote** Python
5. ✅ **Publica no PyPI** (se mudou a versão)
6. ✅ **Atualiza documentação** no GitHub Pages
7. ✅ **Cria release** no GitHub (para tags)

**🎯 Zero trabalho manual!**
