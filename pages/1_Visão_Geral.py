# ===============================================================
# Imports
# ===============================================================
import streamlit as st
from page_config import setup_page

from geral_utils import (
    mapa_cidades,
    metric_cidades,
    metric_paises,
    metric_qtde_avaliacoes,
    metric_qtde_culinaria,
    metric_restaurantes
)
from utils import (
    background,
    convert_to_usd,
    country_name,
    create_price_type,
    rename_columns,
    sidebar_filters,
    ler_csv,
    add_country_column,
    color_name
)

#================================================================
#                           Configuração da Página
#================================================================

st.set_page_config(page_title='Visão Geral', page_icon='🧭', layout='wide')


# ===============================================================
# Leitura do arquivo
# ===============================================================
df = ler_csv("zomato.csv")

# ===============================================================
# Tratamento e criação de colunas
# ===============================================================
add_country_column(df)

df["Country"] = df["Country Code"].apply(country_name)

df["Average Cost for two (USD)"] = df.apply(
    lambda row: round(
        convert_to_usd(row["Country"], row["Average Cost for two"]), 2
    ),
    axis=1
)

df["Price type"] = df["Price range"].apply(create_price_type)
df["Color name"] = df["Rating color"].apply(color_name)

df = df[df["Average Cost for two (USD)"] <= 100000]
df = rename_columns(df)

df = df.dropna(subset=["cuisines"])
df["cuisines"] = df["cuisines"].apply(lambda x: x.split(",")[0])
df = df.drop_duplicates()

df_filtered = df.copy()

# ===============================================================
# Sidebar
# ===============================================================

df_filtered = sidebar_filters(df.copy(), page_name='1_Visão_Geral')  # ou df_filtered = df.copy()

# ===============================================================
# Background
# ===============================================================
background()



# ===============================================================
# Streamlit Layout - Métricas
# ===============================================================
st.markdown(
    "<h2 style='text-align: center;'>Métricas Gerais</h2>",
    unsafe_allow_html=True
)

st.markdown(
    """
<style>
div[data-testid="stMetricValue"] { 
    font-size: 1.5rem; 
    text-align: center; 
}
div[data-testid="stMetric"] label { 
    display: block; 
    width: 100%; 
    text-align: center; 
    transform: scale(1.4); 
    transform-origin: center; 
}
</style>
""",
    unsafe_allow_html=True
)

# Métricas
with st.container():
    col1, col2, col3, col4, col5 = st.columns(5, gap="small")

    with col1:
        metric_restaurantes(df_filtered)
    with col2:
        metric_paises(df_filtered)
    with col3:
        metric_cidades(df_filtered)
    with col4:
        metric_qtde_avaliacoes(df_filtered)
    with col5:
        metric_qtde_culinaria(df_filtered)

# ===============================================================
# Mapa de Cidades
# ===============================================================
mapa_cidades(df_filtered)

# ===============================================================
# final do arquivo
# ===============================================================