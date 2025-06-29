# Makefile refinado para build, testes, documentação e limpeza

.PHONY: all build test clean doc doc-ferramentas help

all: build test

build:
	bash scripts/build.sh

test:
	bash scripts/test.sh

clean:
	bash scripts/clean.sh

doc:
	@echo "Documentação principal: README.md, docs/ e guias didáticos."

doc-ferramentas:
	python cli_agent.py --doc-ferramentas
	@echo "Documentação das ferramentas atualizada em docs/guia_didatico/auto_documentacao_ferramentas.md"

help:
	@echo "Comandos disponíveis:"
	@echo "  make build         - Executa build do projeto (ajuste scripts/build.sh)"
	@echo "  make test          - Roda todos os testes com cobertura"
	@echo "  make clean         - Limpa arquivos temporários, caches e bytecode"
	@echo "  make doc           - Mostra referência de documentação"
	@echo "  make doc-ferramentas - Gera documentação automática das ferramentas"
	@echo "  make help          - Mostra esta mensagem de ajuda"
