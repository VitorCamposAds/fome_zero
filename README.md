# 🍽️ Projeto Fome Zero — Análise de Dados com Streamlit

🔗 **Link da aplicação (Streamlit):**  
👉 https://fomezero-vitorcamposapp.streamlit.app/

---

## 📌 Contexto do Problema de Negócio
Análise de dados para a empresa Fome Zero, um marketplace de restaurantes cujo objetivo é conectar clientes a restaurantes ao redor do mundo.

Os restaurantes cadastrados na plataforma fornecem diversas informações, como:

- Endereço (país e cidade)
- Tipo(s) de culinária
- Preço médio de um prato para duas pessoas
- Se aceitam pedidos online
- Se fazem entregas
- Se aceitam reservas
- Avaliações e nota média

O CEO Kleiton Guerra, recém-contratado, precisa entender melhor os dados do negócio para tomar decisões estratégicas. Para isso, foi solicitado o desenvolvimento de dashboards interativos que respondessem a perguntas-chave sobre a operação da empresa.

Este projeto entrega essa análise por meio de uma aplicação desenvolvida em **Streamlit**, organizada em 4 visões principais: **Geral, País, Cidade e Restaurante**.

---

## 🎯 Objetivo do Projeto
Criar um dashboard interativo que permita ao CEO e demais stakeholders:

- Ter uma visão macro do negócio  
- Comparar desempenho entre países e cidades  
- Identificar restaurantes e tipos de culinária de destaque  
- Apoiar decisões estratégicas baseadas em dados  

---

## 🗂️ Fonte dos Dados
Os dados utilizados neste projeto foram obtidos no Kaggle:

📎 Zomato Restaurants Dataset  
https://www.kaggle.com/datasets/akashram/zomato-restaurants-autoupdated-dataset  

Arquivo utilizado:
- `zomato.csv`

---

## 📊 Estrutura do Dashboard

O dashboard foi construído com base em diversas perguntas estratégicas sobre restaurantes, países, cidades e tipos de culinária. Essas perguntas **orientaram quais métricas e gráficos deveriam ser incluídos**, mas nem todas aparecem individualmente como gráficos, para manter a visualização **limpa e funcional**.

### 🌍 Visão Geral
Permite ter uma visão macro da operação da Fome Zero no mundo, considerando perguntas como:

- Quantidade de restaurantes únicos  
- Quantidade de países e cidades  
- Total de avaliações  
- Total de tipos de culinária  

### 🌎 Visão por País
Analisa os países cadastrados, guiado por perguntas como:

- País com mais cidades e restaurantes  
- País com mais restaurantes de nível de preço 4  
- País com maior diversidade de culinária  
- País com mais avaliações e serviços como entrega e reservas  
- Preço médio e nota média por país  

### 🏙️ Visão por Cidade
Explora as cidades com perguntas como:

- Cidade com mais restaurantes  
- Cidade com mais restaurantes com notas altas ou baixas  
- Cidade com maior preço médio  
- Cidade com maior diversidade culinária  
- Presença de serviços (reservas, entrega, pedidos online)  

### 🍴 Visão por Restaurante
Foca em restaurantes individuais, considerando perguntas como:

- Restaurantes com mais avaliações e maior nota média  
- Restaurantes com maior valor de prato  
- Destaques da culinária brasileira  
- Comparações entre tipos de serviço e culinárias  

### 🍝 Visão por Tipo de Culinária
Analisa tendências por tipo de culinária, guiado por perguntas como:

- Melhores e piores avaliações por tipo  
- Tipos de culinária mais caros  
- Tipos de culinária com maior nota média  
- Tipos com mais pedidos online e entregas  

> **Obs.:** Essas perguntas foram o ponto de partida para o dashboard, mas os gráficos e métricas foram agregados de forma a manter a visualização limpa e intuitiva, evitando sobrecarga de informações.

---

## 🛠️ Tecnologias Utilizadas
- Python  
- Pandas  
- Streamlit & Streamlit Cloud
- Plotly  
- Matplotlib  
- Git  
- GitHub
- Jupyter Lab
- Terminal  

---

## 🚀 Como Executar o Projeto

```bash
git clone <url-do-repositorio>
cd nome-do-projeto
pip install -r requirements.txt
streamlit run app.py

📈 **Considerações Finais**

Este projeto demonstra como dados podem ser transformados em insights estratégicos por meio de um dashboard interativo e exploratório.

👨‍💻 Autor: Vitor Costa
📊 Projeto: Analista de Dados — Fome Zero
