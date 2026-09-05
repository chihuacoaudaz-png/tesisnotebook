# -*- coding: utf-8 -*-
"""
COMPILADOR MAESTRO DEL PLAN DE TESIS OFICIAL UNI FIGMM (50-54 PÁGINAS CONTINUAS)
Estructura rigurosa según PLAN DE TESIS (1).docx y lineamientos de pregrado UNI FIGMM.
"""

import os
import sys
import numpy as np
import pypdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedPlanCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedPlanCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_decorations(self, page_count):
        if self._pageNumber == 1:
            return  # Portada institucional limpia
        
        self.saveState()
        self.setFont("Helvetica", 7.5)
        self.setFillColor(colors.HexColor("#333333"))
        
        # Encabezado institucional UNI FIGMM
        self.drawString(3.5 * cm, 28.3 * cm, "UNIVERSIDAD NACIONAL DE INGENIERÍA — FACULTAD DE INGENIERÍA GEOLÓGICA, MINERA Y METALÚRGICA")
        self.setFont("Helvetica-Oblique", 7)
        self.drawRightString(18.5 * cm, 28.3 * cm, "ESCUELA DE INGENIERÍA DE MINAS")
        self.setStrokeColor(colors.HexColor("#718096"))
        self.setLineWidth(0.5)
        self.line(3.5 * cm, 28.1 * cm, 18.5 * cm, 28.1 * cm)
        
        # Pie de página reglamentario
        self.line(3.5 * cm, 2.0 * cm, 18.5 * cm, 2.0 * cm)
        self.setFont("Helvetica", 7.5)
        self.drawString(3.5 * cm, 1.5 * cm, "Plan de Tesis: Sistema Agéntico de P&V en U.E.A. Lincuna 2026")
        self.drawRightString(18.5 * cm, 1.5 * cm, f"Página {self._pageNumber} de {page_count}")
        
        self.restoreState()

