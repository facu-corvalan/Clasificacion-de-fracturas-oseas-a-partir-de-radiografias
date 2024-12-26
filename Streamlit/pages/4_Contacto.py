import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Función para enviar el correo
def send_email(subject, body, to_email):
    from_email = "-------------"  # Cambia esto por tu correo de Gmail
    password = "---------"  # Cambia esto por tu contraseña de Gmail (o utiliza una contraseña de aplicación si usas 2FA)

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Cuerpo del mensaje
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Conexión al servidor de Gmail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        return True
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
        return False

# Función para mostrar las estrellas
def display_stars(rating):
    stars = "⭐⭐⭐⭐⭐"  # Total de 5 estrellas
    empty_stars = "☆☆☆☆☆"  # Estrellas vacías
    filled_stars = stars[:rating]  # Primeras 'rating' estrellas llenas
    empty_stars = empty_stars[rating:]  # Las restantes estrellas vacías
    return filled_stars + empty_stars  # Estrellas coloreadas y vacías combinadas

# Título de la página
st.title('Formulario de Contacto')

# Formulario de contacto
with st.form(key='contact_form'):
    nombre = st.text_input("Tu nombre:")
    email = st.text_input("Tu correo electrónico:")
    mensaje = st.text_area("Tu mensaje:")

    # Botón para enviar el formulario
    submit_button = st.form_submit_button(label='Enviar')

    if submit_button:
        # Si el formulario fue enviado, se prepara el mensaje
        if nombre and email and mensaje:
            subject = f"Mensaje de {nombre} desde el formulario de contacto"
            body = f"Nombre: {nombre}\nEmail: {email}\nMensaje: {mensaje}\nCalificación: {rating} estrellas"
            to_email = "adrian.facundo2001@gmail.com"  # Tu correo de contacto
            
            if send_email(subject, body, to_email):
                st.success("¡Mensaje enviado con éxito!")
            else:
                st.error("Hubo un error al enviar el mensaje. Intenta de nuevo.")
        else:
            st.error("Por favor, llena todos los campos.")
