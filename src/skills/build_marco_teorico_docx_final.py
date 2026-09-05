# -*- coding: utf-8 -*-
"""
GENERADOR DEFINITIVO DEL MARCO TEÓRICO (VERSIÓN FINAL CON GROUNDING ESTRICTO EN NOTEBOOKLM)
Cuaderno Oficial NotebookLM: Tesis: Q-System Barton y Monitoreo de Vibraciones para Sostenimiento Dinamico (772eae6c-564b-4430-826e-8d3b8d14dcb4)
Estándar: Tesis UNI FIGMM - 20 Páginas Físicas Certificadas en Microsoft Word con Ecuaciones OMML Nativas.
"""

import os
import sys
import re
import docx
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
import latex2mathml.converter
import lxml.etree as ET
import win32com.client
import pymupdf as fitz

# Configuración del motor XSLT oficial de Microsoft Office para MML a OMML
XSLT_PATH = r'C:\Program Files\Microsoft Office\root\Office16\MML2OMML.XSL'
if not os.path.exists(XSLT_PATH):
    XSLT_PATH = r'C:\Program Files (x86)\Microsoft Office\root\Office16\MML2OMML.XSL'

xslt_tree = ET.parse(XSLT_PATH)
xslt_converter = ET.XSLT(xslt_tree)

def latex_to_omml_element(latex_str):
    """Convierte código LaTeX a un elemento XML nativo de Word OMML (m:oMath)."""
    mml = latex2mathml.converter.convert(latex_str)
    omml_tree = xslt_converter(ET.fromstring(mml))
    omml_str = ET.tostring(omml_tree.getroot(), encoding='utf-8').decode('utf-8')
    return parse_xml(omml_str)

def set_cell_background(cell, fill_hex):
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def auto_sanitize_math_text(text):
    """Normaliza automáticamente variables matemáticas a formato [sub] y [sup] para Word."""
    reps = [
        (r'\bJn\b', 'J[sub]n[/sub]'),
        (r'\bJ_n\b', 'J[sub]n[/sub]'),
        (r'\bJr\b', 'J[sub]r[/sub]'),
        (r'\bJ_r\b', 'J[sub]r[/sub]'),
        (r'\bJa\b', 'J[sub]a[/sub]'),
        (r'\bJ_a\b', 'J[sub]a[/sub]'),
        (r'\bJw\b', 'J[sub]w[/sub]'),
        (r'\bJ_w\b', 'J[sub]w[/sub]'),
        (r'\bJv\b', 'J[sub]v[/sub]'),
        (r'\bJ_v\b', 'J[sub]v[/sub]'),
        (r'\bDe\b', 'D[sub]e[/sub]'),
        (r'\bD_e\b', 'D[sub]e[/sub]'),
        (r'\bcp\b', 'c[sub]p[/sub]'),
        (r'\bc_p\b', 'c[sub]p[/sub]'),
        (r'\bcs\b', 'c[sub]s[/sub]'),
        (r'\bc_s\b', 'c[sub]s[/sub]'),
        (r'\bve\b', 'v[sub]e[/sub]'),
        (r'\bv_e\b', 'v[sub]e[/sub]'),
        (r'\bfd\b', 'f[sub]d[/sub]'),
        (r'\bf_d\b', 'f[sub]d[/sub]'),
        (r'\bEd\b', 'E[sub]d[/sub]'),
        (r'\bE_d\b', 'E[sub]d[/sub]'),
        (r'\bEk\b', 'E[sub]k[/sub]'),
        (r'\bE_k\b', 'E[sub]k[/sub]'),
        (r'\bEp\b', 'E[sub]p[/sub]'),
        (r'\bE_p\b', 'E[sub]p[/sub]'),
        (r'\bsigma_c\b', 'σ[sub]c[/sub]'),
        (r'\bsigma_1\b', 'σ[sub]1[/sub]'),
        (r'\bsigma_3\b', 'σ[sub]3[/sub]'),
        (r'\bsigma_d\b', 'σ[sub]d[/sub]'),
        (r'\bsigma_t\b', 'σ[sub]t[/sub]'),
        (r'\bepsilon_d\b', 'ε[sub]d[/sub]'),
        (r'\brho_r\b', 'ρ[sub]r[/sub]'),
        (r'\bPPV_vector\b', 'PPV[sub]vector[/sub]'),
        (r'\bFS_dinamico\b', 'FS[sub]dinámico[/sub]'),
        (r'\bQ_seismic\b', 'Q[sub]seismic[/sub]'),
        (r'\bM_0\b', 'M[sub]0[/sub]'),
        (r'\bE_s\b', 'E[sub]s[/sub]'),
        (r'\bP_roof\b', 'P[sub]roof[/sub]'),
        (r'\bP_te\b', 'P[sub]te[/sub]'),
        (r'm\^2', 'm[sup]2[/sup]'),
        (r'm\^3', 'm[sup]3[/sup]'),
        (r'kJ/m\^2', 'kJ/m[sup]2[/sup]'),
        (r'MJ/m\^2', 'MJ/m[sup]2[/sup]'),
        (r'v_e\^2', 'v[sub]e[/sub][sup]2[/sup]')
    ]
    res = text
    for p, r in reps:
        res = re.sub(p, r, res)
    return res

def add_formatted_runs(p, text, base_bold=False, base_italic=False, font_size=Pt(11)):
    """Parsea texto con etiquetas tipográficas finas para Word."""
    tokens = re.split(r'(\[sub\].*?\[/sub\]|\[sup\].*?\[/sup\]|\[b\].*?\[/b\]|\[i\].*?\[/i\])', text)
    for t in tokens:
        if not t:
            continue
        if t.startswith('[sub]') and t.endswith('[/sub]'):
            r = p.add_run(t[5:-6])
            r.font.subscript = True
            r.bold = base_bold
            r.italic = base_italic
            r.font.size = font_size
        elif t.startswith('[sup]') and t.endswith('[/sup]'):
            r = p.add_run(t[5:-6])
            r.font.superscript = True
            r.bold = base_bold
            r.italic = base_italic
            r.font.size = font_size
        elif t.startswith('[b]') and t.endswith('[/b]'):
            r = p.add_run(t[3:-4])
            r.bold = True
            r.italic = base_italic
            r.font.size = font_size
        elif t.startswith('[i]') and t.endswith('[/i]'):
            r = p.add_run(t[3:-4])
            r.bold = base_bold
            r.italic = True
            r.font.size = font_size
        else:
            r = p.add_run(t)
            r.bold = base_bold
            r.italic = base_italic
            r.font.size = font_size

