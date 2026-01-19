# =================================================================
#                           Imports
# =================================================================
import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# =================================================================
#                           Gráficos
# =================================================================

# 1º gráfico: Top 10 cidades com média acima de 4
def top10_cidades_media_acima_4(df):
    medias = (
        df.groupby('city')['aggregate_rating']
        .mean()
        .reset_index(name='Média')
        .sort_values(by='Média', ascending=False)
    )
    medias['Média'] = medias['Média'].round(2)
    acima_4 = medias[medias['Média'] > 4]
    top10 = acima_4.head(10)

    fig = px.bar(
        top10,
        x='city',
        y='Média',
        text=top10['Média'],
        hover_data={'Média': False}
    )

    fig.update_layout(
        xaxis_title='Cidade',
        yaxis_title='Média de Avaliações',
        xaxis=dict(title_font=dict(color='black'),
                   tickfont=dict(color='black')),
        yaxis=dict(title_font=dict(color='black'),
                   tickfont=dict(color='black')),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        showlegend=False,
        margin=dict(t=5, l=10, r=10, b=10)
    )

    fig.update_traces(
        marker=dict(
            color='rgba(135,206,235,0.7)',
            line=dict(color='black', width=1)
        ),
        textposition='outside',
        textfont=dict(color='black')
    )

    st.plotly_chart(fig, use_container_width=True)


# 2º gráfico: Top 10 cidades com média baixa
def top10_cidades_media_baixa(df):
    medias = (
        df.groupby('city')['aggregate_rating']
        .mean()
        .reset_index(name='media_baixa')
        .sort_values(by='media_baixa', ascending=True)
        .head(10)
    )

    medias = medias.sort_values(by='media_baixa', ascending=False)
    medias['media_baixa'] = medias['media_baixa'].round(2)

    fig = px.bar(
        medias,
        x='city',
        y='media_baixa',
        text=medias['media_baixa'],
        hover_data={'media_baixa': False}
    )

    fig.update_layout(
        xaxis_title='Cidade',
        yaxis_title='Média de Avaliações',
        xaxis=dict(title_font=dict(color='black'),
                   tickfont=dict(color='black')),
        yaxis=dict(title_font=dict(color='black'),
                   tickfont=dict(color='black')),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        showlegend=False,
        margin=dict(t=5, l=10, r=10, b=10)
    )

    fig.update_traces(
        marker=dict(
            color='rgba(255,99,71,0.7)',
            line=dict(color='black', width=1)
        ),
        textposition='outside',
        textfont=dict(color='black')
    )

    st.plotly_chart(fig, use_container_width=True)


# 3º gráfico: Prato para 2 mais caro
def prato_2_mais_caro(df):
    top5 = (
        df.groupby('city')['average_cost_for_two(usd)']
        .mean()
        .reset_index(name='media')
        .sort_values(by='media', ascending=False)
        .head(5)
    )

    fig = px.scatter(
        top5,
        x='city',
        y='media',
        size='media',
        color='media',
        color_continuous_scale=px.colors.sequential.Plasma,
        size_max=50
    )

    fig.update_traces(hovertemplate="%{x}: $%{y:.2f}<extra></extra>")

    fig.update_layout(
        title_text="",
        xaxis_title="Cidade",
        yaxis_title="Média para dois (USD)",
        xaxis=dict(title_font=dict(color='black'), tickangle=-45),
        yaxis=dict(title_font=dict(color='black')),
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=10, r=10, t=10, b=30)
    )

    st.plotly_chart(fig, use_container_width=True)


# 4º gráfico: Cidades com prato mais caro para 2
def cidades_com_prato_mais_caro_2(df):
    top5 = (
        df.groupby('city')['average_cost_for_two(usd)']
        .mean()
        .reset_index(name='media')
        .sort_values(by='media', ascending=False)
        .head(5)
    )

    fig = px.scatter(
        top5,
        x='city',
        y='media',
        size='media',
        color='media',
        color_continuous_scale=px.colors.sequential.Plasma,
        size_max=50
    )

    fig.update_traces(hovertemplate="%{x}: $%{y:.2f}<extra></extra>")

    fig.update_layout(
        title_text="",
        xaxis_title="Cidade",
        yaxis_title="Média para dois (USD)",
        xaxis=dict(title_font=dict(color='black'),
                   tickfont=dict(color='black'),
                   tickangle=-45),
        yaxis=dict(title_font=dict(color='black'),
                   tickfont=dict(color='black')),
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=10, r=10, t=10, b=30)
    )

    st.plotly_chart(fig, use_container_width=True)


