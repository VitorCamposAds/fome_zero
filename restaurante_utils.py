import os
import streamlit as st
import streamlit.components.v1 as components
import plotly.graph_objects as go
import matplotlib.pyplot as plt

#============================================================================================================================
#                           Funções
#============================================================================================================================

# ------------------- CARDS -------------------

def mais_avaliacoes(df):
    qtde_avaliacoes_restaurantes = df.groupby('restaurant_name')['votes'] \
                                    .sum() \
                                    .reset_index() \
                                    .rename(columns={'restaurant_name':'nome_restaurante', 'votes':'qtde_avaliacoes'}) \
                                    .sort_values(by='qtde_avaliacoes', ascending=False) \
                                    .head(1)
    nome = qtde_avaliacoes_restaurantes['nome_restaurante'].iloc[0]
    qtde = qtde_avaliacoes_restaurantes['qtde_avaliacoes'].iloc[0]
    valor_formatado = f"{qtde:,}".replace(",", ".")

    st.markdown(
        f"""
        <div style="
            padding:0.4rem 0.3rem;
            border-radius:8px;
            background-color:#D9E8FF;
            display:inline-block;
            flex: 1 1 200px;  /* responsivo */
            margin: 0.2rem;
        ">
            <div style="font-size:0.90rem;color:#1F3A5F;font-weight:500">
                Mais avaliações
            </div>
            <div style="font-size:1.8rem;font-weight:400;line-height:1.1;color:#102A43">
                {valor_formatado}
            </div>
            <div style="font-size:0.8rem;color:#1F3A5F;font-weight:500;margin-top:1px">
                {nome}
            </div>
        </div>
        """,
        unsafe_allow_html=True            
    )

def media_preco_para_dois(df):
    media = df['average_cost_for_two(usd)'].mean()
    valor_formatado = f"${round(media, 2):,}".replace(",", ".")

    st.markdown(
        f"""
        <div style="
            padding:0.4rem 0.3rem;
            border-radius:8px;
            background-color:#D9E8FF;
            display:inline-block;
            flex: 1 1 200px;
            margin: 0.2rem;
        ">
            <div style="font-size:0.90rem;color:#1F3A5F;font-weight:500; text-align: center">
                Preços Para Dois
            </div>
            <div style="font-size:1.8rem;font-weight:350;line-height:1.1;color:#102A43;text-align:center">
                {valor_formatado}
            </div>
            <div style="font-size:0.90rem;color:#1F3A5F;font-weight:500;text-align: center">
                Média
            </div>
        </div>
        """,
        unsafe_allow_html=True            
    )

