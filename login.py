import streamlit as st
import pandas as pd

# Ruta de la base de datos
db_file = "usuarios.csv"

def show(change_page):
    st.markdown("<h3 style='text-align: center;'>¡Hola, bienvenid@ de nuevo!</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Ingresa a tu cuenta</p>", unsafe_allow_html=True)

    # Campos para el login
    email = st.text_input("Email", placeholder="Correo electrónico")
    password = st.text_input("Contraseña", placeholder="••••••••", type="password")

    # Botón de ingreso
    if st.button("🟢 Ingresa", use_container_width=True):
        # Cargar la base de datos
        try:
            users = pd.read_csv(db_file)
        except FileNotFoundError:
            st.error("No hay usuarios registrados. Regístrate primero.")
            return
        
        # Validar usuario
        user_exists = users[(users["email"] == email) & (users["password"] == password)]

        if not user_exists.empty:
            # Usuario válido
            st.success("Inicio de sesión exitoso")
            change_page("menu")  # Cambiar a la página del menú principal
        else:
            # Usuario no válido
            st.error("Correo o contraseña incorrecta")

    # Botón para registro
    st.markdown("<p style='text-align: center;'>¿No tienes cuenta aún?</p>", unsafe_allow_html=True)
    if st.button("🟣 Regístrate", use_container_width=True):
        change_page("registro")  # Cambiar a la página de registro
