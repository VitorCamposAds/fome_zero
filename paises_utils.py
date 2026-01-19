# =============================================================================
# Imports
# =============================================================================
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# =============================================================================
# Primeiro gráfico (barras)
# =============================================================================
def top_5_paises(df):
    restaurantes_registrados = (
        df.groupby("country")["restaurant_id"]
        .nunique()
        .reset_index(name="Qtde_restaurantes")
        .rename(columns={"country": "País"})
        .sort_values(by="Qtde_restaurantes", ascending=False)
        .head(5)
    )

    fig, ax = plt.subplots(figsize=(25, 10))

    fig.patch.set_alpha(0)
    ax.set_facecolor("none")

    bars = ax.bar(
        restaurantes_registrados["País"],
        restaurantes_registrados["Qtde_restaurantes"],
        color="skyblue",
        edgecolor="black",
        linewidth=1,
    )

    ax.yaxis.grid(True, color="gray", linestyle="--", linewidth=0.5)
    ax.xaxis.grid(False)

    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.set_xlabel("País", labelpad=20, fontsize=25)
    ax.set_ylabel("Quantidade de restaurantes", labelpad=20, fontsize=25)
    plt.xticks(rotation=45, fontsize=20)
    plt.yticks(fontsize=20)

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 2,
            f"{int(height)}",
            ha="center",
            va="bottom",
            fontsize=20,
            fontweight="bold",
        )

    st.pyplot(fig)


# =============================================================================
# Segundo gráfico
# =============================================================================
def plot_media_price_range_por_pais(df):
    media_preco_por_pais = (
        df.groupby("country")["price_range"]
        .mean()
        .reset_index()
        .rename(
            columns={
                "country": "País",
                "price_range": "Média de price range",
            }
        )
        .sort_values(by="Média de price range", ascending=False)
    )

    fig, ax = plt.subplots(figsize=(25, 10))

    fig.patch.set_alpha(0)
    ax.set_facecolor("none")

    bars = ax.bar(
        media_preco_por_pais["País"],
        media_preco_por_pais["Média de price range"],
        color="skyblue",
        alpha=0.6,
        edgecolor="black",
        linewidth=1,
    )

    ax.yaxis.grid(True, linestyle="--", linewidth=0.5)
    ax.xaxis.grid(False)

    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.set_xlabel("País", fontsize=30)
    ax.set_ylabel("Média de price range", fontsize=30)

    plt.xticks(rotation=80, fontsize=20)
    plt.yticks(fontsize=20)

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{height:.2f}",
            ha="center",
            va="bottom",
            fontsize=20,
            fontweight="bold",
        )

    st.pyplot(fig)


# =============================================================================
# Terceiro gráfico
# =============================================================================
def plot_restaurantes_caros(df):
    restaurantes_nota4 = (
        df[df["price_range"] == 4]
        .groupby("country")
        .size()
        .reset_index(name="Qtde. restaurantes com preços mais caros")
        .rename(columns={"country": "País"})
        .sort_values(
            by="Qtde. restaurantes com preços mais caros",
            ascending=True,
        )
    )

    fig = px.bar(
        restaurantes_nota4,
        x="Qtde. restaurantes com preços mais caros",
        y="País",
        orientation="h",
        text="Qtde. restaurantes com preços mais caros",
    )

    fig.update_traces(
        textposition="outside",
        textfont=dict(color="black", size=12),
        texttemplate="<b>%{x}</b>",
        marker=dict(
            color="skyblue",
            opacity=0.6,
            line=dict(color="black", width=1),
        ),
    )

    fig.update_layout(
        title=None,
        annotations=[],
        margin=dict(t=0, b=10, l=10, r=10),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(
            title=dict(
                text="Restaurantes com preços mais caros",
                font=dict(color="black", size=14),
            ),
            tickfont=dict(color="black", size=12),
            range=[
                0,
                restaurantes_nota4[
                    "Qtde. restaurantes com preços mais caros"
                ].max()
                * 1.05,
            ],
        ),
        yaxis=dict(
            title=dict(
                text="País",
                font=dict(color="black", size=14),
            ),
            tickfont=dict(color="black", size=12),
        ),
    )

    st.plotly_chart(fig, use_container_width=True)


# =============================================================================
# Quarto gráfico
# =============================================================================
def grafico_paises_por_culinarias(df):
    pais_culinaria_unica = (
        df[["country", "cuisines"]]
        .dropna(subset=["cuisines"])
        .assign(cuisines=lambda x: x["cuisines"].str.split(", "))
        .explode("cuisines")
        .groupby("country")["cuisines"]
        .nunique()
        .reset_index(name="Culinária")
        .sort_values(by="Culinária", ascending=False)
        .rename(columns={"country": "País"})
    )

    df_plot = pais_culinaria_unica.sort_values("Culinária")

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df_plot["Culinária"],
            y=df_plot["País"],
            mode="lines",
            line=dict(color="#D0D0D0", width=2),
            hoverinfo="skip",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df_plot["Culinária"],
            y=df_plot["País"],
            mode="markers",
            marker=dict(size=10),
            hovertemplate=(
                "<b>%{y}</b><br>"
                "Culinárias distintas: %{x:.0f}"
                "<extra></extra>"
            ),
        )
    )

    fig.update_layout(
        height=350,
        margin=dict(l=10, r=10, t=30, b=10),
        showlegend=False,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )

    fig.update_xaxes(
        showgrid=False,
        zeroline=False,
        title="Culinária",
        title_font=dict(color="black", size=12),
        tickfont=dict(color="black"),
    )

    fig.update_yaxes(
        showgrid=False,
        title="",
        tickfont=dict(color="black"),
    )

    st.plotly_chart(fig, use_container_width=True)


