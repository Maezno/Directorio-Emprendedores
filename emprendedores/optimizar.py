from PIL import Image
import os

# Carpeta raíz (desde donde se ejecuta el script)
root_folder = os.getcwd()

# Calidad de compresión JPG (0-100)
quality = 70  # Ajusta según necesites más o menos peso

# Recorrer hasta 2 niveles de subcarpetas
for dirpath, dirnames, filenames in os.walk(root_folder):
    # Calculamos la profundidad relativa
    depth = dirpath[len(root_folder):].count(os.sep)
    if depth > 2:
        continue  # saltar carpetas más profundas
    for filename in filenames:
        if filename.lower().endswith((".jpg", ".jpeg")):
            file_path = os.path.join(dirpath, filename)
            try:
                # Abrir imagen y asegurar RGB
                img = Image.open(file_path).convert("RGB")
                # Sobrescribir la misma imagen optimizada
                img.save(file_path, "JPEG", quality=quality, optimize=True)
                print(f"Optimizada: {file_path}")
            except Exception as e:
                print(f"Error con {file_path}: {e}")

print("¡Todas las imágenes JPG hasta 2 subcarpetas han sido optimizadas!")

