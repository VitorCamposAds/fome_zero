import folium
import pandas as pd
import streamlit as st
from streamlit_folium import folium_static


# ===========================================================
# Métricas Responsivas
# ===========================================================

def metric_restaurantes(df):
    valor = f"{df['restaurant_id'].nunique():,.0f}".replace(",", ".")
    st.markdown(
        f"""
        <div style="
            padding:0.4rem 1.3rem;
            border-radius:8px;
            background-color:#D9E8FF;
            display:inline-block;
            flex: 1 1 150px;
            margin: 0.2rem;
            min-width:120px;
            text-align:center;
        ">
            <div style="font-size:0.90rem;color:#1F3A5F;font-weight:500">
                Restaurantes
            </div>
            <div style="font-size:1.8rem;font-weight:350;line-height:1.1;color:#102A43">
                {valor}
            </div>
            <div style="font-size:0.90rem;color:#1F3A5F;font-weight:500">
                Total
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def metric_paises(df):
    valor = f"{df['country'].nunique():,.0f}".replace(",", ".")
    st.markdown(
        f"""
        <div style="
            padding:0.4rem 2.3rem;
            border-radius:5px;
            background-color:#D9E8FF;
            display:inline-block;
            flex: 1 1 150px;
            margin: 0.2rem;
            min-width:120px;
            text-align:center;
        ">
            <div style="font-size:0.90rem;color:#1F3A5F;font-weight:500">
                Países
            </div>
            <div style="font-size:1.8rem;font-weight:350;line-height:1.1;color:#102A43">
                {valor}
            </div>
            <div style="font-size:0.90rem;color:#1F3A5F;font-weight:500">
                Total
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def metric_cidades(df):
    valor = f"{df['city'].nunique():,.0f}".replace(",", ".")
    st.markdown(
        f"""
        <div style="
            padding:0.4rem 1.7rem;
            border-radius:8px;
            background-color:#D9E8FF;
            display:inline-block;
            flex: 1 1 150px;
            margin: 0.2rem;
            min-width:120px;
            text-align:center;
        ">
            <div style="font-size:0.90rem;color:#1F3A5F;font-weight:500">
                Cidades
            </div>
            <div style="font-size:1.8rem;font-weight:350;line-height:1.1;color:#102A43">
                {valor}
            </div>
            <div style="font-size:0.90rem;color:#1F3A5F;font-weight:500">
                Total
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def metric_qtde_avaliacoes(df):
    valor = f"{df['votes'].sum():,.0f}".replace(",", ".")
    st.markdown(
        f"""
        <div style="
            padding:0.4rem 0.3rem;
            border-radius:8px;
            background-color:#D9E8FF;
            display:inline-block;
            flex: 1 1 150px;
            margin: 0.2rem;
            min-width:120px;
            text-align:center;
        ">
            <div style="font-size:0.90rem;color:#1F3A5F;font-weight:500">
                Qtde. Avaliações
            </div>
            <div style="font-size:1.8rem;font-weight:350;line-height:1.1;color:#102A43">
                {valor}
            </div>
            <div style="font-size:0.90rem;color:#1F3A5F;font-weight:500">
                Total
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def metric_qtde_culinaria(df):
    valor = f"{df['cuisines'].nunique():,.0f}".replace(",", ".")
    st.markdown(
        f"""
        <div style="
            padding:0.4rem 0.3rem;
            border-radius:8px;
            background-color:#D9E8FF;
            display:inline-block;
            flex: 1 1 150px;
            margin: 0.2rem;
            min-width:120px;
            text-align:center;
        ">
            <div style="font-size:0.90rem;color:#1F3A5F;font-weight:500">
                Qtde. Culinária
            </div>
            <div style="font-size:1.8rem;font-weight:350;line-height:1.1;color:#102A43">
                {valor}
            </div>
            <div style="font-size:0.90rem;color:#1F3A5F;font-weight:500">
                Total
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ===========================================================
# Mapa Responsivo de Cidades
# ===========================================================

def mapa_cidades(df):
    st.markdown(
        "<h3 style='text-align: center;'>Distribuição de Restaurantes por Cidade</h3>",
        unsafe_allow_html=True,
    )

    contagem = (
        df.groupby(["city", "country"], as_index=False)
        .agg(
            qtd_restaurantes=("restaurant_id", "count"),
            latitude=("latitude", "median"),
            longitude=("longitude", "median"),
            rating_medio=("aggregate_rating", "mean"),
            preco_medio=("average_cost_for_two(usd)", "median"),
        )
    )

    mapa = folium.Map(
        location=[contagem["latitude"].median(), contagem["longitude"].median()],
        zoom_start=2,
        tiles="CartoDB positron",
    )

    cluster = folium.plugins.MarkerCluster().add_to(mapa)

    def cor_por_rating(rating):
        if rating >= 4.5:
            return "green"
        elif rating >= 3.5:
            return "orange"
        return "red"

    for row in contagem.itertuples(index=False):
        popup_html = f"""
        <div style="font-size: 13px;">
            <b>📍 {row.city} - {row.country}</b><br><br>
            🍽️ <b>Restaurantes:</b> {row.qtd_restaurantes}<br>
            ⭐ <b>Nota média:</b> {row.rating_medio:.2f}<br>
            💰 <b>Preço médio (2):</b> US$ {row.preco_medio:.2f}
        </div>
        """
        folium.CircleMarker(
            location=[row.latitude, row.longitude],
            radius=min(25, 4 + row.qtd_restaurantes ** 0.5),
            color=cor_por_rating(row.rating_medio),
            fill=True,
            fill_color=cor_por_rating(row.rating_medio),
            fill_opacity=0.7,
            popup=popup_html,
            tooltip=f"{row.city} • {row.country} | 🍽️ {row.qtd_restaurantes}",
        ).add_to(cluster)

    # Responsivo: ocupa 100% da largura da tela
    folium_static(mapa, width="100%", height=600)

# ===========================================================
# Fim do arquivo
# ===========================================================
