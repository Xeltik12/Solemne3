
import streamlit as st
import pandas as pd
import os

# Verificar si existe la base de datos
db_file = "usuarios.csv"
if not os.path.exists(db_file):
    pd.DataFrame(columns=["email", "usuario", "password"]).to_csv(db_file, index=False)

def show(change_page):
    st.markdown("<h3 style='text-align: center;'>Crea tu cuenta</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Comencemos con algunos datos</p>", unsafe_allow_html=True)

    # Campos de registro
    email = st.text_input("Email", placeholder="Correo electrónico")
    usuario = st.text_input("Usuario", placeholder="Nombre de usuario")
    password = st.text_input("Contraseña", placeholder="••••••••", type="password")

    # Botón para registrar
    if st.button("🟢 Siguiente", use_container_width=True):
        # Guardar datos en la base de datos
        new_user = pd.DataFrame({"email": [email], "usuario": [usuario], "password": [password]})
        existing_users = pd.read_csv(db_file)
        updated_users = pd.concat([existing_users, new_user], ignore_index=True)
        updated_users.to_csv(db_file, index=False)
        st.success("¡Registro exitoso!")
        change_page("menu")  # Cambiar a la página del menú principal

    # Botón para ir al login
    st.markdown("<p style='text-align: center;'>¿Ya tienes una cuenta?</p>", unsafe_allow_html=True)
    if st.button("🟣 Ingresa", use_container_width=True):
        change_page("login")  # Cambiar a la página de login
