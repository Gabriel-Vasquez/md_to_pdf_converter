# 📄 Markdown to PDF Converter

This Python project allows you to convert a Markdown (`.md`) file into a beautifully styled PDF using WeasyPrint.

## 📁 Folder Structure

```
md_to_pdf_converter/
├── main.py            # Main script to generate the PDF
├── requirements.txt   # Python dependencies
├── style.css          # Custom CSS for styling the output PDF
└── input/
    └── example.md     # Your Markdown input file
```

## 🚀 How to Use

1. Place your `.md` file in the `input` folder.
2. Open a terminal (CMD or similar) and navigate to the project directory.
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. (Windows only) If WeasyPrint fails, install GTK from:
   [https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases)
   and add the `bin` folder to your PATH.

5. Run the script:
   ```
   python main.py
   ```

6. You'll get `output.pdf` in the root folder.

## 📝 Notes

- Make sure your Markdown file uses valid syntax.
- Style can be adjusted in `style.css`.

Enjoy!
