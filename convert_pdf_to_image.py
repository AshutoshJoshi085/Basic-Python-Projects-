
from pdf2image import convert_from_path

def pdf_to_image(pdf_file, output_folder):
    images = convert_from_path(pdf_file)
    for i, image in enumerate(images):
        image.save(f'{output_folder}/page_{{i+1}}.jpg', 'JPEG')

# Example
pdf_to_image('sample.pdf', 'output_images')
