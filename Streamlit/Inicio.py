import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(page_title='Clasificación de Fracturas Óseas', page_icon='🦴', layout='wide')

# Portada
#with st.container():
#    portada = Image.open('')
#    st.image(portada, use_column_width=True)

# Introducción
with st.container():
    st.markdown("<h2 style='text-align: center;'>Clasificación de Fracturas Óseas a partir de Radiografías</h2>", unsafe_allow_html=True)
    st.markdown("""
        <p style='text-align: center;'>
        Este proyecto utiliza Inteligencia Artificial para detectar y clasificar fracturas óseas, 
        apoyando tanto la formación académica como la práctica médica.
        </p>
        """, unsafe_allow_html=True)

# Objetivos
with st.container():
    st.markdown("## **Objetivos del Proyecto**", unsafe_allow_html=True)
    st.markdown("""
    - 🏥 **Diagnóstico Asistido**: Mejorar la precisión y rapidez en la detección de fracturas.
    - 📚 **Educación**: Facilitar el aprendizaje de estudiantes de medicina y radiología mediante herramientas interactivas.
    - 🔬 **Innovación Tecnológica**: Integrar IA y aprendizaje profundo en aplicaciones médicas prácticas.
    """)

# Servicios/Funciones del Proyecto
with st.container():
    st.markdown("## **Funciones Principales**", unsafe_allow_html=True)
    st.markdown("""
    - 🖼️ **Procesamiento de Imágenes**: Preprocesamiento de radiografías para mejorar su análisis.
    - 🧠 **Modelos de IA**: Detección automática de fracturas óseas utilizando redes neuronales profundas.
    - 📊 **Visualización de Resultados**: Dashboards interactivos para análisis y validación de resultados.
    - 📁 **Gestión de Datos**: Herramientas para etiquetado y segmentación de imágenes médicas.
    """)

# Por qué este proyecto es importante
with st.container():
    st.header("¿Por qué es importante?")
    st.markdown("""
        - 💡 **Diagnósticos más precisos**: Facilita la identificación temprana de fracturas difíciles de detectar.
        - 📈 **Accesibilidad educativa**: Una herramienta innovadora para estudiantes y docentes.
        - 🤖 **Base para investigación clínica**: Potencial para implementación en hospitales y clínicas.
    """)

# Contacto equipo
with st.container():
    st.header('Equipo de trabajo')

    # Datos de los miembros del equipo
    miembros = [
        {"nombre": "Facundo Corvalan", "imagen": "https://avatars.githubusercontent.com/u/166779106?v=4", "linkedin": "www.linkedin.com/in/facundo-corvalan", "github": "https://github.com/facu-corvalan"},
        {"nombre": "Javier Yañez", "imagen": "https://avatars.githubusercontent.com/u/123128073?v=4", "linkedin": "https://www.linkedin.com/in/michael-martinez-8773ab143/", "github": "https://github.com/bkmay1417"},
        {"nombre": "Michael Martinez", "imagen": "https://avatars.githubusercontent.com/u/163685041?v=4", "linkedin": "https://www.linkedin.com/in/jiy93/", "github": "https://github.com/javyleonhart"},
        {"nombre": "Jesus H. Parra B.", "imagen": "https://avatars.githubusercontent.com/u/123877201?v=4", "linkedin": "https://www.linkedin.com/in/jesus-horacio-parra-belandria/", "github": "https://github.com/ing-jhparra"}
    ]

cols = st.columns(4)  

# Iconos para LinkedIn y correo electrónico
icon_linkedin = "https://cdn-icons-png.flaticon.com/256/174/174857.png" 
icon_github = "https://img.icons8.com/m_outlined/512/github.png" 

for col, miembro in zip(cols, miembros):
    with col:
        st.markdown(f"""
        <div style="text-align: center;">
            <img src="{miembro['imagen']}" alt="{miembro['nombre']}" style="width: 200px; height: 200px; border-radius: 50%; margin-bottom: 15px;"> 
            <p style="font-size: 30px; margin-top: 20px; margin-bottom: 10px;"><strong>{miembro['nombre']}</strong></p>
            <div style="margin-top: 10px;">  <!-- Espacio entre el nombre y los iconos -->
                <a href="{miembro['linkedin']}" target="_blank" style="margin-right: 15px;">  <!-- Separación entre los iconos (LinkedIn y GitHub) -->
                    <img src="{icon_linkedin}" alt="LinkedIn" width="30">
                </a>
                <a href="{miembro['github']}" target="_blank">
                    <img src="{icon_github}" alt="GitHub" width="60">
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)
