import streamlit as st

# --- Title Section ---
st.title("PRESENTANDO NOVEDADES TECNOLÓGICAS CON PEPPER")
st.markdown("Interactúa con Pepper para conocer las últimas innovaciones tecnológicas.")

# --- Layout: 2 columns (Video + Descriptions) ---
col1, col2 = st.columns([1, 2])

with col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/5/5c/Pepper_robot.png", width=200)
    if st.button("INICIO VIDEO"):
        st.video("https://youtu.be/onoBBBNCxsY")

with col2:
    st.subheader("Novedades Tecnológicas")
    
    # Buttons for innovations
    if st.button("Novedad Tecnológica 1"):
        st.info("🤖 Agentes Autónomos de IA: Sistemas que perciben su entorno, toman decisiones y actúan sin supervisión constante.")

    if st.button("Novedad Tecnológica 2"):
        st.info("💡 Fotónica Integrada: Chips ópticos para transmisión de datos ultrarrápida y eficiente en energía.")

    if st.button("Novedad Tecnológica 3"):
        st.info("🧫 Órganos en Chip: Dispositivos que replican funciones de órganos humanos para pruebas médicas sin animales.")

# --- Chatbot / Help Section (ahora abajo) ---
st.markdown("---")
st.subheader("¿Tienes dudas? ¡Consulta con tu chatbot de confianza!")
user_input = st.text_input("Escribe tu pregunta aquí:")
if user_input:
    st.success(f"Pepper dice: 'Gracias por tu pregunta: \"{user_input}\". ¡Estoy aprendiendo a responderte pronto!'")


