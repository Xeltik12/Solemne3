
import streamlit as st

def set_global_styles():
    st.markdown("""
        <style>
        /* Fondo de toda la aplicación */
        body {
            background-color: #E0F2F1; /* Verde claro */
            font-family: Arial, sans-serif;
        }
        .stApp {
            background-color: #E0F2F1 !important; /* Fuerza el fondo en todo el contenedor */
        }
        /* Botones */
        .stButton>button {
            background-color: #00695C; /* Verde oscuro */
            color: white;
            border-radius: 5px;
            padding: 10px;
            font-size: 16px;
        }
        .stButton>button:hover {
            background-color: #004D40; /* Hover más oscuro */
        }
        /* Textos en negro */
        h3, p {
            color: black; /* Asegura que los textos sean negros */
        }
        </style>
    """, unsafe_allow_html=True)
