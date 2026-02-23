import streamlit as st
import pandas as pd

st.title("Meu Primeiro App Streamlit 🎀")

st.write("Olá, Michelle! Seu Streamlit está funcionando perfeitamente.")

name = st.text_input("Digite seu nome:")
if name:
    st.success(f"Bem-vinda ao Streamlit, {name}!")

uploaded = st.file_uploader("Envie um arquivo CSV", type=["csv"])
if uploaded:
    df = pd.read_csv(uploaded)
    st.write("Pré-visualização dos dados:")
    st.dataframe(df) 