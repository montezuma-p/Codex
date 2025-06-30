# Makefile refinado para build, testes, documentação multilíngue, limpeza e automação

.PHONY: all build test clean doc doc-ferramentas doc-serve doc-publish help lint coverage install dev-install release check-release

all: build test

install:
	pip install -e .

dev-install:
	pip install -r requirements-dev.txt
	pip install -e .

build:
	bash scripts/build.sh

test:
	bash scripts/test.sh

lint:
	@echo "Executando linting do código..."
	flake8 src/ --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 src/ --count --exit-zero --max-complexidade=10 --max-linha-comprimento=127 --statistics

coverage:
	@echo "Executando testes com cobertura detalhada..."
	pytest --cov=src/codex --cov-report=html --cov-report=term-missing --cov-report=xml -v
	@echo "Relatório de cobertura HTML gerado em htmlcov/index.html"

clean:
	bash scripts/clean.sh

check-release:
	@echo "Verificando se está pronto para release..."
	@echo "1. Executando testes..."
	pytest --cov=src/codex --cov-report=term-missing -v
	@echo "2. Verificando linting..."
	flake8 src/ --count --select=E9,F63,F7,F82 --show-source --statistics
	@echo "3. Buildando pacote..."
	python -m build
	@echo "4. Verificando pacote..."
	twine check dist/*
	@echo "✅ Pronto para release!"

release:
	@echo "Iniciando processo de release automatizado..."
	bash scripts/release.sh

doc:
	@echo "Documentação multilíngue: docs/pt/ (Português), docs/en/ (English) e guias didáticos."

doc-ferramentas:
	python cli_agent.py --doc-ferramentas
	@echo "Documentação das ferramentas atualizada em docs/pt/guia_didatico/auto_documentacao_ferramentas.md e docs/en/guia_didatico/auto_documentacao_ferramentas.md"

doc-serve:
	@echo "Servindo documentação multilíngue localmente (MkDocs) em http://localhost:8000"
	mkdocs serve

doc-publish:
	@echo "Publicando documentação multilíngue (MkDocs) para GitHub Pages"
	mkdocs gh-deploy --clean

help:
	@echo "Comandos disponíveis:"
	@echo ""
	@echo "🔧 Desenvolvimento:"
	@echo "  make install         - Instala o pacote em modo desenvolvimento"
	@echo "  make dev-install     - Instala dependências de desenvolvimento"
	@echo "  make build           - Executa build do projeto"
	@echo "  make test            - Roda todos os testes com cobertura básica"
	@echo "  make coverage        - Testes com cobertura detalhada (HTML + XML)"
	@echo "  make lint            - Executa linting do código com flake8"
	@echo "  make clean           - Limpa arquivos temporários, caches e bytecode"
	@echo ""
	@echo "🚀 Release e Deploy:"
	@echo "  make check-release   - Verifica se está pronto para release (testes, lint, build)"
	@echo "  make release         - Processo completo de release automatizado"
	@echo ""
	@echo "📚 Documentação:"
	@echo "  make doc             - Mostra referência de documentação multilíngue"
	@echo "  make doc-ferramentas - Gera documentação automática das ferramentas (pt/en)"
	@echo "  make doc-serve       - Servidor local do MkDocs (http://localhost:8000)"
	@echo "  make doc-publish     - Publica documentação no GitHub Pages"
	@echo ""
	@echo "💡 Workflow completo:"
	@echo "  1. make dev-install  (primeira vez)"
	@echo "  2. make coverage     (durante desenvolvimento)"
	@echo "  3. make check-release (antes de release)"
	@echo "  4. make release      (para nova versão)"
	@echo ""
	@echo "  make help            - Mostra esta mensagem de ajuda"
