import streamlit as st
from page_config import setup_page


from utils import (
    add_country_column,
    background,
    color_name,
    convert_to_usd,
    country_name,
    create_price_type,
    ler_csv,
    rename_columns,
    sidebar_filters
)

from restaurante_utils import (mais_avaliacoes, entrega_online, media_preco_para_dois,
                               tem_reserva, diversidade_culinaria, 
                               plot_votes_online_vs_offline, plot_top_restaurants,
                               plot_top_cuisines, plot_correlation_heatmap,
                               melhores_e_piores)

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
df_filtered = sidebar_filters(df_filtered)

# =============================================================================
# Background
# =============================================================================
background()
#==============================================================================
df1 = df.copy()

# =============================================================================
# Configura título e ícone da página
# =============================================================================

setup_page("Visão Restaurante", "🍽️")  

# =============================================================================
# Layout Streamlit
# =============================================================================

st.markdown(
    "<h1 style='text-align: center;'>Visão Restaurantes</h1>",
    unsafe_allow_html=True,
)

with st.container():
    col1, col2, col3, col4, col5 = st.columns(5, gap='small')
    
    with col1:
        mais_avaliacoes(df1)
    
    with col2:
        media_preco_para_dois(df1)
    
    with col3:
        entrega_online(df1)
    
    with col4:
        tem_reserva(df1)
    
    with col5:
        diversidade_culinaria(df1)

st.markdown('---')

st.container()

st.markdown(
    "<h3 style='text-align: center;'>Top 10 Restaurantes Mais Caros</h3>",
    unsafe_allow_html=True,
)

plot_top_restaurants(df1)
 
st.markdown('---')

st.markdown(
    "<h3 style='text-align: center;'>Top 10 Culinárias Mais Caras</h3>",
    unsafe_allow_html=True,
)

plot_top_cuisines(df1, top_n=10)

st.markdown('---')

st.container()

st.markdown(
            "<h3 style='text-align: center;'>Votos Médios: Online vs Offline</h3>",
            unsafe_allow_html=True
           )
plot_votes_online_vs_offline(df1)  # sua função de plot

st.markdown('---')

st.container()

st.markdown(
        "<h3 style='text-align: center;'>Matriz de Correlação das Variáveis do Restaurante</h3>",
        unsafe_allow_html=True
    )

plot_correlation_heatmap(df1)

st.markdown('---')
    
with st.container():
    col1, col2 = st.columns(2, gap='small')
    
    with col1:
        st.markdown(
                    "<h3 style='text-align: center;'>Restaurantes Com As Melhores Médias De Avaliação</h3>",
                    unsafe_allow_html=True
                   )
        melhores_e_piores(df1, tipo='melhores')
  
    with col2:
        st.markdown(
                    "<h3 style='text-align: center;'>Restaurantes Com As Piores Médias De Avaliação</h3>",
                    unsafe_allow_html=True
                   )
        melhores_e_piores(df1, tipo='piores')
