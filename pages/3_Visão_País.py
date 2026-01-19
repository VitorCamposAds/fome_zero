# =============================================================================
# Imports
# =============================================================================
import streamlit as st
from page_config import setup_page

from paises_utils import (
    grafico_paises_com_reserva,
    grafico_paises_por_culinarias,
    mostrar_melhores_medias_avaliacoes,
    mostrar_paises_por_qtde_avaliacoes,
    plot_media_price_range_por_pais,
    plot_restaurantes_caros,
    top_5_paises,
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
        convert_to_usd(row["Country"], row["Average Cost for two"]),
        2,
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
df_filtered = sidebar_filters(df.copy(), page_name='3_Visão_País')  # ou df_filtered = df.copy()

# =============================================================================
# Background
# =============================================================================
background()

# ====================================================
# Configura título e ícone da página
# ====================================================

setup_page("Visão País", "🌍")   

# =============================================================================
# Layout Streamlit
# =============================================================================
st.markdown("<h1 style='text-align: center;'>Visão Paíse</h1>", unsafe_allow_html=True)


with st.container():
    st.markdown(
        "<h4 style='text-align: center;'>"
        "Top 5 países com mais restaurantes"
        "</h4>",
        unsafe_allow_html=True,
    )
    top_5_paises(df_filtered)

st.markdown("---")

with st.container():
    st.markdown(
        "<h4 style='text-align: center;'>"
        "Média de price range por país"
        "</h4>",
        unsafe_allow_html=True,
    )
    plot_media_price_range_por_pais(df_filtered)

st.markdown("---")

with st.container():
    st.markdown(
        "<h4 style='text-align: center;'>"
        "Quantidade de restaurantes caros (price_range=4) por país"
        "</h4>",
        unsafe_allow_html=True,
    )
    plot_restaurantes_caros(df_filtered)

st.markdown("---")

with st.container():
    col1, col2 = st.columns(2, gap="small")

    with col1:
        st.markdown(
            "<h5 style='text-align: center;'>"
            "Países por culinárias distintas"
            "</h5>",
            unsafe_allow_html=True,
        )
        grafico_paises_por_culinarias(df_filtered)

    with col2:
        st.markdown(
            "<h5 style='text-align: center;'>"
            "Países por restaurantes que aceitam reservas"
            "</h5>",
            unsafe_allow_html=True,
        )
        grafico_paises_com_reserva(df_filtered)

st.markdown("---")

with st.container():
    col1, col2 = st.columns(2, gap="small")

    with col1:
        st.markdown(
            "<h5 style='text-align: center;'>"
            "Países por quantidade de avaliações"
            "</h5>",
            unsafe_allow_html=True,
        )
        mostrar_paises_por_qtde_avaliacoes(df_filtered)

    with col2:
        st.markdown(
            "<h5 style='text-align: center;'>"
            "Países por média de avaliações"
            "</h5>",
            unsafe_allow_html=True,
        )
        mostrar_melhores_medias_avaliacoes(df_filtered)

# ===============================================================
# final do arquivo
# ===============================================================