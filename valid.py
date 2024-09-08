import os
import torch
from ultralytics import YOLO

# Configuración de las rutas
dataset_yaml = #Dirección del archivo dataset.yaml
weights_path = #Dirección del modelo entrenado

# Crear el directorio de resultados si no existe
results_dir = #Dirección en la que se guardan los resultados
os.makedirs(results_dir, exist_ok=True)

# Inicializar el modelo
model = YOLO(weights_path)

# Evaluar el modelo
metrics = model.val(data=dataset_yaml)
print(metrics)
