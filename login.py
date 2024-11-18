
import streamlit as st

def show(change_page):
    st.markdown("<h3 style='text-align: center;'>¡Hola, bienvenid@ de nuevo!</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Ingresa a tu cuenta</p>", unsafe_allow_html=True)

    # Campos para el login
    email = st.text_input("Email", placeholder="Correo electrónico")
    password = st.text_input("Contraseña", placeholder="••••••••", type="password")

    # Botón de ingreso
    if st.button("🟢 Ingresa", use_container_width=True):
        change_page("menu")  # Cambiar a la página del menú principal

    # Botón para registro
    st.markdown("<p style='text-align: center;'>¿No tienes cuenta aún?</p>", unsafe_allow_html=True)
    if st.button("🟣 Regístrate", use_container_width=True):
        change_page("registro")  # Cambiar a la página de registro