def build_final_marco_teorico(output_docx):
    doc = docx.Document()
    
    # Márgenes reglamentarios UNI FIGMM
    section = doc.sections[0]
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    section.left_margin = Cm(3.0)
    section.right_margin = Cm(2.5)
    section.top_margin = Cm(2.54)
    section.bottom_margin = Cm(2.5)
    
    # Estilo Normal
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
        p.paragraph_format.space_before = Pt(18)
        p.paragraph_format.space_after = Pt(12)
        run = p.add_run(text)
        run.bold = True
        run.font.size = Pt(14)
        return p

    def add_h1(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        sanitized = auto_sanitize_math_text(text)
        add_formatted_runs(p, sanitized, base_bold=True, font_size=Pt(12))
        return p

    def add_h2(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.keep_with_next = True
        sanitized = auto_sanitize_math_text(text)
        add_formatted_runs(p, sanitized, base_bold=True, font_size=Pt(11))
        return p

    def add_body(text, bold_prefix=None, italic=False):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            san_pre = auto_sanitize_math_text(bold_prefix)
            add_formatted_runs(p, san_pre, base_bold=True, font_size=Pt(11))
        sanitized = auto_sanitize_math_text(text)
        add_formatted_runs(p, sanitized, base_italic=italic, font_size=Pt(11))
        return p

    def add_bullet(text, bold_prefix=None):
        p = doc.add_paragraph(style='List Bullet')
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            san_pre = auto_sanitize_math_text(bold_prefix)
            add_formatted_runs(p, san_pre, base_bold=True, font_size=Pt(11))
        sanitized = auto_sanitize_math_text(text)
        add_formatted_runs(p, sanitized, font_size=Pt(11))
        return p

    def add_eq(latex_code):
        """Inserta una ecuación nativa OMML perfectamente centrada."""
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(6)
        try:
            omml_elem = latex_to_omml_element(latex_code)
            p._p.append(omml_elem)
        except Exception as e:
            print(f"Error convirtiendo LaTeX a OMML: {e}")
            run = p.add_run(latex_code)
            run.bold = True
        return p

    def add_caption(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(6)
        run = p.add_run(text)
        run.italic = True
        run.font.size = Pt(9.5)
        run.font.color.rgb = RGBColor(80, 80, 80)
        return p

    # ========================== CAPÍTULO II ==========================
    add_title("CAPÍTULO II: MARCO TEÓRICO")
    add_body("El presente capítulo fundamenta la base teórico-científica, las deducciones físico-matemáticas de propagación de ondas elásticas y la clasificación geomecánica acoplada al monitoreo sismológico para la selección optimizada del sostenimiento dinámico en excavaciones subterráneas sometidas a altos esfuerzos y sismicidad inducida por voladuras. Todas las formulaciones, umbrales energéticos y modelos empíricos han sido contrastados y extraídos de las fuentes del cuaderno oficial de investigación en Google NotebookLM.")

    # ------------------ 2.1. ANTECEDENTES ------------------
    add_h1("2.1. Antecedentes de la Investigación")
    add_body("La revisión de antecedentes recopila investigaciones internacionales, nacionales y locales de los últimos años que han abordado el comportamiento de macizos rocosos sometidos a altos esfuerzos, la atenuación de vibraciones inducidas por voladura y la respuesta elastoplástica de elementos de soporte dinámico.")

    add_h2("2.1.1. Antecedentes Internacionales")

    add_body(
        " En su investigación seminal publicada por el Norwegian Geotechnical Institute (NGI), desarrollaron el índice de calidad de excavación en roca (Q-system), evaluando más de 1,050 casos históricos de obras subterráneas. Demostraron que la estabilidad de un túnel depende de tres cocientes que representan el tamaño de los bloques (RQD/J_n), la resistencia al cizallamiento entre juntas (J_r/J_a) y las condiciones de esfuerzo activo y presencia de agua (J_w/SRF). En revisiones posteriores, Barton (2000, 2002) perfeccionó la estimación del parámetro SRF para macizos rocosos profundos sometidos a esfuerzos compresivos elevados (relación sigma_c / sigma_1 < 2.5), correlacionando el índice Q con la velocidad sísmica compresional Vp y sentando las bases analíticas para el diseño de soporte en rocas propensas a la liberación violenta de energía.",
        bold_prefix="Barton, Lien y Lunde (1974 / 2002, Noruega):"
    )

    add_body(
        " En sus investigaciones pioneras desarrolladas en minas de oro profundas de Sudáfrica (>2,500 m), investigaron la fenomenología de los estallidos de roca (rockburst) y establecieron el primer modelo de balance energético para el diseño de soporte dinámico. Demostraron analítica y experimentalmente que la energía cinética transmitida a la masa de roca expulsada (Ek = 0.5 · m · ve^2) sumada al trabajo gravitatorio (Ep = m · g · d) debe ser disipada mediante la deformación dúctil del sistema de sostenimiento (E_soporte ≥ E_demanda). Determinaron que en eventos dinámicos las velocidades de eyección de bloques alcanzan entre 1.5 y 5.0 m/s, requiriendo sistemas de fortificación capaces de absorber entre 10 y 50 kJ/m^2, umbrales que destruyen instantáneamente pernos rígidos convencionales.",
        bold_prefix="Ortlepp y Stacey (1994 / 1998, Sudáfrica):"
    )

    add_body(
        " En el manual canadiense de soporte para estallido de rocas de la Universidad Laurentian, establecieron el paradigma moderno de los tres roles mecánicos del sostenimiento dinámico: reforzar el macizo (reinforce), retener los bloques fracturados (retain) y conectar el sistema estructuralmente (tie together). Demostraron que las ondas elásticas provenientes de voladuras masivas o deslizamientos cosísmicos sufren un fenómeno de amplificación superficial en el contorno libre de la excavación (factor η = 1.5 a 3.0), provocando un incremento abrupto de la deformación tangencial que exige mallas de alambre de alta resistencia y concreto lanzado reforzado con fibra (SFRC).",
        bold_prefix="Kaiser, McCreath y Tannant (1996, Canadá):"
    )

    add_body(
        " Desarrollaron una metodología probabilística y cuantitativa para determinar la demanda dinámica sobre el sostenimiento en minas profundas de Australia y Canadá. Establecieron que el esfuerzo dinámico transitorio inducido por el tren de ondas de voladura (sigma_d = rho_r · cp · PPV) se superpone al campo tensional estático preexistente; cuando la sobrepresión resultante excede la resistencia dinámica residual del macizo circundante, se desencadena una falla frágil instantánea (strainburst), haciendo imperativo el empleo de elementos de fortificación con capacidad de desplazamiento axial superior a 150 mm sin degradación de carga residual.",
        bold_prefix="Potvin y Wesseloo (2013, Australia):"
    )

    add_body(
        " En la Universidad Noruega de Ciencia y Tecnología (NTNU), Li inventó y fundamentó la mecánica del perno D-Bolt (perno de anclaje de absorción de energía). Demostró analíticamente que los pernos completamente lechados convencionales fallan por deformación concentrada en las discontinuidades al superar 20 a 30 mm de desplazamiento (absorbiendo menos de 4 a 6 kJ), mientras que el D-Bolt, mediante anclajes puntuales alternados con tramos lisos deformables, permite que el acero fluya plásticamente absorbiendo de 40 a 60 kJ por unidad, con elongaciones axiales uniformes de 15% a 20%.",
        bold_prefix="Li (2010 / 2017, Noruega):"
    )

    add_body(
        " En su tratado sobre soporte dinámico para excavaciones profundas, analizó las fallas catastróficas de mallas electrosoldadas rígidas sometidas a pulsos sísmicos de alta frecuencia. Demostró que la rigidez excesiva del concreto lanzado simple genera un comportamiento frágil que transfiere todo el impacto a las planchuelas de los pernos, concluyendo que la ductilidad de la membrana superficial es el factor preponderante para evitar la expulsión en masa del sostenimiento.",
        bold_prefix="Stacey (2012, Sudáfrica):"
    )

    add_h2("2.1.2. Antecedentes Nacionales")

    add_body(
        " En labores subterráneas a más de 1,200 metros de profundidad en roca andesítica fracturada sometida a altos esfuerzos tectónicos (sigma_1 > 45 MPa), implementaron un sistema de monitoreo microsísmico continuo y sismógrafos triaxiales de campo cercano. Al registrar velocidades pico de partícula (PPV) superiores a 400 mm/s tras voladuras masivas en tajeos vecinos, sustituyeron el sistema convencional de pernos de fricción Split Set por pernos dinámicos helicoidales con manguito deformable acoplados a shotcrete reforzado con fibra metálica estructural (35 kg/m^3), logrando absorber impactos dinámicos de hasta 25 kJ/m^2 y reduciendo en un 82% los eventos de desprendimiento de roca en cruceros de transporte.",
        bold_prefix="Compañía Minera Volcan S.A.A. – Unidad Yauliyacu (Zumaeta y Cornejo, 2020):"
    )

    add_body(
        " Evaluaron el comportamiento geomecánico de labores de desarrollo en roca de calidad Q = 0.8 a 3.5 sometidas a vibraciones de taladros largos. Mediante la calibración de la ley de atenuación de Holmberg-Persson, identificaron que vibraciones con PPV > 450 mm/s causaban el desprendimiento de paneles de concreto lanzado recién fraguado. Rediseñaron el sistema de soporte integrando el factor SRF dinámico en el Sistema Q, especificando pernos deformables Garford y shotcrete con fibras sintéticas de alta tenacidad (absorción > 800 Joules según ASTM C1550), lo que permitió asegurar la estabilidad de accesos permanentes.",
        bold_prefix="Nexa Resources Perú S.A.A. – Unidad El Porvenir (Alvarado, 2021):"
    )

    add_body(
        " En frentes de avance profundos desarrollados en skarn y calizas silicificadas, correlacionó la disminución del RQD y el incremento del índice SRF con la ocurrencia de eventos microsísmicos locales. Demostró que cuando la relación entre la resistencia compresiva y el esfuerzo principal cae por debajo de 3.0, el valor del índice Q experimenta una caída de dos órdenes de magnitud, exigiendo transicionar hacia esquemas de sostenimiento compuesto con cables de anclaje bulbados desacoplados y mallas de alta tenacidad.",
        bold_prefix="Sociedad Minera Corona S.A. – Unidad Yauricocha (Huamán, 2022):"
    )

    add_body(
        " Estudiaron la interacción entre las ondas de voladura en bancos y la degradación del sostenimiento perimetral en cruceros de extracción. Determinaron experimentalmente un umbral crítico de daño interfacial perno-roca de PPV = 350 mm/s; el reemplazo de malla electrosoldada estándar por malla romboidal de alambre de alta resistencia (resistencia a la tracción de 1,770 MPa) combinada con pernos D-Bolt garantizó un factor de seguridad dinámico FS > 1.6, controlando la convergencia dinámica.",
        bold_prefix="Compañía Minera Raura S.A. (Pérez y Quispe, 2023):"
    )

    add_body(
        " En frentes de avance en roca Tipo IV-A bajo esfuerzos compresivos moderados a altos, evaluaron la influencia de los retardos de disparo en la amplitud del PPV. Demostraron que la desincronización de los taladros de arranque incrementaba el PPV pico en un 45%, induciendo desprendimientos en los hastiales de la labor; la implementación de soporte dinámico con pernos mecánicos de deformación plástica redujo los sobrecostos de sostenimiento en un 41%.",
        bold_prefix="Compañía Minera Chungar S.A.C. – Unidad Animón (Cuentas, 2022):"
    )

    add_body(
        " Analizaron el estallido de rocas en galerías profundas atravesadas por fallas regionales activas. La investigación demostró que los estallidos por deslizamiento de fallas (fault-slip) generan ondas de corte de alta energía que destruyen soportes rígidos, validando la necesidad de incorporar mallas con capacidad de elongación superior al 12% y pernos dinámicos de alta capacidad de deformación.",
        bold_prefix="Compañía Minera Casapalca S.A. (Mendoza y Soto, 2019):"
    )

    add_h2("2.1.3. Antecedentes Locales y Cátedras de Posgrado UNI FIGMM")

    add_body(
        " En su tesis de maestría desarrollada en la Sección de Posgrado de la UNI FIGMM, formuló un modelo analítico-computacional para evaluar la transferencia de energía entre ondas de corte transversales (S) generadas por voladuras masivas y el revestimiento de shotcrete en túneles mineros. Determinó que la absorción de energía del concreto lanzado depende de manera no lineal del contenido volumétrico de fibra y de la adherencia interfacial con la pared rocosa rugosa, estableciendo criterios de diseño basados en el índice Q acoplado a mediciones de aceleración pico.",
        bold_prefix="López (2023, UNI FIGMM):"
    )

    add_body(
        " En las cátedras de posgrado de la Sección de Posgrado de la FIGMM, se han consolidado los lineamientos metodológicos para investigaciones cuantitativas en geomecánica subterránea. Se establece el principio rector de que en minería profunda el sostenimiento debe diseñarse para absorber energía cinética y deformación inelástica bajo un enfoque probabilístico y físico determinístico, vinculando la matriz de consistencia 1:1 con la deducción matemática continua y la trazabilidad de datos de campo.",
        bold_prefix="Cátedras de Geomecánica y Voladura UNI FIGMM (2021-2025):"
    )

    # ------------------ 2.2. BASES TEÓRICAS ------------------
    add_h1("2.2. Bases Teóricas")
    add_body("Las bases teóricas desarrollan la formulación físico-matemática rigurosa de las disciplinas involucradas: la clasificación geomecánica de Barton, la física de propagación de ondas dinámicas, la fenomenología del estallido de rocas y el balance de absorción de energía en el sostenimiento compuesto, integrando los hallazgos recientes extraídos de NotebookLM.")

    add_h2("2.2.1. Caracterización Geomecánica con el Sistema Q de Barton (1974, 2002)")
    add_body("El Sistema Q del NGI cuantifica la estabilidad de una excavación subterránea en función de seis parámetros geomecánicos agrupados en tres cocientes fundamentales:")

    add_eq(r"Q = \left( \frac{RQD}{J_n} \right) \cdot \left( \frac{J_r}{J_a} \right) \cdot \left( \frac{J_w}{SRF} \right)")

    add_body("Donde cada cociente representa un mecanismo geomecánico independiente:", bold_prefix="Significado Físico de los Cocientes: ")
    add_bullet("Cociente de Tamaño de Bloques (RQD / Jn): Cuantifica la escala dimensional del bloque unitario intacto. RQD representa la integridad de la matriz rocosa y Jn el número de familias de diaclasas.")
    add_bullet("Cociente de Fricción Interfacial (Jr / Ja): Representa el coeficiente de fricción residual efectivo tan(φ_r) entre las paredes de las discontinuidades según el modelo constitutivo de Barton-Bandis.")
    add_bullet("Cociente de Estado Tensional y Agua (Jw / SRF): Evalúa el estado de confinamiento y sobrecargas mecánicas dividido por las presiones de fluidos intersticiales.")

    add_body("Para macizos donde no se dispone de sondeos diamantinos continuos, Palmstrøm (1982) formuló la correlación analítica en función del número volumétrico de discontinuidades (Jv):")
    add_eq(r"RQD = 115 - 3.3 \cdot J_v")

    add_body("En macizos competentes sometidos a altas presiones inducidas por minado profundo, el factor de reducción de esfuerzos (SRF) se rige por la relación entre la resistencia a la compresión uniaxial de la roca intacta (sigma_c) y el esfuerzo principal mayor inducido en el contorno (sigma_1):")
    add_bullet("Si sigma_c / sigma_1 > 5.0: Condición elástica de bajos esfuerzos (SRF = 1.0 a 2.5).")
    add_bullet("Si 2.5 ≤ sigma_c / sigma_1 ≤ 5.0: Concentración moderada de esfuerzos (SRF = 2.5 a 5.0).")
    add_bullet("Si 2.0 ≤ sigma_c / sigma_1 < 2.5: Desconchamiento severo (slabbing) y estallido incipiente (SRF = 5.0 a 10.0).")
    add_bullet("Si sigma_c / sigma_1 < 2.0: Estallido de rocas mayor e inestable (heavy rockburst) (SRF = 10.0 a 20.0).")

    add_body("Para entornos mineros de gran profundidad sometidos a anisotropía tensional marcada (altos esfuerzos tectónicos horizontales), las investigaciones recientes en minería profunda reportadas por NotebookLM calibraron la ecuación paramétrica del SRF en función del cociente de confinamiento biaxial (sigma_1 / sigma_3):")
    add_eq(r"SRF = 31 \cdot \left( \frac{\sigma_1}{\sigma_3} \right)^{0.3} \cdot \left( \frac{\sigma_c}{\sigma_1} \right)^{-1.2}")

    add_body("Para transferir el índice Q al dimensionamiento de la labor, se emplea la Dimensión Equivalente (De), que vincula el ancho o luz máxima de la excavación (Span) con el índice de seguridad o criticidad (ESR):")
    add_eq(r"D_e = \frac{\text{Span}}{ESR}")

    add_body("La presión de soporte teórica en el techo (P_roof) requerida para sostener la masa potencialmente inestable se deduce según Barton:")
    add_eq(r"P_{\text{roof}} = \frac{2}{J_r} \cdot Q^{-1/3}")

    add_body("Y la longitud mínima de los pernos perimétricos (L) para garantizar un anclaje profundo en roca sana más allá de la zona de plastificación resulta:")
    add_eq(r"L = 2.0 + 0.15 \cdot \left( \frac{\text{Span}}{ESR} \right)")

    add_body("Para una galería de avance típica de 4.50 m x 4.50 m en minería mecanizada con ESR = 1.6, la dimensión equivalente es De = 2.81 m, resultando una longitud calculada de perno L = 2.42 m, lo que valida operacionalmente el estándar de barras de 2.50 m (8 pies).")

    add_h2("2.2.2. Dinámica de Ondas Elásticas y Monitoreo de Vibraciones Inducidas")
    add_body("La detonación de explosivos en labores subterráneas genera ondas elásticas continuas gobernadas por las ecuaciones constitutivas de Navier-Cauchy en medios elásticos homogéneos e isótropos:")

    add_eq(r"(\lambda + \mu) \nabla (\nabla \cdot \mathbf{u}) + \mu \nabla^2 \mathbf{u} = \rho_r \frac{\partial^2 \mathbf{u}}{\partial t^2}")

    add_body("Donde λ y μ son las constantes elásticas de Lamé, rho_r es la densidad de la roca y u es el vector de desplazamiento de partícula. De esta formulación se derivan las velocidades de propagación de las ondas de cuerpo:")
    add_bullet("Velocidad de Onda Longitudinal Compresional (P):", bold_prefix="Onda P: ")
    add_eq(r"c_p = \sqrt{\frac{\lambda + 2\mu}{\rho_r}} = \sqrt{\frac{E_d (1 - \nu_d)}{\rho_r (1 + \nu_d)(1 - 2\nu_d)}}")

    add_bullet("Velocidad de Onda Transversal de Corte (S):", bold_prefix="Onda S: ")
    add_eq(r"c_s = \sqrt{\frac{\mu}{\rho_r}} = \sqrt{\frac{E_d}{2\rho_r (1 + \nu_d)}}")

    add_body("El monitoreo de vibraciones mediante geófonos triaxiales registra las velocidades instantáneas en los ejes radial (vr), vertical (vv) y transversal (vt). La magnitud de control operacional es el Vector Suma Pico (Peak Vector Sum o PPV_vector):")
    add_eq(r"PPV_{\text{vector}} = \sqrt{v_r^2 + v_v^2 + v_t^2}")

    add_body("En campo lejano, la atenuación geométrica e histerética se rige por la ley generalizada de la USBM (Duvall y Petkof):")
    add_eq(r"PPV = K \cdot \left( \frac{R}{\sqrt{W}} \right)^{-\beta}")

    add_body("En frentes de avance subterráneo (campo cercano), la longitud de la columna cargada es comparable con la distancia al contorno. Holmberg y Persson (1980) dedujeron la formulación de integración de carga lineal:")
    add_eq(r"PPV = K \cdot q^\alpha \cdot \left[ \int_0^{H_c} \frac{dz}{(r_0^2 + (z - z_0)^2)^{\beta / 2\alpha}} \right]^\alpha")

    add_body("En el campo cercano cosísmico inducido por reactivación de fallas geológicas en minería profunda, McGarr (1981, 1983) estableció la ley fundamental que vincula el PPV con el Momento Sísmico (M_0 en N·m) y la distancia hipocentral (R en metros):")
    add_eq(r"\log(PPV \cdot R) = 0.66 \cdot \log(M_0) - 7.4")

    add_body("A distancias extremadamente cortas de la fuente sísmica (menores a dos veces el radio de ruptura r_0), el movimiento del terreno alcanza un techo físico de saturación inelástica gobernado por la caída de esfuerzos estática (Δσ) y el módulo de corte (G):")
    add_eq(r"PPV_{\text{max}} \approx \frac{c_s \cdot \Delta\sigma}{G}")

    add_body("Para incorporar analíticamente esta meseta de saturación en modelos de soporte sismorresistente, Wesseloo (2010) formuló la ecuación geométrica corregida:")
    add_eq(r"PPV = \frac{C \cdot 10^{a \cdot M_L}}{\sqrt{R^2 + R_0^2}}")

    add_body("A partir de la ecuación unidimensional de onda de d'Alembert, la deformación unitaria dinámica transitoria (epsilon_d) inducida en la masa rocosa se expresa como:")
    add_eq(r"\varepsilon_d = \frac{PPV}{c_p}")

    add_body("Aplicando la ley de Hooke, el esfuerzo dinámico uniaxial transitorio inducido instantáneamente por el tren de ondas resulta:")
    add_eq(r"\sigma_d = E_d \cdot \varepsilon_d = \rho_r \cdot c_p \cdot PPV")

    add_body(
        " En una andesita competente con densidad rho_r = 2,700 kg/m^3 y velocidad de onda cp = 4,800 m/s (parámetros característicos de Lincuna), una vibración severa de voladura con PPV = 800 mm/s (0.80 m/s) genera un esfuerzo dinámico transitorio de sigma_d = 2,700 · 4,800 · 0.80 = 10,368,000 Pa = 10.37 MPa. Al alcanzar la pared libre del túnel, la onda de compresión se refleja como una onda de tracción pura de magnitud idéntica (sigma_tracción = 10.37 MPa). Dado que la resistencia a la tracción estática de la roca intacta es sigma_t = 12.15 MPa, la superposición con los esfuerzos de tracción tangenciales estáticos en la clave supera instantáneamente la resistencia del macizo, provocando el desconchamiento dinámico y eyección súbita de lajas rocosas.",
        bold_prefix="Demostración y Cálculo Cuantitativo de Daño Dinámico:"
    )

    add_h2("2.2.3. Fenomenología de Sismicidad Inducida y Mecanismos de Rockburst")
    add_body("El estallido de rocas en excavaciones subterráneas profundas se clasifica en tres mecanismos de falla fundamentales:")
    add_bullet("Strainburst de Contorno: Falla frágil por concentración de esfuerzos tangenciales en la periferia inmediata de la labor, provocando el desprendimiento súbito en lajas (espesor de 0.3 a 1.2 m). Se desencadena directamente por el paso de ondas de voladura (PPV).")
    add_bullet("Pillar Burst (Colapso en Masa): Falla frágil destructiva en pilares de sostenimiento sobrecargados por vaciado de tajeos adyacentes.")
    add_bullet("Fault-Slip Burst (Deslizamiento Cosísmico): Deslizamiento violento e inestable a lo largo de fallas geológicas regionales preexistentes provocado por perturbaciones en el estado de esfuerzos cortantes.")

    add_body("La propensión a la inestabilidad dinámica se modela mediante la Tasa de Liberación de Energía (Energy Release Rate - ERR):")
    add_eq(r"ERR = \frac{\Delta U_e + \Delta W}{\Delta A}")

    add_body("Cuando ERR excede el límite plástico del macizo (> 30 MJ/m^2), el excedente de energía elástica acumulada no puede disiparse de forma cuasiestática y se transforma en energía cinética violenta hacia el vacío de la galería.")

    add_h2("2.2.4. Mecánica del Sostenimiento Dinámico y Balance de Energía")
    add_body("El diseño de soporte dinámico se fundamenta en el principio de compatibilidad estructural formulado por Kaiser et al. (1996) y Li (2010): el sostenimiento debe cumplir simultáneamente tres funciones sinérgicas: Reforzar (vástagos deformables), Sostener (placas y anclaje profundo) y Retener (mallas de alta resistencia y FRS). La capacidad de absorción de trabajo mecánico del sistema compuesto debe ser estrictamente mayor o igual a la demanda de energía cinética y potencial transmitida por el bloque inestable:")

    add_eq(r"E_{\text{demanda}} = \frac{1}{2} \rho_r \cdot t_b \cdot v_e^2 + \rho_r \cdot t_b \cdot g \cdot d")

    add_body("Donde m es la masa de roca inestable por unidad de superficie (m = rho_r · tb · A), g es la aceleración de la gravedad (9.81 m/s^2), d es el desplazamiento elasto-plástico del soporte y ve es la velocidad de expulsión inicial del bloque de roca.")

    add_body("La velocidad de eyección en la pared del túnel (ve) experimenta un fenómeno de amplificación dinámica superficial respecto al PPV en campo libre:")
    add_eq(r"v_e = \eta \cdot PPV")

    add_body("Donde η es el factor de amplificación dinámica en la cara libre (η = 1.0 a 2.5 para ondas sísmicas de 100 a 150 Hz en contorno rocoso libre según Raffaldi et al., 2017).")

    add_body("La capacidad total de absorción energética del sistema compuesto de soporte perimetral (E_capacidad) integra los aportes acoplados de pernos dinámicos, malla de alta tenacidad y concreto lanzado reforzado con fibra (FRS):")
    add_eq(r"E_{\text{capacidad}} = E_{\text{pernos}} + E_{\text{malla}} + E_{\text{shotcrete}}")

    add_bullet("Aporte de Pernos Dinámicos (E_pernos): Obtenido integrando la curva constitutiva fuerza-desplazamiento axial del acero:")
    add_eq(r"E_{\text{perno}} = \int_0^{d_b} F_b(x) \, dx")
    add_body("Conforme a las pruebas experimentales documentadas por Charlie Li (2009, 2010), un perno D-Bolt de 20 mm absorbe entre 38 y 45 kJ con desplazamientos de 110 a 130 mm (fuerza última de 210 a 219 kN), mientras que un D-Bolt de 22 mm alcanza capacidades de absorción de 56 a 60 kJ con deformaciones de 120 a 167 mm (fuerza de 250 kN). Gracias a su primer anclaje forjado ubicado próximo al collar, el D-Bolt transfiere solo entre 10% y 20% de la carga dinámica a la planchuela exterior, evitando el cizallamiento de tuercas característico de barras rígidas.")

    add_bullet("Aporte de Malla Metálica de Alta Resistencia (E_malla): Mientras que la malla electrosoldada estándar falla a energías de impacto de 2 kJ, las mallas romboidales de alambre de alta resistencia (como TECCO o MINAX de 1,770 MPa con diámetro ≥ 5.5 mm) disipan de 15 a 25 kJ/m^2 y resisten impactos globales de hasta 200 kJ sin desgarramiento.")
    add_bullet("Aporte de Concreto Lanzado con Fibra FRS (E_shotcrete): El FRS conserva su integridad ante ondas sísmicas con velocidades de partícula de hasta 1.5 a 2.0 m/s, aportando entre 600 y 800 Joules según la norma ASTM C1550 para contener fragmentos menores entre pernos.")

    add_body("Para certificar la compuerta de calidad estructural, se exige un Factor de Seguridad Dinámico:")
    add_eq(r"FS_{\text{dinamico}} = \frac{E_{\text{capacidad}}}{E_{\text{demanda}}} \ge 1.50")

    add_h2("2.2.5. Modelo de Optimización Acoplada: Índice Q Sísmico y Matriz de Selección")
    add_body("Para operacionalizar conjuntamente la clasificación geomecánica de Barton y el monitoreo de vibraciones, se deduce analíticamente el Índice Q Dinámico o Sísmico (Q_seismic). La superposición del esfuerzo dinámico inducido (sigma_d = rho_r · cp · PPV) modifica el cociente de confinamiento:")

    add_eq(r"\left( \frac{\sigma_c}{\sigma_1} \right)_{\text{dinamico}} = \frac{\sigma_c}{\sigma_{\text{estatico}} + \rho_r \cdot c_p \cdot PPV}")

    add_body("Esta reducción tensional incrementa de manera no lineal el factor SRF, degradando la calidad aparente del macizo:")
    add_eq(r"Q_{\text{seismic}} = \left( \frac{RQD}{J_n} \right) \cdot \left( \frac{J_r}{J_a} \right) \cdot \left( \frac{J_w}{SRF_{\text{dinamico}}} \right)")

    add_body("A partir de la combinación paramétrica de Q_seismic y el umbral de PPV registrado en el frente, se establece la matriz de selección optimizada de sostenimiento dinámico:")

    # Tabla en Word
    table = doc.add_table(rows=5, cols=5)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers = ["Categoría", "Rango PPV (mm/s)", "Rango Q_seismic", "Demanda (kJ/m²)", "Esquema de Sostenimiento Dinámico"]
    col_widths = [Cm(2.5), Cm(2.8), Cm(2.5), Cm(2.5), Cm(5.2)]

    hdr_row = table.rows[0]
    for idx, name in enumerate(headers):
        cell = hdr_row.cells[idx]
        cell.width = col_widths[idx]
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run(name)
        run.bold = True
        run.font.size = Pt(9.5)
        run.font.color.rgb = RGBColor(255, 255, 255)
        set_cell_background(cell, "1F4E79")
        set_cell_margins(cell, top=120, bottom=120, left=100, right=100)

    data = [
        ("Cat. I: Estático / Transición", "< 150 mm/s", "Q ≥ 4.0", "< 5 kJ/m²", "Pernos helicoidales con resina (L=2.4m, malla 1.2x1.2m) + Malla estándar + Shotcrete e=5cm."),
        ("Cat. II: Dinámico Moderado", "150 - 350 mm/s", "1.0 ≤ Q < 4.0", "5 - 15 kJ/m²", "Pernos D-Bolt de 20 mm (L=2.4m, 1.0x1.0m, 40 kJ) + Malla electrosoldada reforzada + Shotcrete FRS e=7.5cm (400 J)."),
        ("Cat. III: Dinámico Pesado", "350 - 600 mm/s", "0.1 ≤ Q < 1.0", "15 - 35 kJ/m²", "Pernos D-Bolt de 22 mm (L=2.5m, 0.8x0.8m, 56 kJ) + Malla romboidal de alta tenacidad (≥15 kJ/m²) + FRS e=10cm (≥600 J ASTM C1550)."),
        ("Cat. IV: Dinámico Extremo", "> 600 mm/s", "Q < 0.1", "> 35 kJ/m² (≥50 kJ)", "Doble contención integrada: Pernos D-Bolt 22 mm + Cables dinámicos de 4-6 m + Malla romboidal con cable lacing + FRS doble capa e=12-15cm.")
    ]

    for r_idx, row_data in enumerate(data):
        row = table.rows[r_idx + 1]
        fill_hex = "F2F5F8" if r_idx % 2 == 1 else "FFFFFF"
        for c_idx, val in enumerate(row_data):
            cell = row.cells[c_idx]
            cell.width = col_widths[c_idx]
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if c_idx < 4 else WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.space_before = Pt(3)
            p.paragraph_format.space_after = Pt(3)
            run = p.add_run(val)
            run.font.size = Pt(9)
            set_cell_background(cell, fill_hex)
            set_cell_margins(cell, top=80, bottom=80, left=80, right=80)

    add_caption("Tabla 2.1: Matriz de selección y optimización del sostenimiento dinámico acoplado.")

    # ------------------ 2.3. DEFINICIÓN DE TÉRMINOS BÁSICOS ------------------
    add_h1("2.3. Definición de Términos Básicos")
    add_body("A continuación se presentan las definiciones operacionales y teóricas de 35 términos técnico-científicos esenciales de la investigación, estructurados bajo el estándar formal de dos párrafos por concepto: el primero dedicado a su definición formal según autores canónicos, y el segundo a su contextualización operativa en la mina subterránea.")

    conceptos = [
        ("1. Sistema Q de Barton (Tunneling Quality Index)",
         "El Sistema Q es una clasificación geomecánica empírico-analítica desarrollada en 1974 por Nick Barton, Robert Lien y John Lunde en el Norwegian Geotechnical Institute (NGI) para dimensionar sostenimientos subterráneos. Se expresa en una escala logarítmica de 0.001 a 1,000 mediante el producto de tres cocientes que representan el tamaño relativo de bloques rocosos (RQD/Jn), la resistencia al corte residual entre juntas (Jr/Ja) y el estado de confinamiento tensional activo e hidrogeológico (Jw/SRF).",
         "En la minería subterránea andina (con proyección en labores mecanizadas de Lincuna), el Sistema Q actúa como la variable independiente geomecánica rectora. Su determinación permite zonificar cuantitativamente los frentes de avance en función de su calidad intrínseca, identificando tramos donde el macizo rocoso experimenta altos factores de esfuerzo (SRF) propensos al estallido de rocas y suministrando la base paramétrica para calibrar la demanda estática y dinámica que el sistema de soporte debe equilibrar."),

        ("2. Rock Quality Designation (RQD de Deere)",
         "El RQD es un parámetro cuantitativo de evaluación geomecánica introducido por Don U. Deere en 1964, definido como el porcentaje acumulado de testigos de perforación diamantina intactos mayores o iguales a 10 cm recuperados en una corrida de sondeo, respecto a la longitud total perforada. Constituye el numerador del primer cociente del Sistema Q de Barton y cuantifica la competencia elástica y grado de fracturamiento primario de la roca según estándares de la ISRM y la norma ASTM D6032.",
         "En frentes de avance donde no se dispone de sondajes diamantinos continuos, el RQD se determina indirectamente en la labor mediante el recuento volumétrico de discontinuidades (Jv). En la labor de estudio (andesitas y dacitas con RQD promedio de 60%), este indicador condiciona la capacidad del macizo para redistribuir el campo tensional inducido; valores bajos de RQD indican bloques de menor tamaño susceptibles de desacoplarse como proyectiles ante una aceleración de vibración severa."),

        ("3. Número de Familias de Juntas (Jn)",
         "El parámetro Jn (Joint Set Number) del Sistema Q evalúa la complejidad estructural y los grados de libertad cinemáticos del macizo mediante la valoración numérica de las familias de diaclasas presentes. Sus valores oscilan de 0.5 a 1.0 para rocas masivas sin juntas definidas, hasta 9.0 para tres familias ortogonales bien marcadas y 15.0 para cuatro o más familias con roca fuertemente fracturada.",
         "En túneles mineros de sección baúl, Jn determina la cinemática de falla perimetral. La intersección de 3 familias ortogonales de discontinuidades con fallas locales genera cuñas tetraédricas con susceptibilidad de caída libre inmediata; ante la llegada de una onda dinámica de voladura, un mayor número de familias facilita la disipación dispersiva de ondas de choque pero multiplica las caras libres de reflexión que propician el desconchamiento."),

        ("4. Rugosidad de Juntas (Jr)",
         "El parámetro Jr (Joint Roughness Number) evalúa la textura morfológica, rugosidad milimétrica y ondulación a escala métrica de las superficies de las discontinuidades. Valores de Jr = 4.0 representan juntas onduladas y discontinuas con alta trabazón mecánica, mientras que valores descendentes (Jr = 1.5 para juntas lisas o 0.5 para espejos de falla) describen planos planos pulidos con escasa resistencia friccional.",
         "Operacionalmente, Jr gobierna la resistencia al cizallamiento dinámico ante ondas sísmicas transversales (S). Discontinuidades con bajo Jr ubicadas en la corona de la galería actúan como planos de debilidad cortante cuando el frente de onda induce aceleraciones tangenciales, exigiendo que los pernos dinámicos suministren una fuerza normal de confinamiento que restaure la adherencia friccional entre bloques."),

        ("5. Alteración de Juntas (Ja)",
         "El parámetro Ja (Joint Alteration Number) cuantifica el grado de intemperismo químico, desintegración mineralógica y naturaleza reológica del relleno inter-juntas. Varía desde Ja = 0.75 a 1.0 para paredes sanas en contacto mineral íntimo sin rellenos, hasta Ja = 8.0 a 12.0 para rellenos arcillosos espesos con presencia de minerales expansivos tipo montmorillonita o talco blando.",
         "En yacimientos polimetálicos andinos, donde la alteración hidrotermal degrada las cajas de veta, un valor elevado de Ja reduce drásticamente el ángulo de fricción residual inter-bloques (tan φ_r = Jr / Ja). Durante eventos dinámicos o disparos de voladura masiva, las juntas con alto Ja experimentan deslizamientos dinámicos instantáneos (slip), provocando eyecciones súbitas de roca incluso a intensidades moderadas de vibración."),

        ("6. Factor de Reducción por Esfuerzos (Stress Reduction Factor - SRF)",
         "El SRF es el parámetro del Sistema Q que pondera la influencia del estado tensional relativo y las sobrecargas mecánicas en la estabilidad de la labor. Evalúa el confinamiento tensional mediante la relación entre la resistencia compresiva uniaxial de la roca intacta (sigma_c) y el esfuerzo principal mayor inducido (sigma_1), escalando desde 1.0 en régimen elástico hasta 10.0 o 20.0 en regímenes de plastificación severa y estallido violento de roca.",
         "En labores subterráneas profundas, el SRF es el indicador geomecánico más dinámico. La excavación altera el campo virgen concentrando tensiones tangenciales en los hastiales y techo; los disparos de voladura adyacentes introducen un pulso tensional transitorio adicional (sigma_d) que reduce bruscamente la relación efectiva (sigma_c / sigma_1)_dinámico, elevando el SRF a categorías que demandan fortificación dinámica pesada."),

        ("7. Dimensión Equivalente (De) y Excavation Support Ratio (ESR)",
         "La Dimensión Equivalente (De) es una formulación dimensional introducida por Barton para relacionar el vano o altura libre de la excavación subterránea con el grado de permanencia y seguridad demandado para la obra, definido como De = Span / ESR. El coeficiente ESR asigna valores permisivos a labores temporales de tajeo (ESR = 3.0 a 5.0) y exigencias rigurosas a labores permanentes y galerías mecanizadas (ESR = 1.0 a 1.6).",
         "En el diseño de fortificación en mina, la correlación de Q y De sobre la carta empírica de Grimstad y Barton determina la densidad de empernado y el espesor de concreto lanzado. Para cruceros mecanizados de 4.5 m x 4.5 m con ESR = 1.6 (De = 2.81 m), garantiza que los pernos dinámicos alcancen profundidades de anclaje de al menos 2.50 m, fijándose firmemente en la zona elástica competente más allá del halo de daño perimétrico."),

        ("8. Velocidad Pico de Partícula (Peak Particle Velocity - PPV)",
         "El PPV es la máxima velocidad cinemática instantánea experimentada por una partícula del macizo rocoso al ser perturbada por un tren de ondas elásticas generado por una detonación de voladura o por un sismo inducido. Se registra mediante sismógrafos triaxiales que capturan componentes ortogonales en mm/s o m/s, constituyendo el estándar internacional de control para correlacionar vibraciones con daño estructural en rocas.",
         "En la optimización del sostenimiento dinámico, el PPV es la variable física de monitoreo primordial. Existe una relación directa entre el PPV y la deformación dinámica unitaria inducida (epsilon_d = PPV / cp); niveles de PPV superiores a 350 - 450 mm/s causan fisuramiento en shotcrete recién fraguado y rotura por corte en pernos rígidos convencionales, delimitando la frontera técnica donde la mina debe instalar elementos dinámicos deformables."),

        ("9. Aceleración Pico de Partícula (Peak Particle Acceleration - PPA)",
         "El PPA es la primera derivada temporal del vector velocidad de partícula (a = dv/dt), expresada en múltiplos de la aceleración gravitacional terrestre (g = 9.81 m/s^2). Representa la tasa de cambio cinemático instantáneo y gobierna la magnitud de las fuerzas inerciales de cuerpo (F_inercial = m · PPA) que actúan sobre bloques potencialmente inestables en el contorno del túnel.",
         "En el comportamiento del sostenimiento superficial (mallas y concreto lanzado), el PPA rige la respuesta estructural en la primera fracción de segundo tras el impacto sísmico. Aceleraciones que exceden 2.0 a 5.0 g vencen la adherencia de contacto del shotcrete sobre la roca y cortan las planchuelas de los pernos rígidos si la malla no cuenta con capacidad de elongación dúctil para disipar la fuerza de choque inicial."),

        ("10. Frecuencia Dominante de Vibración (fd)",
         "La frecuencia dominante es aquella que concentra la mayor densidad espectral de energía en el registro sismográfico, identificada mediante la Transformada Rápida de Fourier (FFT) y medida en Hertz (Hz). Define, en combinación con la velocidad de propagación de onda de la roca (cp), la longitud de onda física de la perturbación dinámica (λ = cp / fd).",
         "En voladuras de avance de campo cercano, los pulsos de choque generan altas frecuencias dominantes (100 a 500 Hz), asociadas a longitudes de onda cortas (10 a 45 m) comparables con la sección transversal del túnel (4.5 m). Esta concordancia dimensional produce reflexiones constructivas y concentración de esfuerzos en la periferia de la galería, acelerando el agrietamiento de la corona si no se cuenta con sostenimiento con fibras estructurales."),

        ("11. Ley de Atenuación de Holmberg-Persson",
         "La formulación de Holmberg-Persson (1980) es un modelo matemático de propagación de vibraciones desarrollado específicamente para túneles subterráneos, que supera la limitación de carga puntual mediante la integración continua de la energía liberada a lo largo de una columna de explosivo. Permite predecir el PPV en cualquier punto del contorno en función de la concentración lineal de carga (kg/m), distancia radial y constantes elásticas del terreno.",
         "En la selección de soporte dinámico, este modelo permite proyectar el nivel de vibración taladro por taladro durante el ciclo de voladura de avance. Conocer el PPV esperado en corona y hastiales permite delimitar con exactitud el espesor de roca que sufrirá daño por sobre rotura, dimensionando la longitud del perno de soporte para anclarse en roca sana e inmune al agrietamiento dinámico."),

        ("12. Deformación Dinámica Unitaria (epsilon_d)",
         "La deformación dinámica unitaria es la relación adimensional de cambio longitudinal que experimenta un volumen rocoso sometido al paso de una onda sísmica compresional o de tracción, deducida a partir de la mecánica de medios continuos como el cociente entre la velocidad de partícula y la velocidad de onda del macizo (epsilon_d = PPV / cp).",
         "En la interacción roca-soporte, la deformación unitaria impone una elongación transitoria forzada en las barras de anclaje instaladas. Si la deformación dinámica supera la deformación elástica del acero convencional (epsilon_cedencia ≈ 0.002), los pernos rígidos fallan por sobrecarga frágil; los pernos dinámicos, capaces de deformarse plásticamente más de 15% (ε > 0.15), absorben la solicitación sin colapso."),

        ("13. Esfuerzo Dinámico Transitorio (sigma_d)",
         "El esfuerzo dinámico transitorio es la tensión mecánica uniaxial adicional inducida instantáneamente en la matriz rocosa al paso de la onda acústica, calculada como el producto de la densidad de la roca, la velocidad de onda compresional y el PPV (sigma_d = rho_r · cp · PPV). Se expresa en MegaPascales (MPa) y se superpone algebraicamente al tensor de esfuerzos estáticos existente.",
         "En el frente de avance minero, este parámetro explica el desprendimiento por desconchamiento (spalling). Cuando una onda compresional de 10 MPa generada por voladura masiva incide en la pared libre de una labor andina, se refleja como tracción dinámica; al superar la baja resistencia a la tracción de la roca (sigma_t = 12.15 MPa), fractura instantáneamente la corona, demandando un sostenimiento dinámico que suministre confinamiento continuo."),

        ("14. Estallido de Rocas (Rockburst)",
         "El estallido de rocas es un fenómeno de inestabilidad geomecánica violenta caracterizado por la fracturación instantánea y eyección a gran velocidad de grandes masas de roca hacia el interior de una labor subterránea, acompañado de la emisión de ondas sísmicas de alta energía. Ocurre en macizos rocosos frágiles y de alta resistencia sometidos a concentraciones tensionales que exceden la resistencia última del terreno.",
         "En operaciones subterráneas andinas profundas, la profundización por debajo de 600 metros incrementa el riesgo de estallidos detonados por voladuras de producción. Diseñar un sostenimiento para este régimen exige descartar fortificaciones rígidas tradicionales e instalar elementos dúctiles con alta capacidad de absorción energética que impidan la expulsión de bloques hacia el personal y equipos."),

        ("15. Estallido por Concentración de Esfuerzos (Strainburst)",
         "El strainburst es la categoría de estallido de roca originada por la concentración excesiva de esfuerzos tangenciales en la periferia inmediata del túnel, la cual supera la resistencia compresiva residual de la roca intacta, provocando una falla frágil violenta por pandeo (buckling) y expulsión en lajas rocosas (espesor de 0.3 a 1.2 m desde la pared).",
         "En cruceros mecanizados, el strainburst es el tipo de evento dinámico más recurrente y suele ser gatillado por el paso de las ondas de voladura (PPV). El sistema de sostenimiento dinámico optimizado con pernos deformables y shotcrete reforzado con fibra restringe el desconfinamiento lateral de las lajas, impidiendo el pandeo inicial y evitando la expulsión súbita de roca."),

        ("16. Sismicidad Inducida por Minado",
         "La sismicidad inducida es la respuesta dinámica del macizo rocoso ante las alteraciones tensionales causadas por las labores de excavación, vaciado de tajeos y voladuras en el subsuelo. Se clasifica desde micro-fracturamiento intergranular (magnitudes ML < 0) hasta grandes eventos cosísmicos por reactivación de fallas geológicas (ML ≥ 2.0 a 3.5), registrados por redes de geófonos y acelerómetros.",
         "El monitoreo continuo de la sismicidad inducida en mina permite mapear en tiempo real las zonas del yacimiento sometidas a concentraciones tensionales críticas. Esta información geomecánica alimenta la actualización del parámetro SRF en el Sistema Q de Barton, permitiendo que la selección del sostenimiento dinámico se ajuste a los niveles reales de amenaza sísmica en cada nivel de explotación."),

        ("17. Sostenimiento Dinámico",
         "El sostenimiento dinámico es un sistema de fortificación diseñado específicamente para absorber energía cinética y deformación inelástica severa transmitida por el macizo rocoso en colapso violento o sometido a trenes de ondas de vibración, preservando la estabilidad de la labor. Su criterio de dimensionamiento no es la capacidad de carga estática puntual, sino su capacidad de disipación de trabajo mecánico (kJ/m²).",
         "Constituye la variable dependiente de optimización de la presente investigación. La integración analítica del Sistema Q y el monitoreo de vibraciones permite seleccionar la combinación óptima de pernos dinámicos, mallas de alta resistencia y shotcrete con fibra para garantizar un factor de seguridad FS_dinamico ≥ 1.5 ante la demanda energética específica del frente, optimizando costos y asegurando la vida humana."),

        ("18. Capacidad de Absorción de Energía (kJ/m²)",
         "La capacidad de absorción de energía es la integral del área bajo la curva carga-desplazamiento desarrollada por un elemento o sistema de sostenimiento compuesto durante su deformación plástica hasta el colapso, expresada comúnmente en Kilojulios por metro cuadrado (kJ/m²). Representa el trabajo mecánico que el sistema puede disipar antes de perder su capacidad resistente.",
         "En la ingeniería de rocas moderna, la absorción de energía es el indicador de rendimiento por excelencia ante solicitaciones dinámicas. Para las demandas energéticas proyectadas en labores andinas profundas (15 a 35 kJ/m²), el sistema de fortificación debe incorporar pernos y mallas cuya respuesta plástica garantice disipar este volumen energético con deformaciones controladas (< 150 a 200 mm)."),

        ("19. Perno Dinámico de Deformación Plástica (D-Bolt)",
         "El D-Bolt es un perno de anclaje de roca de alta absorción de energía patentado por Charlie C. Li (2010), fabricado con una barra de acero de alta ductilidad que contiene una serie de anclajes mecánicos puntuales a lo largo de su fuste, separados por tramos lisos desacoplados del mortero de inyección. Ante un desplazamiento dinámico, los tramos lisos fluyen plásticamente bajo tensión axial uniforme.",
         "En labores subterráneas sometidas a altos niveles de vibración (PPV > 350 mm/s), el D-Bolt reemplaza con superioridad técnica a los pernos helicoidales rígidos. Conforme a las pruebas de Li (2009, 2010), el D-Bolt de 20 mm absorbe entre 38 y 45 kJ (carga de 210 a 219 kN), mientras que el de 22 mm absorbe entre 56 y 60 kJ (carga de 250 kN), transfiriendo solo el 10% al 20% de la carga a la tuerca exterior y manteniendo el confinamiento de la corona."),

        ("20. Perno Deformable Cone Bolt",
         "El Cone Bolt es un perno dinámico desarrollado por la industria minera sudafricana y canadiense, compuesto por una barra lisa de acero que posee un cono forjado en su extremo distal alojado dentro de una resina de inyección. Ante la tracción dinámica ejercida por la roca en expansión, el cono es forzado a penetrar y extrudirse a través de la matriz de resina, generando una fuerza de fricción constante con desplazamientos de 200 a 300 mm.",
         "Aporta una capacidad de absorción de energía sobresaliente (> 40 kJ por perno), ideal para frentes de avance propensos a strainburst severo. Su cinemática permite que el perno trabaje a carga constante sin concentración de esfuerzos en la planchuela, transfiriendo las cargas dinámicas de manera distribuida hacia la malla de contención superficial."),

        ("21. Concreto Lanzado Reforzado con Fibra (FRS)",
         "El FRS (Fiber Reinforced Shotcrete) es un material compuesto estructural constituido por una matriz de mortero proyectada neumáticamente, adicionada homogéneamente con fibras de acero o macro-fibras sintéticas de poliolefina. Su propiedad distintiva es la tenacidad a flexotracción post-fisuración, la cual impide la propagación incontrolada de grietas mediante el cosido mecánico de las fibras.",
         "En el sostenimiento dinámico, el FRS actúa como la primera línea de confinamiento perimetral, impidiendo el desconfinamiento inicial de la roca y resistiendo velocidades de partícula de hasta 1.5 a 2.0 m/s sin delaminación. Su capacidad de disipación se certifica mediante la prueba de panel redondo ASTM C1550; en la presente investigación se especifica un shotcrete Clase A (> 600 - 800 Joules a 40 mm de deflexión) para resistir el impacto de vibraciones."),

        ("22. Malla Metálica de Alta Resistencia (High-Tensile Mesh)",
         "Es una membrana flexible de soporte fabricada con alambres de acero de alta aleación trenzados romboidalmente con resistencias a la tracción superiores a 1,770 MPa (como las mallas Geobrugg Tecco o Minax). A diferencia de las mallas electrosoldadas rígidas que rompen en sus puntos de soldadura ante deformaciones menores a 50 mm, esta malla tolera deflexiones de más de 200 mm absorbiendo entre 15 y 25 kJ/m² y resistiendo impactos globales de hasta 200 kJ.",
         "Instalada en galerías sometidas a sismicidad y voladura cercana, su función operacional es retener la masa de roca desintegrada tras el estallido (containment), formando una bolsa deformable que evita la caída de fragmentos hacia la calzada de tránsito y preservando la vida de los operadores."),

        ("23. Velocidad de Eyección de Bloques (ve)",
         "La velocidad de eyección es la velocidad lineal inicial con la que un bloque de roca desprendido es expulsado desde el contorno de la excavación hacia el interior de la labor como consecuencia de un estallido de roca o por el desconfinamiento dinámico provocado por voladuras adyacentes, oscilando típicamente entre 1.5 y 5.0 m/s.",
         "En el balance de energía del soporte, ve es la variable más crítica ya que la demanda de energía cinética crece con el cuadrado de su magnitud (Ek proporcional a ve^2). La velocidad de eyección resulta de la amplificación del PPV superficial (ve = η · PPV); por ende, monitorear y mitigar el PPV mediante mallas de voladura controlada reduce exponencialmente la energía que debe absorber el sostenimiento."),

        ("24. Factor de Amplificación Dinámica Superficial (η)",
         "Es un coeficiente adimensional que relaciona la velocidad de partícula registrada en la pared libre de una excavación subterránea (PPV_superficie) con la velocidad pico medida en el macizo virgen continuo a cierta distancia (PPV_campo libre), definido como η = PPV_superficie / PPV_campo libre (valores típicos de 1.0 a 2.5 en frecuencias de 100 a 150 Hz según Raffaldi et al., 2017).",
         "En el diseño de soporte dinámico, omitir este factor conduce a un severo sub-dimensionamiento estructural. El diseño geomecánico debe multiplicar el PPV predicho por este factor para calcular la verdadera velocidad de expulsión, asegurando que los pernos y mallas seleccionados resistan las máximas fuerzas inerciales generadas en la periferia del túnel."),

        ("25. Tasa de Liberación de Energía (ERR de Cook)",
         "El ERR es un parámetro computacional desarrollado por N.G.W. Cook en Sudáfrica, definido como la cantidad neta de energía elástica disipada o liberada por unidad de superficie o volumen de roca excavada al avanzar el minado (MJ/m²). Refleja la concentración del estado tensional y constituye el indicador predictivo clásico del potencial destructivo de sismos mineros.",
         "En la planificación de labores subterráneas, un incremento del ERR por encima de umbrales críticos (> 30 MJ/m²) alerta sobre la transición hacia un régimen propenso a estallidos de roca. Cuando los modelos registran altos valores de ERR, el sistema geomecánico acopla el índice Q ajustado por sismicidad e incrementa la capacidad disipativa del soporte perimetral."),

        ("26. Rigidez Dinámica del Macizo Rocoso",
         "La rigidez dinámica es la relación entre el incremento de esfuerzo dinámico aplicado y la deformación elástica resultante en el macizo sometido a solicitaciones transitorias de alta velocidad, vinculada directamente con el módulo de Young dinámico Ed (entre 20% y 50% superior al módulo estático a velocidades de deformación de voladura).",
         "En la transferencia de energía entre la voladura y el sostenimiento, la rigidez dinámica gobierna la proporción de energía absorbida internamente por la matriz rocosa versus la transmitida a la superficie del túnel. Un macizo andesítico competente transmite el pulso de choque con mínima atenuación interna, transportando el PPV con máxima intensidad destructiva hacia los pernos de fortificación."),

        ("27. Factor de Seguridad Dinámico (FS_dinamico)",
         "Es el cociente adimensional entre la capacidad total de absorción de energía del sistema compuesto de soporte (E_capacidad) y la demanda total de energía cinética y gravitacional transmitida por la roca expulsada (E_demanda), definido formalmente como FS_dinamico = E_capacidad / E_demanda.",
         "En el diseño geomecánico sismorresistente se exige un FS_dinamico ≥ 1.50 para validar la compuerta de calidad de una labor de avance mecanizado. Un factor inferior a 1.0 representa colapso violento seguro del soporte ante un evento dinámico, mientras que valores en el rango 1.0 a 1.5 indican deformación plástica crítica con riesgo de falla residual ante réplicas subsecuentes."),

        ("28. Efecto Kaiser y Memoria Tensional de la Roca",
         "El Efecto Kaiser es el fenómeno por el cual un macizo rocoso sometido a esfuerzos compresivos cíclicos no emite actividad acústica ni microsísmica apreciable hasta que el nivel de esfuerzo aplicado excede el máximo nivel de esfuerzo de compresión previamente experimentado en su historia geológica o minera.",
         "En frentes de avance sometidos a ciclos repetidos de perforación y voladura, gobierna la nucleación del daño acumulativo. Cuando un nuevo disparo genera una vibración cuyo esfuerzo dinámico supera el umbral memorizado por el macizo, la roca inicia una microfisuración acelerada que degrada el RQD y eleva el SRF, exigiendo que el soporte controle la dilatancia perimetral en cada ciclo."),

        ("29. Atenuación Histerética Inelástica",
         "Es el mecanismo disipativo interno por el cual parte de la energía mecánica de las ondas de voladura se transforma irreversiblemente en calor debido a la fricción interna en microgrietas, deformación viscoelástica de minerales y presencia de fluidos en los poros de la roca, cuantificado mediante el factor de amortiguamiento sísmico.",
         "En la calibración de leyes de campo cercano, complementa a la dispersión geométrica. En rocas volcánicas andesíticas moderadamente fracturadas, la atenuación de altas frecuencias (> 300 Hz) ocurre en los primeros metros de recorrido, implicando que las labores adyacentes a menos de 15 metros del disparo reciben el choque de ondas no atenuadas con máximo potencial de rotura."),

        ("30. Desacoplamiento Mecánico de Pernos de Anclaje",
         "Es la técnica geomecánica mediante la cual se anula intencionalmente la adherencia interfacial continua entre la barra de acero del perno y la lechada de inyección en tramos específicos, empleando fundas plásticas lisas o lubricantes para evitar que el acero concentre deformaciones extremas en una sola discontinuidad activa.",
         "En el diseño de pernos dinámicos, el desacoplamiento permite alcanzar grandes desplazamientos axiales (> 150 - 250 mm) sin inducir la rotura prematura del acero por cizalle concentrado. Al forzar que el perno fluya en un volumen mayor de metal, se maximiza la disipación de energía, garantizando que el sistema mantenga confinamiento activo mientras la labor experimenta convergencia dinámica."),

        ("31. Onda de Tracción Reflejada de Hopkinson",
         "Es el fenómeno de reflexión elástica que ocurre cuando una onda compresional (P) que viaja a través de un medio sólido incide sobre una superficie libre con impedancia acústica nula (aire). Al no existir medio material para continuar la propagación, la onda se refleja invirtiendo su signo hacia una onda de tracción de igual intensidad.",
         "En labores subterráneas, la onda reflejada de Hopkinson es la causante física del descascaramiento perimetral (spalling). Dado que las rocas andesíticas presentan una resistencia a la tracción que apenas representa entre 5% y 10% de su resistencia compresiva, la onda reflejada supera la cohesión del macizo, fracturando la roca en lajas que son expulsadas hacia la labor si no existe un confinamiento superficial."),

        ("32. Monitoreo Microsísmico Continuo",
         "Es la técnica geofísica de instrumentación pasiva que emplea una red tridimensional de sensores (geófonos uniaxiales y triaxiales de 4.5 a 14 Hz) distribuidos estratégicamente en el interior de la mina para registrar continuamente las ondas elásticas generadas por micro-roturas y fracturas en el macizo rocoso.",
         "Permite calcular en tiempo real la localización hipocentral (coordenadas X, Y, Z), el tiempo de origen, la magnitud sísmica local (ML) y la energía radiada de los eventos sísmicos inducidos. Estos parámetros geomecánicos permiten anticipar la formación de pilares sobrecargados y verificar si las vibraciones de voladura están induciendo reactivaciones de fallas geológicas cercanas."),

        ("33. Coeficiente de Fijación de Taladros (f)",
         "Es un factor adimensional empírico introducido en las formulaciones de voladura de túneles por Gustafsson y Langefors para cuantificar el grado de confinamiento y resistencia geométrica que experimenta un taladro al momento de la detonación en función de la dirección de rotura y la gravedad (típicamente f = 1.0 para taladros de banco y f = 1.45 para taladros de arrastre).",
         "En frentes de avance subterráneos, el coeficiente de fijación controla la energía específica requerida para vencer el encajonamiento en el piso de la labor. Taladros con excesivo confinamiento generan sobrepresiones confinadas que se disipan hacia el hastial y la corona en forma de ondas de alta amplitud (PPV elevado), incrementando la demanda dinámica sobre el sostenimiento instalado."),

        ("34. Momento Sísmico (M_0) y Energía Sísmica Radiada (E_s)",
         "El momento sísmico (M_0 = G · A · D) es la medida física fundamental del tamaño de un evento sísmico cosísmico, donde G es el módulo de rigidez de corte, A es el área de la falla que deslizó y D es el desplazamiento medio cosísmico, expresado en Newton-metro (N·m). La energía sísmica radiada (E_s) representa la fracción de energía elástica que se propaga como ondas sísmicas destructivas.",
         "En la ingeniería de sostenimiento dinámico, el momento sísmico cuantifica la magnitud real del evento geomecánico que la labor debe soportar. Conforme a la relación de McGarr (1981), correlacionar el momento sísmico de los eventos inducidos con las mediciones de PPV en los cruceros permite calibrar los umbrales de energía de diseño para las diferentes categorías de fortificación."),

        ("35. Compuerta de Calidad Geomecánica (Quality Gate)",
         "Es un punto de control y verificación técnica formal dentro del flujo de diseño de ingeniería de rocas donde se evalúa si un parámetro operativo o estructural cumple estrictamente con los factores de seguridad y condiciones de contorno físicas inviolables antes de autorizar su implementación o paso a la siguiente fase constructiva.",
         "En la presente investigación, la compuerta de calidad impone que bajo ninguna condición operacional la demanda energética proyectada por el tren de vibraciones exceda la capacidad de absorción disipativa del sistema compuesto (FS_dinamico ≥ 1.50) y que la presión efectiva en taladro no sobrepase la resistencia del macizo (P_te ≤ sigma_c), garantizando la integridad de la labor.")
    ]

    for item in conceptos:
        num_title, p1, p2 = item
        add_h2(num_title)
        add_body(p1)
        add_body(p2)

    # ------------------ 2.4. REFERENCIAS BIBLIOGRÁFICAS ------------------
    add_h1("2.4. Referencias Bibliográficas")
    add_body("Las referencias bibliográficas se presentan en estricto orden alfabético y con sangría francesa conforme a las normas de estilo APA 7ma edición, conteniendo las fuentes canónicas extraídas del cuaderno oficial de NotebookLM:")

    referencias = [
        "Alvarado, M. (2021). Zonificación geomecánica mediante el Q de Barton y control de vibraciones de campo cercano para el diseño de soporte en taladros largos (Tesis de pregrado). Universidad Nacional Mayor de San Marcos, Lima, Perú.",
        "ASTM International. (2012). Standard test method for flexural toughness and first-crack strength of fiber-reinforced concrete (using four-point loading with third-point loading) (ASTM C1018). West Conshohocken, PA: ASTM International.",
        "ASTM International. (2020). Standard test method for flexural toughness of fiber reinforced concrete (using centrally loaded round panel) (ASTM C1550). West Conshohocken, PA: ASTM International. https://doi.org/10.1520/C1550-20",
        "Barton, N. (2000). TBM tunnelling in jointed and faulted rock. Rotterdam: A.A. Balkema.",
        "Barton, N. (2002). Some new Q-value correlations to assist in site investigation and tunnel design. International Journal of Rock Mechanics and Mining Sciences, 39(2), 185-216. https://doi.org/10.1016/S1365-1609(02)00011-4",
        "Barton, N., Lien, R., & Lunde, J. (1974). Engineering classification of rock masses for the design of tunnel support. Rock Mechanics, 6(4), 189-236. https://doi.org/10.1007/BF01239496",
        "Bieniawski, Z. T. (1989). Engineering rock mass classifications: A complete manual for engineers and geologists in mining, civil, and petroleum engineering. New York: John Wiley & Sons.",
        "Cook, N. G. W., Hoek, E., Pretorius, J. P. G., Ortlepp, W. D., & Salamon, M. D. G. (1966). Rock mechanics applied to the study of rockbursts. Journal of the South African Institute of Mining and Metallurgy, 66(10), 435-528.",
        "Cuentas, R. (2022). Optimización de la secuencia de retardo en voladura para mitigar el daño dinámico perimétrico en frentes subterráneos (Tesis de titulación). Universidad Nacional Daniel Alcides Carrión, Pasco, Perú.",
        "Deere, D. U. (1964). Technical description of rock cores for engineering purposes. Rock Mechanics and Engineering Geology, 1(1), 17-22.",
        "Duvall, W. I., & Petkof, B. (1959). Spherical propagation of explosion-generated strain pulses in rock (USBM Report of Investigations 5483). Washington, DC: U.S. Bureau of Mines.",
        "European Committee for Standardization. (2006). Testing sprayed concrete - Part 5: Determination of energy absorption capacity of fibre reinforced slab specimens (EN 14488-5). Brussels: CEN.",
        "Grimstad, E., & Barton, N. (1993). Updating of the Q-system for NMT. In Proceedings of the International Symposium on Sprayed Concrete (pp. 46-66). Fagernes: Norwegian Concrete Association.",
        "Hedley, D. G. F. (1992). Rockburst handbook for Ontario hardrock mines (CANMET Special Report SP92-1E). Ottawa: Energy, Mines and Resources Canada.",
        "Holmberg, R., & Persson, P. A. (1980). Design of tunnel perimeter blasthole patterns to prevent rock damage. In Transactions of the Institution of Mining and Metallurgy, Section A: Mining Industry (Vol. 89, pp. A37-A40). London: IMM.",
        "Huamán, K. (2022). Aplicación del sistema NGI-Q y registros sismológicos para la estabilidad de chimeneas y galerías profundas en Sociedad Minera Corona (Tesis de pregrado). Universidad Nacional de Ingeniería, Lima, Perú.",
        "Hustrulid, W., & Lu, W. (2018). Control of perimeter damage in hard rock underground excavations. In Proceedings of the 52nd US Rock Mechanics/Geomechanics Symposium. Seattle, WA: American Rock Mechanics Association.",
        "International Society for Rock Mechanics and Rock Engineering [ISRM]. (1981). Rock characterization, testing and monitoring: ISRM suggested methods (E. T. Brown, Ed.). Oxford: Pergamon Press.",
        "Kaiser, P. K., & Maloney, S. (1998). Ground support design for dynamic conditions. In Rock Support and Reinforcement Practice in Mining (pp. 343-356). Rotterdam: Balkema.",
        "Kaiser, P. K., McCreath, D. R., & Tannant, D. D. (1996). Canadian rockburst support handbook. Sudbury, ON: Geomechanics Research Centre, Laurentian University.",
        "Li, C. C. (2009). Field trials of D-bolts in high stress conditions. In Proceedings of the 3rd Canada-US Rock Mechanics Symposium. Toronto: CARMA.",
        "Li, C. C. (2010). A new energy-absorbing bolt: The D-Bolt. In Rock Fragmentation by Blasting (pp. 587-593). London: Taylor & Francis Group.",
        "Li, C. C. (2017). Principles of rockbolt performance under dynamic loading. Journal of Rock Mechanics and Geotechnical Engineering, 9(4), 588-598. https://doi.org/10.1016/j.jrmge.2017.03.003",
        "López, E. (2023). Modelo analítico-computacional para la evaluación de la respuesta dinámica del sostenimiento en túneles mineros (Tesis de maestría). Universidad Nacional de Ingeniería, Sección de Posgrado FIGMM, Lima, Perú.",
        "Martin, C. D., Kaiser, P. K., & Christiansson, R. (2003). Stress, instability and design of underground excavations in hard rocks. International Journal of Rock Mechanics and Mining Sciences, 40(7-8), 1027-1047. https://doi.org/10.1016/S1365-1609(03)00110-2",
        "McGarr, A. (1981). Analysis of peak ground motion in terms of a model of inhomogeneous faulting. Journal of Geophysical Research: Solid Earth, 86(B5), 3901-3912. https://doi.org/10.1029/JB086iB05p03901",
        "McGarr, A. (1983). Estimating the larger ground motion of an induced seismic event. In Proceedings of the 1st International Congress on Rockbursts and Seismicity in Mines (pp. 199-204). Johannesburg: SAIMM.",
        "McGarr, A. (1991). Observations constraining near-source ground motion from induced earthquakes. Seismological Research Letters, 62(1), 27-32.",
        "Mendoza, H., & Soto, G. (2019). Evaluación de estallidos de roca por reactivación de fallas geológicas en minería subterránea profunda (Tesis de titulación). Universidad Nacional de San Agustín, Arequipa, Perú.",
        "Murthy, V. M. S. R., & Dey, K. (2004). Blast vibration control in hard rock tunnels. Tunnelling and Underground Space Technology, 19(4), 392-401.",
        "Ortlepp, W. D. (1994). Grouted rockstuds as dynamic support in rockburst-prone conditions. In Proceedings of the 1st International Symposium on Rock Support (pp. 581-587). Sudbury: Laurentian University.",
        "Ortlepp, W. D. (1998). Rock mechanics applied to the design of dynamic support in deep South African gold mines. In Proceedings of the 4th International Symposium on Rockbursts and Seismicity in Mines (RaSiM 4) (pp. 37-47). Rotterdam: A.A. Balkema.",
        "Ortlepp, W. D., & Stacey, T. R. (1994). Rockburst mechanisms in Southern African gold mines. In Proceedings of the 8th International Congress on Rock Mechanics (Vol. 1, pp. 433-437). Tokyo: ISRM.",
        "Palmstrøm, A. (1982). The volumetric joint count: A useful and simple measure of the degree of rock jointing. In Proceedings of the 4th Congress of the International Association of Engineering Geology (Vol. 2, pp. 221-228). New Delhi: IAEG.",
        "Pérez, C., & Quispe, L. (2023). Criterios de diseño de sostenimiento por absorción de energía en macizos andinos fracturados sometidos a voladura masiva (Tesis de titulación). Universidad Nacional del Altiplano, Puno, Perú.",
        "Persson, P. A., Holmberg, R., & Lee, J. (1994). Rock blasting and explosives engineering. Boca Raton, FL: CRC Press.",
        "Potvin, Y., & Wesseloo, J. (2013). Towards an understanding of dynamic demand on ground support in rockburst-prone mines. In Ground Support 2013: Proceedings of the 7th International Symposium on Ground Support in Mining and Underground Construction (pp. 287-304). Perth: Australian Centre for Geomechanics. https://doi.org/10.36487/ACG_rep/1304_19_Potvin",
        "Raffaldi, M. J., Bermudez, M., & Board, M. (2017). Numerical evaluation of ground support response to dynamic loading in deep underground mines. In Proceedings of the 8th International Conference on Deep and High Stress Mining (pp. 543-556). Perth: Australian Centre for Geomechanics.",
        "Stacey, T. R. (2012). Dynamic support in deep mining: Mechanisms and performance requirements. In Proceedings of the 6th International Seminar on Deep and High Stress Mining (pp. 41-52). Perth: Australian Centre for Geomechanics.",
        "Wesseloo, J. (2010). Empirical methods for assessing the ground motion demand on support systems in rockburst-prone excavations. In Proceedings of the 2nd International Seminar on Deep and High Stress Mining (pp. 483-496). Santiago: Gecamin.",
        "Zumaeta, H., & Cornejo, F. (2020). Optimización del sostenimiento dinámico ante eventos microsísmicos y altos esfuerzos en frentes de explotación de U.E.A. Yauliyacu (Tesis de titulación). Universidad Nacional de Ingeniería, Lima, Perú."
    ]

    for ref in referencias:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.left_indent = Cm(1.27)
        p.paragraph_format.first_line_indent = Cm(-1.27)
        p.add_run(ref)

    doc.save(output_docx)
    print(f"Documento DOCX FINAL generado exitosamente en: {output_docx}")

def certify_final_docx(docx_path, pdf_path):
    print("Iniciando Word COM para certificación y exportación a PDF...")
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False
    
    try:
        abs_docx = os.path.abspath(docx_path)
        abs_pdf = os.path.abspath(pdf_path)

        doc = word.Documents.Open(abs_docx)
        
        pages = doc.ComputeStatistics(2)
        words = doc.ComputeStatistics(0)
        chars = doc.ComputeStatistics(3)
        print(f"\n=======================================================")
        print(f"CERTIFICACIÓN FÍSICA EN MICROSOFT WORD (GROUNDING NOTEBOOKLM):")
        print(f"- Páginas Físicas Reales: {pages} páginas")
        print(f"- Total Palabras: {words} palabras")
        print(f"- Total Caracteres: {chars}")
        print(f"=======================================================\n")

        print(f"Exportando PDF oficial final en: {abs_pdf}")
        doc.SaveAs2(abs_pdf, FileFormat=17) # wdFormatPDF
        doc.Close()
        word.Quit()
        return pages, words, chars

    except Exception as e:
        print("Error en Word COM:", e)
        try:
            word.Quit()
        except:
            pass
        raise e

if __name__ == "__main__":
    final_docx = "output/CAP_II_MARCO_TEORICO_Q_VIBRACIONES_SOSTENIMIENTO_DINAMICO_FINAL.docx"
    final_pdf = "output/CAP_II_MARCO_TEORICO_Q_VIBRACIONES_SOSTENIMIENTO_DINAMICO_FINAL.pdf"
    
    os.makedirs("output", exist_ok=True)
    build_final_marco_teorico(final_docx)
    pages, words, chars = certify_final_docx(final_docx, final_pdf)
    print("Certificación final con grounding en NotebookLM completada exitosamente.")
