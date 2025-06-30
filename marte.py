import streamlit as st
import time

# Función de login
def login():
    st.title("🔐 AccesoLab - Iniciar Sesión")
    correo = st.text_input("Correo electrónico")
    contraseña = st.text_input("Contraseña", type="password")
    if st.button("Ingresar"):
        if correo == "admin@accesolab.com" and contraseña == "1234":
            st.success("Inicio de sesión exitoso 🎉")
            return True
        else:
            st.error("Correo o contraseña incorrectos.")
    return False

# Función para mostrar backlog con botones reales
def mostrar_backlog_activo():
    st.title("📋 Product Backlog Interactivo")

    st.subheader("⌨️ Navegación con teclado")
    st.write("Puedes usar la tecla TAB y ENTER para moverte por los botones.")
    if st.button("Probar navegación"):
        # Acción real: mostrar barra de progreso para simular carga
        with st.spinner('Probando navegación...'):
            time.sleep(2)
        st.success("🔄 Navegación accesible habilitada (usa TAB para moverte).")

    st.subheader("🗣️ Simulación de TTS (sin audio)")
    st.write("Simula que el sistema lee en voz alta una frase.")
    if st.button("Simular lectura de texto"):
        # Acción real: mostrar texto dinámico con animación simple
        frase = "Bienvenido a AccesoLab, plataforma accesible para todos."
        texto_mostrado = st.empty()
        for i in range(len(frase)+1):
            texto_mostrado.text(frase[:i])
            time.sleep(0.05)
        st.success("📖 Lectura simulada completada.")

    st.subheader("🔊 Feedback sonoro simulado")
    st.write("Simula que se reproduce un sonido al hacer clic.")
    if st.button("Simular sonido"):
        # Acción real: reproducir un sonido con HTML (solo funciona en navegador)
        st.components.v1.html("""
        <audio autoplay>
            <source src="https://actions.google.com/sounds/v1/alarms/alarm_clock.ogg" type="audio/ogg">
        </audio>
        """, height=50)
        st.success("🔔 Sonido reproducido (solo en navegador compatible).")

    st.subheader("⚙️ Ajustes de accesibilidad")
    if st.button("Activar modo accesible"):
        # Acción real: cambiar el tema de la app (simulado con un mensaje y color)
        st.markdown(
            """
            <style>
            .stApp {
                background-color: black;
                color: white;
            }
            </style>
            """, unsafe_allow_html=True
        )
        st.success("✅ Modo accesible activado con alto contraste y soporte ampliado.")

# App principal
if __name__ == "__main__":
    if login():
        st.markdown("---")
        mostrar_backlog_activo()