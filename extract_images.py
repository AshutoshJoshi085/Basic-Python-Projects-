
from pdf2image import convert_from_path

def extract_images(pdf_file):
    images = convert_from_path(pdf_file)
    for i, image in enumerate(images):
        image.save(f'page_{{i+1}}.jpg', 'JPEG')

# Example
extract_images('sample.pdf')
