import streamlit as st
from page_config import setup_page

from cidade_utils import (
    cidades_com_prato_mais_caro_2,
    cidades_restaurantes_reserva,
    culinaria_distinta,
    prato_2_mais_caro,
    restaurantes_entregando_agora,
    top10_cidades_media_acima_4,
    top10_cidades_media_baixa
)
from utils import (
    add_country_column,
    background,
    color_name,
    convert_to_usd,
    country_name,
    create_price_type,
    ler_csv,
    rename_columns,
    sidebar_filters,
)

# =============================================================================
# Leitura do arquivo
# =============================================================================
df = ler_csv("zomato.csv")

# =============================================================================
# Tratamento e criação de colunas
# =============================================================================
add_country_column(df)

df["Country"] = df["Country Code"].apply(country_name)

df["Average Cost for two (USD)"] = df.apply(
    lambda row: round(
        convert_to_usd(row["Country"], row["Average Cost for two"]), 2
    ),
    axis=1,
)

df["Price type"] = df["Price range"].apply(create_price_type)
df["Color name"] = df["Rating color"].apply(color_name)

df = df[df["Average Cost for two (USD)"] <= 100000]
df = rename_columns(df)

df = df.dropna(subset=["cuisines"])
df["cuisines"] = df["cuisines"].apply(lambda x: x.split(",")[0])
df = df.drop_duplicates()

df_filtered = df.copy()

# =============================================================================
# Sidebar
# =============================================================================

df_filtered = sidebar_filters(df.copy(), page_name='2_Visão_Cidade')  # ou df_filtered = df.copy()

# =============================================================================
# Background
# =============================================================================
background()

# ====================================================
# Configura título e ícone da página
# ====================================================

setup_page("Visão Cidade", "🏙️")   


# =============================================================================
# Layout Streamlit
# =============================================================================
st.markdown(
    "<h1 style='text-align: center;'>Visão Cidade</h1>",
    unsafe_allow_html=True,
)

st.container()

st.markdown(
    "<h4 style='text-align: center; margin: 0; padding: 7;'>"
    "Top 10 cidades com melhores médias por restaurantes</h4>",
    unsafe_allow_html=True,
)

top10_cidades_media_acima_4(df_filtered)

st.markdown("---")

st.container()

st.markdown(
    "<h4 style='text-align: center; margin: 0; padding: 7;'>"
    "Top 10 cidades com piores médias por restaurantes</h4>",
    unsafe_allow_html=True,
)

top10_cidades_media_baixa(df_filtered)

st.markdown("---")

with st.container():
    col1, col2 = st.columns(2, gap="small")

    with col1:
        st.markdown(
            "<h5 style='text-align: center; margin: 0; padding: 7;'>"
            "Top 5 cidades com prato para 2 mais caro</h5>",
            unsafe_allow_html=True,
        )
        cidades_com_prato_mais_caro_2(df_filtered)

    with col2:
        st.markdown(
            "<h5 style='text-align: center; margin: 0; padding: 7;'>"
            "Top 5 cidades com mais diversidade culinária</h5>",
            unsafe_allow_html=True,
        )
        culinaria_distinta(df_filtered)

st.markdown("---")

with st.container():
    col1, col2 = st.columns(2, gap="small")

    with col1:
        st.markdown(
            "<h4 style='text-align: center; margin: 0; padding: 7;'>"
            "Cidades Com Restaurantes Que Aceitam Reserva</h4>",
            unsafe_allow_html=True,
        )
        cidades_restaurantes_reserva(df_filtered)

    with col2:
        st.markdown(
            "<h4 style='text-align: center; margin: 0; padding: 7;'>"
            "Cidades Com Restaurantes Rue Realizam Entregas</h4>",
            unsafe_allow_html=True,
        )
        restaurantes_entregando_agora(df_filtered)

# ===============================================================
# final do arquivo
# ===============================================================