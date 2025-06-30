# Makefile refinado para build, testes, documentação multilíngue e limpeza

.PHONY: all build test clean doc doc-ferramentas doc-serve doc-publish help

all: build test

build:
	bash scripts/build.sh

test:
	bash scripts/test.sh

clean:
	bash scripts/clean.sh

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
	@echo "  make build           - Executa build do projeto (ajuste scripts/build.sh)"
	@echo "  make test            - Roda todos os testes com cobertura"
	@echo "  make clean           - Limpa arquivos temporários, caches e bytecode"
	@echo "  make doc             - Mostra referência de documentação multilíngue (docs/pt, docs/en)"
	@echo "  make doc-ferramentas - Gera documentação automática das ferramentas (pt/en)"
	@echo "  make doc-serve       - Sobe servidor local do MkDocs para navegação multilíngue"
	@echo "  make doc-publish     - Publica documentação multilíngue no GitHub Pages (mkdocs.yml)"
	@echo "  make help            - Mostra esta mensagem de ajuda"
