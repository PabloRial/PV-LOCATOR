import os
from ultralytics import YOLO

# Configuración de las rutas
dataset_yaml = #Dirección del archivo dataset.yaml
weights_path =  # Dirección del modelo de origen para realizar el nuevo entrenamiento (Puede empezarse de cero o elegir el último modelo entrenado)

# Crear el directorio de resultados si no existe
results_dir = #Dirección en la que guardar el nuevo modelo
os.makedirs(results_dir, exist_ok=True)

# Inicializar el modelo
model = YOLO(weights_path)

# Configuración de hiperparámetros y entrenamiento

model.train(
    data=dataset_yaml, 
    epochs=300,  # Número de épocas
    batch=32,  # Tamaño del batch 
    imgsz=640, 
    project=results_dir,
    optimizer='Adam',  # Especificar el optimizador
    lr0=0.001,  # Tasa de aprendizaje inicial
    lrf=0.0005,  # Tasa de aprendizaje final
    momentum=0.9,  # Momentum ajustado
    weight_decay=0.0006,  # Decaimiento de peso
    warmup_epochs=20.0,  # Epocas de calentamiento
    warmup_momentum=0.8,  # Momentum durante el calentamiento
    warmup_bias_lr=0.1,  # Tasa de aprendizaje del bias durante el calentamiento
    mosaic=1.0,  # Datos con mosaico
    augment=True,  # Activar augmentación de datos
)