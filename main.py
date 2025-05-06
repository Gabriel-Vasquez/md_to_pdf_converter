
from markdown2 import markdown
from weasyprint import HTML, CSS
import os

input_dir = "input"
output_file = "output.pdf"
css_file = "style.css"

md_files = [f for f in os.listdir(input_dir) if f.endswith(".md")]
if not md_files:
    print("No hay archivos .md en la carpeta 'input'.")
    exit()

with open(os.path.join(input_dir, md_files[0]), "r", encoding="utf-8") as f:
    md_content = f.read()

html = markdown(md_content)
HTML(string=html).write_pdf(output_file, stylesheets=[CSS(css_file)])
print(f"PDF generado '{output_file}'")
