from PIL import Image

def resize_image(image_path, output_path, new_width, new_height):
    # Abrir la imagen
    image = Image.open(image_path)
    
    # Redimensionar la imagen
    resized_image = image.resize((new_width, new_height))
    
    # Guardar la imagen redimensionada
    resized_image.save(output_path)

# Ruta de la imagen original
image_path = "C:/Users/varel/Pictures/NC.png"

# Ruta de la imagen redimensionada
output_path = "C:/Users/varel/Pictures/NC1.png"

# Nuevas dimensiones
new_width = 600
new_height = 400

# Redimensionar la imagen
resize_image(image_path, output_path, new_width, new_height)
