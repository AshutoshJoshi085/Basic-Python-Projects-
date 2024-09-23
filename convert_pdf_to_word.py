
import pdfplumber

def pdf_to_text(pdf_file, output_file):
    with pdfplumber.open(pdf_file) as pdf:
        with open(output_file, 'w') as out:
            for page in pdf.pages:
                text = page.extract_text()
                out.write(text)

# Example
pdf_to_text('sample.pdf', 'output.txt')
