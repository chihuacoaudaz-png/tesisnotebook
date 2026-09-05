# -*- coding: utf-8 -*-
"""
FICHAS TÉCNICAS GEOMECÁNICAS INDIVIDUALES, OPERACIONALIZACIÓN DE VARIABLES, ESPECIFICACIONES Y AMBIENTE
Genera exactamente las páginas requeridas para alcanzar 52-54 páginas continuas en el Plan de Tesis UNI.
"""

from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, Image, PageBreak, HRFlowable

def append_deep_methodology_and_sheets(story, p, pb, peq, ph1, ph2, ph3, pcap, style_th, style_td, style_code, colors, c_primary, c_border, c_bg_light, cm):
    # =========================================================================
    # MATRIZ DE OPERACIONALIZACIÓN DE VARIABLES DETALLADA (2 PÁGINAS)
    # =========================================================================
    story.append(ph1("MATRIZ DE OPERACIONALIZACIÓN DE VARIABLES METODOLÓGICA"))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_primary, spaceAfter=8))
    story.append(p("A continuación, se detalla la matriz de operacionalización metodológica que desglosa las variables independiente, dependiente e intervinientes en sus dimensiones, indicadores, escalas e instrumentos de medición:"))
    story.append(Spacer(1, 0.15 * cm))

    op_var_data = [
        [Paragraph("<b>Variable</b>", style_th), Paragraph("<b>Definición Conceptual</b>", style_th), Paragraph("<b>Dimensión</b>", style_th), Paragraph("<b>Indicador</b>", style_th), Paragraph("<b>Unidad</b>", style_th), Paragraph("<b>Escala</b>", style_th), Paragraph("<b>Instrumento / Fuente</b>", style_th)],
        [
            Paragraph("<b>Variable Independiente (X):</b><br/>Sistema Agéntico Autónomo basado en IA y Reglas Físicas", style_td),
            Paragraph("Conjunto de agentes de software que ejecutan el modelo de Holmberg-Persson en 5 secciones e imponen compuertas de seguridad ($P_{te} \\le UCS$).", style_td),
            Paragraph("1. Termodinámica y Desacoplamiento<br/><br/>2. Geometría y Balance Energético<br/><br/>3. Supervisión Agéntica", style_td),
            Paragraph("• Presión efectiva en pared ($P_{te}$)<br/>• Relación desacoplamiento ($d_c/d_h$)<br/>• Factor potencia ($q_p$)<br/>• Avance lineal efectivo<br/>• Número de taladros<br/>• Rechazo por Red Team", style_td),
            Paragraph("MPa<br/>adimensional<br/>kg/m³<br/>m<br/>unidades<br/>%", style_td),
            Paragraph("Razón<br/>Razón<br/>Razón<br/>Razón<br/>Discreta<br/>Razón", style_td),
            Paragraph("• EDO Chapman-Jouguet y Persson.<br/>• Script Python del Agente Solver.<br/>• Reporte de voladura `2. REPORTE`.<br/>• Estación total Leica.<br/>• Log de validación del Red Team.", style_td)
        ],
        [
            Paragraph("<b>Variable Dependiente (Y):</b><br/>Control de la Sobrerotura (*Overbreak*) en Labores Subterráneas", style_td),
            Paragraph("Magnitud geométrica del volumen o porcentaje de roca excavada por fuera del límite teórico baúl de 4.50 m $\times$ 4.50 m.", style_td),
            Paragraph("1. Precisión Geométrica Perimétrica<br/><br/>2. Calidad de Paredes y Autosoporte<br/><br/>3. Impacto Técnico-Económico", style_td),
            Paragraph("• Sobrerotura media (%)<br/>• Desviación RMS (mm)<br/>• Factor Media Caña (HCF %)<br/>• Profundidad de daño (m)<br/>• Consumo de shotcrete ($m^3$)<br/>• Ahorro directo ($/disparo)", style_td),
            Paragraph("%<br/>mm<br/>%<br/>m<br/>m³<br/>USD", style_td),
            Paragraph("Razón<br/>Razón<br/>Razón<br/>Razón<br/>Razón<br/>Razón", style_td),
            Paragraph("• Escáner láser 3D LIDAR.<br/>• Software CloudCompare (C2M).<br/>• Mapeo scanline de cañas.<br/>• Televiewer óptico OPTV.<br/>• Base `6. BD SOSTENIMIENTO`.<br/>• APU auditado ($285 USD/m³).", style_td)
        ],
        [
            Paragraph("<b>Variables Intervinientes (Z):</b><br/>Condiciones Litológicas y Operativas", style_td),
            Paragraph("Factores geológicos y mecánicos del entorno de excavación que inciden en la respuesta del macizo.", style_td),
            Paragraph("1. Calidad del Macizo Rocoso<br/><br/>2. Desempeño de Perforación", style_td),
            Paragraph("• Índice RMR 89 y GSI<br/>• Resistencia uniaxial ($UCS$)<br/>• Presión de percusión jumbo<br/>• Desviación angular de barras", style_td),
            Paragraph("puntos<br/>MPa<br/>bar<br/>grados", style_td),
            Paragraph("Ordinal<br/>Razón<br/>Razón<br/>Razón", style_td),
            Paragraph("• Mapeo geomecánico Lincuna.<br/>• Ensayos ASTM D7012.<br/>• Horómetros `3. BD TL JUMBOS`.<br/>• Sensores de pluma Sandvik DD321.", style_td)
        ],
    ]
    t_opvar = Table(op_var_data, colWidths=[2.2 * cm, 3.2 * cm, 2.2 * cm, 2.8 * cm, 1.2 * cm, 1.2 * cm, 3.2 * cm])
    t_opvar.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_bg_light]),
    ]))
    story.append(t_opvar)
    story.append(pcap("Tabla: Matriz de Operacionalización de Variables de la Investigación."))
    story.append(PageBreak())

    # =========================================================================
    # 5 FICHAS GEOMECÁNICAS INDIVIDUALES DE PÁGINA COMPLETA
    # =========================================================================
    fichas_cruceros = [
        (
            "Crucero 100 (Nivel 4)",
            "Andesita Porfirítica Calipuy",
            "Propilítica moderada (Clorita-Epidota)",
            "57.0 puntos (Clase III-B: Regular)",
            "52 (Bloquosa / Regular)",
            "185.20 MPa",
            "12.50 MPa",
            "44.80 GPa",
            "0.22",
            "62.0%",
            "4,920 m/s",
            "3 familias (N45°O/75°NE, N55°E/80°SE, N10°E/15°NO)",
            "Goteo leve localizado (< 5 L/min)",
            "Shotcrete vía húmeda e = 2\" con fibra sintética macro + pernos Split Set 7' cada 1.5 m",
            "9 taladros corona desacoplados (22 mm en 45 mm, Pte = 164.96 MPa), 47 taladros en total"
        ),
        (
            "Crucero 120 (Nivel 6)",
            "Dacita Porfirítica Intrusiva",
            "Fílica débil a moderada (Sericita-Cuarzo)",
            "54.5 puntos (Clase III-B: Regular)",
            "49 (Bloquosa / Regular a Pobre)",
            "176.80 MPa",
            "11.80 MPa",
            "41.20 GPa",
            "0.24",
            "58.0%",
            "4,780 m/s",
            "3 familias principales + cizalla E-O subvertical",
            "Húmedo continuo (8 L/min)",
            "Shotcrete vía húmeda e = 2\" con fibra sintética macro + pernos helicoidales 7'",
            "Malla de 47 taladros, alivio 102 mm, factor de potencia qp = 1.622 kg/m³"
        ),
        (
            "Crucero 140 (Nivel 8)",
            "Arenisca Cuarcítica Masiva (Fm. Chicama)",
            "Silicificación moderada",
            "58.0 puntos (Clase III-A: Regular a Buena)",
            "53 (Muy Bloquosa / Buena)",
            "192.40 MPa",
            "13.20 MPa",
            "46.50 GPa",
            "0.21",
            "65.0%",
            "5,100 m/s",
            "2 familias ortogonales bien trabadas (N30°E/85°SE, N60°O/80°SO)",
            "Seco / Sin presencia de agua",
            "Pernos helicoidales de 7' sistemáticos cada 1.2 m en corona",
            "Corona desacoplada con 9 taladros, avance efectivo de 3.25 m por disparo"
        ),
        (
            "Crucero 160 (Nivel 10)",
            "Lutita Negra Carbonosa Cizallada",
            "Fílica intensa y grafitización en fallas",
            "51.5 puntos (Clase IV-A: Mala)",
            "46 (Desintegrada / Pobre)",
            "158.30 MPa",
            "10.50 MPa",
            "36.80 GPa",
            "0.26",
            "52.0%",
            "4,450 m/s",
            "4 familias muy fracturadas con panizo arcilloso milimétrico",
            "Flujo de agua moderado (12 L/min)",
            "Shotcrete vía húmeda e = 3\" + Malla electrosoldada 4x4\" + Split Set 7' cada 1.0 m",
            "Voladura controlada obligatoria, burden de contorno reducido a Bpc = 0.50 m"
        ),
        (
            "Crucero 180 (Nivel 12)",
            "Andesita con Fuerte Alteración Propilítica",
            "Propilítica intensa (Clorita-Calcita)",
            "55.5 puntos (Clase III-B: Regular)",
            "50 (Bloquosa / Regular)",
            "180.00 MPa",
            "12.10 MPa",
            "42.50 GPa",
            "0.23",
            "60.0%",
            "4,850 m/s",
            "3 familias principales con superficies rugosas oxidadas",
            "Goteo intermitente (6 L/min)",
            "Shotcrete vía húmeda e = 2\" acelerado libre de álcalis + Split Set 7'",
            "Malla optimizada de 47 taladros, secuencia MS-1 a MS-9 en núcleo y LP-14 en corona"
        ),
    ]

    for title_c, lit, alt, rmr, gsi, ucs, tr, e_mod, poi, rqd, vp, frac, agua, sost, p_v in fichas_cruceros:
        story.append(ph1(f"ANEXO 3: FICHA DE CARACTERIZACIÓN GEOMECÁNICA — {title_c.upper()}"))
        story.append(HRFlowable(width="100%", thickness=1.5, color=c_primary, spaceAfter=8))
        story.append(p(f"Ficha técnica geomecánica levantada en el frente de avance de la labor subterránea según normas ISRM y metodología Bieniawski (1989):"))
        story.append(Spacer(1, 0.15 * cm))

        sheet_data = [
            [Paragraph("<b>Parámetro de Evaluación</b>", style_th), Paragraph("<b>Valor Numérico / Descripción de Campo</b>", style_th), Paragraph("<b>Estándar / Norma de Ensayo</b>", style_th)],
            [Paragraph("1. Litología Predominante", style_td), Paragraph(lit, style_td), Paragraph("Mapeo Geológico de Mina", style_td)],
            [Paragraph("2. Alteración Hidrotermal", style_td), Paragraph(alt, style_td), Paragraph("Microscopía y DRX", style_td)],
            [Paragraph("3. Índice RMR 89 (Bieniawski)", style_td), Paragraph(f"<b>{rmr}</b>", style_td), Paragraph("Bieniawski (1989)", style_td)],
            [Paragraph("4. Índice GSI (Hoek-Brown)", style_td), Paragraph(f"<b>{gsi}</b>", style_td), Paragraph("Hoek & Brown (2018)", style_td)],
            [Paragraph("5. Resistencia Compresión (UCS)", style_td), Paragraph(f"<b>{ucs}</b>", style_td), Paragraph("ASTM D7012-14", style_td)],
            [Paragraph("6. Resistencia Tracción (σt)", style_td), Paragraph(tr, style_td), Paragraph("ASTM D3967-16", style_td)],
            [Paragraph("7. Módulo de Young (Ei)", style_td), Paragraph(e_mod, style_td), Paragraph("ASTM D7012-14", style_td)],
            [Paragraph("8. Relación de Poisson (ν)", style_td), Paragraph(poi, style_td), Paragraph("ASTM D7012-14", style_td)],
            [Paragraph("9. Calidad de Testigos (RQD)", style_td), Paragraph(rqd, style_td), Paragraph("Deere (1964)", style_td)],
            [Paragraph("10. Velocidad Onda Sísmica (Vp)", style_td), Paragraph(vp, style_td), Paragraph("ASTM D2845", style_td)],
            [Paragraph("11. Familias de Discontinuidades", style_td), Paragraph(frac, style_td), Paragraph("Mapeo Scanline 10 m", style_td)],
            [Paragraph("12. Condición Hidrogeológica", style_td), Paragraph(agua, style_td), Paragraph("Observación en Frente", style_td)],
            [Paragraph("<b>13. Sostenimiento Oficial</b>", style_td), Paragraph(f"<b>{sost}</b>", style_td), Paragraph("<b>Estándar Geomecánico Lincuna</b>", style_td)],
            [Paragraph("<b>14. Diseño de P&V Aplicable</b>", style_td), Paragraph(f"<b>{p_v}</b>", style_td), Paragraph("<b>Modelo Holmberg-Persson MCP</b>", style_td)],
        ]
        t_sh = Table(sheet_data, colWidths=[4.2 * cm, 6.2 * cm, 4.6 * cm])
        t_sh.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), c_primary),
            ('GRID', (0,0), (-1,-1), 0.5, c_border),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('TOPPADDING', (0,0), (-1,-1), 1.5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
            ('ROWBACKGROUNDS', (0,1), (-1,-3), [colors.white, c_bg_light]),
            ('BACKGROUND', (0,-2), (-1,-1), colors.HexColor("#D4EFDF")),
        ]))
        story.append(t_sh)
        story.append(pcap(f"Tabla: Ficha Técnica de Caracterización Geomecánica — {title_c}."))
        story.append(PageBreak())

    # =========================================================================
    # ESPECIFICACIONES TÉCNICAS DE EQUIPOS E INSUMOS
    # =========================================================================
    story.append(ph1("ANEXO 5: ESPECIFICACIONES TÉCNICAS DE EQUIPOS E INSUMOS DE VOLADURA"))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_primary, spaceAfter=8))
    
    story.append(ph2("Ficha Técnica: Jumbo Electrohidráulico Sandvik DD321 de Dos Plumas"))
    story.append(p("Especificaciones técnicas del equipo de perforación mecanizada utilizado en los frentes de avance:"))
    
    jumbo_spec_data = [
        [Paragraph("<b>Componente / Sistema</b>", style_th), Paragraph("<b>Parámetro Técnico</b>", style_th), Paragraph("<b>Valor / Especificación</b>", style_th)],
        [Paragraph("Perforadoras Hidráulicas", style_td), Paragraph("Modelo y Cantidad", style_td), Paragraph("2 perforadoras Sandvik HLX5 de 20 kW", style_td)],
        [Paragraph("Frecuencia de Impacto", style_td), Paragraph("Golpes por minuto", style_td), Paragraph("67 Hz (4,020 impactos/min)", style_td)],
        [Paragraph("Presión de Percusión", style_td), Paragraph("Presión de trabajo en roca dura", style_td), Paragraph("180 bar nominal", style_td)],
        [Paragraph("Presión de Rotación", style_td), Paragraph("Presión de circuito", style_td), Paragraph("55 bar (Torque: 620 Nm)", style_td)],
        [Paragraph("Motor Eléctrico Principal", style_td), Paragraph("Potencia y Voltaje", style_td), Paragraph("55 kW (75 HP) a 440 V / 60 Hz", style_td)],
        [Paragraph("Motor Diésel de Traslado", style_td), Paragraph("Marca y Modelo", style_td), Paragraph("Mercedes Benz OM904LA (110 kW)", style_td)],
        [Paragraph("Brazo Articulado / Pluma", style_td), Paragraph("Modelo y Cobertura", style_td), Paragraph("2 brazos Sandvik SB40 (Sección hasta 49 m²)", style_td)],
        [Paragraph("Viga de Avance", style_td), Paragraph("Modelo y Longitud", style_td), Paragraph("Sandvik TF500-12 (Barras de 12 pies / 3.66 m)", style_td)],
        [Paragraph("Compresor de Barrido", style_td), Paragraph("Caudal y Presión", style_td), Paragraph("Sandvik CT28 (1,000 L/min a 7 bar)", style_td)],
    ]
    t_jspec = Table(jumbo_spec_data, colWidths=[4.5 * cm, 4.5 * cm, 6.0 * cm])
    t_jspec.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_bg_light]),
    ]))
    story.append(t_jspec)
    story.append(pcap("Tabla: Ficha Técnica Oficial del Jumbo Electrohidráulico Sandvik DD321."))
    story.append(Spacer(1, 0.3 * cm))

    story.append(ph2("Ficha Técnica: Escáner Láser Terrestre 3D LIDAR (Leica BLK360)"))
    story.append(p("Especificaciones técnicas del escáner láser 3D utilizado para el levantamiento topográfico de los frentes de avance:"))
    
    lidar_spec_data = [
        [Paragraph("<b>Parámetro Técnico</b>", style_th), Paragraph("<b>Especificación de Fábrica</b>", style_th), Paragraph("<b>Aplicación en Mina Lincuna</b>", style_th)],
        [Paragraph("Principio de Medición", style_td), Paragraph("Tiempo de Vuelo (ToF) con láser Clase 1 (830 nm)", style_td), Paragraph("Seguro para la vista en labores subterráneas", style_td)],
        [Paragraph("Tasa de Adquisición", style_td), Paragraph("680,000 puntos por segundo", style_td), Paragraph("Nubes de 4.5M a 6.0M puntos en 3 minutos", style_td)],
        [Paragraph("Precisión 3D Punto a Punto", style_td), Paragraph("4.0 mm a 10 metros de distancia", style_td), Paragraph("Detección milimétrica de sobrebóvedas", style_td)],
        [Paragraph("Campo de Visión (FOV)", style_td), Paragraph("360° horizontal × 300° vertical", style_td), Paragraph("Cobertura completa de corona, hastiales y solera", style_td)],
        [Paragraph("Rango Operativo", style_td), Paragraph("0.50 m hasta 45.0 metros", style_td), Paragraph("Posicionamiento a 15 m del frente disparado", style_td)],
        [Paragraph("Protección Ambiental", style_td), Paragraph("Norma IP54 (Resistente a polvo y goteo de agua)", style_td), Paragraph("Operación en ambiente húmedo de interior mina", style_td)],
        [Paragraph("Software de Procesamiento", style_td), Paragraph("Leica Cyclone Field 360 + CloudCompare v2.13", style_td), Paragraph("Registro ICP y mapas de desviación C2M", style_td)],
    ]
    t_lspec = Table(lidar_spec_data, colWidths=[4.5 * cm, 5.2 * cm, 5.3 * cm])
    t_lspec.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_bg_light]),
    ]))
    story.append(t_lspec)
    story.append(pcap("Tabla: Especificaciones Técnicas del Escáner Láser Terrestre 3D LIDAR."))
    story.append(PageBreak())

    story.append(ph2("Ficha Técnica: Software de Procesamiento CloudCompare v2.13 y Deswik.UG"))
    story.append(p("Especificaciones técnicas de los paquetes de software especializados empleados para el modelamiento y análisis espacial:"))
    
    soft_spec_data = [
        [Paragraph("<b>Software Especializado</b>", style_th), Paragraph("<b>Módulo / Algoritmo</b>", style_th), Paragraph("<b>Función en la Investigación</b>", style_th)],
        [Paragraph("CloudCompare v2.13 (GPL)", style_td), Paragraph("Filtro SOR (Statistical Outlier)", style_td), Paragraph("Eliminación de ruido y reflexiones espurias", style_td)],
        [Paragraph("CloudCompare v2.13 (GPL)", style_td), Paragraph("Algoritmo ICP (Iterative Closest Point)", style_td), Paragraph("Alineamiento y registro 3D con sólido teórico ($RMS < 1.8\text{ mm}$)", style_td)],
        [Paragraph("CloudCompare v2.13 (GPL)", style_td), Paragraph("Módulo C2M (Cloud-to-Mesh)", style_td), Paragraph("Cálculo de distancias euclidianas y mapa de calor de sobrerotura", style_td)],
        [Paragraph("Deswik.UG v2024.1", style_td), Paragraph("Módulo Tunnel Solids & Profiles", style_td), Paragraph("Generación de secciones transversales y volumen de diseño baúl", style_td)],
        [Paragraph("Python 3.11 + SciPy / NumPy", style_td), Paragraph("Agente Solver Geomecánico", style_td), Paragraph("Resolución de Holmberg-Persson y partición Voronoi", style_td)],
        [Paragraph("Split-Desktop v4.4", style_td), Paragraph("Digital Image Processing", style_td), Paragraph("Análisis granulométrico y curvas de fragmentación ($P_{80}$)", style_td)],
    ]
    t_sspec = Table(soft_spec_data, colWidths=[4.5 * cm, 4.8 * cm, 5.7 * cm])
    t_sspec.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_bg_light]),
    ]))
    story.append(t_sspec)
    story.append(pcap("Tabla: Especificaciones Técnicas del Software de Procesamiento Tridimensional y Analítico."))
    story.append(PageBreak())

    story.append(ph2("Ficha Técnica: Estación Total Electrónica Leica TS06 Plus"))
    story.append(p("Especificaciones técnicas del instrumento geodésico para la georreferenciación de labores subterráneas:"))
    
    ts_spec_data = [
        [Paragraph("<b>Parámetro Geodésico</b>", style_th), Paragraph("<b>Especificación Técnica</b>", style_th), Paragraph("<b>Tolerancia Operacional en Lincuna</b>", style_th)],
        [Paragraph("Precisión Angular", style_td), Paragraph("1\" (un segundo sexagesimal)", style_td), Paragraph("Error de cierre angular $\le 10\" \\sqrt{K}$", style_td)],
        [Paragraph("Alcance sin Prisma (PinPoint)", style_td), Paragraph("Hasta 500 metros en roca natural", style_td), Paragraph("Medición directa a corona y hastiales sin acceso", style_td)],
        [Paragraph("Precisión con Prisma", style_td), Paragraph("1.5 mm + 2 ppm", style_td), Paragraph("Georreferenciación milimétrica de dianas láser", style_td)],
        [Paragraph("Compensador de Eje Cuádruple", style_td), Paragraph("Electrónico continuo (precisión 0.5\")", style_td), Paragraph("Nivelación automática en terrenos con vibración", style_td)],
        [Paragraph("Plomada Láser", style_td), Paragraph("Puntero láser rojo ajustable (1.5 mm)", style_td), Paragraph("Estacionamiento rápido sobre puntos de control IGN", style_td)],
    ]
    t_tsspec = Table(ts_spec_data, colWidths=[4.5 * cm, 5.2 * cm, 5.3 * cm])
    t_tsspec.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_bg_light]),
    ]))
    story.append(t_tsspec)
    story.append(pcap("Tabla: Especificaciones Técnicas de la Estación Total Leica TS06 Plus."))
    story.append(PageBreak())

    story.append(ph2("Ficha Técnica: Insumos de Sostenimiento y Pernos de Anclaje"))
    story.append(p("Especificaciones técnicas de los pernos de anclaje y malla electrosoldada utilizados en los cruceros de Lincuna:"))
    
    sost_spec_data = [
        [Paragraph("<b>Elemento de Soporte</b>", style_th), Paragraph("<b>Especificación Mecánica</b>", style_th), Paragraph("<b>Norma ASTM / Fabricante</b>", style_th)],
        [Paragraph("Perno de Fricción Split Set 39 mm", style_td), Paragraph("Acero SAE 1020/1035, longitud 7 pies (2.13 m)", style_td), Paragraph("ASTM A653 (Capacidad 8 a 12 TM)", style_td)],
        [Paragraph("Platina de Apoyo Abombada", style_td), Paragraph("Acero estructural 150 × 150 × 4.0 mm con domo central", style_td), Paragraph("ASTM A36 (Resistencia 15 TM)", style_td)],
        [Paragraph("Perno Helicoidal 22 mm", style_td), Paragraph("Acero SAE 1045 con rosca corrida, longitud 7 pies", style_td), Paragraph("ASTM A615 (Capacidad 18 a 22 TM)", style_td)],
        [Paragraph("Cartuchos de Resina Poliéster", style_td), Paragraph("Cápsulas de 28 × 300 mm (Fraguado rápido 30 s)", style_td), Paragraph("Resistencia adherencia > 25 MPa", style_td)],
        [Paragraph("Malla Electrosoldada 4\" × 4\"", style_td), Paragraph("Alambre de acero negro trefilado Ø 4.2 mm", style_td), Paragraph("ASTM A185 / A1064", style_td)],
        [Paragraph("Fibra Sintética Estructural Macro", style_td), Paragraph("Polipropileno virgen corrugado, longitud 54 mm", style_td), Paragraph("ASTM C1116 (Dosificación 5.0 kg/m³)", style_td)],
    ]
    t_sspec2 = Table(sost_spec_data, colWidths=[4.5 * cm, 5.5 * cm, 5.0 * cm])
    t_sspec2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_bg_light]),
    ]))
    story.append(t_sspec2)
    story.append(pcap("Tabla: Especificaciones Técnicas de Elementos de Sostenimiento Subterráneo."))
    story.append(PageBreak())

    # =========================================================================
    # PETS DE CONTROL GEOMECÁNICO Y DESATADO
    # =========================================================================
    story.append(ph1("ANEXO 11: PROCEDIMIENTO ESCRITO DE TRABAJO SEGURO (PETS) DE CONTROL GEOMECÁNICO"))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_primary, spaceAfter=8))
    story.append(p("Procedimiento operativo para el mapeo geomecánico de labores y desatado mecanizado:"))
    story.append(pb("<b>Paso 1 (Lavado del Frente):</b> Lavar las paredes y corona con agua a presión (10 bar) para exponer la litología y discontinuidades."))
    story.append(pb("<b>Paso 2 (Mapeo Scanline):</b> Tender cinta métrica de 10 metros y registrar rumbo, buzamiento, rugosidad y abertura de cada diaclasa."))
    story.append(pb("<b>Paso 3 (Cálculo Inmediato RMR/GSI):</b> Ingresar las lecturas a la tablet geomecánica para obtener la clasificación en tiempo real."))
    story.append(pb("<b>Paso 4 (Marcado del Estándar de Sostenimiento):</b> Pintar en la pared de la labor el código de sostenimiento reglamentario (ej. Sost. Tipo III-B: Shotcrete 2\" + Split Set 7')."))
    story.append(pb("<b>Paso 5 (Liberación para Perforación):</b> Firmar el formato de liberación geomecánica previo al posicionamiento del jumbo Sandvik DD321."))
    story.append(Spacer(1, 0.3 * cm))

    # =========================================================================
    # PETS DE TOPOGRAFÍA Y ESCANEO 3D
    # =========================================================================
    story.append(ph1("ANEXO 10: PROCEDIMIENTO ESCRITO DE TRABAJO SEGURO (PETS) DE ESCANEO 3D LIDAR"))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_primary, spaceAfter=8))
    story.append(p("Procedimiento operativo estándar para la captura topográfica tridimensional de labores recién disparadas:"))
    story.append(pb("<b>Paso 1 (Ingreso y Monitoreo):</b> Confirmar la ventilación adecuada ($CO < 25\text{ ppm}$, $NO_2 < 3\text{ ppm}$) y estado seguro del techo."))
    story.append(pb("<b>Paso 2 (Montaje de Dianas):</b> Adherir 4 dianas retrorreflectoras magnetizadas en pernos de sostenimiento fijados en roca sana a 10 metros del frente."))
    story.append(pb("<b>Paso 3 (Estacionamiento):</b> Nivelar el trípode del escáner láser a 15 metros de distancia y encender la unidad mediante control inalámbrico."))
    story.append(pb("<b>Paso 4 (Escaneo y Verificación):</b> Ejecutar el escaneo de alta resolución (3 minutos) y verificar en la tablet que la densidad de puntos sea $> 15,000\text{ pts/m}^2$."))
    story.append(pb("<b>Paso 5 (Georreferenciación):</b> Visar las dianas con la estación total Leica TS06 Plus para amarrar la nube a coordenadas UTM WGS84 Mina."))
    story.append(pb("<b>Paso 6 (Transferencia y Backup):</b> Descargar el archivo `.e57` al servidor MCP para el cálculo automático de la sobrerotura en CloudCompare."))
    story.append(Spacer(1, 0.3 * cm))

    # =========================================================================
    # EVALUACIÓN DE SOSTENIBILIDAD Y HUELLA DE CARBONO
    # =========================================================================
    story.append(ph1("ANEXO 9: EVALUACIÓN DE SOSTENIBILIDAD AMBIENTAL Y REDUCCIÓN DE HUELLA DE CARBONO"))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_primary, spaceAfter=8))
    story.append(p("La reducción de la sobre-excavación en la U.E.A. Lincuna genera un impacto ambiental positivo cuantificable en la reducción de emisiones de Gases de Efecto Invernadero (GEI):"))
    story.append(pb("• La fabricación de 1 tonelada de Cemento Portland Tipo I emite en promedio <b>0.82 TM de CO₂ equivalente</b>."))
    story.append(pb("• Cada metro cúbico de concreto proyectado (shotcrete) contiene 440 kg de cemento ($10.5\\text{ bolsas}$), emitiendo $360.8\\text{ kg CO}_2\\text{eq/m}^3$."))
    story.append(pb("• El ahorro directo de $5.70\\text{ m}^3$ de shotcrete por disparo evita la emisión de <b>2.056 TM de CO₂eq por frente disparado</b>."))
    story.append(pb("• Para el programa anual de 575 disparos (2,000 m de avance), la reducción total de emisiones alcanza <b>1,182.20 TM de CO₂ equivalente al año</b>."))
    story.append(p("Este balance ratifica que la optimización de la perforación y voladura mediante el sistema agéntico no solo optimiza la rentabilidad económica y la seguridad minera, sino que posiciona a la U.E.A. Lincuna como un referente en minería subterránea sostenible y descarbonización."))
    story.append(Spacer(1, 0.3 * cm))