def entrega_online(df):
    online = df[df['has_online_delivery'] == 1]
    valor_formatado = f"{online['restaurant_id'].count():,}".replace(",", ".")
    st.markdown(
        f"""
        <div style="
            padding:0.4rem 0.3rem;
            border-radius:8px;
            background-color:#D9E8FF;
            display:inline-block;
            flex: 1 1 200px;
            margin: 0.2rem;
        ">
            <div style="font-size:0.90rem;color:#1F3A5F;font-weight:500">
                Delivery Online
            </div>
            <div style="font-size:1.8rem;font-weight:400;line-height:1.1;color:#102A43; text-align: center">
                {valor_formatado}
            </div>
            <div style="font-size:0.90rem;color:#1F3A5F;font-weight:500;text-align: center">
                Restaurantes
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

def tem_reserva(df):
    tem_reserva = df[df['has_table_booking'] == 1]
    valor_formatado = f"{tem_reserva['restaurant_id'].count():,}".replace(",", ".")
    st.markdown(
        f"""
        <div style="
            padding:0.4rem 0.3rem;
            border-radius:8px;
            background-color:#D9E8FF;
            display:inline-block;
            flex: 1 1 200px;
            margin: 0.2rem;
        ">
            <div style="font-size:0.90rem;color:#1F3A5F;font-weight:500">
                    Aceitam Reserva
            </div>
            <div style="font-size:1.8rem;font-weight:400;line-height:1.1;color:#102A43; text-align: center">
                {valor_formatado}
            </div>
            <div style="font-size:0.90rem;color:#1F3A5F;font-weight:500;text-align: center">
                Restaurantes
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

def diversidade_culinaria(df):
    diversidade_cuisines = df.groupby('restaurant_name')['cuisines'] \
                             .nunique() \
                             .reset_index(name='qtd_cozinhas') \
                             .sort_values(by='qtd_cozinhas', ascending=False)\
                             .head(1)
    nome = diversidade_cuisines['restaurant_name'].iloc[0]
    qtde = diversidade_cuisines['qtd_cozinhas'].iloc[0]
    valor_formatado = f"{qtde}"

    st.markdown(
        f"""
        <div style="
            padding:0.4rem 0.3rem;
            border-radius:8px;
            background-color:#D9E8FF;
            display:inline-block;
            flex: 1 1 200px;
            margin: 0.2rem;
        ">
            <div style="font-size:0.90rem;color:#1F3A5F;font-weight:500; text-align: center">
                Tipos de Comida
            </div>
            <div style="font-size:1.8rem;font-weight:350;line-height:1.1;color:#102A43;text-align:center">
                {valor_formatado}
            </div>
            <div style="font-size:0.8rem;color:#1F3A5F;font-weight:500;margin-top:1px;text-align:center">
                {nome}
            </div>
        </div>
        """,
        unsafe_allow_html=True            
    )

# ------------------- GRÁFICOS -------------------

def plot_top_restaurants(df, top_n=10):
    media_preco = df.groupby('restaurant_name')['average_cost_for_two(usd)'].mean().reset_index()
    media_preco = media_preco.sort_values(by='average_cost_for_two(usd)', ascending=False)
    media_preco_top = media_preco.head(top_n)

    fig, ax = plt.subplots(figsize=(25, 10))
    fig.patch.set_alpha(0)
    ax.set_facecolor("none")

    bars = ax.bar(
        media_preco_top["restaurant_name"],
        media_preco_top["average_cost_for_two(usd)"],
        color="skyblue",
        edgecolor="black",
        linewidth=1,
    )

    ax.yaxis.grid(True, color="gray", linestyle="--", linewidth=0.5)
    ax.xaxis.grid(False)
    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.set_xlabel("Nome do Restaurante", labelpad=20, fontsize=25)
    ax.set_ylabel("Preço Médio (USD)", labelpad=20, fontsize=25)
    plt.xticks(rotation=75, fontsize=30)
    plt.yticks(fontsize=30)

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 2,
            f"${height:.2f}",
            ha="center",
            va="bottom",
            fontsize=25,
            fontweight="bold",
        )

    st.pyplot(fig)

def plot_top_cuisines(df, coluna_culinaria='cuisines', coluna_preco='average_cost_for_two(usd)', top_n=10):
    media_preco = df.groupby(coluna_culinaria)[coluna_preco].mean().reset_index()
    media_preco = media_preco.sort_values(by=coluna_preco, ascending=False)
    media_preco_top = media_preco.head(top_n)

    fig, ax = plt.subplots(figsize=(25, 10))
    fig.patch.set_alpha(0)
    ax.set_facecolor("none")

    bars = ax.bar(
        media_preco_top[coluna_culinaria],
        media_preco_top[coluna_preco],
        color="skyblue",
        edgecolor="black",
        linewidth=1,
    )

    ax.yaxis.grid(True, color="gray", linestyle="--", linewidth=0.5)
    ax.xaxis.grid(False)
    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.set_xlabel("Tipo de Culinária", labelpad=20, fontsize=25)
    ax.set_ylabel("Preço Médio (USD)", labelpad=20, fontsize=25)
    plt.xticks(rotation=75, fontsize=30)
    plt.yticks(fontsize=30)

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 2,
            f"${height:.2f}",
            ha="center",
            va="bottom",
            fontsize=25,
            fontweight="bold",
        )

    st.pyplot(fig)

def plot_votes_online_vs_offline(df):
    media_votes_online = df[df['has_online_delivery'] == 1]['votes'].mean()
    media_votes_offline = df[df['has_online_delivery'] == 0]['votes'].mean()
    diferenca_percentual = ((media_votes_online - media_votes_offline) / media_votes_offline) * 100

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=['Sem entrega online','Com entrega online'],
        y=[media_votes_offline, media_votes_online],
        mode='lines+markers+text',
        text=[f"{round(media_votes_offline,0)}", f"{round(media_votes_online,0)}"],
        textposition='top center',
        line=dict(color='black', width=2),
        marker=dict(color='black', size=12),
        textfont=dict(color='black', size=12)
    ))

    fig.add_annotation(
        x=1,
        y=media_votes_online + (media_votes_online * 0.05),
        text=f"{round(diferenca_percentual, 2)}% a mais de avaliações",
        showarrow=True,
        arrowhead=2,
        arrowcolor='black',
        font=dict(color='black', size=12),
        bgcolor='rgba(255,255,255,0.8)',
        bordercolor='black',
        borderwidth=1
    )

    fig.update_layout(
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        showlegend=False,
        xaxis=dict(
            tickfont=dict(color='black', size=12),
            showgrid=True,
            gridcolor='rgba(0,0,0,0.3)',
            zeroline=False
        ),
        yaxis=dict(
            tickfont=dict(color='black', size=12),
            showgrid=True,
            gridcolor='rgba(0,0,0,0.3)',
            zeroline=False
        )
    )

    st.plotly_chart(fig, use_container_width=True)

