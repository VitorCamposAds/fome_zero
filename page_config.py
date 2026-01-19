import streamlit as st

def setup_page(title: str, icon: str):
    """Configura título e ícone da página Streamlit."""
    st.set_page_config(
        page_title=title,
        page_icon=icon,
        layout="wide"
    )