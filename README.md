#  Clasificación de fracturas óseas a partir de radiografías

<p align="center">
   <br />
   <img src="img\hueso-roto.png" width="55%">
   <br />
</p>

# Contenido

* [Introducción](#Introducción)
* [Definición del Problema](#Definición-del-Problema)
* [Recopilación de Datos](#Recopilación-de-Datos)
* [Selección de la Arquitectura del Modelo](#Selección-de-la-Arquitectura-del-Modelo)
* [Entrenamiento del Modelo](#Entrenamiento-del-Modelo)
* [Evaluación y Validación](#Evaluación-y-Validación)
* [Despliegue](#Despliegue)
* [Cumplimiento Ético y Regulatorio](#Cumplimiento-Ético-y-Regulatorio)
* [Herramientas y Tecnologías Recomendadas](#Herramientas-y-Tecnologías-Recomendadas)
* [Conclusión](#Conclusión)
* [Recursos](#Recursos)
* [Autores](#Autores)

# Introducción  

La detección y clasificación precisa de fracturas óseas es un desafío crucial en el ámbito de la radiología, ya que un diagnóstico temprano y exacto puede marcar la diferencia en el tratamiento y recuperación de los pacientes. La integración de tecnologías avanzadas, como la inteligencia artificial (IA), representa una oportunidad significativa para mejorar la eficiencia y efectividad en los procesos de diagnóstico médico.  

Este proyecto tiene como objetivo principal desarrollar un modelo de IA capaz de clasificar fracturas óseas en tipos específicos, como cerradas, abiertas, desplazadas y no desplazadas, proporcionando un soporte valioso para los radiólogos en su toma de decisiones clínicas. A través del análisis automatizado de imágenes médicas, como radiografías, tomografías y resonancias magnéticas, el modelo permitirá identificar rápidamente anomalías, reducir los tiempos de evaluación y priorizar casos críticos para garantizar una atención más inmediata y precisa.  

El sistema se centrará en partes del cuerpo de alta incidencia clínica, como la muñeca, cadera, pierna y columna vertebral, abarcando una amplia variedad de clasificaciones de fracturas según tipologías estándar. Además, estará diseñado para integrarse de manera fluida en los flujos de trabajo radiológicos, ofreciendo informes preliminares, capacitación al personal médico y soporte técnico continuo, todo ello bajo estrictas normativas de protección de datos. Este avance tecnológico promete no solo optimizar el diagnóstico médico, sino también mejorar significativamente la experiencia y los resultados para los pacientes.  

# Definición del Problema

## Objetivo Principal
Desarrollar un modelo de inteligencia artificial capaz de clasificar fracturas óseas en tipos específicos, como fracturas cerradas, abiertas, desplazadas y no desplazadas, para apoyar el diagnóstico médico y mejorar la precisión en la toma de decisiones clínicas

## Uso del Modelo
Un modelo de inteligencia artificial podría ser utilizado para asistir a los radiólogos en el diagnóstico médico, analizando imágenes como radiografías, tomografías o resonancias magnéticas para identificar rápidamente anomalías o patrones asociados a enfermedades. Este modelo ayudaría a mejorar los tiempos de evaluación al preclasificar casos según su nivel de urgencia, permitiendo que los radiólogos prioricen casos críticos para una atención más inmediata, mientras mantienen el enfoque en los detalles clínicos relevantes para cada paciente.

## Alcance
El sistema de diagnóstico asistido se enfocará en el análisis automatizado de imágenes médicas relacionadas con fracturas óseas. Inicialmente, se priorizarán las evaluaciones de partes del cuerpo clave, como la muñeca, cadera, pierna y columna vertebral, debido a su alta incidencia en accidentes y su importancia clínica. El modelo estará diseñado para identificar y clasificar fracturas según tipologías estándar, incluyendo fracturas simples, compuestas, desplazadas, no desplazadas y fracturas en tallo verde, entre otras.

Además, el sistema proporcionará informes preliminares que detallarán el tipo y ubicación de las fracturas, permitiendo que los radiólogos validen los hallazgos y tomen decisiones informadas. Esta herramienta estará integrada en los flujos de trabajo radiológicos, con capacitación al personal médico, cumplimiento de normativas de protección de datos y soporte técnico continuo para garantizar su correcta operación.

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

## Tamaño del Dataset
Se recomienda un mínimo de 10,000 radiografías bien etiquetadas para una clasificación robusta.

# Preparación de los Datos

## Preprocesamiento de Imágenes
- Conversión a escala de grises (si las imágenes no lo están).
- Normalización de valores de píxeles.
- Redimensionamiento a un tamaño uniforme (e.g., 224x224 píxeles).

## Data Augmentation
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
  - EfficientNet
  - InceptionV3
  - DenseNet
- **Customización:** Ajustar capas finales para adaptarlas al problema específico de clasificación.

# Entrenamiento del Modelo

## Hiperparámetros
- Learning rate
- Batch size
- Optimizador (Adam, SGD)

## Pérdida (Loss Function)
- Cross-entropy (si es clasificación multicategoría).

## Aceleración
- Entrenamiento en GPU (e.g., NVIDIA).

## Validación
- Monitorear métricas como accuracy, F1-score, AUC-ROC.


# Evaluación y Validación

## Métricas de Desempeño
- Accuracy
- Precision
- Recall
- F1-score

## Confusion Matrix
- Ayuda a identificar categorías mal clasificadas.

## Visualización
- Grad-CAM para identificar las áreas donde el modelo presta atención.

## Prueba en Datos Reales
- Evaluar en un entorno clínico o con nuevos conjuntos de datos.

# Despliegue

## Integración
- Implementar como una API REST o herramienta standalone.
- Usar frameworks como TensorFlow Serving o FastAPI.

## Interfaz para Usuarios
- Interfaz gráfica simple para que médicos carguen radiografías y obtengan resultados.

## Infraestructura
- Hospedaje en la nube (GCP, AWS, Azure).

## Mantenimiento
- Actualización del modelo con nuevos datos.
- Monitoreo de desempeño para identificar sesgos o errores.

# Cumplimiento Ético y Regulatorio

- Garantizar que los datos están anonimizados.
- Adherirse a normativas locales e internacionales.
- Implementar explicabilidad en el modelo (e.g., por qué clasifica como fractura).


# Herramientas y Tecnologías Recomendadas

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

## Infraestructura en la Nube
- Google Cloud AI
- Amazon SageMaker

# Conclusión

# Autores

La dedicación y el espíritu colaborativo del equipo fundamentales para hacer realidad este proyecto.

| [<img src="https://avatars.githubusercontent.com/u/166779106?v=4" width=115><br><sub>Adrian Facundo Corvalan</sub>](https://github.com/facu-corvalan) | [<img src="https://avatars.githubusercontent.com/u/123128073?v=4" width=115><br><sub>Javier Yañez</sub>](https://github.com/javyleonhart) | [<img src="https://avatars.githubusercontent.com/u/163685041?v=4" width=115><br><sub>Michael Martinez</sub>](https://github.com/bkmay1417) | [<img src="https://avatars.githubusercontent.com/u/123877201?v=4" width=115><br><sub>Jesus H. Parra B.</sub>](https://github.com/ing-jhparra)
| :---: | :---: | :---: | :---: |