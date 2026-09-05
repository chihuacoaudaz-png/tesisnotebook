# -*- coding: utf-8 -*-
"""
MOTOR DE FORMATEO Y ESTRUCTURACIÓN ACADÉMICA UNI
Transforma cualquier texto/Markdown/documento de investigación al formato normado UNI FIGMM
sin alterar una sola línea de lógica, datos o conclusiones.
"""

import os
import re

class UniFormatterEngine:
    def __init__(self, template_dir="templates"):
        self.template_dir = template_dir
        
    def escape_latex(self, text):
        """
        Escapa caracteres especiales de LaTeX respetando entornos matemáticos existentes.
        """
        # Proteger ecuaciones matemáticas $...$ y $$...$$
        math_blocks = []
        def save_math(match):
            math_blocks.append(match.group(0))
            return f"__MATH_BLOCK_{len(math_blocks)-1}__"
            
        text = re.sub(r'\$\$.*?\$\$|\$.*?\$|\\begin\{equation\}.*?\\end\{equation\}', save_math, text, flags=re.DOTALL)
        
        # Escapar caracteres de texto
        text = text.replace("&", r"\&")
        text = text.replace("%", r"\%")
        text = text.replace("#", r"\#")
        text = text.replace("_", r"\_")
        
        # Restaurar ecuaciones
        for i, block in enumerate(math_blocks):
            text = text.replace(f"__MATH_BLOCK_{i}__", block)
            
        return text

    def build_latex_document(self, metadata, sections_content, output_path="output/documento_formateado.tex"):
        """
        Ensambla el documento LaTeX completo a partir de los metadatos y el contenido de las secciones.
        """
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        header = rf'''\documentclass[11pt,a4paper]{{article}}
\input{{{os.path.join(self.template_dir, "preamble.tex")}}}

\newcommand{{\TipoDocumento}}{{{metadata.get('tipo_documento', 'PLAN DE TESIS')}}}
\newcommand{{\TituloTesis}}{{{metadata.get('titulo', 'TITULO DE LA INVESTIGACION')}}}
\newcommand{{\LineaInvestigacion}}{{{metadata.get('linea_investigacion', 'Ingenieria de Minas')}}}
\newcommand{{\NombreAutor}}{{{metadata.get('autor', 'Bachiller en Ciencias')}}}
\newcommand{{\NombreAsesor}}{{{metadata.get('asesor', 'Docente Ordinario UNI FIGMM')}}}
\newcommand{{\AnioDocumento}}{{{metadata.get('anio', '2026')}}}

\begin{document}

\pagenumbering{{roman}}
\input{{{os.path.join(self.template_dir, "portada_uni.tex")}}}

\tableofcontents
\newpage

\pagenumbering{{arabic}}
\setcounter{{page}}{{1}}

'''
        footer = r'''
\end{document}
'''
        body = ""
        for sec_title, sec_text in sections_content:
            body += f"\n\\section{{{sec_title}}}\n"
            body += f"{sec_text}\n"
            
        full_tex = header + body + footer
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(full_tex)
            
        print(f"[EXITO] Archivo TeX estructurado generado en: {output_path}")
        return output_path

if __name__ == "__main__":
    engine = UniFormatterEngine(template_dir="../templates")
    meta = {
        "tipo_documento": "PLAN DE TESIS",
        "titulo": "SISTEMA AGENTICO BASADO EN IA PARA DISENO DE P&V - LINCUNA 2026",
        "linea_investigacion": "Geomecanica y Transformacion Digital Minera",
        "autor": "Bachiller UNI FIGMM",
        "asesor": "Docente Ordinario UNI",
        "anio": "2026"
    }
    sec = [
        ("PLANTEAMIENTO DEL PROBLEMA", "Descripcion de la realidad problematica sin alterar datos."),
        ("MARCO TEORICO", "Formulacion matematica de presiones de detonacion.")
    ]
    engine.build_latex_document(meta, sec, "output/test_output.tex")
