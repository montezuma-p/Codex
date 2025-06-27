# IA_Pessoal – Aprendizado com APIs, IA e Automação de Projetos

Bem-vindo(a) ao IA_Pessoal! Este projeto marca minha primeira experiência desenvolvendo e consumindo APIs, além de ser um laboratório para criar um agente de IA pessoal focado em programação e automação de projetos.

## Sobre o Projeto
O repositório nasceu com o objetivo de aprender e estudar:
- Como funcionam APIs e integração de serviços.
- Persistência de dados com SQLite e SQLAlchemy.
- Criação de interfaces web com Flask.
- Automação de tarefas e uso de IA para auxiliar no desenvolvimento de projetos.

## Funcionalidades Atuais
- Armazena conversas entre usuário e IA em um banco SQLite, com histórico consultável.
- Permite busca por palavras-chave no histórico de interações.
- Interface web (Flask) para chat com a IA.
- Integração com modelo Gemini da Google para respostas inteligentes.
- Implementação de ferramentas customizadas, como escrita de arquivos e busca no histórico, acionadas por prompt.

## Estrutura dos Arquivos
- `database.py`: Gerenciamento da memória (criação do banco, salvar e buscar conversas).
- `memoria_codex.db`: Banco de dados SQLite.
- `web_agent.py`: Aplicação web Flask, integra IA, banco e ferramentas customizadas.
- `templates/`: Templates HTML para interface web (ex: `chat.html`).
- `docs/`: Documentação e roadmap do projeto.

## Tecnologias Utilizadas
- **Python** 🐍
- **Flask** – Interface web
- **SQLAlchemy** – ORM para SQLite
- **Google Gemini API** – IA generativa
- Outras: requests, json, etc.

## Como Usar
1. **Instale as dependências:**
   ```bash
   pip install sqlalchemy flask
   ```
2. **Configure a variável de ambiente da API:**
   ```bash
   export GOOGLE_API_KEY='sua-api-key-aqui'
   ```
3. **Inicialize o banco de dados:**
   ```bash
   python database.py
   ```
4. **Rode a aplicação web:**
   ```bash
   python web_agent.py
   ```

## Exemplo de Uso em Python
```python
from database import Session, Conversa, criar_banco_e_tabelas, carregar_historico, buscar_no_historico

criar_banco_e_tabelas()
session = Session()
nova_msg = Conversa(role='user', content='Olá, IA!')
session.add(nova_msg)
session.commit()
resultados = buscar_no_historico(session, 'Olá')
for msg in resultados:
    print(msg.timestamp, msg.role, msg.content)
```

## Roadmap e Visão de Futuro
Veja o arquivo [`docs/roadmap.md`](docs/roadmap.md) para saber o que já foi implementado e os próximos passos, incluindo a visão de um agente de IA que automatiza tarefas, gerencia projetos e aprende com o uso.

## Observações
- Projeto didático e experimental, aberto a sugestões!
- Não compartilhe sua chave real da API.
- O parâmetro `check_same_thread=False` permite integração com frameworks web como Flask.

---

**Autor:** montezuma-p

**Licença:** MIT
