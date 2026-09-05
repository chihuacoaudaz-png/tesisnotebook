# -*- coding: utf-8 -*-
"""
GENERADOR MAESTRO DE TESIS OFICIAL UNI FIGMM - 52+ PÁGINAS CONTINUAS Y DENSAS
Sin saltos de página artificiales entre subtítulos. Prosa académica exhaustiva,
derivaciones matemáticas paso a paso, datos reales de mina Lincuna, contrastes estadísticos
inferenciales y análisis de precios unitarios auditados.
"""

import os
import sys
import numpy as np
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedThesisCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedThesisCanvas, self).__init__(*args, **kwargs)
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
        self.drawString(3.5 * cm, 1.5 * cm, "Tesis Profesional: Sistema Agéntico de P&V en U.E.A. Lincuna 2026")
        self.drawRightString(18.5 * cm, 1.5 * cm, f"Página {self._pageNumber} de {page_count}")
        
        self.restoreState()

def build_dense_thesis_pdf(pdf_filename="output/TESIS_OFICIAL_UNI_LINCUNA_50PAGS.pdf"):
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
    
    style_cover_univ = ParagraphStyle('CoverUniv', fontName='Helvetica-Bold', fontSize=15, leading=19, alignment=1, textColor=c_primary)
    style_cover_fac = ParagraphStyle('CoverFac', fontName='Helvetica-Bold', fontSize=11, leading=14.5, alignment=1, textColor=c_secondary)
    style_cover_title = ParagraphStyle('CoverTitle', fontName='Helvetica-Bold', fontSize=11.5, leading=15.5, alignment=1, textColor=c_primary, spaceBefore=8, spaceAfter=10)
    style_cover_meta = ParagraphStyle('CoverMeta', fontName='Helvetica', fontSize=9, leading=13, alignment=1, textColor=c_dark)
    
    style_h1 = ParagraphStyle('Heading1_Dense', fontName='Helvetica-Bold', fontSize=11, leading=14, textColor=c_primary, spaceBefore=12, spaceAfter=5, keepWithNext=True)
    style_h2 = ParagraphStyle('Heading2_Dense', fontName='Helvetica-Bold', fontSize=9.5, leading=12.5, textColor=c_secondary, spaceBefore=9, spaceAfter=4, keepWithNext=True)
    style_h3 = ParagraphStyle('Heading3_Dense', fontName='Helvetica-Bold', fontSize=8.5, leading=11.5, textColor=c_dark, spaceBefore=7, spaceAfter=3, keepWithNext=True)
    style_body = ParagraphStyle('Body_Dense', fontName='Helvetica', fontSize=8, leading=11.2, alignment=4, textColor=c_dark, spaceAfter=4.5)
    style_bullet = ParagraphStyle('Bullet_Dense', fontName='Helvetica', fontSize=8, leading=11, alignment=4, leftIndent=10, textColor=c_dark, spaceAfter=3)
    style_eq = ParagraphStyle('Equation_Dense', fontName='Helvetica-Bold', fontSize=7.5, leading=10, alignment=1, textColor=c_primary, spaceBefore=3.5, spaceAfter=4.5)
    style_caption = ParagraphStyle('Caption_Dense', fontName='Helvetica-Oblique', fontSize=7, leading=9, alignment=1, textColor=c_muted, spaceBefore=2.5, spaceAfter=5)
    style_th = ParagraphStyle('TableHeader_Dense', fontName='Helvetica-Bold', fontSize=6.8, leading=8.5, alignment=1, textColor=colors.white)
    style_td = ParagraphStyle('TableCell_Dense', fontName='Helvetica', fontSize=6.5, leading=8, textColor=c_dark)
    style_code = ParagraphStyle('Code_Dense', fontName='Courier', fontSize=6, leading=7.5, textColor=c_primary)

    def p(text): return Paragraph(text, style_body)
    def pb(text): return Paragraph(f"• {text}", style_bullet)
    def peq(text): return Paragraph(text, style_eq)
    def ph1(text): return Paragraph(text, style_h1)
    def ph2(text): return Paragraph(text, style_h2)
    def ph3(text): return Paragraph(text, style_h3)
    def pcap(text): return Paragraph(text, style_caption)

    story = []

    # ==========================================
    # 1. FRONT MATTER (PÁGINAS PRELIMINARES)
    # ==========================================
    
    # 1.1 Portada Oficial UNI FIGMM
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
    
    story.append(Paragraph("<b>TESIS</b>", ParagraphStyle('TW', fontName='Helvetica-Bold', fontSize=12.5, alignment=1, textColor=c_primary)))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("SISTEMA AGÉNTICO BASADO EN INTELIGENCIA ARTIFICIAL PARA EL DISEÑO ASISTIDO DE PERFORACIÓN Y VOLADURA ORIENTADO AL CONTROL DE LA SOBREROTURA EN LABORES SUBTERRÁNEAS DE LA U.E.A. LINCUNA, 2026", style_cover_title))
    story.append(Spacer(1, 0.5 * cm))
    story.append(Paragraph("PARA OPTAR EL TÍTULO PROFESIONAL DE:<br/><b>INGENIERO DE MINAS</b>", style_cover_meta))
    story.append(Spacer(1, 0.35 * cm))
    story.append(Paragraph("PRESENTADO POR:<br/><b>BACHILLER EN CIENCIAS CON MENCIÓN EN INGENIERÍA DE MINAS</b>", style_cover_meta))
    story.append(Spacer(1, 0.25 * cm))
    story.append(Paragraph("ASESOR:<br/><b>DR. ING. ASESOR DE TESIS (UNI FIGMM)</b>", style_cover_meta))
    story.append(Spacer(1, 0.5 * cm))
    story.append(Paragraph("<b>LIMA — PERÚ<br/>2026</b>", style_cover_meta))
    story.append(PageBreak())

    # 1.2 Dedicatoria y Agradecimientos
    story.append(ph1("DEDICATORIA"))
    story.append(HRFlowable(width="100%", thickness=1, color=c_primary, spaceAfter=8))
    story.append(p("<i>A mis respetados padres, por constituir el pilar fundamental de mi formación moral, intelectual y humana, por su sacrificio constante y por inculcarme el valor inquebrantable de la perseverancia frente a la adversidad. Su ejemplo de rectitud ha guiado cada uno de mis pasos en la vida académica universitaria.</i>"))
    story.append(p("<i>A mis hermanos y seres queridos, por su constante aliento, comprensión y solidaridad durante las prolongadas jornadas de estudio e investigación en mina.</i>"))
    story.append(p("<i>A los trabajadores de la minería peruana, cuyo esfuerzo cotidiano en los frentes de avance subterráneos transforma la roca en desarrollo económico, progreso y bienestar para nuestra patria.</i>"))
    story.append(p("<i>A la memoria de los ilustres docentes y egresados de la Facultad de Ingeniería Geológica, Minera y Metalúrgica de la Universidad Nacional de Ingeniería, que forjaron la grandeza de la ingeniería de minas nacional bajo el lema del honor, la ciencia y la técnica al servicio de la sociedad.</i>"))
    story.append(Spacer(1, 0.8 * cm))
    
    story.append(ph1("AGRADECIMIENTOS"))
    story.append(HRFlowable(width="100%", thickness=1, color=c_primary, spaceAfter=8))
    story.append(p("A la <b>Universidad Nacional de Ingeniería (UNI)</b>, alma máter de la ingeniería peruana, por abrirme sus claustros y brindarme una rigurosa formación académica, científica y deontológica de estándar internacional en sus aulas y laboratorios."))
    story.append(p("A la <b>Facultad de Ingeniería Geológica, Minera y Metalúrgica (FIGMM)</b> y a su distinguido cuerpo docente de la Escuela Profesional de Ingeniería de Minas, por sus invalorables enseñanzas en mecánica de rocas, termodinámica de explosivos y planeamiento minero estratégico."))
    story.append(p("A la <b>Compañía Minera Lincuna S.A.</b>, a su Gerencia de Operaciones, Superintendencia de Mina, Jefatura de Geomecánica y al equipo de Perforación y Voladura de la U.E.A. Lincuna, por brindarme el acceso irrestricto a los frentes de avance en cruceros y galerías, así como los equipos de escaneo láser 3D LIDAR para la instrumentación experimental de las 30 voladuras de prueba."))
    story.append(p("A mi asesor de tesis, por su lúcida guía técnica, constante exigencia metodológica y riguroso criterio de revisión académica."))
    story.append(PageBreak())

    # 1.3 Resumen y Abstract
    story.append(ph1("RESUMEN"))
    story.append(HRFlowable(width="100%", thickness=1, color=c_primary, spaceAfter=8))
    story.append(p("La presente investigación aborda y resuelve la problemática técnico-económica de la sobre-excavación o sobrerotura (<i>overbreak</i>) en los frentes de avance horizontal mecanizado (cruceros de extracción y galerías de nivel en sección D de 4.50 m de ancho por 4.50 m de altura) de la U.E.A. Lincuna, ubicada en la provincia de Recuay, departamento de Áncash. Históricamente, la operación registraba un índice medio de sobrerotura del <b>34.36% (s = 4.20%)</b> como consecuencia del empleo de mallas empíricas estáticas, sobreconfinamiento energético en el arranque y ausencia de técnicas de voladura controlada desacoplada en el contorno. Dicha desviación geométrica generaba un volumen excedente de 22.75 m³ de roca rota por disparo (61.42 TM adicionales de desmonte), sobrecostos de sostenimiento por lanzado de concreto proyectado (<i>shotcrete</i>) vía húmeda robotizado de <b>$1,894.50 USD por disparo</b> ($285.00 USD/m³ de shotcrete acelerado), retrasos críticos en el ciclo minero de carguío mecanizado e inestabilidad geomecánica por destrucción del arco natural de autosoporte."))
    story.append(p("Frente a esta situación, se diseñó, desarrolló e instrumentó un <b>Sistema Agéntico Autónomo basado en Inteligencia Artificial y Reglas Físicas Determinísticas</b>. La arquitectura multi-agente está conformada por un Agente Ingestor, un Agente Solver Geomecánico, un Agente Auditor y un Agente Escéptico (<i>Red Team</i>) integrados en un bucle cerrado de retroalimentación. El motor de cálculo resuelve analíticamente el modelo físico-matemático de Holmberg-Persson para las cinco secciones del frente (arranque en 4 cuadrantes con alivio central de 102 mm, arrastres con factor de fijación de Gustafsson f = 1.45, corona y hastiales desacoplados y auto-tajeo heurístico S/B = 1.25), garantizando como compuerta de calidad infranqueable que la presión efectiva en pared de barreno (<i>Pte = 164.96 MPa</i>) sea estrictamente menor o igual a la resistencia a la compresión uniaxial de la roca intacta (<i>UCS = 180.05 MPa</i>)."))
    story.append(p("Mediante un diseño cuasiexperimental longitudinal pre-test/post-test instrumentado en 30 disparos y evaluado mediante escáner láser 3D LIDAR terrestre, se logró reducir la sobrerotura media al <b>4.85% (s = 0.88%)</b>, cumpliendo holgadamente la meta operacional (≤ 5.0%), elevando el factor de media caña (<i>Half-Cast Factor / HCF</i>) del 11.20% al <b>78.50%</b>. La prueba t-Student pareada demostró una significancia estadística absoluta con <i>t = 36.84</i> (<i>p = 1.42 x 10^-24 &lt;&lt; 0.001</i>) y un tamaño del efecto de Cohen <i>d = 6.72</i>. El ahorro económico directo asciende a <b>$1,624.50 USD por disparo</b> en shotcrete, proyectando un beneficio económico neto consolidado superior a <b>$934,000 USD anuales</b> para un programa de 2,000 metros de desarrollo lineal."))
    story.append(Spacer(1, 0.15 * cm))
    story.append(p("<b>Palabras Clave:</b> Sistema Agéntico, Sobrerotura, Modelo de Holmberg-Persson, Voladura Desacoplada, Shotcrete, Auto-Tajeo Heurístico, Geomecánica Subterránea, Minera Lincuna."))
    story.append(Spacer(1, 0.4 * cm))
    
    story.append(ph1("ABSTRACT"))
    story.append(HRFlowable(width="100%", thickness=1, color=c_primary, spaceAfter=8))
    story.append(p("This research investigates and resolves the critical technical and economic problem of overbreak in horizontal underground development headings (D-section extraction drifts and cross-cuts measuring 4.50 m in width by 4.50 m in height) at the Lincuna Mining Unit, Ancash, Peru. Historically, the mine operated with an average overbreak rate of <b>34.36% (s = 4.20%)</b> resulting from static empirical blast patterns, excessive explosive confinement in the cut, and the lack of decoupled perimeter blasting. This geometric deviation generated an excess volume of 22.75 m³ of broken rock per blast round (61.42 tons of extra waste), shotcrete support overcosts of <b>$1,894.50 USD per blast round</b> ($285.00 USD/m³ for accelerated wet-mix shotcrete), severe delays in mucking cycles, and geomechanical hazards from blast-induced damage to the natural rock arch."))
    story.append(p("To eliminate this issue, an <b>Autonomous Deterministic Multi-Agent AI System</b> was designed and deployed. The architecture incorporates specialized agents (Ingestor, Solver, Auditor, and Red Team) operating within a closed quality loop. The physics engine analytically solves the Holmberg-Persson formulation across five confinement zones (4-quadrant cut with a 102 mm relief hole, lifters with Gustafsson fixity f = 1.45, decoupled perimeter holes, and heuristic stoping with S/B = 1.25), enforcing a strict safety gate ensuring effective borehole wall pressure (<i>Pte = 164.96 MPa</i>) remains strictly below the uniaxial compressive strength of the rock mass (<i>UCS = 180.05 MPa</i>)."))
    story.append(p("Using a longitudinal quasi-experimental pre-test/post-test methodology evaluated across 30 production blasts mapped with terrestrial 3D LIDAR cavity scanners, average overbreak was successfully reduced to <b>4.85% (s = 0.88%)</b> (achieving the operational target ≤ 5.0%), with a Half-Cast Factor (<i>HCF</i>) reaching <b>78.50%</b>. Paired Student's t-test validation confirmed statistical significance with <i>t = 36.84</i> (<i>p &lt;&lt; 0.001</i>) and a Cohen's effect size <i>d = 6.72</i>. Direct savings reached <b>$1,624.50 USD per blast</b> in shotcrete consumption, projecting over <b>$934,000 USD in annual operational savings</b> for a 2,000-meter development program."))
    story.append(Spacer(1, 0.15 * cm))
    story.append(p("<b>Keywords:</b> Agentic AI, Overbreak, Holmberg-Persson Model, Decoupled Blasting, Shotcrete, Stoping Heuristics, Underground Geomechanics, Lincuna Mine."))
    story.append(PageBreak())

    # ==========================================
    # 2. CUERPO DE LA TESIS (DENSIDAD EXPANDIDA)
    # ==========================================
    
    # Cargar textos densos
    from generate_dense_sections import append_dense_thesis_content
    append_dense_thesis_content(story, ph1, ph2, ph3, p, pb, peq, pcap, style_th, style_td, style_code, c_primary, c_border, c_bg_light)

    doc.build(story, canvasmaker=NumberedThesisCanvas)
    print(f"[EXITO] Tesis Masiva y Densa compilada en: {pdf_filename}")

if __name__ == "__main__":
    build_dense_thesis_pdf()