def plot_correlation_heatmap(df, method='spearman'):
    df_corr = df.copy()
    df_corr['has_table_booking'] = df_corr['has_table_booking'].apply(lambda x: 1 if x else 0)
    df_corr['has_online_delivery'] = df_corr['has_online_delivery'].apply(lambda x: 1 if x else 0)
    df_corr['is_delivering_now'] = df_corr['is_delivering_now'].apply(lambda x: 1 if x else 0)

    cols = ['aggregate_rating', 'average_cost_for_two(usd)', 'votes', 
            'has_table_booking', 'has_online_delivery', 'is_delivering_now', 'price_range']
    df_corr = df_corr[cols]
    corr_matrix = df_corr.corr(method=method)

    fig = go.Figure(data=go.Heatmap(
        z=corr_matrix.values,
        x=corr_matrix.columns,
        y=corr_matrix.columns,
        colorscale='RdBu',
        zmid=0,
        showscale=True,
        text=corr_matrix.round(2).values,
        texttemplate="%{text}",
        hovertemplate=" %{x} x %{y} = %{z}<extra></extra>"
    ))

    fig.update_layout(
        height=500,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        showlegend=False,
        xaxis=dict(
            tickfont=dict(color='black', size=12),
            showgrid=True,
            gridcolor='rgba(0,0,0,0.3)',
            zeroline=False
        ),
        yaxis=dict(
            tickfont=dict(color='black', size=12),
            showgrid=True,
            gridcolor='rgba(0,0,0,0.3)',
            zeroline=False
        )
    )

    st.plotly_chart(fig, use_container_width=True)

# ------------------- TABELAS -------------------

def melhores_e_piores(df, tipo="melhores"):
    restaurante_media = (
        df.groupby('restaurant_name')['aggregate_rating']
          .mean()
          .reset_index(name='Nota média')
          .sort_values(by='restaurant_name', ascending=True)
          .rename(columns={'restaurant_name':'Nome do Restaurante'})
    )

    if tipo == "melhores":
        nota_ref = restaurante_media['Nota média'].max()
    else:
        nota_ref = restaurante_media['Nota média'].min()

    tabela = restaurante_media[
        restaurante_media['Nota média'] == nota_ref
    ].reset_index(drop=True)

    tabela.index += 1  # índice começa em 1

    # Constrói tabela HTML (mesmo padrão)
    tabela_html = '<table style="width:100%; border-collapse: collapse;">'

    # Cabeçalho
    tabela_html += '<thead>'
    tabela_html += '<tr>'
    tabela_html += '<th style="border-bottom: 1px solid #ddd; text-align: center; font-weight: bold;"></th>'
    for col in tabela.columns:
        tabela_html += f'<th style="border-bottom: 1px solid #ddd; text-align: center; font-weight: bold;">{col}</th>'
    tabela_html += '</tr>'
    tabela_html += '</thead>'

    # Corpo
    tabela_html += '<tbody>'
    for idx, row in tabela.iterrows():
        tabela_html += '<tr>'
        tabela_html += f'<td style="text-align: center;">{idx}</td>'
        for col in tabela.columns:
            valor = f"{row[col]:.2f}" if col == "Nota média" else row[col]
            tabela_html += f'<td style="text-align: center;">{valor}</td>'
        tabela_html += '</tr>'
    tabela_html += '</tbody>'
    tabela_html += '</table>'

    # Wrapper com scroll (igual às outras)
    st.markdown(
        f"""
        <div style="max-height:400px; overflow-y:auto;">
            {tabela_html}
        </div>
        """,
        unsafe_allow_html=True
    )

# ------------------- CONTAINER RESPONSIVO PARA CARDS -------------------

def exibir_cards_responsivos(df):
    st.markdown(
        """
        <div style="
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
            justify-content: flex-start;
        ">
        """,
        unsafe_allow_html=True
    )

    mais_avaliacoes(df)
    media_preco_para_dois(df)
    entrega_online(df)
    tem_reserva(df)
    diversidade_culinaria(df)

    st.markdown("</div>", unsafe_allow_html=True)