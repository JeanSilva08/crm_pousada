Markdown

# CRM Pousada - Automação de Fichas com IA 🏨🤖

Sistema inteligente para digitalização de fichas de hóspedes e gestão automatizada de clientes (CRM), integrando FastAPI, PostgreSQL via Docker e inteligência artificial com Gemini.

---

## 🛠️ Tecnologias e Ferramentas

* **Backend:** Python 3.10+ & FastAPI
* **Banco de Dados:** PostgreSQL (Rodando em container isolado via Docker)
* **ORM:** SQLAlchemy (Gerenciamento e criação automática de tabelas)
* **IA / Visão Computacional:** SDK do Google GenAI (Gemini)

---

## 🚀 Status do Projeto e Funcionalidades

### 🟩 Módulo 1: Core & Infraestrutura de Clientes (Concluído)
* Container PostgreSQL configurado e persistindo dados na porta `5434`.
* CRUD completo de clientes estruturado via endpoints na tag `/clientes`.
* Swagger UI ativo e documentando os esquemas de entrada e saída.

### 🟨 Módulo 2: Upload e Gerenciamento de Fichas (Em Andamento)
* [x] Criação do modelo de banco de dados e tabela `fichas`.
* [x] Implementação de upload físico de imagens (`.jpg`, `.jpeg`, `.png`) via formulário `multipart`.
* [x] Sistema antifraude e colisões de arquivos gerando hashes baseados em **UUID**.
* [x] Salvamento automatizado e organizado no diretório `uploads/`.
* [ ] Criação das rotas de consulta e listagem de fichas pendentes (**Próximo Passo — Level 3**).
* [ ] Integração com o cérebro do Gemini para leitura óptica dos dados.

---

## 💻 Como Executar o Projeto Localmente

### 1. Iniciar o Banco de Dados (Docker)
Certifique-se de que o Docker está rodando e inicie o banco de dados:
```bash
docker-compose up -d

2. Ativar o Ambiente Virtual e Instalar Dependências
Bash

source venv/bin/activate
pip install -r requirements.txt

3. Rodar o Servidor de Desenvolvimento
Bash

uvicorn backend.app.main:app --reload

Acesse a documentação interativa em: http://127.0.0.1:8000/docs


