# -*- coding: utf-8 -*-
"""
ENSAMBLADOR COMPLETO Y DEFINITIVO DEL PLAN DE TESIS OFICIAL UNI FIGMM (META: >= 48-52 PÁGINAS FÍSICAS VERIFICADAS)
"""

import os
import sys
import docx
from docx.shared import Inches, Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
import win32com.client

def set_cell_background(cell, fill_hex):
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def generate_and_verify_master_plan():
    print("[*] Iniciando ensamblado exhaustivo del Plan de Tesis Oficial UNI FIGMM (Meta: >= 48 a 52 páginas)...")
    
    docx_path = "output/PLAN_DE_TESIS_OFICIAL_UNI_LINCUNA.docx"
    pdf_path = "output/PLAN_DE_TESIS_OFICIAL_UNI_LINCUNA.pdf"
    md_path = "output/01_PLAN_DE_TESIS_OFICIAL_UNI_LINCUNA.md"
    tex_path = "latex/PLAN_DE_TESIS_OFICIAL_UNI_LINCUNA.tex"
    
    os.makedirs("output", exist_ok=True)
    os.makedirs("latex", exist_ok=True)
    
    doc = docx.Document()
    
    # Configuración de página A4 y márgenes UNI FIGMM (Izquierdo: 3.0 cm, Superior: 2.54 cm, Derecho: 2.5 cm, Inferior: 2.5 cm)
    section = doc.sections[0]
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    section.left_margin = Cm(3.0)
    section.right_margin = Cm(2.5)
    section.top_margin = Cm(2.54)
    section.bottom_margin = Cm(2.5)
    
    # Estilo Normal Arial 11pt, interlineado 1.15, espaciado posterior 6pt
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Arial'
    normal_style.font.size = Pt(11)
    normal_style.font.color.rgb = RGBColor(0, 0, 0)
    normal_style.paragraph_format.line_spacing = 1.15
    normal_style.paragraph_format.space_after = Pt(6)
    normal_style.paragraph_format.space_before = Pt(0)
    normal_style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    def add_title(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(12)
        run = p.add_run(text)
        run.bold = True
        run.font.size = Pt(13.5)
        return p

    def add_h1(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.bold = True
        run.font.size = Pt(12)
        return p

    def add_h2(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(11)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.bold = True
        run.font.size = Pt(11)
        return p

    def add_h3(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(9)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.bold = True
        run.italic = True
        run.font.size = Pt(11)
        return p

    def add_body(text, bold_prefix=None, italic=False):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_pre = p.add_run(bold_prefix)
            r_pre.bold = True
        run = p.add_run(text)
        run.italic = italic
        return p

    def add_bullet(text, bold_prefix=None):
        p = doc.add_paragraph(style='List Bullet')
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_pre = p.add_run(bold_prefix)
            r_pre.bold = True
        p.add_run(text)
        return p

    def add_formula(eq_text, where_items=None):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.left_indent = Inches(0.4)
        p.paragraph_format.right_indent = Inches(0.4)
        run = p.add_run(eq_text)
        run.bold = True
        run.font.name = 'Consolas'
        run.font.size = Pt(10.0)
        run.font.color.rgb = RGBColor(15, 30, 60)
        
        if where_items:
            pw = doc.add_paragraph()
            pw.alignment = WD_ALIGN_PARAGRAPH.LEFT
            pw.paragraph_format.space_after = Pt(2)
            r_w = pw.add_run("donde:")
            r_w.italic = True
            r_w.font.size = Pt(10.0)
            for item in where_items:
                add_bullet(item)

    def add_table_caption(tab_num, tab_title):
        p1 = doc.add_paragraph()
        p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p1.paragraph_format.space_before = Pt(8)
        p1.paragraph_format.space_after = Pt(2)
        p1.paragraph_format.keep_with_next = True
        r1 = p1.add_run(f"Tabla {tab_num}")
        r1.bold = True
        
        p2 = doc.add_paragraph()
        p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p2.paragraph_format.space_after = Pt(6)
        p2.paragraph_format.keep_with_next = True
        r2 = p2.add_run(tab_title)
        r2.italic = True

    # -------------------------------------------------------------------------
    # PORTADA
    # -------------------------------------------------------------------------
    add_title("UNIVERSIDAD NACIONAL DE INGENIERÍA\nFACULTAD DE INGENIERÍA GEOLÓGICA, MINERA Y METALÚRGICA\nESCUELA PROFESIONAL DE INGENIERÍA DE MINAS")
    add_title("PLAN DE TESIS\n\n“SISTEMA AGÉNTICO BASADO EN INTELIGENCIA ARTIFICIAL PARA EL DISEÑO ASISTIDO DE PERFORACIÓN Y VOLADURA ORIENTADO AL CONTROL DE LA SOBREROTURA EN LABORES SUBTERRÁNEAS DE LA U.E.A. LINCUNA, 2026”")
    add_body("Geomecánica Aplicada, Perforación, Voladura y Transformación Digital Minera", bold_prefix="LÍNEA DE INVESTIGACIÓN: ")
    add_body("Bachiller en Ciencias con Mención en Ingeniería de Minas", bold_prefix="AUTOR: ")
    add_body("Docente Ordinario de la Escuela Profesional de Ingeniería de Minas - UNI FIGMM", bold_prefix="ASESOR: ")
    add_body("LIMA – PERÚ | 2026", bold_prefix="LUGAR Y FECHA: ")

    # -------------------------------------------------------------------------
    # 1. TITULO
    # -------------------------------------------------------------------------
    add_h1("1. TITULO")
    add_body("“SISTEMA AGÉNTICO BASADO EN INTELIGENCIA ARTIFICIAL PARA EL DISEÑO ASISTIDO DE PERFORACIÓN Y VOLADURA ORIENTADO AL CONTROL DE LA SOBREROTURA EN LABORES SUBTERRÁNEAS DE LA U.E.A. LINCUNA, 2026”")

    # Importar el generador maestro
    from generate_full_official_plan_50p import build_full_docx_document
    build_full_docx_document(docx_path)
    
    # Compilar a PDF con Word COM
    print(f"[*] Compilando PDF de alta fidelidad en: {pdf_path}...")
    word = win32com.client.Dispatch('Word.Application')
    word.Visible = False
    doc_com = word.Documents.Open(os.path.abspath(docx_path))
    num_pages = doc_com.ComputeStatistics(2)  # wdStatisticPages
    doc_com.SaveAs(os.path.abspath(pdf_path), FileFormat=17)  # wdFormatPDF
    doc_com.Close()
    word.Quit()
    print(f"[RESULTADO FINAL] PDF compilado con Microsoft Word. Total de páginas físicas calculadas: {num_pages}")
    
    return num_pages

if __name__ == "__main__":
    generate_and_verify_master_plan()
