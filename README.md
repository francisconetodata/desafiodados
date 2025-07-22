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

# Análise Estratégica e Recomendações de Melhoria

Com base nos dados de desempenho fornecidos, compilamos um diagnóstico dos pontos fortes e fracos das campanhas atuais, seguido por um plano de ação com recomendações práticas para otimizar o investimento e aumentar a geração de leads.

## 1. Diagnóstico e Principais Insights

A análise do painel de desempenho revela padrões claros que nos permitem entender a dinâmica das suas campanhas.

### Insight 1: Campanhas de Leads focadas em modelos específicos são as estrelas.

As campanhas `atr_leads | promo - hb20 (CBO) 2` e `atr_leads | promo - creta [CBO] 2` são, de longe, as mais eficientes. Elas não apenas geram o maior volume de leads, mas o fazem com um Custo por Lead (CPL) muito baixo. A taxa de conversão delas é excelente (acima de 23%), indicando que a oferta, o criativo e a página de destino estão perfeitamente alinhados com o público.

**Ponto-chave:** A especificidade (falar de um modelo de carro) gera mais resultado do que abordagens genéricas.

### Insight 2: O dilema das Campanhas de Search: Atraem cliques, mas perdem na conversão.

As campanhas de search (marca, Joinville, Jaraguá do Sul) mostram uma Taxa de Cliques (CTR) altíssima (até 9.27% para "marca"). Isso é ótimo e prova que os anúncios são relevantes para quem busca. O problema está no pós-clique: a Taxa de Conversão é muito baixa (entre 5% e 9%).

**Ponto-chave:** Estamos pagando caro por cliques que não se tornam leads. O problema não está no anúncio, mas provavelmente na página de destino ou na oferta apresentada após o clique.

### Insight 3: Existe uma "joia escondida" de alta eficiência.

A campanha `atr_leads | Hyundai Day` possui a maior taxa de conversão de todas (27.78%) e um CPL muito competitivo (R$ 13,54). No entanto, ela gerou apenas 25 leads.

**Ponto-chave:** Esta campanha é extremamente eficaz. O seu baixo volume de leads sugere que ela teve um orçamento limitado ou foi veiculada por um curto período. Há um enorme potencial de crescimento aqui.

---

## 2. Plano de Ação: Recomendações para Otimizar Resultados

Com base no diagnóstico, sugerimos as seguintes ações para o próximo período, visando obter mais resultados com o mesmo investimento.

### Ação 1: Realocar o Orçamento para Maximizar a Eficiência

O princípio é simples: invista mais no que já funciona e reduza o custo do que não performa bem.

* **Aumentar o Investimento nos Campeões:** Realoque parte do orçamento das campanhas de search (com CPL acima de R$ 27) para as campanhas `atr_leads | promo - hb20 (CBO) 2` e `atr_leads | promo - creta [CBO] 2`. Elas já provaram que convertem leads a um custo baixo e podem gerar ainda mais volume com mais verba.
* **Escalar a Campanha de Alto Potencial:** Dê um orçamento significativamente maior para a campanha `atr_leads | Hyundai Day` ou crie campanhas similares baseadas em eventos sazonais ou ofertas especiais. Com uma taxa de conversão tão alta, cada real investido aqui tem um retorno muito maior.

### Ação 2: Otimizar a Taxa de Conversão (CRO) das Campanhas de Search

O objetivo aqui é transformar os cliques caros em leads valiosos.

* **Revise as Páginas de Destino:** Analise a página para a qual os anúncios de search estão enviando os usuários.
    * **A promessa do anúncio corresponde à página?** Se o anúncio fala de "Hyundai em Joinville", a página deve reforçar essa mensagem.
    * **O formulário de contato é simples e visível?** Remova campos desnecessários. Deixe claro o que o usuário ganha ao preencher.
    * **A página é rápida e otimizada para celular?** Lentidão é um dos maiores inimigos da conversão.
* **Teste Ofertas Diferentes:** Para quem vem da busca, a intenção é alta. Teste ofertas mais agressivas na página de destino, como "Receba uma oferta especial online" ou "Agende um test-drive prioritário".

### Ação 3: Refinar Criativos e Públicos

Aprenda com os melhores e aplique aos demais.

* **Modele os Criativos de Sucesso:** Analise os textos e imagens dos anúncios das campanhas `hb20` e `creta`. Use esses mesmos elementos e estilo de comunicação para criar novas versões de anúncios para campanhas com desempenho inferior, como a `Promo HR [CBO]`.
* **Teste Novos Públicos:** Para a campanha `Promo HR [CBO]`, que tem um CPL alto (R$ 31,05), o público-alvo pode não ser o ideal. Teste segmentações diferentes, como "pequenos empresários", "frotistas" ou pessoas que demonstraram interesse em veículos utilitários.

---

### Resumo Estratégico

Para o próximo período, a estratégia deve ser:

* **Focar:** Dobrar o investimento nas campanhas de leads para modelos específicos (`hb20`, `creta`).
* **Consertar:** Pausar o aumento de verba nas campanhas de search e focar em otimizar suas páginas de destino para melhorar a conversão.
* **Expandir:** Reativar e escalar campanhas de alta eficiência como a `Hyundai Day`.

Seguindo estes passos, a tendência é que o volume total de leads aumente e o Custo por Lead médio geral diminua, gerando mais resultados com o mesmo orçamento.
