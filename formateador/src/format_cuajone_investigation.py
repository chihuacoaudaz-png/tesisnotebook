# -*- coding: utf-8 -*-
"""
GENERADOR Y FORMATEADOR OFICIAL UNI FIGMM PARA EL TRABAJO DE INVESTIGACIÓN:
'PESAJE DE VOLQUETES GERENCIA MINA CUAJONE 2025'
Preserva el 100% del contenido original, datos, figuras, tablas y fórmulas sin alterar la lógica.
Aplica el formato normado por la Resolución Rectoral UNI (RR 1439-2023).
"""

import os
import sys
import docx
from docx.shared import Inches, Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn
import win32com.client

def set_cell_background(cell, fill_hex):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def generate_formatted_docx():
    print("[*] Iniciando maquetación en formato oficial UNI (RR 1439-2023)...")
    doc = docx.Document()
    
    # 1. Configuración de Márgenes Oficiales UNI (3.0 cm Izq, 2.54 cm Sup, 2.5 cm Der, 2.5 cm Inf)
    sections = doc.sections
    for section in sections:
        section.top_margin = Cm(2.54)
        section.bottom_margin = Cm(2.50)
        section.left_margin = Cm(3.00)
        section.right_margin = Cm(2.50)
        section.page_width = Cm(21.0)
        section.page_height = Cm(29.7)
        section.different_first_page_header_footer = True
        
        # Encabezados y Pies
        header = section.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("UNIVERSIDAD NACIONAL DE INGENIERÍA | FIGMM")
        hrun.font.name = "Arial"
        hrun.font.size = Pt(8.5)
        hrun.font.color.rgb = RGBColor(0, 0, 0)
        
        footer = section.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        frun = fp.add_run("Trabajo de Investigación Técnica - Gerencia Mina Cuajone 2025")
        frun.font.name = "Arial"
        frun.font.size = Pt(8.0)
        frun.font.color.rgb = RGBColor(0, 0, 0)

    # Estilos Base (100% Negro)
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Arial'
    normal_style.font.size = Pt(11)
    normal_style.font.color.rgb = RGBColor(0, 0, 0)

    # Helper Functions
    def add_h1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.bold = True
        run.font.size = Pt(13)
        run.font.color.rgb = RGBColor(0, 0, 0)
        return p

    def add_h2(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.bold = True
        run.font.size = Pt(11.5)
        run.font.color.rgb = RGBColor(0, 0, 0)
        return p

    def add_body(text, bold_prefix="", italic=False):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.15
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        if bold_prefix:
            r_b = p.add_run(bold_prefix)
            r_b.bold = True
            r_b.font.color.rgb = RGBColor(0, 0, 0)
        r_t = p.add_run(text)
        r_t.font.color.rgb = RGBColor(0, 0, 0)
        r_t.italic = italic
        return p

    def add_alpha_item(letter, text):
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Cm(0.75)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        rb = p.add_run(f"{letter}. ")
        rb.bold = True
        rb.font.color.rgb = RGBColor(0, 0, 0)
        rt = p.add_run(text)
        rt.font.color.rgb = RGBColor(0, 0, 0)
        return p

    def add_bullet(text, bold_prefix=""):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        if bold_prefix:
            r_b = p.add_run(bold_prefix)
            r_b.bold = True
            r_b.font.color.rgb = RGBColor(0, 0, 0)
        r_t = p.add_run(text)
        r_t.font.color.rgb = RGBColor(0, 0, 0)
        return p

    def add_formula(eq_text, desgloses=[]):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(6)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(eq_text)
        r.font.name = 'Consolas'
        r.font.size = Pt(10.0)
        r.bold = True
        r.font.color.rgb = RGBColor(0, 0, 0)
        
        if desgloses:
            p_donde = doc.add_paragraph()
            p_donde.paragraph_format.space_after = Pt(2)
            r_d = p_donde.add_run("Donde:")
            r_d.italic = True
            r_d.font.size = Pt(9.5)
            r_d.font.color.rgb = RGBColor(0, 0, 0)
            for d in desgloses:
                p_item = doc.add_paragraph(style='List Bullet')
                p_item.paragraph_format.space_after = Pt(2)
                p_item.paragraph_format.line_spacing = 1.05
                r_item = p_item.add_run(d)
                r_item.font.size = Pt(9.5)
                r_item.font.color.rgb = RGBColor(0, 0, 0)

    def add_figure(img_path, caption_text, width_cm=13.0):
        if os.path.exists(img_path):
            p_img = doc.add_paragraph()
            p_img.paragraph_format.space_before = Pt(6)
            p_img.paragraph_format.space_after = Pt(3)
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.add_run().add_picture(img_path, width=Cm(width_cm))
            
            p_cap = doc.add_paragraph()
            p_cap.paragraph_format.space_after = Pt(2)
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r_cap = p_cap.add_run(caption_text)
            r_cap.bold = True
            r_cap.font.size = Pt(9.0)
            r_cap.font.color.rgb = RGBColor(0, 0, 0)
            
            p_src = doc.add_paragraph()
            p_src.paragraph_format.space_after = Pt(8)
            p_src.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r_src = p_src.add_run("Fuente: Registro de Operaciones Mina Cuajone (2025).")
            r_src.italic = True
            r_src.font.size = Pt(8.0)
            r_src.font.color.rgb = RGBColor(0, 0, 0)

    def add_figure_pair(img_path1, caption1, img_path2, caption2, width_cm=7.2):
        """Inserta dos figuras lado a lado en una misma fila sin bordes para evitar pixelado."""
        tbl = doc.add_table(rows=3, cols=2)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        for row in tbl.rows:
            for cell in row.cells:
                cell.width = Cm(width_cm)
                tcPr = cell._tc.get_or_add_tcPr()
                tcBorders = parse_xml(r'<w:tcBorders xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
                                      r'<w:top w:val="none"/><w:left w:val="none"/><w:bottom w:val="none"/><w:right w:val="none"/>'
                                      r'</w:tcBorders>')
                tcPr.append(tcBorders)
        
        # Fila 0: Imágenes
        cell_l, cell_r = tbl.rows[0].cells
        if os.path.exists(img_path1):
            p1 = cell_l.paragraphs[0]
            p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p1.paragraph_format.space_before = Pt(4)
            p1.paragraph_format.space_after = Pt(2)
            p1.add_run().add_picture(img_path1, width=Cm(width_cm))
        if os.path.exists(img_path2):
            p2 = cell_r.paragraphs[0]
            p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p2.paragraph_format.space_before = Pt(4)
            p2.paragraph_format.space_after = Pt(2)
            p2.add_run().add_picture(img_path2, width=Cm(width_cm))
            
        # Fila 1: Títulos
        cell_cap1, cell_cap2 = tbl.rows[1].cells
        p_c1 = cell_cap1.paragraphs[0]
        p_c1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_c1.paragraph_format.space_after = Pt(1)
        r_c1 = p_c1.add_run(caption1)
        r_c1.bold = True
        r_c1.font.size = Pt(8.5)
        r_c1.font.color.rgb = RGBColor(0, 0, 0)
        
        p_c2 = cell_cap2.paragraphs[0]
        p_c2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_c2.paragraph_format.space_after = Pt(1)
        r_c2 = p_c2.add_run(caption2)
        r_c2.bold = True
        r_c2.font.size = Pt(8.5)
        r_c2.font.color.rgb = RGBColor(0, 0, 0)
        
        # Fila 2: Fuente
        cell_s1, cell_s2 = tbl.rows[2].cells
        p_s1 = cell_s1.paragraphs[0]
        p_s1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_s1.paragraph_format.space_after = Pt(6)
        r_s1 = p_s1.add_run("Fuente: Operaciones Mina Cuajone.")
        r_s1.italic = True
        r_s1.font.size = Pt(7.5)
        r_s1.font.color.rgb = RGBColor(0, 0, 0)
        
        p_s2 = cell_s2.paragraphs[0]
        p_s2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_s2.paragraph_format.space_after = Pt(6)
        r_s2 = p_s2.add_run("Fuente: Operaciones Mina Cuajone.")
        r_s2.italic = True
        r_s2.font.size = Pt(7.5)
        r_s2.font.color.rgb = RGBColor(0, 0, 0)

    # -------------------------------------------------------------------------
    # PORTADA OFICIAL FORMATO UNI FIGMM
    # -------------------------------------------------------------------------
    p_uni = doc.add_paragraph()
    p_uni.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_uni.paragraph_format.space_before = Pt(10)
    p_uni.paragraph_format.space_after = Pt(2)
    r1 = p_uni.add_run("UNIVERSIDAD NACIONAL DE INGENIERÍA\n")
    r1.bold = True
    r1.font.size = Pt(15)
    r1.font.color.rgb = RGBColor(0, 0, 0)
    
    r2 = p_uni.add_run("FACULTAD DE INGENIERÍA GEOLÓGICA, MINERA Y METALÚRGICA\n")
    r2.bold = True
    r2.font.size = Pt(12)
    r2.font.color.rgb = RGBColor(0, 0, 0)
    
    r3 = p_uni.add_run("ESCUELA PROFESIONAL DE INGENIERÍA DE MINAS\n")
    r3.bold = True
    r3.font.size = Pt(11)
    r3.font.color.rgb = RGBColor(0, 0, 0)
    
    p_line = doc.add_paragraph()
    p_line.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_line.paragraph_format.space_after = Pt(20)
    r_bar = p_line.add_run("____________________________________________________")
    r_bar.font.color.rgb = RGBColor(0, 0, 0)

    p_tipo = doc.add_paragraph()
    p_tipo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_tipo.paragraph_format.space_after = Pt(14)
    r_tipo = p_tipo.add_run("INFORME DE INVESTIGACIÓN TÉCNICA OPERACIONAL\n")
    r_tipo.bold = True
    r_tipo.font.size = Pt(13)
    r_tipo.font.color.rgb = RGBColor(0, 0, 0)

    p_tit = doc.add_paragraph()
    p_tit.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_tit.paragraph_format.space_after = Pt(26)
    r_tit = p_tit.add_run("“PESAJE DE VOLQUETES GERENCIA MINA CUAJONE 2025”\n")
    r_tit.bold = True
    r_tit.font.size = Pt(15)
    r_tit.font.color.rgb = RGBColor(0, 0, 0)

    p_meta = doc.add_paragraph()
    p_meta.paragraph_format.space_after = Pt(4)
    p_meta.paragraph_format.left_indent = Cm(3.0)
    
    r_m1 = p_meta.add_run("ÁREA:\n")
    r_m1.bold = True
    r_m1.font.size = Pt(10.5)
    r_m1.font.color.rgb = RGBColor(0, 0, 0)
    r_m1_t = p_meta.add_run("Entrenamiento Mina / Operaciones Mina\nSuperintendencia de Operaciones Mina Cuajone\n\n")
    r_m1_t.font.color.rgb = RGBColor(0, 0, 0)
    
    r_m2 = p_meta.add_run("DIRIGIDO A:\n")
    r_m2.bold = True
    r_m2.font.size = Pt(10.5)
    r_m2.font.color.rgb = RGBColor(0, 0, 0)
    r_m2_t = p_meta.add_run("Superintendente de Operaciones Mina\n\n")
    r_m2_t.font.color.rgb = RGBColor(0, 0, 0)
    
    r_m3 = p_meta.add_run("ELABORADO POR:\n")
    r_m3.bold = True
    r_m3.font.size = Pt(10.5)
    r_m3.font.color.rgb = RGBColor(0, 0, 0)
    r_m3_t = p_meta.add_run("Becario de Operaciones Mina\n\n")
    r_m3_t.font.color.rgb = RGBColor(0, 0, 0)
    
    r_m4 = p_meta.add_run("FECHA DE ELABORACIÓN:\n")
    r_m4.bold = True
    r_m4.font.size = Pt(10.5)
    r_m4.font.color.rgb = RGBColor(0, 0, 0)
    r_m4_t = p_meta.add_run("24 de Octubre del 2025\n")
    r_m4_t.font.color.rgb = RGBColor(0, 0, 0)

    p_loc = doc.add_paragraph()
    p_loc.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_loc.paragraph_format.space_before = Pt(36)
    r_loc = p_loc.add_run("MOQUEGUA – PERÚ\n2025")
    r_loc.font.size = Pt(11)
    r_loc.bold = True
    r_loc.font.color.rgb = RGBColor(0, 0, 0)

    # -------------------------------------------------------------------------
    # CONTENIDO / ÍNDICE OFICIAL (Página 2)
    # -------------------------------------------------------------------------
    doc.add_page_break()
    add_h1("CONTENIDO")
    
    indice_items = [
        "1. RESUMEN",
        "   1.1. ALCANCES",
        "   1.2. UBICACIÓN",
        "   1.3. PERSONAL A CARGO",
        "2. OBJETIVOS",
        "3. PROCEDIMIENTO DEL PESAJE",
        "   3.1. PROCEDIMIENTO DE PESAJE",
        "4. DATOS RECOPILADOS",
        "   4.1. DATOS PROCESADOS",
        "   4.2. CÁLCULO DEL VOLQUETE CARGADO/VACÍO",
        "5. ANÁLISIS DE PESO VACIO, CARGADO Y PAYLOAD",
        "   5.1. FLOTA CATERPILLAR 797F",
        "   5.2. FLOTA CATERPILLAR 798AC",
        "   5.3. FLOTA CATERPILLAR 793D",
        "   5.4. FLOTA KOMATSU 930E",
        "   5.5. FLOTA KOMATSU 930E-4",
        "   5.6. FLOTA KOMATSU 930E-4SE",
        "   5.7. FLOTA KOMATSU 980E-4",
        "   5.8. FLOTA KOMATSU 980E-5",
        "6. DISTRIBUCIÓN DE CARGA EN EL EJE DELANTERO",
        "   6.1. ANÁLISIS DE DISTRIBUCIÓN EN FLOTA DE MAYOR TONELAJE",
        "   6.2. ANÁLISIS DE DISTRIBUCIÓN EN FLOTA DE MENOR TONELAJE",
        "7. DISTRIBUCIÓN DE CARGA EN EL EJE POSTERIOR",
        "   7.1. ANÁLISIS DE DISTRIBUCIÓN EN FLOTA DE MAYOR TONELAJE",
        "   7.2. ANÁLISIS DE DISTRIBUCIÓN EN FLOTA DE MENOR TONELAJE",
        "8. DISTRIBUCIÓN DE CARGA POR EJE",
        "   8.1. ANÁLISIS POR FLOTA",
        "   8.2. ANÁLISIS POR VOLQUETE",
        "9. EFICIENCIA DE LOS PALEROS EN EL CENTRADO DE LA CARGA",
        "   9.1. LISTA DE OPERADORES DE PALA",
        "10. PAYLOAD VS TONELAJE VIMS/PLM",
        "11. CÁLCULO DEL PESO DEL PARACHOQUE",
        "12. CONCLUSIONES"
    ]
    for item in indice_items:
        p_ind = doc.add_paragraph()
        p_ind.paragraph_format.space_after = Pt(2)
        p_ind.paragraph_format.line_spacing = 1.10
        r_ind = p_ind.add_run(item)
        r_ind.font.size = Pt(10)
        r_ind.font.color.rgb = RGBColor(0, 0, 0)
        if any(item.strip().startswith(f"{n}.") for n in range(1, 13)):
            r_ind.bold = True

    # -------------------------------------------------------------------------
    # 1. RESUMEN (Página 3 - HOJA NUEVA TRAS EL ÍNDICE)
    # -------------------------------------------------------------------------
    doc.add_page_break()

    # -------------------------------------------------------------------------
    # 1. RESUMEN
    add_h1("1. RESUMEN")
    add_h2("1.1. Alcances")
    add_body("El 12 de octubre de 2025 se llevaron a cabo los trabajos finales de preparación en la zona de pesaje, los cuales comprendieron labores de relleno, nivelación y compactación del terreno. Para la ejecución de estas actividades se emplearon los equipos Cargador Frontal WA470 (F972), Motoniveladora CAT 24M (M244) y Rodillo Bomag WB 226 DH-5 (RCC-1). Asimismo, con el propósito de garantizar una mayor precisión en la nivelación del terreno, se contó con el apoyo técnico de la empresa contratista Mincoser. En las Figuras 1 y 2 se presentan los trabajos realizados durante esta etapa.")
    
    add_figure("formateador/figuras/figura_01.png", "Figura 1. Nivelación con la Motoniveladora CAT 24M (M244).", width_cm=13.0)
    add_figure("formateador/figuras/figura_02.png", "Figura 2. Compactación con Rodillo Bomag y apoyo técnico de MINCOSER.", width_cm=13.0)

    add_h2("1.2. Ubicación")
    add_body("El área de pesaje estuvo delimitada por el parqueo Cocotea Bajo (Sur Oeste), Grifo Cocotea Bajo (Sur Este) y la Tranquera 4 (Norte). En la Figura 3 se muestra la ubicación del área del pesaje en el software MineOperate.")
    
    add_figure("formateador/figuras/figura_03.png", "Figura 3. Ubicación de la zona de pesaje en software MineOperate.", width_cm=13.0)

    add_h2("1.3. Personal a Cargo")
    add_body("Durante la realización del pesaje participaron diversas áreas y empresas contratistas, según la Tabla 1 adjunta:")
    add_figure("formateador/figuras/tabla_01.png", "Tabla 1. Funciones del personal a cargo del pesaje.", width_cm=13.5)

    add_body("El trabajo tuvo una duración total de nueve (9) días, iniciando el 12 de octubre de 2025 y culminando el 20 de octubre de 2025. Durante la jornada final, y a solicitud de la empresa Ferreyros CAT, se realizaron repesajes de los volquetes V132, V144, V163 y V164, efectuándose dos mediciones por cada unidad en condición de carga.")

    # 2. OBJETIVOS (LISTA ALFABÉTICA a., b., c., d., e.)
    add_h1("2. OBJETIVOS")
    add_alpha_item("a", "Determinar el peso vacío (EMW) y carga útil (Payload) de los 46 volquetes de Operaciones Mina Cuajone.")
    add_alpha_item("b", "Mostrar la distribución de peso (ton) en cada posición de los neumáticos.")
    add_alpha_item("c", "Cuantificar en toneladas, el impacto de los accesorios adicionales en la distribución del peso del volquete.")
    add_alpha_item("d", "Calcular la diferencia entre el tonelaje real (balanza) y el tonelaje de la pantalla de ADVISOR (Caterpillar) y Payload meter (Komatsu).")
    add_alpha_item("e", "Determinar los operadores de pala con mayor eficiencia en el centrado de carga.")

    # 3. PROCEDIMIENTO DEL PESAJE
    add_h1("3. PROCEDIMIENTO DEL PESAJE")
    add_body("El área de pesaje, de 15 m de ancho por 30 m de largo, se ubicó en la ruta de descarga hacia el depósito de desmonte Cocotea Bajo. En la Figura 4 se muestra la ubicación de los PADs y el acceso a la balanza. Los volquetes ingresaron a los PADs a una velocidad máxima de 5 km/h para garantizar la estabilidad de la balanza durante la medición.")
    
    add_figure("formateador/figuras/figura_04.png", "Figura 4. Vista en planta de la zona de pesaje y acceso a balanza PADs.", width_cm=13.0)

    add_body("El pesaje de cada volquete se realizó tres (3) veces vacío y cuatro (4) veces cargado con desmonte. El requerimiento del fabricante indica que el cálculo del peso del volquete vacío (EMW), debe realizarse con los fluidos al 100%, debido a ello cada volquete contó con al menos 90 % de combustible. En el pesaje cargado se mantuvo un mínimo de 50 % de combustible. En la Figura 5 y 6 se muestra el procedimiento de pesaje de los volquetes vacíos y cargados.")

    add_h2("3.1. Procedimiento de Pesaje Operacional")
    add_alpha_item("a", "Previa coordinación entre Control Mina y el becario de Operaciones Mina vía radial (frecuencia C2) para autorizar el ingreso de los volquetes.")
    add_alpha_item("b", "En la frecuencia 13 (local), y con apoyo del vigía, se brindan las indicaciones al operador del volquete para posicionar el eje delantero sobre ambos PADs.")
    add_alpha_item("c", "Una vez que los neumáticos del eje delantero se encuentran centrados y la lectura del pesómetro se estabiliza, se registran los datos en el formato establecido.")
    add_alpha_item("d", "Posteriormente, bajo las indicaciones del becario de Operaciones Mina, se posiciona el eje trasero sobre ambos PADs y se realiza el registro correspondiente.")
    add_alpha_item("e", "Finalmente, se indica al operador del volquete su salida de la zona de pesaje si se encuentra cargado; en caso de estar vacío, debe retornar inmediatamente a la zona de ingreso hasta completar sus 3 pasadas.")

    add_figure("formateador/figuras/figura_05.png", "Figura 5. Procedimiento de pesaje del volquete vacío sobre PADs.", width_cm=12.5)
    add_figure("formateador/figuras/figura_06.png", "Figura 6. Procedimiento de pesaje del volquete cargado sobre PADs.", width_cm=12.5)

    # 4. DATOS RECOPILADOS
    add_h1("4. DATOS RECOPILADOS")
    add_h2("4.1. Datos Procesados")
    add_body("Los datos registrados en campo correspondieron a:")
    add_bullet("Fecha y hora del pesaje.")
    add_bullet("Tipo de material transportado.")
    add_bullet("Asignación de pala y número de pases de carguío.")
    add_bullet("Condición de volquete: cargado o vacío.")
    add_bullet("Lectura de los PADs: Eje delantero, eje posterior derecho e izquierdo.")
    add_bullet("Payload del volquete, tonelaje de la pantalla VIMS / Display.")
    add_bullet("Nivel de combustible (%) y horómetro del equipo.")

    add_h2("4.2. Cálculo del Volquete Vacío y Cargado")
    add_body("El cálculo del peso del volquete cargado y vacío se realizó mediante la siguiente formulación física:")
    add_formula("Peso del eq. vacío/cargado = ED(TI + TD) + EP(TI + TD)", [
        "ED: Eje delantero.",
        "EP: Eje posterior.",
        "TI: Tonelaje registrado en PAD izquierdo.",
        "TD: Tonelaje registrado en PAD derecho."
    ])

    add_body("El tonelaje correspondiente al combustible se determinó mediante:")
    add_formula("Toneladas de Combustible = (Capacidad volumétrica) · (Densidad) · (% Combustible)", [
        "Capacidad volumétrica: Galones de capacidad nominal del tanque de combustible.",
        "Densidad: Densidad del combustible diésel (0.00322 tn/gl).",
        "% Combustible: Indicador de nivel de combustible al momento del pesaje."
    ])

    add_figure("formateador/figuras/figura_07.png", "Figura 7. Capacidad volumétrica del tanque de combustible por modelo de volquete (Galones).", width_cm=13.0)

    # 5. ANÁLISIS DE PESO VACIO, CARGADO Y PAYLOAD
    add_h1("5. ANÁLISIS DE PESO VACIO, CARGADO Y PAYLOAD")
    add_body("En la flota Komatsu, el nivel de combustible se visualiza a través de un indicador analógico, mientras que en la flota CAT se muestra de forma similar, complementándose además con la información proporcionada por el sistema ADVISOR.")

    # 5.1. CAT 797F
    add_h2("5.1. Flota Caterpillar 797F")
    add_body("El volquete V144 destaca por ser el más ligero con 284 toneladas, debido a que su tolva es una Austin Westech, a diferencia de los demás volquetes que presentan una tolva Austin JEC. En promedio hay una variación de 14 toneladas entre ambos modelos de tolva.")
    add_figure("formateador/figuras/figura_08.png", "Figura 8. Pesaje de la flota CAT 797F.", width_cm=12.5)
    
    add_body("Comparativa técnica de tolvas instaladas en la flota CAT 797F:")
    add_body("TOLVA AUSTIN JEC: Ancho: 7.6 m | Altura de carga: 7.4 m | Cola: 4.8 m | Espesor: 0.4 m | Enclavamiento: 10° | Peso: 43.6 t.")
    add_figure("formateador/figuras/figura_09a.png", "Figura 9a. Tolva Austin JEC (Flota CAT 797F).", width_cm=11.0)
    
    add_body("TOLVA AUSTIN WESTECH: Ancho: 7.7 m | Altura de carga: 7.3 m | Cola: 4.9 m | Espesor: 0.4 m | Enclavamiento: 8° | Peso: 30.6 t.")
    add_figure("formateador/figuras/figura_09b.png", "Figura 9b. Tolva Austin WESTECH (Flota CAT 797F).", width_cm=11.0)

    # 5.2. CAT 798AC
    add_h2("5.2. Flota Caterpillar 798AC")
    add_body("En la Figura 10 se muestra el resultado de pesaje de la flota CAT 798AC. En carga útil, el volquete V10 de tolva MP supera en 3 toneladas al volquete V11 de tolva HE. Estos volquetes no presentan parachoque.")
    add_figure("formateador/figuras/figura_10.png", "Figura 10. Pesaje de la flota CAT 798AC.", width_cm=12.5)
    
    add_body("Comparativa técnica de tolvas instaladas en la flota CAT 798AC:")
    add_body("TOLVA MP: Max Payload (MP) | Ancho: 9.93 m | Altura de carga: 7.04 m | Cola: 5.03 m | Espesor: 0.4 m | Enclavamiento: 12°.")
    add_figure("formateador/figuras/figura_11a.png", "Figura 11a. Tolva MP (Max Payload) - CAT 798AC.", width_cm=10.0)
    
    add_body("TOLVA HE: High Efficiency (HE) | Ancho: 9.74 m | Altura de carga: 7.66 m | Cola: 4.91 m | Espesor: 0.44 m | Enclavamiento: 16°.")
    add_figure("formateador/figuras/figura_11b.png", "Figura 11b. Tolva HE (High Efficiency) - CAT 798AC.", width_cm=10.0)

    # 5.3. CAT 793D
    add_h2("5.3. Flota Caterpillar 793D")
    add_body("El peso del volquete V120 supera en 5 toneladas al volquete V121. El volquete V120 cargó en promedio 9 toneladas más que el V121. El análisis se muestra en la Figura 12. La tolva del volquete V120 tiene una mayor capacidad volumétrica que la tolva del V121.")
    add_figure("formateador/figuras/figura_12.png", "Figura 12. Pesaje de la flota CAT 793D.", width_cm=12.5)
    
    add_body("Comparativa técnica de tolvas MSDII instaladas en la flota CAT 793D:")
    add_body("TOLVA MSDII (V120): Estándar | Ancho: 7.72 m | Altura de carga: 6.41 m | Cola: 4.35 m | Espesor: 0.43 m | Enclavamiento: 9°.")
    add_figure("formateador/figuras/figura_13a.png", "Figura 13a. Tolva MSDII de 7.72 m (Volquete V120).", width_cm=11.0)
    
    add_body("TOLVA MSDII (V121): Estándar | Ancho: 7.44 m | Altura de carga: 6.19 m | Cola: 4.17 m | Espesor: 0.44 m | Enclavamiento: 13°.")
    add_figure("formateador/figuras/figura_13b.png", "Figura 13b. Tolva MSDII de 7.44 m (Volquete V121).", width_cm=11.0)

    # 5.4. KOMATSU 930E
    add_h2("5.4. Flota Komatsu 930E")
    add_body("Los volquetes V100 y V101, equipados con tolvas DT-Hiload, presentan pesos vacíos con mínima variación (1 t). En su lugar, el V103 posee tolva Estándar, mientras que el V105 una Austin WESTECH. La variación en los modelos de tolva y de Motor (QSK60, MTU2000), justifican una variación en el EMW. NOTA: Todos los volquetes presentan parachoque y ninguno protector de goma.")
    add_figure("formateador/figuras/figura_14.png", "Figura 14. Pesaje de la flota Komatsu 930E.", width_cm=12.5)
    
    add_body("Comparativa técnica de tolvas instaladas en la flota Komatsu 930E:")
    add_body("TOLVA DT HILOAD: Ancho: 8.66 m | Altura de carga: 7.41 m | Cola: 4.85 m | Espesor: 0.26 m | Enclavamiento: 13° | Peso: 33.2 t.")
    add_figure("formateador/figuras/figura_15a.png", "Figura 15a. Tolva DT Hiload (Komatsu 930E).", width_cm=10.5)
    
    add_body("TOLVA AUSTIN WESTECH: Ancho: 8.58 m | Altura de carga: 7.47 m | Cola: 4.6 m | Espesor: 0.39 m | Enclavamiento: 9° | Peso: 39.5 t.")
    add_figure("formateador/figuras/figura_15b.png", "Figura 15b. Tolva Austin WESTECH (Komatsu 930E).", width_cm=11.5)

    # 5.5. KOMATSU 930E-4
    add_h2("5.5. Flota Komatsu 930E-4")
    add_body("Los volquetes que comparten el modelo de tolva tienen un peso vacío muy similar. Cabe mencionar que el volquete V106 es de tolva WESTECH. DT Hiload: V107, V108 y V112. NOTA: Todos los volquetes presentan parachoque y ninguno protector de goma.")
    add_figure("formateador/figuras/figura_16.png", "Figura 16. Pesaje de la flota Komatsu 930E-4.", width_cm=12.5)
    
    add_body("Comparativa técnica de tolvas instaladas en la flota Komatsu 930E-4:")
    add_body("TOLVA AUSTIN JEC (V110, V112): Altura de carga: 7.28 m | Cola: 4.71 m | Espesor: 0.5 m | Enclavamiento: 8° | Peso: 35.5 t.")
    add_figure("formateador/figuras/figura_17a.png", "Figura 17a. Tolva Austin JEC (Flota 930E-4).", width_cm=11.0)
    
    add_body("TOLVA ESTÁNDAR (V109, V111, V113): Cola: 4.6 m | Espesor: 0.39 m | Enclavamiento: 9°.")
    add_figure("formateador/figuras/figura_17b.png", "Figura 17b. Tolva Estándar (Flota 930E-4).", width_cm=11.0)

    # 5.6. KOMATSU 930E-4SE
    add_h2("5.6. Flota Komatsu 930E-4SE")
    add_body("En la flota 930E-4SE, el volquete V116 supera en 6 toneladas al volquete V115. Esta ventaja en peso es en el eje trasero, debido a que el volquete V116 tiene instalados dados en su tolva DT Hiload Phase X.")
    add_figure("formateador/figuras/figura_18.png", "Figura 18. Pesaje de la flota Komatsu 930E-4SE.", width_cm=12.5)
    
    add_body("Comparativa de dados de tolva instalados:")
    add_body("VOLQUETE V115: Sin dados de protección instalados en tolva.")
    add_figure("formateador/figuras/figura_19a.png", "Figura 19a. Volquete V115 sin dados.", width_cm=10.5)
    
    add_body("VOLQUETE V116: Con dados de refuerzo instalados en tolva DT Hiload Phase X.")
    add_figure("formateador/figuras/figura_19b.png", "Figura 19b. Volquete V116 con dados instalados.", width_cm=11.5)

    # 5.7. KOMATSU 980E-4
    add_h2("5.7. Flota Komatsu 980E-4")
    add_body("El menor peso vacío (EMW) de los volquetes V160 y V165 se debe a que no tienen instaladas gomas de protección en sus tolvas, a diferencia de los demás. En promedio hay una diferencia de 15 toneladas en comparación a los volquetes que presentan liner.")
    add_figure("formateador/figuras/figura_20.png", "Figura 20. Pesaje de la flota Komatsu 980E-4.", width_cm=13.0)

    # 5.8. KOMATSU 980E-5
    add_h2("5.8. Flota Komatsu 980E-5")
    add_body("En la flota 980 E-5, no hay una variación significativa en el peso vacío, esta flota, en su totalidad presenta tolva DT Hiload Phase X y motor QSK78, además, todos presentan protector de caucho y ninguno parachoque.")
    add_figure("formateador/figuras/figura_21.png", "Figura 21. Pesaje de la flota Komatsu 980E-5.", width_cm=12.5)
    
    add_figure("formateador/figuras/figura_22.png", "Figura 22. Modelo de tolva DT Hiload Phase X (Flota 980E-5).", width_cm=11.5)
    add_figure("formateador/figuras/figura_23.png", "Figura 23. Análisis de distribución en la posición 1 y 2 vacío.", width_cm=13.0)

    # 6. DISTRIBUCIÓN DE CARGA EN EL EJE DELANTERO
    add_h1("6. DISTRIBUCIÓN DE CARGA EN EL EJE DELANTERO")
    add_h2("6.1. Análisis de Distribución en Flota de Mayor Tonelaje")
    add_body("En la flota CAT 797F y CAT 798AC hay un desbalance de 7.5 toneladas entre la posición 1 y 2 en vacío. En el caso de la flota Komatsu el desbalance es de 2 toneladas a favor de la posición 2. Este desbalance se debe a la ubicación del tanque de combustible, en la flota CAT el desbalance es mayor debido a que el tanque de combustible es de 2000 gl frente a los 1400 gl de la flota Komatsu.")
    add_body("En la flota CAT 797F la posición 1 y 2 cargan en promedio 115 toneladas, con picos de hasta 134 toneladas, superando excesivamente al target de Michelin (109 toneladas) en el tamaño 59/80R63 y en ocasiones al target de Bridgestone VREV (123.5 toneladas). Esto se agrava en la rampa negativa de la ruta de P08 hacia Cuajone Este. Esta condición podría provocar prematuramente una separación mecánica.")
    add_figure("formateador/figuras/figura_24.png", "Figura 24. Análisis de distribución de peso en la posición 1 y 2 cargado.", width_cm=13.0)

    add_h2("6.2. Análisis de Distribución en Flota de Menor Tonelaje")
    add_body("En la flota CAT 793D existe un desbalance de 2.6 toneladas a favor de la posición 1. En la flota Komatsu 930 hay un desbalance de 3 toneladas a favor de la posición 2. Este desbalance se debe a la ubicación respectiva del tanque de combustible. La capacidad del tanque de combustible en la flota Komatsu 930E-4SE es de 1400 galones.")
    add_figure("formateador/figuras/figura_25.png", "Figura 25. Análisis de distribución de peso en posición 1 y 2 vacío.", width_cm=13.0)

    # 7. DISTRIBUCIÓN DE CARGA EN EL EJE POSTERIOR
    add_h1("7. DISTRIBUCIÓN DE CARGA EN EL EJE POSTERIOR")
    add_h2("7.1. Análisis de Distribución en Flota de Mayor Tonelaje")
    add_body("Distribución de cargas del volquete cargado y vacío por neumáticos en flotas de mayor tonelaje:")
    add_figure("formateador/figuras/figura_26.png", "Figura 26. Análisis de distribución de peso en posición 3&4 vs 5&6 cargado.", width_cm=13.0)
    add_figure("formateador/figuras/figura_27.png", "Figura 27. Análisis de distribución de peso en posición 3&4 vs 5&6 vacío.", width_cm=13.0)

    add_h2("7.2. Análisis de Distribución en Flota de Menor Tonelaje")
    add_body("Distribución de cargas del volquete cargado y vacío por neumáticos en flotas de menor tonelaje:")
    add_figure("formateador/figuras/figura_28.png", "Figura 28. Distribución de peso en posición 3&4 vs 5&6 cargado (Menor tonelaje).", width_cm=13.0)
    add_figure("formateador/figuras/figura_29.png", "Figura 29. Distribución de peso en posición 3&4 vs 5&6 vacío (Menor tonelaje).", width_cm=13.0)

    # 8. DISTRIBUCIÓN DE CARGA POR EJE
    add_h1("8. DISTRIBUCIÓN DE CARGA POR EJE")
    add_h2("8.1. Análisis por Flota")
    add_body("Distribución porcentual de cargas por eje en condición de vacío y cargado:")
    add_figure("formateador/figuras/figura_30.png", "Figura 30. Distribución de carga por eje en vacío (Flota mayor).", width_cm=13.0)
    add_figure("formateador/figuras/figura_31.png", "Figura 31. Distribución de carga por eje en vacío (Flota menor).", width_cm=13.0)
    add_figure("formateador/figuras/figura_32.png", "Figura 32. Distribución de carga por eje en condición de carga.", width_cm=13.0)

    add_h2("8.2. Análisis por Volquete")
    add_body("Análisis individualizado por cada unidad en las flotas operativas:")

    # Flota CAT 797F
    add_h2("8.2.1. Flota Caterpillar 797F")
    add_figure("formateador/figuras/figura_33.png", "Figura 33. Distribución por eje en vacío (CAT 797F).", width_cm=13.0)
    add_figure("formateador/figuras/figura_34.png", "Figura 34. Distribución por eje en cargado (CAT 797F).", width_cm=13.0)
    add_body("La distribución del peso en condición de carga en la flota CAT 797 F, en el eje delantero, fue mayor al target (33.33%). Se debe retroalimentar a los operadores de pala sobre la importancia del centrado de carga en el rendimiento de neumáticos. A partir de un 34.2% excedemos el límite carga de los neumáticos Michelin de tamaño 59/80R63.")

    # Flota CAT 798AC
    add_h2("8.2.2. Flota Caterpillar 798AC")
    add_figure_pair("formateador/figuras/figura_35.png", "Figura 35. Distribución de peso por eje en vacío (CAT 798AC).",
                    "formateador/figuras/figura_36.png", "Figura 36. Distribución de peso por eje cargado (CAT 798AC).", width_cm=7.2)
    add_body("La distribución del peso en condición de carga en la flota CAT 798 AC, en el eje delantero, fue mayor al target (33.33%). El eje delantero del V11 (36.5%) soporta 231.7 ton, asumiendo una distribución uniforme, cada neumático del eje delantero soporta 115.9 toneladas, excediendo el target de Michelin (109 ton).")

    # Flota Komatsu 930E
    add_h2("8.2.3. Flota Komatsu 930E")
    add_figure_pair("formateador/figuras/figura_37.png", "Figura 37. Distribución de peso por eje en vacío (Komatsu 930E).",
                    "formateador/figuras/figura_38.png", "Figura 38. Distribución de peso por eje en cargado (Komatsu 930E).", width_cm=7.2)
    add_body("En la flota 930E el volquete con mayor % de peso en el eje delantero es el V101, esta distribución de carga de 34.4% significa un peso de al menos 89.1 toneladas en cada neumático, por debajo del target de Michelin (92 toneladas).")

    # Flota Komatsu 930E-4
    add_h2("8.2.4. Flota Komatsu 930E-4")
    add_figure_pair("formateador/figuras/figura_39.png", "Figura 39. Distribución de peso por eje en vacío (Komatsu 930E-4).",
                    "formateador/figuras/figura_40.png", "Figura 40. Distribución de peso por eje cargado (Komatsu 930E-4).", width_cm=7.2)
    add_body("Solo en el volquete V114, con una distribución de 36.2% en el eje delantero, se excede el límite de carga de Michelin en 1 tonelada, teniendo en cuenta que en condición vacía, es el volquete con mayor distribución en el eje delantero.")

    # Flota Komatsu 930E-4SE
    add_h2("8.2.5. Flota Komatsu 930E-4SE")
    add_figure_pair("formateador/figuras/figura_41.png", "Figura 41. Distribución de peso por eje en vacío (Komatsu 930E-4SE).",
                    "formateador/figuras/figura_42.png", "Figura 42. Distribución de peso por eje en cargado (Komatsu 930E-4SE).", width_cm=7.2)
    add_body("El exceso de +1.5% en la distribución de peso en el eje delantero del V116, no significa un exceso al límite de carga de Michelin. En conclusión, los neumáticos de tamaño 53/80 R63 instalados en la flota Komatsu 930E, E4, 4SE trabajan por debajo del límite de carga de Michelin.")

    # Flota Komatsu 980E-4
    add_h2("8.2.6. Flota Komatsu 980E-4")
    add_figure_pair("formateador/figuras/figura_43.png", "Figura 43. Distribución de peso por eje en vacío (Komatsu 980E-4).",
                    "formateador/figuras/figura_44.png", "Figura 44. Distribución de peso por eje cargado (Komatsu 980E-4).", width_cm=7.2)
    add_body("Los volquetes V162, V163, V161 y V164 tienen instalado un protector de goma en su tolva (liner), por esa razón, en condición vacía, tienen mayor distribución en el eje posterior a comparación de los volquetes V160 y V165.")

    # Flota Komatsu 980E-5
    add_h2("8.2.7. Flota Komatsu 980E-5")
    add_figure_pair("formateador/figuras/figura_45.png", "Figura 45. Distribución de peso por eje en vacío (Komatsu 980E-5).",
                    "formateador/figuras/figura_46.png", "Figura 46. Distribución de peso por eje en cargado (Komatsu 980E-5).", width_cm=7.2)
    add_body("No se observan diferencias significativas en distribución de peso en condición vacía, pues los 3 volquetes presentan liner y el mismo modelo de tolva. En condición de carga, el volquete V167 presenta un exceso de carga en el eje posterior, recalcando que fue cargado dos veces en la pala P08 con una distribución de 30% / 70%.")

    # Flota Caterpillar 793D
    add_h2("8.2.8. Flota Caterpillar 793D")
    add_figure_pair("formateador/figuras/figura_47.png", "Figura 47. Distribución por eje en vacío (CAT 793D).",
                    "formateador/figuras/figura_48.png", "Figura 48. Distribución por eje en cargado (CAT 793D).", width_cm=7.2)
    add_body("En condición vacía, el volquete V120 presenta mayor distribución en el eje posterior debido a su tolva más pesada y cola más larga en comparación al V121. Cada neumático del eje delantero soporta al menos 67 toneladas, los neumáticos usados en esta flota son de tamaño 40.00 R57.")

    # 9. EFICIENCIA DE LOS PALEROS EN EL CENTRADO DE LA CARGA
    add_h1("9. EFICIENCIA DE LOS PALEROS EN EL CENTRADO DE LA CARGA")
    add_body("Los operadores Oscar Pinedo, Efraín Huaypuna y Edil Valdivia destacan con la mayor eficiencia en la distribución de carga. En la Figura 49 se muestra la distribución de carga de todos los operadores evaluados.")
    add_figure("formateador/figuras/figura_49.png", "Figura 49. Ranking de operadores con mejor eficiencia en la distribución de carga.", width_cm=13.0)

    # 10. PAYLOAD VS TONELAJE VIMS/PLM
    add_h1("10. PAYLOAD VS TONELAJE VIMS/PLM")
    add_body("El tonelaje de la pantalla VIMS en el volquete V11 es mayor en 1.6% que la carga real. En la flota CAT 793D, en el volquete V121 el sistema VIMS marca un 4.4% menos respecto a la carga útil real. En el caso del volquete V121 se debe inspeccionar las suspensiones.")
    add_figure("formateador/figuras/figura_50.png", "Figura 50. Tonelaje VIMS vs Payload CAT 798AC.", width_cm=11.5)
    add_figure("formateador/figuras/figura_51.png", "Figura 51. Tonelaje VIMS vs Payload CAT 793D.", width_cm=11.5)

    add_body("El sistema Payload Meter en los volquetes Komatsu calcula la carga útil a partir de la presión de las suspensiones, la velocidad y la inclinación del equipo. El tonelaje mostrado en la pantalla de instrumentación electrónica varía en más de 5% con respecto a la carga útil en los volquetes V108, V112 y V115. En ocasiones la configuración del PLM está en toneladas cortas, por lo que se recomienda una inspección en esos volquetes.")
    add_figure("formateador/figuras/figura_52.png", "Figura 52. Tonelaje VIMS vs Payload CAT 797F.", width_cm=13.0)
    add_figure("formateador/figuras/figura_53.png", "Figura 53. Tonelaje VIMS vs Payload Komatsu 930E.", width_cm=13.0)

    add_body("En la flota Komatsu 980 la variación entre el tonelaje Payload Meter y el payload real varía en más de 5% en los volquetes V163, V164 y V165. Se recomienda verificar la configuración de unidades (Toneladas Cortas).")
    add_figure("formateador/figuras/figura_54.png", "Figura 54. Tonelaje VIMS vs Payload Komatsu 980E.", width_cm=13.0)

    # 11. CÁLCULO DEL PESO DEL PARACHOQUE
    add_h1("11. CÁLCULO DEL PESO DEL PARACHOQUE")
    add_body("El volquete V131 fue pesado 6 veces vacío; la primera vez se pesó 3 veces sin el parachoques, posteriormente se instaló el parachoques el 15 de octubre del 2025, procediéndose nuevamente con su pesaje 3 veces vacío. El primer pesaje fue con un 92.61% de combustible y el segundo a 94.00%.")

    add_body("Formulaciones de balance de masa aplicadas:")
    add_formula("Peso Total 1 = Peso Vacío + Combustible 1")
    add_formula("Peso Total 2 = Peso Vacío + Combustible 2 + Parachoques")
    add_formula("Parachoque (t) = Peso Total 2 - Peso Total 1 - Combustible 2 + Combustible 1")
    add_formula("Parachoque (t) = 299.30 t - 296.93 t - 94.00%(T) + 92.61%(T) = 2.37 t - 1.39%(T)")
    add_formula("Parachoque (t) = 2.37 t - (1.39% × 2,000 gl × 3.22 kg/gl) = 2.30 t")

    # 12. CONCLUSIONES
    add_h1("12. CONCLUSIONES")
    add_bullet("El tonelaje añadido por la instalación del parachoques en los volquetes CATERPILLAR 797F le añade 2.3 toneladas al eje delantero.", bold_prefix="1. ")
    add_bullet("El tonelaje añadido al eje posterior por la instalación del liner en la flota KOMATSU 980E-4 significa un adicional de 15 toneladas.", bold_prefix="2. ")
    add_bullet("Los operadores de pala con mejor centrado de carga son Oscar Pinedo, Efraín Huaypuna y Edil Valdivia.", bold_prefix="3. ")
    add_bullet("En la flota CATERPILLAR 798 AC, el volquete V10 de tolva MP presenta 3 toneladas más de carga útil que el volquete V11 de tolva HE.", bold_prefix="4. ")
    add_bullet("En condición vacía, en las flotas CAT 797F y CAT 798AC existe un desbalance de más de 7 toneladas entre los neumáticos del eje delantero, debido a la ubicación del tanque de combustible.", bold_prefix="5. ")
    add_bullet("En condición de carga, los neumáticos de posición 1 de la flota CAT 797F soportan más de 115 toneladas, excediendo el target de Michelin en el tamaño 59/80R63 (109 t).", bold_prefix="6. ")
    add_bullet("Se debe inspeccionar las suspensiones y/o las unidades de tonelajes del sistema Payload Meter en los volquetes V108, V115, V112, V165, V163, V164 y V165.", bold_prefix="7. ")

    # Guardar DOCX
    docx_out = "formateador/output/INFORME_PESAJE_VOLQUETES_CUAJONE_UNI.docx"
    doc.save(docx_out)
    print(f"[EXITO] Documento DOCX oficial guardado en: {docx_out}")
    return docx_out

def convert_docx_to_pdf(docx_path, pdf_path):
    print(f"[*] Compilando a PDF mediante Microsoft Word COM...")
    word = win32com.client.Dispatch('Word.Application')
    word.Visible = False
    doc = word.Documents.Open(os.path.abspath(docx_path))
    num_pages = doc.ComputeStatistics(2)
    doc.SaveAs(os.path.abspath(pdf_path), FileFormat=17)
    doc.Close()
    word.Quit()
    print(f"[EXITO] PDF compilado. Total de páginas físicas: {num_pages}")
    return pdf_path, num_pages

if __name__ == "__main__":
    out_docx = generate_formatted_docx()
    out_pdf = "formateador/output/INFORME_PESAJE_VOLQUETES_CUAJONE_UNI.pdf"
    convert_docx_to_pdf(out_docx, out_pdf)
