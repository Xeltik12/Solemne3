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
    if st.button("🟢 Registrarse", use_container_width=True):
        try:
            # Cargar la base de datos
            users = pd.read_csv(db_file)

            # Verificar si el correo ya existe
            if email in users["email"].values:
                st.error("El correo ya existe. Intenta con otro.")
                return

            # Registrar al nuevo usuario
            new_user = pd.DataFrame({"email": [email], "usuario": [usuario], "password": [password]})
            updated_users = pd.concat([users, new_user], ignore_index=True)
            updated_users.to_csv(db_file, index=False)
            st.success("¡Registro exitoso!")

            # Redirigir al login
            change_page("login")

        except Exception as e:
            st.error(f"Hubo un error al registrar: {e}")
