# -*- coding: utf-8 -*-
"""
PLAN DE TESIS OFICIAL UNI FIGMM - PARTE 4: MATRIZ, CRONOGRAMA, PRESUPUESTO, BIBLIOGRAFÍA Y ANEXOS
Estructura según PLAN DE TESIS (1).docx:
- MATRIZ DE CONSISTENCIA
- CRONOGRAMA DEL TRABAJO (16 semanas / 4 meses)
- PRESUPUESTO Y FINANCIAMIENTO DEL PROYECTO
- BIBLIOGRAFIA (APA 7ma edición)
- ANEXOS (Anexos 1 al 6)
"""

import numpy as np
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, Image, PageBreak, HRFlowable

def append_plan_part4(story, p, pb, peq, ph1, ph2, ph3, pcap, style_th, style_td, style_code, colors, c_primary, c_border, c_bg_light, cm):
    # MATRIZ DE CONSISTENCIA
    story.append(ph1("MATRIZ DE CONSISTENCIA"))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_primary, spaceAfter=8))
    story.append(p("A continuación, se presenta la <b>Matriz de Consistencia Metodológica</b> que garantiza la coherencia biunívoca entre problemas, objetivos, hipótesis, variables, indicadores y técnicas de investigación según el modelo oficial de la Escuela Profesional de Ingeniería de Minas (UNI FIGMM):"))
    story.append(Spacer(1, 0.15 * cm))

    matriz_data = [
        [
            Paragraph("<b>PROBLEMA</b>", style_th),
            Paragraph("<b>OBJETIVO</b>", style_th),
            Paragraph("<b>HIPÓTESIS</b>", style_th),
            Paragraph("<b>VARIABLE DEPENDIENTE</b>", style_th),
            Paragraph("<b>VARIABLE INDEPENDIENTE</b>", style_th),
            Paragraph("<b>INDICADORES</b>", style_th),
            Paragraph("<b>TÉCNICA E INSTRUMENTOS</b>", style_th)
        ],
        [
            Paragraph("<b>PROBLEMA GENERAL:</b><br/>¿En qué medida el diseño asistido de perforación y voladura mediante un sistema agéntico basado en IA y reglas físicas influye en el control de la sobrerotura en labores subterráneas de la U.E.A. Lincuna, 2026?", style_td),
            Paragraph("<b>OBJETIVO GENERAL:</b><br/>Desarrollar, validar e instrumentar un sistema agéntico basado en IA y reglas físicas para el diseño asistido de P&V orientado a reducir la sobrerotura a valores $\le 5.0\%$ en la U.E.A. Lincuna, 2026.", style_td),
            Paragraph("<b>HIPÓTESIS GENERAL:</b><br/>La implementación de un sistema agéntico basado en IA y reglas físicas determinísticas para el diseño asistido de P&V reducirá la sobrerotura a valores $\le 5.0\%$ en la U.E.A. Lincuna, 2026.", style_td),
            Paragraph("<b>Porcentaje de Sobrerotura (%):</b><br/>Volumen excedente de sobre-excavación por fuera del perfil teórico de diseño (4.50 m $\times$ 4.50 m).", style_td),
            Paragraph("<b>Sistema Agéntico Autónomo:</b><br/>Arquitectura multi-agente MCP con motor determinístico de Holmberg-Persson en 5 secciones.", style_td),
            Paragraph("• Sobrerotura media (%)<br/>• Factor de Media Caña (HCF %)<br/>• Desviación cuadrática RMS (mm)<br/>• Ahorro de shotcrete ($/disp)", style_td),
            Paragraph("• Escáner láser 3D LIDAR terrestre.<br/>• Software CloudCompare (C2M).<br/>• 5 Bases de datos Excel Lincuna.<br/>• Prueba t-Student pareada.", style_td)
        ],
        [
            Paragraph("<b>PROBLEMA ESPECÍFICO 1:</b><br/>¿En qué medida la modelación analítica del desacoplamiento de contorno reduce la presión en pared por debajo del UCS y disminuye la sobrerotura perimétrica?", style_td),
            Paragraph("<b>OBJETIVO ESPECÍFICO 1:</b><br/>Modelar el desacoplamiento en corona y hastiales con cartuchos de 22 mm en barrenos de 45 mm para garantizar $P_{te} \le UCS$, elevando el HCF $\ge 75\%$.", style_td),
            Paragraph("<b>HIPÓTESIS ESPECÍFICA 1:</b><br/>La modelación del desacoplamiento con cartuchos de 22 mm generará $P_{te} = 164.96\text{ MPa} \le UCS = 180.05\text{ MPa}$, elevando el HCF $\ge 75\%$.", style_td),
            Paragraph("<b>Daño Perimétrico y HCF:</b><br/>Micro-fisuración inducida y porcentaje de cañas visibles en corona y hastiales.", style_td),
            Paragraph("<b>Presión Efectiva Desacoplada (Pte):</b><br/>Factor de desacoplamiento ($d_c/d_h$) y diámetro de cartucho de 22 mm.", style_td),
            Paragraph("• $P_{te}$ calculada (MPa)<br/>• $UCS$ de roca intacta (MPa)<br/>• Factor de Media Caña (%)<br/>• Profundidad de daño (m)", style_td),
            Paragraph("• Ensayos ASTM D7012-14.<br/>• Televiewer óptico de barreno.<br/>• Mapeo fotogramétrico de trazas.<br/>• Modelo de Persson (1994).", style_td)
        ],
        [
            Paragraph("<b>PROBLEMA ESPECÍFICO 2:</b><br/>¿En qué medida la optimización del corte en 4 cuadrantes, arrastres y auto-tajeo espacial optimiza el factor de potencia y el avance lineal?", style_td),
            Paragraph("<b>OBJETIVO ESPECÍFICO 2:</b><br/>Diseñar una malla optimizada de 47 taladros mediante Holmberg-Persson y auto-tajeo ($S/B = 1.25$, $f = 1.45$), logrando $q_p \le 1.65\text{ kg/m}^3$ y avance $\ge 88\%$.", style_td),
            Paragraph("<b>HIPÓTESIS ESPECÍFICA 2:</b><br/>El diseño analítico del corte y el auto-tajeo espacial optimizarán el factor de potencia a $q_p = 1.622\text{ kg/m}^3$ con un avance efectivo $\ge 88\%$.", style_td),
            Paragraph("<b>Factor de Potencia y Avance:</b><br/>Consumo específico de explosivo ($kg/m^3$) y metros avanzados por disparo.", style_td),
            Paragraph("<b>Malla Optimizada de 47 Taladros:</b><br/>Distribución espacial de 4 cuadrantes y celdas de Voronoi ($S/B = 1.25$).", style_td),
            Paragraph("• Factor de potencia $q_p$ ($kg/m^3$)<br/>• Avance lineal efectivo (m)<br/>• Eficiencia de perforación (%)<br/>• Número total de taladros (47)", style_td),
            Paragraph("• Registro `1. BD AVANCES.xlsx`.<br/>• Reporte `2. REPORTE DE VOLADURA`.<br/>• Topografía con estación total.<br/>• Balance masa y energía.", style_td)
        ],
        [
            Paragraph("<b>PROBLEMA ESPECÍFICO 3:</b><br/>¿En qué medida la reducción de la sobrerotura influye en la disminución de sobrecostos de sostenimiento y tiempos de carguío en Lincuna?", style_td),
            Paragraph("<b>OBJETIVO ESPECÍFICO 3:</b><br/>Cuantificar el beneficio económico demostrando un ahorro en shotcrete $> $1,500.00 USD/disparo y reducción de tiempos de ciclo mecanizado.", style_td),
            Paragraph("<b>HIPÓTESIS ESPECÍFICA 3:</b><br/>La reducción de sobrerotura al $4.85\%$ disminuirá el consumo de shotcrete en $> 5.70\text{ m}^3$/disparo, ahorrando $> $1,600.00 USD por frente.", style_td),
            Paragraph("<b>Costos y Tiempos de Ciclo:</b><br/>Gasto en concreto lanzado ($/disp) y minutos de carguío y acarreo.", style_td),
            Paragraph("<b>Reducción de Sobrerotura:</b><br/>Disminución del volumen sobre-excavado alcanzada por el sistema agéntico.", style_td),
            Paragraph("• Ahorro directo ($/disparo)<br/>• Consumo de shotcrete ($m^3$)<br/>• Tiempo de scoop Cat R1600 (min)<br/>• VAN ($) y TIR (%)", style_td),
            Paragraph("• APU auditado ($285 USD/m³).<br/>• Base `6. BD SOSTENIMIENTO`.<br/>• Base `5. BD-SCOOP 2026`.<br/>• Evaluación financiera 5 años.", style_td)
        ],
    ]
    t_mat = Table(matriz_data, colWidths=[2.4 * cm, 2.4 * cm, 2.4 * cm, 2.2 * cm, 2.2 * cm, 2.2 * cm, 2.2 * cm])
    t_mat.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_bg_light]),
    ]))
    story.append(t_mat)
    story.append(pcap("Tabla: Matriz de Consistencia Metodológica del Plan de Tesis (Escuela Profesional de Ingeniería de Minas, UNI FIGMM)."))
    story.append(Spacer(1, 0.3 * cm))

    # CRONOGRAMA DEL TRABAJO
    story.append(ph1("CRONOGRAMA DEL TRABAJO"))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_primary, spaceAfter=8))
    story.append(p("El plan de investigación se ejecutará en un período de <b>16 semanas (4 meses)</b> según el siguiente cronograma de actividades tipo Gantt:"))
    story.append(Spacer(1, 0.15 * cm))

    col_g = [4.2 * cm] + [0.72 * cm] * 16
    cron_data = [
        [Paragraph("<b>ACTIVIDADES DEL PROYECTO</b>", style_th)] + [Paragraph(f"<b>S{i+1}</b>", style_th) for i in range(16)],
        [Paragraph("1. Aprobación del Plan de Tesis e IPERC", style_td)] + [Paragraph("X" if i < 2 else "", style_td) for i in range(16)],
        [Paragraph("2. Mapeo geomecánico de cruceros (RMR/GSI)", style_td)] + [Paragraph("X" if 1 <= i < 4 else "", style_td) for i in range(16)],
        [Paragraph("3. Ensayos de laboratorio (UCS, tracción)", style_td)] + [Paragraph("X" if 2 <= i < 5 else "", style_td) for i in range(16)],
        [Paragraph("4. Ingesta de bases de datos Excel de Lincuna", style_td)] + [Paragraph("X" if 3 <= i < 6 else "", style_td) for i in range(16)],
        [Paragraph("5. Calibración del Solver de Holmberg-Persson", style_td)] + [Paragraph("X" if 5 <= i < 8 else "", style_td) for i in range(16)],
        [Paragraph("6. Programación de agentes MCP y Red Team", style_td)] + [Paragraph("X" if 6 <= i < 9 else "", style_td) for i in range(16)],
        [Paragraph("7. Instrumentación de 30 disparos en mina", style_td)] + [Paragraph("X" if 8 <= i < 12 else "", style_td) for i in range(16)],
        [Paragraph("8. Escaneo láser 3D LIDAR y registro ICP", style_td)] + [Paragraph("X" if 9 <= i < 13 else "", style_td) for i in range(16)],
        [Paragraph("9. Mapeo C2M de desviaciones en CloudCompare", style_td)] + [Paragraph("X" if 10 <= i < 14 else "", style_td) for i in range(16)],
        [Paragraph("10. Análisis estadístico inferencial (t / ANOVA)", style_td)] + [Paragraph("X" if 12 <= i < 15 else "", style_td) for i in range(16)],
        [Paragraph("11. Análisis granulométrico Split-Desktop", style_td)] + [Paragraph("X" if 13 <= i < 15 else "", style_td) for i in range(16)],
        [Paragraph("12. Evaluación financiera (VAN, TIR, Payback)", style_td)] + [Paragraph("X" if 14 <= i < 16 else "", style_td) for i in range(16)],
        [Paragraph("13. Redacción final del informe de tesis", style_td)] + [Paragraph("X" if 14 <= i < 16 else "", style_td) for i in range(16)],
        [Paragraph("14. Sustentación pública ante el Jurado UNI", style_td)] + [Paragraph("X" if i == 15 else "", style_td) for i in range(16)],
    ]
    t_cron = Table(cron_data, colWidths=col_g)
    t_cron.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ALIGN', (1,0), (-1,-1), 'CENTER'),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_bg_light]),
    ]))
    story.append(t_cron)
    story.append(pcap("Tabla: Cronograma de Trabajo de 16 Semanas (Diagrama de Gantt del Plan de Tesis)."))
    story.append(Spacer(1, 0.3 * cm))

    # PRESUPUESTO Y FINANCIAMIENTO
    story.append(ph1("PRESUPUESTO Y FINANCIAMIENTO DEL PROYECTO"))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_primary, spaceAfter=8))
    story.append(p("El presupuesto consolidado del proyecto de investigación se detalla en el siguiente cuadro analítico:"))
    story.append(Spacer(1, 0.15 * cm))

    pres_data = [
        [Paragraph("<b>Rubro / Concepto</b>", style_th), Paragraph("<b>Unidad</b>", style_th), Paragraph("<b>Cantidad</b>", style_th), Paragraph("<b>Costo Unit. (USD)</b>", style_th), Paragraph("<b>Total (USD)</b>", style_th), Paragraph("<b>Fuente de Financiamiento</b>", style_th)],
        [Paragraph("Investigador Principal (Tesista)", style_td), Paragraph("meses", style_td), Paragraph("4.0", style_td), Paragraph("$1,200.00", style_td), Paragraph("$4,800.00", style_td), Paragraph("Recursos Propios", style_td)],
        [Paragraph("Asesoría Geomecánica Especializada", style_td), Paragraph("horas", style_td), Paragraph("40.0", style_td), Paragraph("$50.00", style_td), Paragraph("$2,000.00", style_td), Paragraph("Recursos Propios", style_td)],
        [Paragraph("Alquiler de Escáner Láser 3D LIDAR", style_td), Paragraph("días", style_td), Paragraph("15.0", style_td), Paragraph("$250.00", style_td), Paragraph("$3,750.00", style_td), Paragraph("Cía. Minera Lincuna S.A.", style_td)],
        [Paragraph("Ensayos de Laboratorio UNI FIGMM", style_td), Paragraph("ensayos", style_td), Paragraph("15.0", style_td), Paragraph("$80.00", style_td), Paragraph("$1,200.00", style_td), Paragraph("Recursos Propios", style_td)],
        [Paragraph("Servidores Cloud e Infraestructura MCP", style_td), Paragraph("meses", style_td), Paragraph("4.0", style_td), Paragraph("$200.00", style_td), Paragraph("$800.00", style_td), Paragraph("Recursos Propios", style_td)],
        [Paragraph("Viáticos y Estadía en Mina Ticapampa", style_td), Paragraph("días", style_td), Paragraph("30.0", style_td), Paragraph("$60.00", style_td), Paragraph("$1,800.00", style_td), Paragraph("Cía. Minera Lincuna S.A.", style_td)],
        [Paragraph("Materiales, EPP y Accesorios Topográficos", style_td), Paragraph("gl", style_td), Paragraph("1.0", style_td), Paragraph("$900.00", style_td), Paragraph("$900.00", style_td), Paragraph("Recursos Propios", style_td)],
        [Paragraph("Imprevistos y Contingencias (5%)", style_td), Paragraph("gl", style_td), Paragraph("1.0", style_td), Paragraph("$740.00", style_td), Paragraph("$740.00", style_td), Paragraph("Recursos Propios", style_td)],
        [Paragraph("<b>TOTAL PRESUPUESTO DEL PROYECTO</b>", style_td), Paragraph("<b>gl</b>", style_td), Paragraph("<b>1.0</b>", style_td), Paragraph("<b>$15,990.00</b>", style_td), Paragraph("<b>$15,990.00</b>", style_td), Paragraph("<b>Autofinanciado + Empresa</b>", style_td)],
    ]
    t_pres = Table(pres_data, colWidths=[4.2 * cm, 1.4 * cm, 1.4 * cm, 2.5 * cm, 2.5 * cm, 4.0 * cm])
    t_pres.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('ROWBACKGROUNDS', (0,1), (-1,-2), [colors.white, c_bg_light]),
        ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor("#D4EFDF")),
    ]))
    story.append(t_pres)
    story.append(pcap("Tabla: Presupuesto Analítico Consolidado y Fuentes de Financiamiento del Plan de Tesis."))
    story.append(Spacer(1, 0.3 * cm))

    # BIBLIOGRAFIA
    story.append(ph1("BIBLIOGRAFIA"))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_primary, spaceAfter=8))
    
    bibs = [
        "ASTM International. (2014). <i>Standard Test Method for Compressive Strength and Elastic Moduli of Intact Rock Core Specimens under Varying States of Stress and Temperatures (ASTM D7012-14)</i>. West Conshohocken, PA.",
        "ASTM International. (2016). <i>Standard Test Method for Splitting Tensile Strength of Intact Rock Core Specimens [Brazilian Method] (ASTM D3967-16)</i>. West Conshohocken, PA.",
        "Barton, N., Lien, R. & Lunde, J. (1974). Engineering classification of rock masses for the design of tunnel support. <i>Rock Mechanics</i>, 6(4), 189-236.",
        "Barrutia Feijóo, M. & Mamani Apaza, H. (2021). <i>Directivas de Rigor Metodológico y Criterios Científicos para Tesis de Ingeniería de Minas</i>. Facultad de Ingeniería Geológica, Minera y Metalúrgica, Universidad Nacional de Ingeniería, Lima.",
        "Bieniawski, Z. T. (1989). <i>Engineering Rock Mass Classifications: A Complete Manual for Engineers and Geologists in Mining, Civil, and Petroleum Engineering</i>. John Wiley & Sons, New York.",
        "Cardu, M., Coragliotto, D. & Oreste, P. (2020). Analysis of the blast-induced damage zone in tunnel walls through numerical modeling and field trials. <i>Mining Technology</i>, 129(4), 215-228.",
        "Cárdenas, L. (2023). <i>Aplicación de escáner láser 3D terrestre para la cuantificación y control de sobrerotura en galerías de nivel de Unidad Minera San Rafael, Minsur S.A.</i> (Tesis de Título Profesional). Universidad Nacional de Ingeniería, Lima.",
        "Caterpillar Inc. (2024). <i>Cat Underground Mining Systems: Technical Performance Manual for R1600 Series Loaders</i>. Peoria, IL.",
        "Chapman, D. L. (1899). On the rate of explosion in gases. <i>Philosophical Magazine</i>, 47(284), 90-104.",
        "Chauca, J. & Medina, E. (2022). <i>Optimización de mallas de perforación y voladura para el control de sobre-excavación en la galería Esperanza, Compañía Minera Poderosa S.A.</i> (Tesis de Titulación Profesional). UNI FIGMM, Lima.",
        "Cunningham, C. V. (1983). The Kuz-Ram model for prediction of fragmentation from blasting. <i>First International Symposium on Rock Fragmentation by Blasting</i>, Luleå, Sweden, 439-453.",
        "Cunningham, C. V. (2005). Fragmentation estimations and the Kuz-Ram model—four decades on. <i>EFEE Second World Conference on Explosives and Blasting</i>, Prague, 249-260.",
        "Deere, D. U. (1964). Technical description of rock cores for engineering purposes. <i>Rock Mechanics and Engineering Geology</i>, 1(1), 17-22.",
        "Gustafsson, R. (1981). <i>Swedish Blasting Technique</i>. SPI, Gothenburg, Sweden.",
        "Hernández-Sampieri, R., Fernández-Collado, C. & Baptista-Lucio, P. (2018). <i>Metodología de la investigación: Las rutas cuantitativa, cualitativa y mixta</i>. McGraw-Hill Education, México.",
        "Hoek, E., Carranza-Torres, C. & Corkum, B. (2002). Hoek-Brown failure criterion - 2002 edition. <i>NARMS-TAC Conference</i>, Toronto, 267-273.",
        "Hoek, E. & Brown, E. T. (2018). The Hoek-Brown failure criterion and GSI—2018 edition. <i>Journal of Rock Mechanics and Geotechnical Engineering</i>, 11(3), 445-463.",
        "Holmberg, R. & Persson, P. A. (1980). Design of tunnel perimeter blasting using peak particle velocity criteria. <i>Third International Symposium on Tunnelling</i>, Institution of Mining and Metallurgy, London, 181-192.",
        "Huamán, G. (2020). <i>Evaluación del factor de fijación en arrastres y zapateras en excavaciones subterráneas de Sociedad Minera Corona</i> (Tesis de Pregrado). Pontificia Universidad Católica del Perú, Lima.",
        "ISRM. (2007). <i>The Complete ISRM Suggested Methods for Rock Characterization, Testing and Monitoring: 1974-2006</i>. Commission on Testing Methods, International Society for Rock Mechanics.",
        "Jouguet, É. (1905). Sur la propagation des réactions chimiques dans les gaz. <i>Journal de Mathématiques Pures et Appliquées</i>, 1, 347-425.",
        "Kastner, H. (1962). <i>Statik des Tunnel- und Stollenbaues</i>. Springer-Verlag, Berlin.",
        "Kirsch, G. (1898). Die Theorie der Elastizität und die Bedürfnisse der Festigkeitslehre. <i>Zeitschrift des Vereines Deutscher Ingenieure</i>, 42, 797-807.",
        "Konečný, P. & Kořínek, R. (2021). Blast damage zone extent in underground excavations: A review of analytical and empirical models. <i>Geotechnical and Geological Engineering</i>, 39(6), 4055-4072.",
        "Lee, E. L., Hornig, H. C. & Kury, J. W. (1968). <i>Adiabatic Expansion of High Explosive Detonation Products</i> (Report UCRL-50422). Lawrence Radiation Laboratory, University of California, Livermore.",
        "Langefors, U. & Kihlström, B. (1978). <i>The Modern Technique of Rock Blasting</i>. John Wiley & Sons, New York.",
        "Lee, J. H. (2008). <i>The Detonation Phenomenon</i>. Cambridge University Press, Cambridge.",
        "Mendoza, M. E. (2016). <i>Tipificación de las causas que influyen en la vida útil de los neumáticos de volquetes y su incidencia en la producción: Caso Toquepala</i> (Tesis de Pregrado). Universidad Nacional del Altiplano, Puno.",
        "Montgomery, D. C. (2017). <i>Design and Analysis of Experiments</i> (9th ed.). John Wiley & Sons, New York.",
        "Olovsson, L., Sjöberg, F. & Simonsson, K. (2020). Numerical simulation of rock blasting using a coupled Eulerian-Lagrangian formulation. <i>International Journal of Impact Engineering</i>, 143, 103598.",
        "Ozkahraman, H. T. & Bolukbasi, N. (2022). Evaluation of overbreak in underground drifts using empirical formulas and digital photogrammetry. <i>International Journal of Rock Mechanics and Mining Sciences</i>, 154, 105112.",
        "Paredes, C. (2008). <i>Eficiencia en tiempo de vida de neumáticos con relación a rotación de posiciones 01 y 02 en volquetes Komatsu 930E-3</i> (Tesis de Pregrado). UNI FIGMM, Lima.",
        "Persson, P. A., Holmberg, R. & Lee, J. (1994). <i>Rock Blasting and Explosives Engineering</i>. CRC Press, Boca Raton, FL.",
        "Sari, M., Ghasemi, E. & Ataei, M. (2023). Stochastic simulation and machine learning for overbreak risk assessment in drill and blast tunnelling. <i>Bulletin of Engineering Geology and the Environment</i>, 82(5), 184.",
        "Sandvik Mining and Rock Solutions. (2024). <i>Sandvik DD321 Development Drill Rig: Technical Specification Manual</i>. Tampere, Finland.",
        "Siskind, D. E., Stagg, M. S., Kopp, J. W. & Dowding, C. H. (1980). <i>Structure Response and Damage Produced by Ground Vibration from Surface Mine Blasting</i> (Report of Investigations 8507). United States Bureau of Mines (USBM), Washington, D.C.",
        "Terzaghi, K. (1946). Rock defects and loads on tunnel supports. In R. V. Proctor & T. L. White (Eds.), <i>Rock Tunneling with Steel Supports</i> (pp. 17-99). Commercial Shearing and Stamping Co., Youngstown, OH.",
        "Vargas, R. (2021). <i>Modelamiento geomecánico y termodinámico de voladura controlada en frentes de avance de Consorcio Minero Horizonte</i> (Tesis de Maestría). Sección de Posgrado UNI FIGMM, Lima.",
        "Zeldovich, Y. B., Barenblatt, G. I., Librovich, V. B. & Makhviladze, G. M. (1985). <i>The Mathematical Theory of Combustion and Explosions</i>. Consultants Bureau, New York.",
        "Zhang, Z., Gao, W. & Peng, K. (2024). A hybrid physics-informed neural network framework for blast-induced damage prediction in deep underground tunnels. <i>Tunnelling and Underground Space Technology</i>, 144, 105542.",
    ]

    for b in bibs:
        story.append(pb(b))
    story.append(Spacer(1, 0.3 * cm))

    # =========================================================================
    # ANEXOS EXHAUSTIVOS
    # =========================================================================
    story.append(ph1("ANEXOS"))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_primary, spaceAfter=8))
    
    # Anexo 1: Matriz Expandida
    story.append(ph2("ANEXO 1: MATRIZ DE CONSISTENCIA METODOLÓGICA EXPANDIDA"))
    story.append(p("La matriz de consistencia vincula los tres problemas específicos con sus correspondientes hipótesis, variables, indicadores de campo y métodos de contrastación analítica en Lincuna."))
    story.append(Spacer(1, 0.2 * cm))

    # Anexo 2: Fichas de Recolección de Datos de Excel de Lincuna
    story.append(ph2("ANEXO 2: FICHAS DE RECOLECCIÓN DE DATOS DE LAS 5 BASES DE DATOS DE LINCUNA"))
    story.append(p("Estructura de recolección de variables operacionales auditadas a partir de los 5 libros de Excel:"))
    story.append(pb("<b>Base 1 (Avances):</b> 120 frentes históricos registrados, avance lineal medio de 3.15 m, volumen sobre-excavado de 22.75 m³."))
    story.append(pb("<b>Base 2 (Voladura):</b> 54 taladros cargados, emulsión de 32 mm, factor de potencia histórico de 2.08 kg/m³."))
    story.append(pb("<b>Base 3 (Jumbos):</b> Jumbo Sandvik DD321, presión percusión 180 bar, velocidad de penetración 1.85 m/min."))
    story.append(pb("<b>Base 4 (Scoops):</b> Scooptramp Cat R1600 de 6 yd³, tiempo de limpieza de 135 min por disparo con sobrerotura."))
    story.append(pb("<b>Base 5 (Sostenimiento):</b> Consumo mensual de 14 a 16 m³ de shotcrete vía húmeda robotizado por disparo."))
    story.append(Spacer(1, 0.2 * cm))

    # Anexo 3: Fichas Geomecánicas de los 5 Cruceros
    cruceros_data = [
        ("Crucero 100", "Andesita Porfirítica Calipuy", "57.0", "52", "185.2 MPa", "12.5 MPa", "62%", "Shotcrete 2\" + Pernos Split Set 7'"),
        ("Crucero 120", "Dacita Porfirítica", "54.5", "49", "176.8 MPa", "11.8 MPa", "58%", "Shotcrete 2\" con fibra estructural"),
        ("Crucero 140", "Arenisca Cuarcítica Masiva", "58.0", "53", "192.4 MPa", "13.2 MPa", "65%", "Pernos helicoidales 7' sistemáticos"),
        ("Crucero 160", "Lutita Chicama Cizallada", "51.5", "46", "158.3 MPa", "10.5 MPa", "52%", "Shotcrete 3\" + Malla 4x4\" + Split Set 7'"),
        ("Crucero 180", "Andesita Propilítica Húmeda", "55.5", "50", "180.0 MPa", "12.1 MPa", "60%", "Shotcrete 2\" vía húmeda acelerado"),
    ]
    story.append(ph2("ANEXO 3: RESUMEN DE FICHAS GEOMECÁNICAS DE LOS 5 CRUCEROS INSTRUMENTADOS"))
    f_res_data = [
        [Paragraph("<b>Crucero</b>", style_th), Paragraph("<b>Litología Dominante</b>", style_th), Paragraph("<b>RMR</b>", style_th), Paragraph("<b>GSI</b>", style_th), Paragraph("<b>UCS (MPa)</b>", style_th), Paragraph("<b>Tracción (MPa)</b>", style_th), Paragraph("<b>RQD (%)</b>", style_th), Paragraph("<b>Sostenimiento Estándar</b>", style_th)],
    ]
    for c_id, lit, rmr, gsi, ucs, tr, rqd, sost in cruceros_data:
        f_res_data.append([
            Paragraph(c_id, style_td), Paragraph(lit, style_td), Paragraph(rmr, style_td), Paragraph(gsi, style_td), Paragraph(ucs, style_td), Paragraph(tr, style_td), Paragraph(rqd, style_td), Paragraph(sost, style_td)
        ])
    t_fres = Table(f_res_data, colWidths=[2.0 * cm, 3.4 * cm, 1.2 * cm, 1.2 * cm, 1.8 * cm, 1.8 * cm, 1.4 * cm, 3.2 * cm])
    t_fres.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_bg_light]),
    ]))
    story.append(t_fres)
    story.append(pcap("Tabla: Resumen Consolidado de Fichas Geomecánicas de los Cruceros de Prueba."))
    story.append(Spacer(1, 0.2 * cm))

    # Anexo 4: Coordenadas de los 47 Taladros
    story.append(ph2("ANEXO 4: CATÁLOGO MAESTRO DE COORDENADAS (X,Y) Y RETARDOS DE LOS 47 TALADROS"))
    story.append(p("Distribución de los 47 taladros de la malla optimizada calculada por el Agente Solver:"))
    story.append(pb("• 1 Taladro de alivio central (102 mm, vacío)"))
    story.append(pb("• 16 Taladros de corte en 4 cuadrantes concéntricos ($B_{p1}=0.153\text{ m}$ a $B_{p4}=0.840\text{ m}$, retardos MS-1 a MS-4)"))
    story.append(pb("• 5 Taladros de arrastre en solera ($B=0.850\text{ m}$, retardo LP-12)"))
    story.append(pb("• 9 Taladros de corona desacoplados (22 mm en 45 mm, $P_{te}=164.96\text{ MPa}$, retardo LP-14)"))
    story.append(pb("• 6 Taladros de hastiales desacoplados (retardo LP-15)"))
    story.append(pb("• 10 Taladros de ayudas / auto-tajeo espacial ($S/B=1.25$, retardos MS-5 a MS-9)"))
    story.append(Spacer(1, 0.2 * cm))

    # Anexo 5: Especificaciones de Equipos
    story.append(ph2("ANEXO 5: ESPECIFICACIONES TÉCNICAS DE EQUIPOS E INSUMOS"))
    story.append(p("Fichas técnicas de jumbo Sandvik DD321, emulsión encartuchada Famesa / Exsa (22 mm y 32 mm), detonadores Dual Dets Exel y escáner láser terrestre LIDAR."))
    story.append(Spacer(1, 0.2 * cm))

    # Anexo 6: Código Python
    story.append(ph2("ANEXO 6: CÓDIGO FUENTE PYTHON DEL SISTEMA AGÉNTICO MCP Y MOTOR HOLMBERG"))
    story.append(p("Arquitectura de código modular en Python con funciones `calcular_corte_4_cuadrantes()`, `calcular_desacoplamiento_persson()`, `auditoria_red_team()` y exportación a archivos DXF y CSV para jumbos Sandvik."))
    story.append(Spacer(1, 0.2 * cm))
