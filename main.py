from fastapi import FastAPI
from fastapi.responses import FileResponse
from PIL import Image
import numpy as np
import random
import os

app = FastAPI(title="Pixel Art Generator API")

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.get("/")
def root():
    return {
        "endpoints": {
            "/pixel": "Generate pixel art image"
        }
    }

@app.get("/pixel")
def generate_pixel(
    size: int = 32,
    scale: int = 16
):
    # random pixel data
    pixels = np.random.randint(0, 255, (size, size, 3), dtype=np.uint8)

    img = Image.fromarray(pixels, "RGB")
    img = img.resize((size * scale, size * scale), Image.NEAREST)

    filename = f"pixel_{random.randint(1000,9999)}.png"
    path = os.path.join(OUTPUT_DIR, filename)
    img.save(path)

    return FileResponse(path, media_type="image/png")
