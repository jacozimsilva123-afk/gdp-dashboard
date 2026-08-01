import streamlit as st

st.set_page_config(page_title="Meus Atalhos", layout="centered")
st.title("🔗 Meus Atalhos")

st.link_button("Abrir Google", "https://google.com", use_container_width=True)
st.link_button("Abrir YouTube", "https://youtube.com", use_container_width=True)
st.link_button("Abrir WhatsApp Web", "https://web.whatsapp.com", use_container_width=True)
