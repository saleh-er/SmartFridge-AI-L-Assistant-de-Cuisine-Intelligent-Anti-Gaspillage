from ultralytics import YOLO
import cv2
import numpy as np

# On charge un modèle pré-entraîné (il se téléchargera tout seul au premier lancement)
model = YOLO('yolov8n.pt') 

def detect_ingredients(image_bytes):
    # Convertir les bytes de l'image en format OpenCV
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Prédire les objets
    results = model(img)
    
    # Extraire les noms des objets détectés (ex: apple, broccoli, etc.)
    ingredients = []
    for r in results:
        for c in r.boxes.cls:
            ingredients.append(model.names[int(c)])
            
    return list(set(ingredients)) # Retourne une liste unique