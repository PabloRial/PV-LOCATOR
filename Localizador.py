import os
from ultralytics import YOLO
import cv2

# Cargar el modelo entrenado
results_dir = #Dirección en la que se guarda el .txt con los resultados
resumen_dir = #Direccion en la que se guardan las imagenes procesadas
model_dir = #Dirección del modelo
model = YOLO(model_dir)

# Ruta a las nuevas imágenes
img_path = #Dirección de las imagenes a procesar

# Crear la carpeta para guardar las imágenes procesadas
processed_images_dir = os.path.join(results_dir, 'imagenes procesadas')
os.makedirs(processed_images_dir, exist_ok=True)

# Realizar inferencias
results = model(img_path)

# Archivo para guardar los resultados
results_file = os.path.join(resumen_dir, 'detections.txt')

# Inicializar contador total de placas solares
total_solar_panels = 0

# Guardar resultados
with open(results_file, mode='w') as file:
    file.write('Image\tSolar Panels\n')

    for result in results:
        # Obtener la imagen procesada con las anotaciones
        annotated_img = result.plot()

        # Guardar la imagen procesada
        save_path = os.path.join(processed_images_dir, os.path.basename(result.path))
        cv2.imwrite(save_path, annotated_img)

        # Contar las detecciones de placas solares en la imagen
        num_solar_panels = sum([1 for cls in result.boxes.cls if int(cls) == 0])  # Asegúrate de que la clase 0 corresponde a 'solar_panel'
        total_solar_panels += num_solar_panels

        # Escribir resultados de la imagen en el archivo
        file.write(f'{os.path.basename(result.path)}\t{num_solar_panels}\n')

    # Escribir el total de placas solares detectadas
    file.write('\n')
    file.write(f'Total\t{total_solar_panels}\n')

print("Detections saved in", processed_images_dir)
print("Results saved in", results_file)