# =============================================================================
# Quinto gráfico
# =============================================================================
def grafico_paises_com_reserva(df):
    aceita_reserva = (
        df[df["has_table_booking"] == 1]
        .groupby("country")["has_table_booking"]
        .count()
        .reset_index(name="Aceita_reserva")
        .sort_values(by="Aceita_reserva", ascending=True)
        .rename(columns={"country": "País"})
    )

    fig = px.scatter(
        aceita_reserva,
        x="Aceita_reserva",
        y="País",
        size="Aceita_reserva",
        size_max=14,
        height=450,
    )

    fig.update_layout(
        margin=dict(l=20, r=20, t=10, b=20),
        xaxis_title="Restaurantes que aceitam reservas",
        yaxis_title="",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
        xaxis=dict(
            title_font=dict(color="black", size=12),
            tickfont=dict(color="black"),
        ),
        yaxis=dict(
            tickfont=dict(color="black"),
        ),
    )

    fig.update_yaxes(automargin=True)

    st.plotly_chart(fig, use_container_width=True)


# =============================================================================
# Sexto gráfico (tabela)
# =============================================================================
def mostrar_paises_por_qtde_avaliacoes(df):
    pais_qtde_avaliacao = (
        df.groupby("country")["aggregate_rating"]
        .count()
        .reset_index(name="Avaliações")
        .sort_values(by="Avaliações", ascending=False)
        .rename(columns={"country": "País"})
        .reset_index(drop=True)
    )

    pais_qtde_avaliacao.index += 1  # índice começa em 1

    # Constrói tabela HTML centralizada
    tabela_html = '<table style="width:100%; border-collapse: collapse;">'
    
    # Cabeçalho
    tabela_html += '<thead>'
    tabela_html += '<tr>'
    tabela_html += '<th style="border-bottom: 1px solid #ddd; text-align: center; font-weight: bold;"></th>'
    for col in pais_qtde_avaliacao.columns:
        tabela_html += f'<th style="border-bottom: 1px solid #ddd; text-align: center; font-weight: bold;">{col}</th>'
    tabela_html += '</tr>'
    tabela_html += '</thead>'
    
    # Corpo da tabela
    tabela_html += '<tbody>'
    for idx, row in pais_qtde_avaliacao.iterrows():
        tabela_html += '<tr>'
        tabela_html += f'<td style="text-align: center;">{idx}</td>'  # só idx, sem +1
        for col in pais_qtde_avaliacao.columns:
            tabela_html += f'<td style="text-align: center;">{row[col]}</td>'
        tabela_html += '</tr>'
    tabela_html += '</tbody>'
    tabela_html += '</table>'

    # Mostra no Streamlit
    st.markdown(tabela_html, unsafe_allow_html=True)


# =============================================================================
# Sétimo gráfico (tabela)
# =============================================================================
import streamlit as st

def mostrar_melhores_medias_avaliacoes(df):
    media_nota_registrada = (
        df.groupby("country")["aggregate_rating"]
        .mean()
        .reset_index(name="Média")
        .sort_values(by="Média", ascending=False)
        .rename(columns={"country": "País"})
        .reset_index(drop=True)
    )

    media_nota_registrada.index += 1  # índice começa em 1

    # Constrói tabela HTML centralizada
    tabela_html = '<table style="width:100%; border-collapse: collapse;">'
    
    # Cabeçalho
    tabela_html += '<thead>'
    tabela_html += '<tr>'
    tabela_html += '<th style="border-bottom: 1px solid #ddd; text-align: center; font-weight: bold;"></th>'
    for col in media_nota_registrada.columns:
        tabela_html += f'<th style="border-bottom: 1px solid #ddd; text-align: center; font-weight: bold;">{col}</th>'
    tabela_html += '</tr>'
    tabela_html += '</thead>'
    
    # Corpo da tabela
    tabela_html += '<tbody>'
    for idx, row in media_nota_registrada.iterrows():
        tabela_html += '<tr>'
        tabela_html += f'<td style="text-align: center;">{idx}</td>'  # índice
        tabela_html += f'<td style="text-align: center;">{row["País"]}</td>'  # País
        tabela_html += f'<td style="text-align: center;">{row["Média"]:.2f}</td>'  # Média com 2 casas
        tabela_html += '</tr>'
    tabela_html += '</tbody>'
    tabela_html += '</table>'

    # Mostra no Streamlit
    st.markdown(tabela_html, unsafe_allow_html=True)

# ===============================================================
# final do arquivo
# ===============================================================