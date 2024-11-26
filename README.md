#  Clasificación de fracturas óseas a partir de radiografías

<p align="center">
   <br />
   <img src="img\hueso-roto.png" width="55%">
   <br />
</p>

# Contenido

* [Introducción](#Introducción)
* [Recursos](#Recursos)
* [Autores](#Autores)

# 1. Definición del Problema

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

# 2. Recopilación de Datos

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

# 3. Preparación de los Datos

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

# 4. Selección de la Arquitectura del Modelo

- **Redes Neuronales Convolucionales (CNN):** Ideales para el análisis de imágenes médicas.
- **Modelos Preentrenados (Transfer Learning):**
  - ResNet
  - EfficientNet
  - InceptionV3
  - DenseNet
- **Customización:** Ajustar capas finales para adaptarlas al problema específico de clasificación.

# 5. Entrenamiento del Modelo

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


# 6. Evaluación y Validación

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

# 7. Despliegue

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

# 8. Cumplimiento Ético y Regulatorio

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

## Autores

La dedicación y el espíritu colaborativo del equipo fundamentales para hacer realidad este proyecto.

| [<img src="https://avatars.githubusercontent.com/u/166779106?v=4" width=115><br><sub>Adrian Facundo Corvalan</sub>](https://github.com/facu-corvalan) | [<img src="https://avatars.githubusercontent.com/u/123128073?v=4" width=115><br><sub>Javier Yañez</sub>](https://github.com/javyleonhart) | [<img src="https://avatars.githubusercontent.com/u/163685041?v=4" width=115><br><sub>Michael Martinez</sub>](https://github.com/bkmay1417) | [<img src="https://avatars.githubusercontent.com/u/123877201?v=4" width=115><br><sub>Jesus H. Parra B.</sub>](https://github.com/ing-jhparra)
| :---: | :---: | :---: | :---: |