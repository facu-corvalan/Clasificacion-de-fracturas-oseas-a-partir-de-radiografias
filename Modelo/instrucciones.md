# Entrenamiento del modelo

Para el armado del siguiente modelo se utilizó un modelo de detección de objetos preentrenado llamado Faster R-CNN inception ResNet V2 de https://github.com/tensorflow/models/tree/master.
Antes de entrenarlo para nuestro fines, primero hace falta preparar los datos con los que va a entrenar nuestro modelo. Para ello, creamos una carpeta con todas la imagenes con las que vamos a entrenar el modelo.

## Etiquetado de imagenes

1. Como primer paso, instalaremos el programa LabelImg. Para ello se adjunta el link del repositorio original con las instrucciones necesarias -> https://github.com/HumanSignal/labelImg

2. Una vez listo LabelImg, se abre y se elige el directorio de las imagenes, donde etiquetamos manualmente una por una, identificando aquello que queremos que detecte, en este caso fracturas

![](img\img1.png)

**Aclaracion** El formato utilizado en esta tarea fue Pascal/VOC

3. Una vez etiquetadas todas las fotos para el entrenamiento, es necesario pasar todo aquello en el formato TFRecord, que es el formato con el cual entrena este modelo.
Como breve explicación, extraeremos la información de las etiquetas en los archivos .xml generados con LabelImg, luego la de las imagenes para crear el ejemplo en TFRecord y por ultimo escribirlo en un archivo. A continuación de adjunta el código.
```ruby

import os
import tensorflow as tf
from lxml import etree
import cv2
import numpy as np

# Función para leer el archivo XML y obtener las anotaciones
def parse_xml(xml_file):
    tree = etree.parse(xml_file)
    root = tree.getroot()

    # Obtener la información de la imagen
    filename = root.find('filename').text
    size = root.find('size')
    width = int(size.find('width').text)
    height = int(size.find('height').text)

    # Leer las etiquetas de los objetos
    objects = []
    for obj in root.iter('object'):
        label = obj.find('name').text
        bndbox = obj.find('bndbox')
        xmin = int(bndbox.find('xmin').text)
        ymin = int(bndbox.find('ymin').text)
        xmax = int(bndbox.find('xmax').text)
        ymax = int(bndbox.find('ymax').text)
        objects.append({'label': label, 'bbox': [xmin, ymin, xmax, ymax]})

    return filename, width, height, objects

# Función para crear el ejemplo de TFRecord
def create_tf_example(image_path, filename, width, height, objects):
    # Leer la imagen
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    encoded_image = tf.io.encode_jpeg(image).numpy()

    # Crear las características de las etiquetas
    xmins = []
    ymins = []
    xmaxs = []
    ymaxs = []
    classes = []
    classes_text = []

    for obj in objects:
        label = obj['label']
        bbox = obj['bbox']

        xmins.append(bbox[0] / width)
        ymins.append(bbox[1] / height)
        xmaxs.append(bbox[2] / width)
        ymaxs.append(bbox[3] / height)
        classes.append(1)  # En este proyecto sólo hay una clase. Aquí podrías mapear etiquetas a números.
        classes_text.append(label.encode('utf8'))

    # Crear el ejemplo de TFRecord
    tf_example = tf.train.Example(features=tf.train.Features(feature={
        'image/encoded': tf.train.Feature(bytes_list=tf.train.BytesList(value=[encoded_image])),
        'image/filename': tf.train.Feature(bytes_list=tf.train.BytesList(value=[filename.encode('utf8')])),
        'image/height': tf.train.Feature(int64_list=tf.train.Int64List(value=[height])),
        'image/width': tf.train.Feature(int64_list=tf.train.Int64List(value=[width])),
        'image/object/bbox/xmin': tf.train.Feature(float_list=tf.train.FloatList(value=xmins)),
        'image/object/bbox/ymin': tf.train.Feature(float_list=tf.train.FloatList(value=ymins)),
        'image/object/bbox/xmax': tf.train.Feature(float_list=tf.train.FloatList(value=xmaxs)),
        'image/object/bbox/ymax': tf.train.Feature(float_list=tf.train.FloatList(value=ymaxs)),
        'image/object/class/label': tf.train.Feature(int64_list=tf.train.Int64List(value=classes)),
        'image/object/class/text': tf.train.Feature(bytes_list=tf.train.BytesList(value=classes_text)),
    }))

    return tf_example

# Función para convertir el conjunto de datos
def convert_to_tfrecord(image_dir, annotations_dir, output_path):
    writer = tf.io.TFRecordWriter(output_path)

    for xml_file in os.listdir(annotations_dir):
        if xml_file.endswith('.xml'):
            # Generar la ruta de la imagen
            xml_path = os.path.join(annotations_dir, xml_file)
            filename, width, height, objects = parse_xml(xml_path)
            image_path = os.path.join(image_dir, filename)

            # Crear el ejemplo de TFRecord
            tf_example = create_tf_example(image_path, filename, width, height, objects)

            # Escribir el ejemplo en el archivo TFRecord
            writer.write(tf_example.SerializeToString())

    writer.close()

# Ruta de las imágenes y anotaciones
image_dir = 'ruta de las imágenes etiquetadas'
annotations_dir = 'ruta de los archivos .xml'
output_path = 'ruta donde se guardará el archivo nuevo'

# Convertir a TFRecord
convert_to_tfrecord(image_dir, annotations_dir, output_path)
```


Una vez realizado esto, obtendremos el archivo, al cual hay que darle la terminación .tfrecord

