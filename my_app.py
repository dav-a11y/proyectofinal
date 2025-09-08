import streamlit as st

# --- Title Section ---
st.title("PRESENTANDO NOVEDADES TECNOLÓGICAS CON PEPPER")
st.markdown("Interactúa con Pepper para conocer las últimas innovaciones tecnológicas.")

# --- Layout: 2 columns (Video + Descriptions) ---
col1, col2, col3 = st.columns([1, 2, 3 ])

with col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/5/5c/Pepper_robot.png", width=200)
    if st.button("INICIO VIDEO"):
        st.video("https://youtu.be/onoBBBNCxsY")

with col2:
    st.subheader("Novedades Tecnológicas")
    
    # Buttons for innovations
    if st.button("Novedad Tecnológica 1"):
        st.info("Breve Descripción: Esta tecnología permite que Pepper interactúe de forma más natural con los humanos.")
        
    if st.button("Novedad Tecnológica 2"):
        st.info("Breve Descripción: Sistema de reconocimiento facial avanzado para identificar emociones.")
        
    if st.button("Novedad Tecnológica 3"):
        st.info("Breve Descripción: Integración de sensores para mejorar la navegación autónoma del robot.")

# --- Chatbot / Help Section ---
with col3:
    st.markdown("---")
    st.subheader("¿Tienes dudas? Consulta con tu chatbot de confianza!")
    user_input = st.text_input("Escribe tu pregunta aquí:")
    if user_input:
    # Simulated chatbot response
        st.success(f"Pepper dice: 'Gracias por tu pregunta: \"{user_input}\". Estoy aprendiendo a responderte pronto!'")

