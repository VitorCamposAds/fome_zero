# =============================================================================
# Imports
# =============================================================================
import os
import base64
from typing import Optional

import pandas as pd
from PIL import Image
import streamlit as st
import inflection
from pathlib import Path

# ==============================================================================
#                               CONFIGURAÇÕES PÁGINA HOME
# ==============================================================================

# Caminho base do projeto (universal)
BASE_DIR = Path(__file__).resolve().parent
LOGO_PATH = BASE_DIR / "logo" / "logo.png"

def setup_sidebar(
    logo_path: Path = LOGO_PATH,
    company_name: str = "Fome Zero",
    slogan: str = "O maior dashboard de restaurantes à sua disposição"
):
    """Configura sidebar da página home."""
    image = Image.open(logo_path)
    st.sidebar.image(image, width=120)
    st.sidebar.markdown(f"# {company_name}")
    st.sidebar.markdown(f"## {slogan}")
    st.sidebar.markdown("---")


def home_text():
    """Exibe conteúdo principal do dashboard."""
    st.write("# Dashboard Fome Zero")
    st.markdown(
        """
        Este dashboard foi desenvolvido para acompanhar as métricas e prover insights para a empresa
        **Fome Zero**, cujo modelo de negócio é o tradicional de *restaurantes*.

        Ele apresenta quatro visões principais: **Geral**, **Cidade**, **País** e **Restaurante**.

        ---

        ### 🧭 Como utilizar o dashboard
        - Utilize o **menu lateral** para navegar entre as diferentes visões disponíveis.
        - Em cada visão, aplique os **filtros interativos** para ajustar a análise conforme o país desejado.
        - Os gráficos e indicadores são atualizados **automaticamente** de acordo com o(s) país(es) selecionado(s).
        - Para uma análise mais detalhada, explore cada visão de forma individual.
        - Caso esteja usando o modo **Dark**, utilize os três pontos pontilhados na vertical, localizados no canto superior direito, para acessar as configurações (Settings), ir em "Use system settings" e clicar com o mouse para uso do modo **Light**,
          uma vez que este dashboard não foi desenvolvido para o modo **Dark**.

        ---

        ### 🔹 Visões do Dashboard
        - **Visão Geral**: métricas gerenciais e cartões consolidados
        - **Visão Cidade**: insights sobre as cidades que possuem restaurantes cadastrados
        - **Visão País**: insights comparativos entre os países cadastrados
        - **Visão Restaurantes**: insights sobre as principais variáveis relacionadas aos restaurantes

        ---

        ### 🆘 Precisa de ajuda?
        - Time de Data Science no Discord  
        - 📧 vitorcampomouracosta@gmail.com
        """
    )

def setup_sidebar(logo_path: str = LOGO_PATH, company_name: str = "Fome Zero", slogan: str = "Saiba tudo sobre os melhores restaurantes!"):
    """Configura sidebar da página home."""
    image = Image.open(logo_path)
    st.sidebar.image(image, width=120)
    st.sidebar.markdown(f'# {company_name}')
    st.sidebar.markdown(f'## {slogan}')
    st.sidebar.markdown('---')

# =============================================================================
# Final do arquivo
# =============================================================================

# ==============================================================================
#                               CAMINHOS DO PROJETO
# ==============================================================================

# Caminho base do projeto (raiz)
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Pasta de imagens
LOGO_DIR = os.path.join(BASE_DIR, "logo")

# Caminhos dos arquivos
LOGO_PATH = os.path.join(LOGO_DIR, "logo.png")
BACKGROUND_PATH = os.path.join(LOGO_DIR, "background.jpg")

# Função utilitária para gerar caminhos
def get_path(*args) -> str:
    """Gera o caminho absoluto a partir da raiz do projeto."""
    return os.path.join(BASE_DIR, *args)

# =============================================================================
# Leitura de arquivos
# =============================================================================
def ler_csv(caminho_arquivo: str, **kwargs) -> Optional[pd.DataFrame]:
    """
    Lê um arquivo CSV e retorna um DataFrame do pandas.

    Parâmetros
    ----------
    caminho_arquivo : str
        Caminho do arquivo CSV.
    **kwargs
        Parâmetros adicionais do pandas.read_csv.

    Retorna
    -------
    Optional[pd.DataFrame]
        DataFrame carregado ou None se ocorrer erro.
    """
    if not os.path.exists(caminho_arquivo):
        print(f"❌ Erro: Arquivo '{caminho_arquivo}' não encontrado.")
        return None

    try:
        df = pd.read_csv(caminho_arquivo, **kwargs)
        print(f"✅ Arquivo '{caminho_arquivo}' lido com sucesso!")
        return df
    except Exception as exc:
        print(f"❌ Erro ao ler '{caminho_arquivo}': {exc}")
        return None


