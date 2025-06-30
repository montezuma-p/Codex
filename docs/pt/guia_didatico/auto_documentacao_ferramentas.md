# Documentação automática das ferramentas do Codex CLI

> **Sumário das Mudanças Recentes (2025)**
> - Geração automática deste arquivo a partir do código-fonte das ferramentas.
> - Todas as ferramentas seguem padrão de modularização, type hints e logging estruturado.
> - Exemplos de uso e argumentos atualizados conforme nova arquitetura.
> - Documentação e exemplos revisados para onboarding de novos contribuidores.
> - Guia expandido com troubleshooting, integração contínua e dicas avançadas.

---

## Sobre este Guia
Este arquivo é gerado automaticamente a partir do código-fonte das ferramentas do Codex CLI. Serve como referência rápida e onboarding para desenvolvedores e usuários avançados.

- Consulte sempre após adicionar ou modificar ferramentas.
- Exemplos e argumentos são extraídos diretamente dos módulos em `src/integrations/`.
- Siga os padrões de modularização, type hints e logging para garantir documentação consistente.

---

## Troubleshooting e Dicas
- Se uma ferramenta não aparecer aqui, verifique se está registrada corretamente no dicionário `FERRAMENTAS`.
- Para dúvidas sobre testes, consulte [como_escrever_testes.md](como_escrever_testes.md).
- Para integração contínua, veja o Makefile e scripts de automação.

---

## Onboarding para Novos Contribuidores
1. Sempre documente novas ferramentas seguindo o padrão dos exemplos abaixo.
2. Rode o comando de geração automática após alterações:
   ```bash
   python cli_agent.py --doc-ferramentas
   ```
3. Consulte este guia para exemplos de argumentos e chamadas.
4. Em caso de dúvida, abra uma issue ou peça revisão no PR.

---

## escrever_arquivo

(Sem descrição)

**Exemplo de chamada:**
`{"ferramenta": "escrever_arquivo", "argumentos": {...}}`

## listar_arquivos

Lista arquivos e pastas do diretório informado (relativo ao projeto).
    Parâmetro extra 'base_path' (Path) para facilitar testes.

**Exemplo de chamada:**
`{"ferramenta": "listar_arquivos", "argumentos": {...}}`

## ler_arquivo

Lê e retorna o conteúdo de um arquivo de texto de projeto.
    Parâmetro extra 'base_path' (Path) para facilitar testes.

**Exemplo de chamada:**
`{"ferramenta": "ler_arquivo", "argumentos": {...}}`