def build_official_plan_pdf(pdf_filename="output/PLAN_DE_TESIS_OFICIAL_UNI_50PAGS.pdf"):
    os.makedirs(os.path.dirname(pdf_filename), exist_ok=True)
    
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=A4,
        leftMargin=3.5 * cm,
        rightMargin=2.5 * cm,
        topMargin=2.5 * cm,
        bottomMargin=2.5 * cm
    )
    
    c_primary = colors.HexColor("#0D233A")
    c_secondary = colors.HexColor("#1B4F72")
    c_dark = colors.HexColor("#2C3E50")
    c_muted = colors.HexColor("#566573")
    c_bg_light = colors.HexColor("#F8F9FA")
    c_border = colors.HexColor("#CBD5E0")
    
    style_cover_univ = ParagraphStyle('CoverUniv_P', fontName='Helvetica-Bold', fontSize=15, leading=19, alignment=1, textColor=c_primary)
    style_cover_fac = ParagraphStyle('CoverFac_P', fontName='Helvetica-Bold', fontSize=11, leading=14.5, alignment=1, textColor=c_secondary)
    style_cover_title = ParagraphStyle('CoverTitle_P', fontName='Helvetica-Bold', fontSize=11.5, leading=15.5, alignment=1, textColor=c_primary, spaceBefore=8, spaceAfter=10)
    style_cover_meta = ParagraphStyle('CoverMeta_P', fontName='Helvetica', fontSize=9, leading=13, alignment=1, textColor=c_dark)
    
    style_h1 = ParagraphStyle('Heading1_P', fontName='Helvetica-Bold', fontSize=11.5, leading=15, textColor=c_primary, spaceBefore=14, spaceAfter=6, keepWithNext=True)
    style_h2 = ParagraphStyle('Heading2_P', fontName='Helvetica-Bold', fontSize=10, leading=13, textColor=c_secondary, spaceBefore=10, spaceAfter=4.5, keepWithNext=True)
    style_h3 = ParagraphStyle('Heading3_P', fontName='Helvetica-Bold', fontSize=8.8, leading=12, textColor=c_dark, spaceBefore=8, spaceAfter=3.5, keepWithNext=True)
    style_body = ParagraphStyle('Body_P', fontName='Helvetica', fontSize=8.5, leading=12.2, alignment=4, textColor=c_dark, spaceAfter=5.5)
    style_bullet = ParagraphStyle('Bullet_P', fontName='Helvetica', fontSize=8.5, leading=12, alignment=4, leftIndent=12, textColor=c_dark, spaceAfter=3.5)
    style_eq = ParagraphStyle('Equation_P', fontName='Helvetica-Bold', fontSize=8.0, leading=11, alignment=1, textColor=c_primary, spaceBefore=4.5, spaceAfter=5.5)
    style_caption = ParagraphStyle('Caption_P', fontName='Helvetica-Oblique', fontSize=7.2, leading=9.5, alignment=1, textColor=c_muted, spaceBefore=3.0, spaceAfter=6.0)
    style_th = ParagraphStyle('TableHeader_P', fontName='Helvetica-Bold', fontSize=7.0, leading=9.0, alignment=1, textColor=colors.white)
    style_td = ParagraphStyle('TableCell_P', fontName='Helvetica', fontSize=6.8, leading=8.5, textColor=c_dark)
    style_code = ParagraphStyle('Code_P', fontName='Courier', fontSize=6.5, leading=8.2, textColor=c_primary)

    def p(text): return Paragraph(text, style_body)
    def pb(text): return Paragraph(f"• {text}", style_bullet)
    def peq(text): return Paragraph(text, style_eq)
    def ph1(text): return Paragraph(text, style_h1)
    def ph2(text): return Paragraph(text, style_h2)
    def ph3(text): return Paragraph(text, style_h3)
    def pcap(text): return Paragraph(text, style_caption)

    story = []

    # Portada Oficial de Plan de Tesis UNI FIGMM
    story.append(Spacer(1, 0.3 * cm))
    story.append(Paragraph("UNIVERSIDAD NACIONAL DE INGENIERÍA", style_cover_univ))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("FACULTAD DE INGENIERÍA GEOLÓGICA, MINERA Y METALÚRGICA", style_cover_fac))
    story.append(Paragraph("ESCUELA PROFESIONAL DE INGENIERÍA DE MINAS", style_cover_fac))
    story.append(Spacer(1, 0.6 * cm))
    
    fig1_path = "./output/figures/figura_01_malla_perforacion.png"
    if os.path.exists(fig1_path):
        story.append(Image(fig1_path, width=6.5 * cm, height=6.5 * cm))
    story.append(Spacer(1, 0.4 * cm))
    
    story.append(Paragraph("<b>PLAN DE TESIS</b>", ParagraphStyle('TW_P', fontName='Helvetica-Bold', fontSize=13.0, alignment=1, textColor=c_primary)))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("“SISTEMA AGÉNTICO BASADO EN INTELIGENCIA ARTIFICIAL PARA EL DISEÑO ASISTIDO DE PERFORACIÓN Y VOLADURA ORIENTADO AL CONTROL DE LA SOBREROTURA EN LABORES SUBTERRÁNEAS DE LA U.E.A. LINCUNA, 2026”", style_cover_title))
    story.append(Spacer(1, 0.5 * cm))
    story.append(Paragraph("PARA OPTAR EL TÍTULO PROFESIONAL DE:<br/><b>INGENIERO DE MINAS</b>", style_cover_meta))
    story.append(Spacer(1, 0.35 * cm))
    story.append(Paragraph("PRESENTADO POR:<br/><b>BACHILLER EN CIENCIAS CON MENCIÓN EN INGENIERÍA DE MINAS</b>", style_cover_meta))
    story.append(Spacer(1, 0.25 * cm))
    story.append(Paragraph("ASESOR:<br/><b>DR. ING. ASESOR DE TESIS (UNI FIGMM)</b>", style_cover_meta))
    story.append(Spacer(1, 0.5 * cm))
    story.append(Paragraph("<b>LIMA — PERÚ<br/>2026</b>", style_cover_meta))
    story.append(PageBreak())

    # Cargar partes estructuradas del Plan de Tesis
    from generate_plan_part1 import append_plan_part1
    append_plan_part1(story, p, pb, peq, ph1, ph2, ph3, pcap, style_th, style_td, style_code, colors, c_primary, c_border, c_bg_light, cm)

    from generate_fully_expanded_52p_content import append_fully_expanded_content
    append_fully_expanded_content(story, ph1, ph2, ph3, p, pb, peq, pcap, style_th, style_td, style_code, c_primary, c_border, c_bg_light)

    from generate_plan_deep_expansions import append_plan_deep_expansions
    append_plan_deep_expansions(story, p, pb, peq, ph1, ph2, ph3, pcap, style_th, style_td, style_code, colors, c_primary, c_border, c_bg_light, cm)

    from generate_super_expanded_sections import get_super_expanded_sections
    for el in get_super_expanded_sections(p, pb, peq, ph2, ph3, pcap, style_th, style_td, style_code, Table, TableStyle, colors, c_primary, c_border, c_bg_light, cm):
        story.append(el)

    from generate_ultra_dense_52p import append_ultra_dense_sections
    append_ultra_dense_sections(story, p, pb, peq, ph1, ph2, ph3, pcap, style_th, style_td, style_code, colors, c_primary, c_border, c_bg_light, cm)

    from generate_plan_part3 import append_plan_part3
    append_plan_part3(story, p, pb, peq, ph1, ph2, ph3, pcap, style_th, style_td, style_code, colors, c_primary, c_border, c_bg_light, cm)

    from generate_plan_part4 import append_plan_part4
    append_plan_part4(story, p, pb, peq, ph1, ph2, ph3, pcap, style_th, style_td, style_code, colors, c_primary, c_border, c_bg_light, cm)

    from generate_mega_annexes_and_discussions import append_mega_annexes
    append_mega_annexes(story, p, pb, peq, ph1, ph2, ph3, pcap, style_th, style_td, style_code, colors, c_primary, c_border, c_bg_light, cm)

    doc.build(story, canvasmaker=NumberedPlanCanvas)
    
    reader = pypdf.PdfReader(pdf_filename)
    num_pages = len(reader.pages)
    print(f"[*] Conteo de páginas del Plan de Tesis: {num_pages}")
    return num_pages

if __name__ == "__main__":
    build_official_plan_pdf()
