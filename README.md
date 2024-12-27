#  Clasificación de fracturas óseas a partir de radiografías
<p align="center">
   <br />
   <img src="img\hueso-roto.jpg" width="55%">
   <br />
</p>
<div align="center">
  <img src="https://img.shields.io/badge/Estado-En%20desarrollo-yellow" alt="Proyecto en desarrollo">
</div>

# Tabla de Contenido

* [Contextualización](#Contextualización)
* [Enfoque en Estudiantes y Formación](#Enfoque-en-Estudiantes-y-Formación)
* [Futuras Funcionalidades y Escalabilidad](#Futuras-Funcionalidades-y-Escalabilidad)
* [Beneficios](#Beneficios)
* [La Importancia de la Inteligencia Artificial en el Ámbito Médico](#La-Importancia-de-la-Inteligencia-Artificial-en-el-Ámbito-Médico)
* [Nuestra plataforma y productos](#Nuestra-plataforma-y-productos)
* [Conjunto de Datos](#Conjunto-de-Datos)
* [Preprocesamiento de Imágenes](#Preprocesamiento-de-Imágenes)
* [División del Dataset](#División-del-Dataset)
* [Herramientas para el etiquetado de datos](#Herramientas-para-el-etiquetado-de-datos)
* [Librerías para la creación del modelo](#Librerías-para-la-creación-del-modelo)
* [Herramientas para la Visualización de Datos](#Herramientas-para-la-Visualización-de-Datos)
* [Cumplimiento Ético y Regulatorio](#Cumplimiento-Ético-y-Regulatorio)
* [Autores](#Autores)

# Contextualización

La detección y clasificación de fracturas óseas es un desafío significativo tanto en la formación académica como en la práctica médica, ya que un diagnóstico temprano y preciso es crucial para el tratamiento efectivo y la recuperación de los pacientes. En este contexto, la integración de tecnologías avanzadas como la inteligencia artificial (IA) y el aprendizaje profundo ofrece una herramienta poderosa para apoyar no solo a los profesionales de la salud, sino también a estudiantes que buscan fortalecer sus habilidades en interpretación radiológica.

Nuestro MVP (Producto Mínimo Viable) se desarrolla con un enfoque educativo y práctico, centrándose en esta primera etapa exclusivamente en la detección de fracturas. Este sistema es capaz de detectar de manera eficiente áreas sospechosas en radiografías que podrían corresponder a fracturas, apoyando como un recurso innovador tanto para la formación académica como para la validación en entornos médicos. Al facilitar el aprendizaje práctico y optimizar el análisis radiológico, el sistema contribuye al desarrollo de habilidades clínicas

# Enfoque en Estudiantes y Formación

Este MVP está diseñado principalmente hacia estudiantes de medicina, radiología y áreas relacionadas. Al proporcionarles acceso a un sistema automatizado, los estudiantes podrán:

Practicar y reforzar sus habilidades: Identificando fracturas en radiografías con la ayuda de un modelo inteligente.
Obtener retroalimentación objetiva: Comparando sus interpretaciones con los resultados del sistema para mejorar su precisión.
Familiarizarse con tecnologías avanzadas: Integrando IA y aprendizaje profundo en su formación desde etapas tempranas.
Además, el sistema apoyará como un recurso educativo a docentes, facilitando la enseñanza de la interpretación radiológica mediante el uso de ejemplos interactivos y casos prácticos guiados.

# Futuras Funcionalidades y Escalabilidad

Si bien el MVP se limita inicialmente a la detección, las futuras actualizaciones incluirán un etiquetado detallado de las imágenes, desarrollado en colaboración con médicos y expertos para garantizar su precisión y utilidad clínica. A medida que el sistema evolucione, se incorporarán funciones avanzadas, como la clasificación de fracturas según tipologías específicas y el análisis de regiones anatómicas adicionales, ampliando así su utilidad tanto en entornos educativos como médicos.

# Beneficios 
* Accesibilidad educativa: Una herramienta innovadora para estudiantes y docentes que refuerza el aprendizaje práctico.
* Facilitación del aprendizaje: Proporciona un entorno seguro para la práctica y la experimentación con imágenes médicas reales o simuladas.
* Base para investigación y desarrollo: Posibilita la validación del modelo en entornos educativos, sentando las bases para su implementación clínica en el futuro.

# La Importancia de la Inteligencia Artificial en el Ámbito Médico

La Inteligencia Artificial está transformando la medicina al mejorar el diagnóstico, tratamiento y gestión de enfermedades. Algunos de sus principales beneficios son:

1. **Diagnóstico más preciso**: Analizar grandes cantidades de datos médicos, detectando patrones difíciles de identificar para los médicos, lo que permite diagnósticos más tempranos y precisos.

2. **Optimización de la atención al paciente**: Mejora la gestión hospitalaria, optimizando recursos y procesos, y agiliza la atención al paciente.

3. **Investigación acelerada**: Acelera el descubrimiento de nuevos tratamientos y medicamentos mediante el análisis de grandes volúmenes de datos clínicos.

4. **Telemedicina**: Facilita consultas a distancia de calidad, mejorando el acceso a la atención médica en áreas remotas.


## Nuestra plataforma y productos 

Contamos con nuestra web donde podrás encontrar los productos desarrollados durante este proyecto.
En ella puedes encontrar:

* **Home**: Presentación del proyecto.
* **Sobre nosotros**: Información sobre nuestra empresa, quiénes somos y qué hacemos.
* **Productos**: En esta sección encontrarás los productos que desarrollamos para este proyecto y la descripción de cada uno de ellos.
* **Equipo**: En este apartado conocerás al increíble equipo que desarrolló este proyecto y su información de contacto.


# Conjunto de Datos
Para este proyecto utilizamos como fuente de datos:
  - MURA, para su descarga haga clic [aquí](https://stanfordmlgroup.github.io/competitions/mura/)

## Preprocesamiento de Imágenes
- Conversión a escala de grises (si las imágenes no lo están).
- Normalización de valores de píxeles.
- Redimensionamiento a un tamaño uniforme.

## División del Dataset
- Entrenamiento (80%)
- Prueba (20%)

## Herramientas para el etiquetado de datos

<img src="https://cdn-icons-png.flaticon.com/512/8552/8552125.png" width="20px" height="20px"> **LabelImg**: Herramienta de código abierto para el etiquetado de imágenes.

## Libreria y framework de aprendizaje profundo 

<img src="https://static-00.iconduck.com/assets.00/tensorflow-icon-955x1024-hd4xzbqj.png" width="20px" > **TensorFlow**: Biblioteca de Google para construir y entrenar modelos de machine learning.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Keras_logo.svg/1200px-Keras_logo.svg.png" width="20px" height="20px"> **Keras**: Simplifica la construcción y el entrenamiento de redes neuronales al proporcionar una API fácil de usar.

<img src="https://static-00.iconduck.com/assets.00/pytorch-icon-1694x2048-jgwjy3ne.png" width="20px" height="20px"> **PyTorch**: Plataforma de aprendizaje profundo que destaca por su enfoque dinámico y facilidad para depuración, ideal tanto para investigación como producción.

## Herramientas para la Visualización de Datos

<img src="img\streamlit-removebg-preview.png" width="30px"> **Streamlit**: Para la creación de aplicaciones web interactivas y visualización de datos en tiempo real.

# Cumplimiento Ético y Regulatorio

- Garantizar que los datos están anonimizados.
- Adherirse a normativas locales e internacionales.
- Implementar explicabilidad en el modelo (e.g., por qué clasifica como fractura).

# Autores

La dedicación y el espíritu colaborativo del equipo fundamentales para hacer realidad este proyecto.

| [<img src="https://avatars.githubusercontent.com/u/166779106?v=4" width=115><br><sub>Facundo Corvalan</sub>](https://github.com/facu-corvalan) | [<img src="https://avatars.githubusercontent.com/u/123128073?v=4" width=115><br><sub>Javier Yañez</sub>](https://github.com/javyleonhart) | [<img src="https://avatars.githubusercontent.com/u/163685041?v=4" width=115><br><sub>Michael Martinez</sub>](https://github.com/bkmay1417) | [<img src="https://avatars.githubusercontent.com/u/123877201?v=4" width=115><br><sub>Jesus H. Parra B.</sub>](https://github.com/ing-jhparra)
| :---: | :---: | :---: | :---: |