import os
import cv2

# Establecer la ruta para la carpeta Images
ruta = "Images/"

# Crear una lista vacía para almacenar los nombres de los archivos de imagen
Images = []

# Utilizar os.listdir para iterar sobre los archivos en la carpeta
for file in os.listdir(ruta):
    # Obtener el nombre y la extensión del archivo
    base_name, file_extension = os.path.splitext(file)
    # Comprobar si la extensión del archivo corresponde a una imagen
    if file_extension.lower() in ['.jpg', '.jpeg', '.png', '.gif']:
        # Crear la ruta completa del archivo
        file_name = os.path+"/"+file
        # Imprimir el nombre del archivo
        print(file_name)
        # Agregar el archivo a la lista Images
        Images.append(file_name)

# Obtener la cantidad de imágenes en la lista
count = len(Images)

# Leer la primera imagen de la lista para obtener su tamaño
frame = cv2.imread(Images[0])
# Obtener las dimensiones de la imagen (ancho, altura y canales)
height, width, channels = frame.shape
# Crear una tupla size con las dimensiones de la imagen
size = (width, height)
# Imprimir el tamaño
print(size)

# Crear el archivo de video
out = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

# Agregar las imágenes al archivo de video
for i in range(0, count):
    # Leer la imagen
    img = cv2.imread(Images[i])
    # Añadir la imagen al video
    out.write(img)

# Cerrar el archivo de video
out.release()

# Imprimir un mensaje cuando el video se haya terminado
print("Fin")
