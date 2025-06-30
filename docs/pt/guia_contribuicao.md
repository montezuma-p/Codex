# Guia de Contribuição

Bem-vindo(a)! Este guia reúne as melhores práticas, padrões e dicas para contribuir com excelência no Codex CLI.

---

## 1. Como começar
- Leia o [README.md](../README.md) e o [Índice Geral](indice_geral.md) para entender a arquitetura e cultura do projeto.
- Instale as dependências:
  ```bash
  pip install -r requirements-dev.txt
  ```
- Rode os testes:
  ```bash
  pytest
  ```

## 2. Padrões de Código
- Use type hints e docstrings em todas as funções/métodos.
- Implemente logging estruturado conforme `src/log_config.py`.
- Separe código em módulos claros: core, integrações, banco, sugestões, etc.
- Siga o padrão de modularização e extensibilidade.

## 3. Testes e Automação
- Crie/atualize testes automatizados para toda nova feature ou correção.
- Use mocks para integrações externas.
- Rode `make test` e confira a cobertura.
- Consulte o [Guia de Testes](guia_didatico/como_escrever_testes.md).

## 4. Documentação
- Atualize o sumário de mudanças em cada documento afetado.
- Adicione exemplos e instruções nos guias relevantes.
- Atualize o [Índice Geral](indice_geral.md) e o [Índice Visual](indice_visual.md) se necessário.
- Consulte o [Checklist de PR](checklist_pr.md) antes de submeter.

## 5. Onboarding e Revisão
- Siga o onboarding de cada guia.
- Peça revisão cruzada e use o checklist de PR.
- Registre decisões e aprendizados no [Diário de Bordo](diario_de_bordo.md).

## 6. Integração com Ferramentas Externas de Documentação
- Use [MkDocs](https://www.mkdocs.org/) ou [Sphinx](https://www.sphinx-doc.org/) para gerar documentação navegável a partir dos arquivos markdown.
- Gere documentação automática das ferramentas com:
  ```bash
  python cli_agent.py --doc-ferramentas
  ```
- Considere publicar a documentação em [Read the Docs](https://readthedocs.org/) ou [GitHub Pages](https://pages.github.com/).

## 7. Dicas Finais
- Consulte sempre o índice visual e o checklist de PR.
- Mantenha exemplos e instruções alinhados à CLI e arquitetura vigente.
- Em caso de dúvida, abra uma issue ou peça revisão.

---

> **Contribua, aprenda e ajude a manter o Codex CLI como referência em excelência, integração e didática!**
