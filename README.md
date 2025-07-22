# Teste Analista de Dados - Histórico do Tempo

Este é um projeto simples em **Flask** desenvolvido como parte do processo seletivo para a vaga de Analista de Dados, por **Francisco de Assis Pereira Neto**.

-----

## 📝 Sobre o Projeto

A aplicação web consulta o histórico do tempo dos últimos 7 dias para uma cidade informada pelo usuário. Para isso, ela utiliza a API da **WeatherAPI**.

Os dados são exibidos em uma tabela na página e podem ser baixados como um arquivo **Excel** (`.xlsx`).

-----

## 🛠️ Tecnologias Utilizadas

  * **Python 3.13**
  * **Flask**
  * **Pandas**
  * Requests
  * Python-dotenv
  * Openpyxl

-----

## 🚀 Como Instalar e Executar

Siga os passos abaixo para rodar o projeto em sua máquina.

### 1\. Pré-requisitos

  * Você precisa ter o **Python 3.13** (ou superior) instalado.
  * Ter o `pip` (gerenciador de pacotes do Python) disponível no seu terminal.

### 2\. Instalação

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/francisconetodata/desafiodados.git
    cd desafiodados
    ```

2.  **Crie e ative um ambiente virtual** (prática recomendada):

    ```bash
    # Cria o ambiente virtual
    python -m venv venv

    # Ativa o ambiente (Windows)
    .\venv\Scripts\activate

    # Ativa o ambiente (Linux/macOS)
    source venv/bin/activate
    ```

3.  **Crie um arquivo `requirements.txt`** na pasta raiz do projeto com o seguinte conteúdo:

    ```
    Flask
    pandas
    requests
    python-dotenv
    openpyxl
    ```

4.  **Instale as dependências** do projeto:

    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure sua Chave de API:**

      * Crie um arquivo chamado `.env` na raiz do projeto.
      * Dentro deste arquivo, adicione sua chave da WeatherAPI da seguinte forma:
        ```
        API_KEY="SUA_CHAVE_DE_API_VEM_AQUI"
        ```

### 3\. Execução

1.  Com o ambiente virtual ativado, execute o seguinte comando no terminal:
    ```bash
    # Supondo que seu arquivo se chame app.py
    python app.py
    ```
2.  Abra seu navegador e acesse a URL: `http://127.0.0.1:5000`

-----

## 👨‍💻 Como Usar

1.  Na página inicial, digite o nome de uma cidade (ex: "Fortaleza") e clique em **"Buscar"**.
2.  Os dados do tempo serão exibidos na tabela.
3.  Para baixar um relatório, clique no botão **"Baixar Tabela como Excel"**.

---