# =============================================================================
# Países
# =============================================================================
COUNTRIES = {
    1: "India",
    14: "Australia",
    30: "Brazil",
    37: "Canada",
    94: "Indonesia",
    148: "New Zealand",
    162: "Philippines",
    166: "Qatar",
    184: "Singapore",
    189: "South Africa",
    191: "Sri Lanka",
    208: "Turkey",
    214: "United Arab Emirates",
    215: "England",
    216: "United States of America",
}


def country_name(country_id: int) -> str:
    """Retorna o nome do país a partir do código."""
    return COUNTRIES.get(country_id, "Unknown")


def add_country_column(
    df: pd.DataFrame,
    code_col: str = "Country Code",
    new_col: str = "Country",
) -> pd.DataFrame:
    """Adiciona coluna de país ao DataFrame."""
    df[new_col] = df[code_col].map(COUNTRIES)
    return df


# =============================================================================
# Conversão de moedas
# =============================================================================
EXCHANGE_RATES_TO_USD = {
    "India": 0.0112,
    "Australia": 0.65,
    "Brazil": 0.186,
    "Canada": 0.72,
    "Indonesia": 0.000063,
    "New Zealand": 0.62,
    "Philippines": 0.0179,
    "Qatar": 0.27,
    "Singapore": 0.74,
    "South Africa": 0.057,
    "Sri Lanka": 0.00325,
    "Turkey": 0.025,
    "United Arab Emirates": 0.27,
    "England": 1.27,
    "United States of America": 1.0,
}


def convert_to_usd(country: str, value: float) -> Optional[float]:
    """Converte um valor para USD com base no país."""
    if pd.notnull(value) and country in EXCHANGE_RATES_TO_USD:
        return value * EXCHANGE_RATES_TO_USD[country]
    return None


# =============================================================================
# Price range
# =============================================================================
def create_price_type(price_range: int) -> str:
    """Cria categoria de preço."""
    price_map = ["cheap", "normal", "expensive", "gourmet"]
    if 1 <= price_range <= 4:
        return price_map[price_range - 1]
    return "gourmet"


# =============================================================================
# Cores
# =============================================================================
COLORS = {
    "3F7E00": "darkgreen",
    "5BA829": "green",
    "9ACD32": "lightgreen",
    "CDD614": "orange",
    "FFBA00": "red",
    "CBCBC8": "darkred",
    "FF7800": "darkred",
}


def color_name(color_code: str) -> str:
    """Retorna o nome da cor a partir do código."""
    return COLORS.get(color_code, "unknown")


# =============================================================================
# Padronização de colunas
# =============================================================================
def rename_columns(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Renomeia colunas para snake_case."""
    df = dataframe.copy()

    title = lambda x: inflection.titleize(x)
    remove_spaces = lambda x: x.replace(" ", "")
    snakecase = lambda x: inflection.underscore(x)

    cols = df.columns.map(title).map(remove_spaces).map(snakecase)
    df.columns = cols

    return df


# =============================================================================
# Sidebar (Streamlit)
# =============================================================================
def sidebar_filters(df: pd.DataFrame, page_name: str) -> pd.DataFrame:
    """
    Cria os filtros da sidebar do Streamlit.
    """

    base_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(base_dir, "logo", "logo.png")
    image = Image.open(image_path)
    st.sidebar.image(image, width=120)

    st.sidebar.markdown("# Fome Zero")
    st.sidebar.markdown("## Encontre os melhores restaurantes")
    st.sidebar.markdown("---")

    # Gera um key único por página
    key_multiselect = f"filter_country_multiselect_{page_name}"

    country_options = st.sidebar.multiselect(
        "Filtre selecionando os países",
        sorted(EXCHANGE_RATES_TO_USD.keys()),
        default=sorted(EXCHANGE_RATES_TO_USD.keys()),
        key=key_multiselect
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown("### Powered by @vitorcampos")

    return df[df["country"].isin(country_options)]


# =============================================================================
# Background
# =============================================================================
def background(image_file: str = BACKGROUND_PATH):
    """Adiciona imagem de fundo ao Streamlit."""

    if not os.path.exists(image_file):
        st.error(f"Imagem de fundo não encontrada: {image_file}")
        return

    with open(image_file, "rb") as f:
        data = f.read()

    encoded = base64.b64encode(data).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

