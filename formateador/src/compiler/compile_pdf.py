# -*- coding: utf-8 -*-
"""
COMPILADOR AUTOMATIZADO DE ALTA FIDELIDAD (FORMATEADOR UNI)
Soporta compilación vía LaTeX (pdflatex / xelatex / latexmk) y Word COM.
"""

import os
import sys
import subprocess
import shutil

def compile_latex(tex_path, output_dir="output", engine="pdflatex"):
    """
    Compila un archivo LaTeX (.tex) a PDF.
    Ejecuta múltiples pasadas para resolver referencias cruzadas, índices y bibliografía.
    """
    if not os.path.exists(tex_path):
        raise FileNotFoundError(f"No se encontró el archivo TeX en: {tex_path}")
    
    os.makedirs(output_dir, exist_ok=True)
    tex_dir = os.path.dirname(os.path.abspath(tex_path))
    tex_file = os.path.basename(tex_path)
    base_name = os.path.splitext(tex_file)[0]
    
    # Verificar disponibilidad del ejecutable LaTeX
    compiler_bin = shutil.which(engine)
    
    if compiler_bin:
        print(f"[*] Compilando {tex_file} con {engine} (2 pasadas)...")
        for pass_num in [1, 2]:
            cmd = [
                compiler_bin,
                "-interaction=nonstopmode",
                f"-output-directory={os.path.abspath(output_dir)}",
                tex_file
            ]
            result = subprocess.run(cmd, cwd=tex_dir, capture_output=True, text=True)
            if result.returncode != 0 and pass_num == 2:
                print(f"[AVISO] Advertencia durante compilación LaTeX:")
                print(result.stdout[-500:])
        
        pdf_out = os.path.join(output_dir, f"{base_name}.pdf")
        if os.path.exists(pdf_out):
            print(f"[EXITO] PDF compilado mediante {engine} en: {pdf_out}")
            return pdf_out
    else:
        print(f"[AVISO] Compilador '{engine}' no detectado en el PATH del sistema.")
        return None

def convert_docx_to_pdf_word(docx_path, pdf_path):
    """
    Compila/Convierte un documento DOCX a PDF usando Microsoft Word COM y reporta páginas físicas exactas.
    """
    import win32com.client
    print(f"[*] Compilando {docx_path} a PDF mediante Microsoft Word COM...")
    word = win32com.client.Dispatch('Word.Application')
    word.Visible = False
    try:
        doc = word.Documents.Open(os.path.abspath(docx_path))
        num_pages = doc.ComputeStatistics(2)  # wdStatisticPages
        os.makedirs(os.path.dirname(os.path.abspath(pdf_path)), exist_ok=True)
        doc.SaveAs(os.path.abspath(pdf_path), FileFormat=17)  # wdFormatPDF
        doc.Close()
        word.Quit()
        print(f"[EXITO] PDF compilado con Microsoft Word. Total de páginas físicas: {num_pages}")
        return pdf_path, num_pages
    except Exception as e:
        word.Quit()
        raise e

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
        if target.endswith(".tex"):
            compile_latex(target)
        elif target.endswith(".docx"):
            out_pdf = os.path.splitext(target)[0] + ".pdf"
            convert_docx_to_pdf_word(target, out_pdf)
    else:
        print("Uso: python compile_pdf.py <archivo.tex | archivo.docx>")
