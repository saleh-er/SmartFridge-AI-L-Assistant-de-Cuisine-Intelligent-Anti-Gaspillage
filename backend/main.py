from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from model_ia import detect_ingredients

app = FastAPI()

# Permet à ton navigateur d'accéder à l'API sans blocage de sécurité
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    # Lecture de l'image envoyée
    image_bytes = await file.read()
    # Analyse par l'IA
    found = detect_ingredients(image_bytes)
    return {"ingredients": found}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)