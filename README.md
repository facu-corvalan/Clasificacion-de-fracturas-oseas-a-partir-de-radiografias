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

* [Introducción](#Introducción)
* [Definición del Problema](#Definición-del-Problema)
* [Recopilación de Datos](#Recopilación-de-Datos)
* [Selección de la Arquitectura del Modelo](#Selección-de-la-Arquitectura-del-Modelo)
* [Evaluación y Validación](#Evaluación-y-Validación)
* [Despliegue](#Despliegue)
* [Tecnologías Utilizadas](#Herramientas-y-Tecnologías-Recomendadas)
* [Conclusión](#Conclusión)
* [Recursos](#Recursos)
* [Cumplimiento Ético y Regulatorio](#Cumplimiento-Ético-y-Regulatorio)
* [Autores](#Autores)

# Introducción  

La detección y clasificación de fracturas óseas es un desafío crucial en el ámbito de la radiología, ya que un diagnóstico temprano y exacto puede marcar la diferencia en el tratamiento y recuperación de los pacientes. La integración de tecnologías avanzadas, como la inteligencia artificial (IA), representa una oportunidad significativa para mejorar la eficiencia y efectividad en los procesos de diagnóstico médico.

A través del análisis automatizado de imágenes médicas, como radiografías el modelo permitirá identificar rápidamente anomalías, reducir los tiempos de evaluación y priorizar casos críticos para garantizar una atención más inmediata y precisa.

El sistema se centrará inicialmente en el húmero, abordando las fracturas de este hueso según las tipologías estándar de clasificación. En un futuro, si el proyecto demuestra ser efectivo, se considerará la incorporación de otras partes del cuerpo de alta incidencia clínica, como la muñeca, cadera, pierna y columna vertebral. Además, estará diseñado para integrarse de manera fluida en los flujos de trabajo radiológicos, ofreciendo informes preliminares y soporte técnico continuo, todo ello bajo estrictas normativas de protección de datos. Este avance tecnológico promete no solo optimizar el diagnóstico médico, sino también mejorar significativamente la experiencia y los resultados para los pacientes.

# Definición del Problema

## Nuestro objetivo principal (temp)
Desarrollar un modelo de inteligencia artificial capaz de clasificar fracturas óseas en tipos específicos, como fracturas cerradas, abiertas, desplazadas y no desplazadas, para apoyar el diagnóstico médico y mejorar la precisión en la toma de decisiones clínicas 

## Alcance
(En proceso de cambios)

## Restricciones
- Privacidad
- Disponibilidad de datos médicos
- Regulación (e.g., HIPAA o GDPR)

# Recopilación de Datos

## Fuentes de Datos
- Bases de datos públicas como:
  - MURA
  - NIH Chest X-rays
  - Kaggle
- Colaboraciones con hospitales o centros médicos.
- Generación propia mediante convenios.

## Etiquetado de Datos
- Por radiólogos o expertos médicos para garantizar la precisión.
- Herramientas de etiquetado para imágenes médicas (e.g., LabelImg, RadiAnt DICOM Viewer).

# Preparación de los Datos

## Preprocesamiento de Imágenes
- Conversión a escala de grises (si las imágenes no lo están).
- Normalización de valores de píxeles.
- Redimensionamiento a un tamaño uniforme (e.g., 224x224 píxeles).

## Aumento de datos
- Rotación, escalado, inversión horizontal, zoom aleatorio.
- Simula variedad y aumenta robustez.

## División del Dataset
- Entrenamiento (70%)
- Validación (20%)
- Prueba (10%)

# Selección de la Arquitectura del Modelo

- **Redes Neuronales Convolucionales (CNN):** Ideales para el análisis de imágenes médicas.
- **Modelos Preentrenados (Transfer Learning):**
  - ResNet
- **Customización:** Ajustar capas finales para adaptarlas al problema específico de clasificación.

# Evaluación y Validación

## Métricas de Desempeño
- Accuracy
- Precision
- Recall
- F1-score

## Prueba en Datos Reales
- Evaluar en un entorno clínico o con nuevos conjuntos de datos.

# Despliegue

## Integración
- Usar frameworks como TensorFlow Serving o FastAPI.

## Interfaz para Usuarios
- Interfaz gráfica simple para que médicos carguen radiografías y obtengan resultados.

## Mantenimiento
- Actualización del modelo con nuevos datos.
- Monitoreo de desempeño para identificar sesgos o errores.

# Tecnologías Utilizadas

## Bibliotecas y Frameworks
- TensorFlow
- PyTorch
- Keras

## Plataformas de Etiquetado
- LabelImg
- CVAT

## Visualización
- Matplotlib
- Seaborn

# Conclusión

# Recursos

# Cumplimiento Ético y Regulatorio

- Garantizar que los datos están anonimizados.
- Adherirse a normativas locales e internacionales.
- Implementar explicabilidad en el modelo (e.g., por qué clasifica como fractura).

# Autores

La dedicación y el espíritu colaborativo del equipo fundamentales para hacer realidad este proyecto.

| [<img src="https://avatars.githubusercontent.com/u/166779106?v=4" width=115><br><sub>Facundo Corvalan</sub>](https://github.com/facu-corvalan) | [<img src="https://avatars.githubusercontent.com/u/123128073?v=4" width=115><br><sub>Javier Yañez</sub>](https://github.com/javyleonhart) | [<img src="https://avatars.githubusercontent.com/u/163685041?v=4" width=115><br><sub>Michael Martinez</sub>](https://github.com/bkmay1417) | [<img src="https://avatars.githubusercontent.com/u/123877201?v=4" width=115><br><sub>Jesus H. Parra B.</sub>](https://github.com/ing-jhparra)
| :---: | :---: | :---: | :---: |