# 5º gráfico: Culinária distinta por cidade
def culinaria_distinta(df):
    culinaria_distinta = (
        df[['city', 'cuisines']]
        .assign(cuisines=df['cuisines'].str.split(', '))
        .explode('cuisines')
        .groupby('city')['cuisines']
        .nunique()
        .reset_index(name='qtde')
        .sort_values(by='qtde', ascending=False)
        .head(5)
    )

    culinaria_distinta['city'] = pd.Categorical(
        culinaria_distinta['city'],
        categories=culinaria_distinta['city'],
        ordered=True
    )

    fig = px.scatter(
        culinaria_distinta,
        x='qtde',
        y='city',
        size='qtde',
        color='qtde',
        color_continuous_scale=px.colors.sequential.Viridis,
        size_max=50
    )

    fig.update_traces(hovertemplate="%{y}: %{x} tipos<extra></extra>")

    fig.update_layout(
        title_text="",
        xaxis_title="Quantidade de tipos de culinária",
        yaxis_title="Cidade",
        xaxis=dict(title_font=dict(color='black'),
                   tickfont=dict(color='black')),
        yaxis=dict(title_font=dict(color='black'),
                   tickfont=dict(color='black'),
                   autorange="reversed"),
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=10, r=10, t=10, b=30)
    )

    st.plotly_chart(fig, use_container_width=True)


# 6º gráfico (Tabela 1): Restaurantes que aceitam reserva
def cidades_restaurantes_reserva(df):
    reserva = df[df['has_table_booking'] == 1]

    top_cidade = (
        reserva.groupby('city')['restaurant_id']
        .count()
        .reset_index(name='Aceitam reserva')
        .sort_values(by='Aceitam reserva', ascending=False)
        .rename(columns={'city': 'Cidade'})
        .reset_index(drop=True)
    )

    top_cidade.index += 1  # índice começa em 1

    # Constrói tabela HTML
    tabela_html = '<table style="width:100%; border-collapse: collapse;">'

    # Cabeçalho
    tabela_html += '<thead>'
    tabela_html += '<tr>'
    tabela_html += '<th style="border-bottom: 1px solid #ddd; text-align: center; font-weight: bold;"></th>'
    for col in top_cidade.columns:
        tabela_html += f'<th style="border-bottom: 1px solid #ddd; text-align: center; font-weight: bold;">{col}</th>'
    tabela_html += '</tr>'
    tabela_html += '</thead>'

    # Corpo
    tabela_html += '<tbody>'
    for idx, row in top_cidade.iterrows():
        tabela_html += '<tr>'
        tabela_html += f'<td style="text-align: center;">{idx}</td>'
        for col in top_cidade.columns:
            tabela_html += f'<td style="text-align: center;">{row[col]}</td>'
        tabela_html += '</tr>'
    tabela_html += '</tbody>'
    tabela_html += '</table>'

    # Wrapper com scroll (IGUAL ao que funciona)
    st.markdown(
        f"""
        <div style="max-height:300px; overflow-y:auto;">
            {tabela_html}
        </div>
        """,
        unsafe_allow_html=True
    )

# 7º gráfico (Tabela 2): Restaurantes entregando agora
def restaurantes_entregando_agora(df):
    entregando_agora = (
        df[df['is_delivering_now'] == 1]
        .groupby('city')['restaurant_id']
        .count()
        .reset_index(name='Qtde. Restaurantes')
        .sort_values(by='Qtde. Restaurantes', ascending=False)
        .rename(columns={'city': 'Cidade'})
        .reset_index(drop=True)
    )

    entregando_agora.index += 1  # índice começa em 1

    # Constrói tabela HTML
    tabela_html = '<table style="width:100%; border-collapse: collapse;">'

    # Cabeçalho
    tabela_html += '<thead>'
    tabela_html += '<tr>'
    tabela_html += '<th style="border-bottom: 1px solid #ddd; text-align: center; font-weight: bold;"></th>'
    for col in entregando_agora.columns:
        tabela_html += f'<th style="border-bottom: 1px solid #ddd; text-align: center; font-weight: bold;">{col}</th>'
    tabela_html += '</tr>'
    tabela_html += '</thead>'

    # Corpo
    tabela_html += '<tbody>'
    for idx, row in entregando_agora.iterrows():
        tabela_html += '<tr>'
        tabela_html += f'<td style="text-align: center;">{idx}</td>'
        for col in entregando_agora.columns:
            tabela_html += f'<td style="text-align: center;">{row[col]}</td>'
        tabela_html += '</tr>'
    tabela_html += '</tbody>'
    tabela_html += '</table>'

    # Wrapper com scroll (igual às outras)
    st.markdown(
        f"""
        <div style="max-height:300px; overflow-y:auto;">
            {tabela_html}
        </div>
        """,
        unsafe_allow_html=True
    )
    
# ===============================================================
# final do arquivo
# ===============================================================