4. Como último paso, crearemos un archivo .txt (comunmente llamado label_map) con todas la etiquetas que se encontraban en las imágenes convertidas a TFRecord en formato de diccionario. A continuación se proporciona como ejemplo el archivo creado para la única clase de nuestro conjunto de datos.

```
item {
  id: 1
  name: 'Fractura'
  display_name: 'Fractura'
}
```

## Cargar el modelo y entrenamiento

1. Para cargar y utilizar el modelo elegido en TensorFlow, es importante elegir versiones compatibles de Python, TensorFlow y Protobuf para evitar problemas de compatibilidad. Se recomienda utilizar:

        Python 3.8.20
        Tensorflow 2.9.1
        Protobuff 3.19.6

Tambien será necesario tener instalados los driver de la GPU compatibles con la version de Tensorflow. En el presente proyecto se utilizó una Nvidia RTX3060 y se utilizaron los driver **CUDA 11.2** y **cuDNN 8.1**

**Nota** En el caso de ser usuario de windows, se recomienda instalar anaconda o miniconda para crear un entorno virtual en el cual instalar todas las dependencias descritas.

Tambien, se recomienda instalar todas las dependencias del archivo requirements_model.txt proporcionado en el repositorio.

2. En el directorio en el que estamos trabajando clonamos el repositorio que se mencionó al inicio

        git clone https://github.com/tensorflow/models.git

Luego, descargamos el modelo preentrenado que queremos utilizar en https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md y lo descomprimimos dentro de la carpeta models

3. Configurar el pipeline.config

El modelo descargado trae el archivo mencionado que es el que proporciona la información de como se va a entrenar el modelo. Aqui tendremos que:

- Actualizar las rutas de datos

        localiza esta porción de codigo y modifica

        train_input_reader {
        label_map_path: "ruta del label map del dataset creado "
        tf_record_input_reader {
            input_path: "ruta del archivo .tfrecord creado"
            }
        }

- Actualizar las rutas del modelo preentrenado:

        localiza esta porción de codigo

        fine_tune_checkpoint: "ruta del archivo ckpt-0 del modelo descargado"

- Checkea que la siguiente opcion figure así. De lo contrario, modificala:

        fine_tune_checkpoint_type: "detection"

- Definir el número de clases: Busca num_classes y actualízalo con el número de clases en tu conjunto de datos:

        num_classes: 1  # Cambia este valor según el caso

- Configurar otros parámetros de entrenamiento (opcional):

    batch_size: Reduce este valor si tienes limitaciones de memoria GPU:
        
        batch_size: 2

    num_steps: Define cuántos pasos entrenará el modelo:

        num_steps: 20000


4. Una vez configurado esto, procedemos a entrenar el modelo. Para ello, debemos ejecutar el archivo model_main_tf2.py que está dentro de la carpeta research/object-detection del repositorio clonado. A continuación, ofrecemos el codigo utilizado por consola para ejecutar este archivo:

        python ruta_del_archivo/model_main_tf2.py --pipeline_config_path="ruta_del_archivo/pipeline.config" --model_dir="ruta_de_salida_del_modelo_entrenado" --alsologtostderr


5. Cuando el modelo termine de entrenarse, tendremos que exportarlo para luego poder utilizarlo. Para esto utilizaremos el archivo exporter_main_v2.py ubicado en la misma carpeta que model_main_tf2.py. Lo ejecutamos con el siguiente comando por consola:

        python ruta_del_archivo/exporter_main_v2.py --input_type image_tensor --pipeline_config_path ruta_del_archivo/pipeline.config --trained_checkpoint_dir ruta_del_directorio_donde_se_guardo_el_modelo_recien_entrenado --output_directory ruta_de_salida_al_exportar_el_modelo

## Prueba del modelo

Al completar lo pasos anteriores, el modelo ya está listo para utilizarse. Cabe tener en cuenta que la imagen que queremos que sea evaluada, debe ser procesadar y transformada en tensor antes de pasarsela al modelo. A continuación se proporciona un código para poder llevar a cabo está tarea:

```ruby
import tensorflow as tf
import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt

# Ruta del modelo exportado
SAVED_MODEL_DIR = "ruta_del_modelo_exportado/saved_model"

# Cargar el modelo
print("Cargando modelo...")
detect_fn = tf.saved_model.load(SAVED_MODEL_DIR)
print("Modelo cargado exitosamente.")

# Ruta de la imagen de prueba
IMAGE_PATH = "ruta_a/imagen.jpg"

# Función para cargar y preprocesar la imagen
def load_image_into_numpy_array(path):
    return np.array(Image.open(path))

# Cargar la imagen
image_np = load_image_into_numpy_array(IMAGE_PATH)

# Convertir la imagen a un tensor
input_tensor = tf.convert_to_tensor(image_np)
input_tensor = input_tensor[tf.newaxis, ...]

# Realizar la detección
print("Realizando detección...")
detections = detect_fn(input_tensor)

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
for i in range(num_detections):
    if detection_scores[i] > 0.5:  # Umbral de confianza
        box = detection_boxes[i]
        y_min, x_min, y_max, x_max = box
        h, w, _ = image_np.shape
        start_point = (int(x_min * w), int(y_min * h))
        end_point = (int(x_max * w), int(y_max * h))
        color = (0, 255, 0)
        thickness = 2
        cv2.rectangle(image_np_with_detections, start_point, end_point, color, thickness)

# Mostrar la imagen con las detecciones
plt.figure(figsize=(12, 8))
plt.imshow(image_np_with_detections)
plt.axis("off")
plt.show()
```
