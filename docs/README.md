# Travel Prediction App

Um sistema completo para prever o propósito de viagem com base em dados de entrada fornecidos pelo usuário. Este projeto utiliza um modelo de aprendizado de máquina (Árvore de Decisão), FastAPI para o back-end e PostgreSQL para armazenamento de dados.

## Funcionalidades

- Previsão de propósito de viagem (Exemplo: Trabalho, Lazer, etc.).
- Formulário de entrada simples para o usuário.
- Armazenamento de dados no banco de dados PostgreSQL.
- Exibição de resultados ao usuário.

## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **FastAPI**: Framework para criação de APIs.
- **PostgreSQL**: Banco de dados relacional.
- **Scikit-Learn**: Biblioteca para aprendizado de máquina.
- **HTML/CSS**: Para o front-end simples.
- **SQLAlchemy**: Para conexão com PostgreSQL.

## Estrutura do Projeto

- **backend/**: Código do servidor FastAPI.
- **frontend/**: Formulário HTML para entrada de dados.
- **models/**: Scripts para treinamento e armazenamento do modelo de IA.
- **database/**: Scripts SQL para criação e configuração do banco de dados.

## Como Executar

1. Clone o repositório:
   ```bash
   [git clone https://github.com/AndersonVelos0/travel-prediction-app.git](https://github.com/AndersonVelos0/travel-prediction-app.git)


## Como Executar

1. Configure o banco de dados PostgreSQL.
2. Treine o modelo utilizando o script `backend/models/train_model.py`.
3. Inicie o servidor FastAPI com:
   ```bash
   uvicorn backend.main:app --reload