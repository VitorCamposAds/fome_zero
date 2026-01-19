# 🍽️ Projeto Fome Zero — Análise de Dados com Streamlit

## 📌 Contexto do Problema de Negócio

Você foi contratado como **Cientista de Dados** pela empresa **Fome Zero**, um *marketplace de restaurantes* cujo objetivo é conectar clientes a restaurantes ao redor do mundo.

Os restaurantes cadastrados na plataforma fornecem diversas informações, como:

* Endereço (país e cidade)
* Tipo(s) de culinária
* Preço médio de um prato para duas pessoas
* Se aceitam pedidos online
* Se fazem entregas
* Se aceitam reservas
* Avaliações e nota média

O CEO **Kleiton Guerra**, recém-contratado, precisa entender melhor os dados do negócio para tomar decisões estratégicas. Para isso, foi solicitado o desenvolvimento de **dashboards interativos** que respondessem a perguntas-chave sobre a operação da empresa.

Este projeto entrega essa análise por meio de uma aplicação desenvolvida em **Streamlit**, organizada em **4 visões principais**: **Geral, País, Cidade e Restaurante**.

---

## 🎯 Objetivo do Projeto

Criar um dashboard interativo que permita ao CEO e demais stakeholders:

* Ter uma visão macro do negócio
* Comparar desempenho entre países e cidades
* Identificar restaurantes e tipos de culinária de destaque
* Apoiar decisões estratégicas baseadas em dados

---

## 🗂️ Fonte dos Dados

Os dados utilizados neste projeto foram obtidos no Kaggle:

📎 **Zomato Restaurants Dataset**
[https://www.kaggle.com/datasets/akashram/zomato-restaurants-autoupdated-dataset](https://www.kaggle.com/datasets/akashram/zomato-restaurants-autoupdated-dataset)

Arquivo utilizado:

* `zomato.csv`

---

## 📊 Estrutura do Dashboard

A aplicação foi construída em **Streamlit** e está dividida nas seguintes visões:

---

## 🌍 Visão Geral

Essa visão apresenta um panorama global da base de dados, respondendo às seguintes perguntas:

1. Quantos restaurantes únicos estão registrados?
2. Quantos países únicos estão registrados?
3. Quantas cidades únicas estão registradas?
4. Qual o total de avaliações feitas?
5. Qual o total de tipos de culinária registrados?

👉 **Objetivo:** fornecer uma visão macro da operação da Fome Zero no mundo.

---

## 🌎 Visão por País

Nesta visão, é possível analisar o desempenho e as características dos países presentes na base.

Perguntas respondidas:

1. Qual o país com mais cidades registradas?
2. Qual o país com mais restaurantes registrados?
3. Qual o país com mais restaurantes de nível de preço 4?
4. Qual o país com maior diversidade de tipos de culinária?
5. Qual o país com mais avaliações registradas?
6. Qual o país com mais restaurantes que fazem entrega?
7. Qual o país com mais restaurantes que aceitam reservas?
8. Qual o país com maior média de avaliações por restaurante?
9. Qual o país com a maior nota média?
10. Qual o país com a menor nota média?
11. Qual a média de preço de um prato para duas pessoas por país?

👉 **Objetivo:** comparar mercados internacionais e identificar países estratégicos para expansão ou investimento.

---

## 🏙️ Visão por Cidade

Essa visão aprofunda a análise no nível das cidades.

Perguntas respondidas:

1. Qual a cidade com mais restaurantes registrados?
2. Qual a cidade com mais restaurantes com nota média acima de 4?
3. Qual a cidade com mais restaurantes com nota média abaixo de 2,5?
4. Qual a cidade com maior valor médio de um prato para duas pessoas?
5. Qual a cidade com maior diversidade de tipos de culinária?
6. Qual a cidade com mais restaurantes que aceitam reservas?
7. Qual a cidade com mais restaurantes que fazem entregas?
8. Qual a cidade com mais restaurantes que aceitam pedidos online?

👉 **Objetivo:** entender o comportamento local e identificar cidades com maior potencial ou possíveis gargalos.

---

## 🍴 Visão por Restaurante

Nesta visão, o foco é o desempenho individual dos restaurantes.

Perguntas respondidas:

1. Qual restaurante possui a maior quantidade de avaliações?
2. Qual restaurante possui a maior nota média?
3. Qual restaurante possui o maior valor de prato para duas pessoas?
4. Qual restaurante de culinária brasileira possui a menor média de avaliação?
5. Qual restaurante de culinária brasileira, localizado no Brasil, possui a maior média de avaliação?
6. Restaurantes que aceitam pedidos online possuem, em média, mais avaliações?
7. Restaurantes que aceitam reservas possuem, em média, maior valor de prato para duas pessoas?
8. Restaurantes japoneses dos EUA possuem preço médio maior que churrascarias americanas (BBQ)?

👉 **Objetivo:** identificar restaurantes de destaque, padrões de comportamento e correlações relevantes.

---

## 🍝 Visão por Tipo de Culinária

Essa visão analisa o desempenho dos restaurantes com base no tipo de culinária.

Perguntas respondidas:

1. Restaurante italiano com maior média de avaliação
2. Restaurante italiano com menor média de avaliação
3. Restaurante americano com maior média de avaliação
4. Restaurante americano com menor média de avaliação
5. Restaurante árabe com maior média de avaliação
6. Restaurante árabe com menor média de avaliação
7. Restaurante japonês com maior média de avaliação
8. Restaurante japonês com menor média de avaliação
9. Restaurante de culinária caseira com maior média de avaliação
10. Restaurante de culinária caseira com menor média de avaliação
11. Tipo de culinária com maior valor médio de prato para duas pessoas
12. Tipo de culinária com maior nota média
13. Tipo de culinária com mais restaurantes que aceitam pedidos online e fazem entregas

👉 **Objetivo:** apoiar decisões relacionadas a posicionamento, parcerias e foco em tipos de culinária mais rentáveis ou melhor avaliados.

---

## 🛠️ Tecnologias Utilizadas

* Python
* Pandas
* Streamlit
* Plotly / Matplotlib (se aplicável)
* Jupyter Notebook (análises exploratórias)

---

## 🚀 Como Executar o Projeto

```bash
# clonar o repositório
git clone <url-do-repositorio>

# entrar no diretório
cd nome-do-projeto

# instalar dependências
pip install -r requirements.txt

# executar a aplicação
streamlit run app.py
```

---

## 📈 Considerações Finais

Este projeto demonstra como dados podem ser transformados em **insights estratégicos**, auxiliando diretamente a tomada de decisão da liderança da empresa.

O dashboard é totalmente interativo, permitindo filtros dinâmicos e análises exploratórias em diferentes níveis de granularidade.

---

👨‍💻 **Autor:** Vitor Costa
📊 **Projeto:** Cientista de Dados — Fome Zero
