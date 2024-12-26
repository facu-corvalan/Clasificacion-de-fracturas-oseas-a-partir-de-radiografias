import os
import requests
import time
import zipfile
import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image
from functools import lru_cache
import cv2

# Ruta donde se descargará y descomprimirá el modelo
SAVED_MODEL_DIR = "modeloexportado\saved_model"
MODEL_ZIP = "modeloexportado.zip"

# Función para descargar y preparar el modelo desde Dropbox
def download_model():
    # URL de Dropbox modificada para la descarga directa
    url = "https://www.dropbox.com/scl/fi/4n3u85naocg8t4bot4z8y/modeloexportado.zip?rlkey=35ghoaaqbiq67y7ggyr5nc23l&st=l78bt9m7&dl=1"  # URL de Dropbox modificada
    output = MODEL_ZIP
    
    # Inicializamos la barra de progreso
    progress_bar = st.progress(0)  # Establece el progreso inicial a 0%
    status_text = st.empty()  # Texto para actualizar el estado

    # Tamaño esperado del archivo en KB (432430 KB, que son 422 MB)
    expected_size = 432431 * 1024  # Convertido a bytes
    max_allowed_deviation = 10 * 1024  # Permitimos una pequeña desviación de 10 KB

    # Usamos st.spinner para mostrar un indicador mientras se realiza la descarga
    with st.spinner("Cargando el modelo..."):
        try:
            # Realizamos la descarga con streaming
            response = requests.get(url, stream=True)
            if response.status_code != 200:
                st.error(f"Error al obtener el archivo. Código de estado: {response.status_code}")
                return
            
            total_downloaded = 0
            chunk_size = 1024 * 1024  # 1 MB

            # Escribimos el archivo mientras descargamos
            with open(output, 'wb') as file:
                for chunk in response.iter_content(chunk_size=chunk_size):
                    if chunk:
                        file.write(chunk)
                        total_downloaded += len(chunk)
                        
                        # Calculamos el porcentaje de descarga
                        percentage = (total_downloaded / expected_size) * 100
                        # Actualizamos el progreso basado en el porcentaje
                        progress_bar.progress(int(percentage))
                        status_text.text(f"Cargando: {percentage:.2f}% de 100%")
            
            # Esperamos 2 segundos después de que el archivo supere el tamaño esperado para dar tiempo a la descarga final
            time.sleep(2)

            # Verificamos si el tamaño es dentro de un rango aceptable (con una pequeña desviación)
            if abs(total_downloaded - expected_size) <= max_allowed_deviation:
                st.success("Modelo Cargado Exitosamente.")
                
                # Intentamos descomprimir el archivo ZIP
                try:
                    with zipfile.ZipFile(output, "r") as zip_ref:
                        zip_ref.extractall('')  # Extrae el contenido al directorio
                    st.success("Modelo descomprimido exitosamente.")
                except zipfile.BadZipFile:
                    st.error("El archivo descargado no es un archivo ZIP válido.")
            else:
                st.error(f"La descarga no se completó correctamente. El archivo descargado tiene un tamaño de {total_downloaded / (1024 * 1024):.2f} MB, que no cumple con el tamaño esperado.")
                # El archivo se descargó, pero su tamaño es incorrecto, por lo que se debe intentar nuevamente.
                os.remove(output)
                st.warning("Intentando nuevamente la descarga...")
                download_model()

        except Exception as e:
            st.error(f"Ocurrió un error durante la descarga: {e}")

# Función para cargar el modelo en memoria
@lru_cache(maxsize=1)
def load_model():
    print("Cargando modelo...")
    model = tf.saved_model.load(SAVED_MODEL_DIR)
    print("Modelo cargado exitosamente.")
    return model

# Función para cargar imágenes y convertirlas en arreglos de NumPy
def load_image_into_numpy_array(image):
    img = Image.open(image).convert('RGB')  # Asegurar que la imagen tiene 3 canales (RGB)
    return np.array(img, dtype=np.uint8)  # Convertir a uint8

# Interfaz de Streamlit
st.title("Detección de fracturas óseas")

# Descargar el modelo si no está presente
if not os.path.exists(SAVED_MODEL_DIR):
    download_model()

# Subir la imagen para la detección
uploaded_file = st.file_uploader("Sube una imagen", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Cargar la imagen desde Streamlit
    image_np = load_image_into_numpy_array(uploaded_file)

    # Verificar las dimensiones de la imagen cargada
    st.write(f"Dimensiones de la imagen: {image_np.shape}")

    # Convertir la imagen a un tensor
    input_tensor = tf.convert_to_tensor(image_np, dtype=tf.uint8)
    input_tensor = input_tensor[tf.newaxis, ...]  # Agregar una dimensión para el lote

    # Cargar el modelo
    detect_fn = load_model()

    # Realizar la detección
    st.write("Realizando detección...")
    detections = detect_fn(input_tensor)

    # Verificar si las detecciones están presentes antes de procesarlas
    if detections is not None and "num_detections" in detections:
        # Procesar las detecciones
        num_detections = int(detections.pop("num_detections"))
        detections = {key: value[0, :num_detections].numpy()
                      for key, value in detections.items()}
        detections["num_detections"] = num_detections

        # Filtrar resultados con alta confianza
        detection_classes = detections["detection_classes"].astype(np.int64)
        detection_boxes = detections["detection_boxes"]
        detection_scores = detections["detection_scores"]

        # Dibujar las cajas en la imagen
        image_np_with_detections = image_np.copy()

        # Iterar sobre las detecciones y dibujar las cajas con alta confianza
        for i in range(num_detections):
            if detection_scores[i] > 0.5:  # Umbral de confianza
                box = detection_boxes[i]
                y_min, x_min, y_max, x_max = box
                h, w, _ = image_np.shape
                start_point = (int(x_min * w), int(y_min * h))
                end_point = (int(x_max * w), int(y_max * h))

                # Dibujar rectángulo rojo para fractura
                color_box = (255, 0, 0)  # Rojo
                thickness = 2
                cv2.rectangle(image_np_with_detections, start_point, end_point, color_box, thickness)

                # Añadir texto "Fractura"
                text = "Fractura"
                font = cv2.FONT_HERSHEY_SIMPLEX
                font_scale = 0.6
                color_text = (255, 255, 255)  # Blanco
                thickness_text = 2
                text_size = cv2.getTextSize(text, font, font_scale, thickness_text)[0]
                text_x = start_point[0]
                text_y = start_point[1] - 10
                background_start = (text_x, text_y - text_size[1] - 4)
                background_end = (text_x + text_size[0] + 4, text_y + 4)
                cv2.rectangle(image_np_with_detections, background_start, background_end, color_box, -1)  # Fondo rojo
                cv2.putText(image_np_with_detections, text, (text_x, text_y), font, font_scale, color_text, thickness_text)

        # Mostrar la imagen con las detecciones
        st.image(image_np_with_detections, caption="Detecciones", use_column_width=True)
    else:
        st.error("No se encontraron detecciones válidas.")
