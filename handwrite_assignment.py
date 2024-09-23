
from PIL import Image, ImageDraw, ImageFont

def handwritten_text(text, font_path, output_file):
    img = Image.new('RGB', (800, 300), color='white')
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, 50)
    d.text((50, 100), text, fill='black', font=font)
    img.save(output_file)

# Example
handwritten_text("This is a handwritten assignment.", "arial.ttf", "output.png")
