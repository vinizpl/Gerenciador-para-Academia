# Sistema de Gerenciamento de Academia

Este é um sistema de linha de comando (CLI) para gerenciamento de academias, desenvolvido em Python. Ele utiliza um banco de dados PostgreSQL para armazenar e gerenciar informações sobre alunos, instrutores, planos, treinos e avaliações físicas.

## 📜 Visão Geral

O projeto foi desenvolvido para simplificar a administração de uma academia, centralizando as operações mais importantes em uma interface de texto interativa. Ele permite o cadastro e gerenciamento completo de todas as entidades principais do negócio, além de extrair relatórios gerenciais para apoiar a tomada de decisão.

## ✨ Funcionalidades Principais

O sistema é modular e organizado nas seguintes seções:

### 🏋️‍♂️ Gerenciamento de Alunos

  - **Cadastro completo:** Inserção de novos alunos com nome, data de nascimento, e-mail, telefone e associação a um plano.
  - **Listagem e Busca:** Visualização de todos os alunos e busca por ID ou e-mail.
  - **Atualização:** Edição das informações cadastrais de um aluno.
  - **Remoção:** Exclusão de alunos do sistema.

### 👩‍🏫 Gerenciamento de Instrutores

  - **Cadastro de instrutores:** Adição de novos instrutores com nome, CPF e especialidade.
  - **Busca flexível:** Localização de instrutores por ID ou CPF.
  - **Gerenciamento:** Listagem, atualização e remoção de instrutores.

### 💪 Gerenciamento de Exercícios

  - **Catálogo de exercícios:** Adição de novos exercícios com nome, grupo muscular e instruções de execução.
  - **Organização:** Listagem de exercícios ordenados por grupo muscular.
  - **Manutenção:** Atualização, remoção e busca de exercícios por ID ou nome.

### 📋 Gerenciamento de Planos

  - **Criação de planos:** Cadastro de diferentes tipos de planos com nome, valor mensal e descrição.
  - **Manutenção:** Listagem, atualização, busca por ID e remoção de planos.

### 📝 Gerenciamento de Treinos

  - **Criação de fichas de treino:** Associação de um aluno e um instrutor a uma nova ficha com um objetivo específico.
  - **Montagem de treino:** Adição de exercícios à ficha, especificando séries, repetições, carga e observações.
  - **Consulta fácil:** Visualização de todos os treinos de um aluno e detalhamento completo de uma ficha específica.
  - **Remoção:** Exclusão de fichas de treino.

### 📈 Gerenciamento de Avaliações Físicas

  - **Registro de avaliações:** Cadastro de avaliações físicas para um aluno, incluindo peso, altura, percentual de gordura e observações.
  - **Histórico:** Listagem de todas as avaliações já realizadas por um aluno.
  - **Remoção:** Exclusão de registros de avaliação.

### 📊 Relatórios e Consultas Avançadas

O sistema pode gerar relatórios estratégicos para análise gerencial:

1.  **Treinos por Instrutor:** Exibe a quantidade de treinos criados por cada instrutor.
2.  **Exercícios Mais Populares:** Lista os exercícios mais utilizados nas fichas de treino.
3.  **Alunos Desatualizados:** Identifica alunos com avaliação física vencida (há mais de 6 meses) ou nunca realizada.
4.  **Média de Idade por Plano:** Calcula a média de idade dos alunos para cada plano disponível.
5.  **Último Treino do Aluno:** Permite consultar em detalhes a ficha de treino mais recente de um aluno específico.

## 🛠️ Estrutura do Projeto

O código é organizado de forma modular para facilitar a manutenção e escalabilidade:

  - `main.py`: Ponto de entrada da aplicação. Gerencia os menus de navegação e a interação com o usuário.
  - `database.py`: Centraliza a configuração e a função de conexão com o banco de dados PostgreSQL.
  - `*_controller.py`: Arquivos que contêm a lógica de negócio e as operações de CRUD (Create, Read, Update, Delete) para cada entidade do sistema (ex: `aluno_controller.py`, `treino_controller.py`).
  - `reports_controller.py`: Contém as funções que geram os relatórios e consultas avançadas.

## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar e rodar o sistema em seu ambiente local.

### Pré-requisitos

  - **Python 3.x**
  - **PostgreSQL** instalado e em execução.
  - A biblioteca `psycopg2` para a conexão entre Python e PostgreSQL.

### 1\. Clone o Repositório

```bash
git clone <URL_DO_SEU_REPOSITORIO_GIT>
cd <NOME_DA_PASTA_DO_PROJETO>
```

### 2\. Instale as Dependências

É recomendável criar um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

Instale a biblioteca necessária:

```bash
pip install psycopg2-binary
```

### 3\. Configure o Banco de Dados

1.  Crie um banco de dados no PostgreSQL para o projeto.

2.  Execute os scripts SQL necessários para criar as tabelas (`alunos`, `instrutores`, `planos`, `exercicios`, `treinos`, etc.).

3.  Abra o arquivo `database.py` e atualize o dicionário `DB_CONFIG` com suas credenciais do PostgreSQL:

    ```python
    DB_CONFIG = {
        "dbname": "SEU_DB_NAME",
        "user": "SEU_USER",
        "password": "SEU_PASSWORD",
        "host": "localhost",
        "port": "5432" # ou a porta do seu PostgreSQL
    }
    ```

### 4\. Execute a Aplicação

Com o ambiente configurado, basta executar o arquivo `main.py`:

```bash
python main.py
```

Você será apresentado ao menu principal, onde poderá navegar por todas as funcionalidades do sistema.

-----
