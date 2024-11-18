
import streamlit as st
import login
import registro
import menu
import styles

# Configuración inicial
st.set_page_config(page_title="PymeConecta", layout="centered")

# Aplicar estilos globales
styles.set_global_styles()

# Control de navegación entre pantallas
if "page" not in st.session_state:
    st.session_state.page = "login"  # Página inicial

# Función para cambiar de página
def change_page(page):
    st.session_state.page = page

# Navegación entre las páginas
if st.session_state.page == "login":
    login.show(change_page)
elif st.session_state.page == "registro":
    registro.show(change_page)
elif st.session_state.page == "menu":
    menu.show(change_page)
