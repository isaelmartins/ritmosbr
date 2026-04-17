from PIL import Image
import os

def resize_image(input_path, output_path, size):
    try:
        with Image.open(input_path) as img:
            # Mantendo a transparência se houver
            img = img.convert("RGBA")
            img_resized = img.resize(size, Image.Resampling.LANCZOS)
            img_resized.save(output_path, "PNG")
            print(f"Sucesso: {input_path} -> {output_path} ({size})")
    except Exception as e:
        print(f"Erro ao processar {input_path}: {e}")

# Icon
resize_image("app_icon_v2.png", "app_icon_512.png", (512, 512))

# Banner
resize_image("feature_graphic.png", "feature_graphic_1024x500.png", (1024, 500))
