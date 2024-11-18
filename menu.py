
import streamlit as st

def show(change_page):
    # Barra superior con mensaje de bienvenida
    st.markdown("""
        <div style="background-color: #00695C; padding: 10px; text-align: center; border-radius: 5px;">
            <h1 style="color: white; margin: 0;">Bienvenid@, Usuario!</h1>
        </div>
    """, unsafe_allow_html=True)

    # Espacio
    st.markdown("<br>", unsafe_allow_html=True)

    # Botones organizados en dos columnas
    st.markdown("### Accede a:")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Cursos/Talleres"):
            st.write("Aquí iría la sección de Cursos/Talleres.")
        if st.button("7R"):
            st.write("Aquí iría la sección de 7R.")

    with col2:
        if st.button("Podcast"):
            st.write("Aquí iría la sección de Podcast.")
        if st.button("Comunidad"):
            st.write("Aquí iría la sección de Comunidad.")

    # Barra de navegación inferior
    st.markdown("""
        <style>
        .nav-bar {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #00695C;
            padding: 10px 0;
            display: flex;
            justify-content: space-around;
            align-items: center;
            color: white;
            font-size: 16px;
            font-weight: bold;
            z-index: 9999;
        }
        .nav-button {
            color: white;
            text-decoration: none;
            background-color: transparent;
            border: none;
            cursor: pointer;
            font-size: 16px;
        }
        .nav-button:hover {
            color: #E0F2F1;
        }
        </style>
        <div class="nav-bar">
            <form>
                <button class="nav-button" type="button">🏠 Home</button>
                <button class="nav-button" type="button">🤝 Comunidad</button>
                <button class="nav-button" type="button">📚 Talleres</button>
                <button class="nav-button" type="button">👤 Perfil</button>
            </form>
        </div>
    """, unsafe_allow_html=True)
