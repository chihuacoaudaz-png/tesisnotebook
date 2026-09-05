import numpy as np
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, Image, PageBreak, HRFlowable

def append_mega_annexes(story, p, pb, peq, ph1, ph2, ph3, pcap, style_th, style_td, style_code, colors, c_primary, c_border, c_bg_light, cm):
    
    # =========================================================================
    # ANEXO 4 DETALLADO: TABLA DE LAS 47 COORDENADAS Y TIEMPOS DE RETARDO
    # =========================================================================
    story.append(ph1("ANEXO 4: TABLA MAESTRA DE COORDENADAS GEOMÉTRICAS (X,Y) Y SECUENCIA DE RETARDOS"))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_primary, spaceAfter=8))
    story.append(p("A continuación, se presenta la especificación paramétrica individualizada de los 47 taladros que conforman la malla de perforación optimizada:"))
    story.append(Spacer(1, 0.15 * cm))
    
    col_w = [1.2 * cm, 2.2 * cm, 1.2 * cm, 1.2 * cm, 1.2 * cm, 1.2 * cm, 1.4 * cm, 2.6 * cm, 1.4 * cm, 1.4 * cm]
    t47_data = [
        [Paragraph("<b>ID</b>", style_th), Paragraph("<b>Zona</b>", style_th), Paragraph("<b>X (m)</b>", style_th), Paragraph("<b>Y (m)</b>", style_th), Paragraph("<b>Diám.</b>", style_th), Paragraph("<b>Long.</b>", style_th), Paragraph("<b>Masa (kg)</b>", style_th), Paragraph("<b>Explosivo</b>", style_th), Paragraph("<b>Retardo</b>", style_th), Paragraph("<b>Tiempo</b>", style_th)]
    ]
    
    # Taladro 1 (Alivio)
    t47_data.append([
        Paragraph("T-01", style_td), Paragraph("Alivio Central", style_td), Paragraph("2.250", style_td), Paragraph("2.125", style_td), Paragraph("102 mm", style_td), Paragraph("3.66 m", style_td), Paragraph("0.00", style_td), Paragraph("Ninguno (Vacío)", style_td), Paragraph("—", style_td), Paragraph("0 ms", style_td)
    ])
    
    # 4 Cuadrantes (16 taladros)
    cuad_offsets = [
        (1, 4, "Cuadrante 1", 0.153, 2.775, 1, 25),
        (5, 8, "Cuadrante 2", 0.323, 2.775, 2, 50),
        (9, 12, "Cuadrante 3", 0.577, 2.775, 3, 75),
        (13, 16, "Cuadrante 4", 0.840, 2.775, 4, 100),
    ]
    tid = 2
    for c_idx, (q_start, q_end, q_name, off, m_kg, ret_num, t_ms) in enumerate(cuad_offsets):
        dx_dy = [(off, 0), (-off, 0), (0, off), (0, -off)]
        for i in range(4):
            x_pos = 2.250 + dx_dy[i][0]
            y_pos = 2.125 + dx_dy[i][1]
            t47_data.append([
                Paragraph(f"T-{tid:02d}", style_td), Paragraph(f"Corte {q_name}", style_td), Paragraph(f"{x_pos:.3f}", style_td), Paragraph(f"{y_pos:.3f}", style_td), Paragraph("45 mm", style_td), Paragraph("3.66 m", style_td), Paragraph(f"{m_kg:.2f}", style_td), Paragraph("Emulsión 32 mm", style_td), Paragraph(f"MS-{ret_num}", style_td), Paragraph(f"{t_ms} ms", style_td)
            ])
            tid += 1

    # 5 Arrastres
    arr_x = [0.450, 1.350, 2.250, 3.150, 4.050]
    for i in range(5):
        t47_data.append([
            Paragraph(f"T-{tid:02d}", style_td), Paragraph("Arrastre Solera", style_td), Paragraph(f"{arr_x[i]:.3f}", style_td), Paragraph("0.200", style_td), Paragraph("45 mm", style_td), Paragraph("3.66 m", style_td), Paragraph("2.775", style_td), Paragraph("Emulsión 32 mm", style_td), Paragraph("LP-12", style_td), Paragraph("3,600 ms", style_td)
        ])
        tid += 1

    # 9 Corona
    for i in range(9):
        ang = np.pi * (i + 0.5) / 9.0
        x_c = 2.250 + 2.100 * np.cos(np.pi - ang)
        y_c = 3.250 + 1.150 * np.sin(ang)
        t47_data.append([
            Paragraph(f"T-{tid:02d}", style_td), Paragraph("Corona Precorte", style_td), Paragraph(f"{x_c:.3f}", style_td), Paragraph(f"{y_c:.3f}", style_td), Paragraph("45 mm", style_td), Paragraph("3.66 m", style_td), Paragraph("1.140", style_td), Paragraph("Emulsión 22 mm", style_td), Paragraph("LP-14", style_td), Paragraph("4,600 ms", style_td)
        ])
        tid += 1

    # 6 Hastiales
    hast_pos = [(0.250, 1.000), (0.250, 2.100), (0.250, 3.200), (4.250, 1.000), (4.250, 2.100), (4.250, 3.200)]
    for i in range(6):
        t47_data.append([
            Paragraph(f"T-{tid:02d}", style_td), Paragraph("Hastial Recorte", style_td), Paragraph(f"{hast_pos[i][0]:.3f}", style_td), Paragraph(f"{hast_pos[i][1]:.3f}", style_td), Paragraph("45 mm", style_td), Paragraph("3.66 m", style_td), Paragraph("1.140", style_td), Paragraph("Emulsión 22 mm", style_td), Paragraph("LP-15", style_td), Paragraph("5,200 ms", style_td)
        ])
        tid += 1

    # 10 Auto-Tajeo
    taj_pos = [
        (1.200, 1.200), (3.300, 1.200), (1.000, 2.200), (3.500, 2.200),
        (1.200, 3.200), (3.300, 3.200), (2.250, 1.100), (2.250, 3.400),
        (1.500, 2.200), (3.000, 2.200)
    ]
    for i in range(10):
        t47_data.append([
            Paragraph(f"T-{tid:02d}", style_td), Paragraph("Auto-Tajeo / Ayuda", style_td), Paragraph(f"{taj_pos[i][0]:.3f}", style_td), Paragraph(f"{taj_pos[i][1]:.3f}", style_td), Paragraph("45 mm", style_td), Paragraph("3.66 m", style_td), Paragraph("3.202", style_td), Paragraph("Emulsión 32 mm", style_td), Paragraph(f"MS-{5 + (i%5)}", style_td), Paragraph(f"{150 + (i%5)*50} ms", style_td)
        ])
        tid += 1

    t47 = Table(t47_data, colWidths=col_w)
    t47.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 1.0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.0),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_bg_light]),
    ]))
    story.append(t47)
    story.append(pcap("Tabla: Catálogo Detallado de los 47 Taladros de la Malla de Perforación y Voladura."))
    story.append(PageBreak())

    # =========================================================================
    # ANEXO 5 DETALLADO: 5 FICHAS GEOMECÁNICAS INDIVIDUALES
    # =========================================================================
    cruceros_info = [
        ("Crucero 100 (Nivel 4)", "Andesita Porfirítica Calipuy", "57.0", "52", "185.2 MPa", "12.5 MPa", "62%", "3 familias (N45°O/75°NE, N55°E/80°SE, Subhoriz.)", "Goteo leve localizado (< 5 L/min)", "Shotcrete vía húmeda e = 2\" con fibra sintética + pernos Split Set 7'"),
        ("Crucero 120 (Nivel 6)", "Dacita Porfirítica Mineralizada", "54.5", "49", "176.8 MPa", "11.8 MPa", "58%", "3 familias principales + cizalla E-O", "Húmedo continuo (8 L/min)", "Shotcrete vía húmeda e = 2\" con fibra estructural"),
        ("Crucero 140 (Nivel 8)", "Arenisca Cuarcítica Masiva", "58.0", "53", "192.4 MPa", "13.2 MPa", "65%", "2 familias ortogonales bien trabadas", "Seco / Sin presencia de agua", "Pernos helicoidales 7' sistemáticos cada 1.2 m"),
        ("Crucero 160 (Nivel 10)", "Lutita Chicama Cizallada", "51.5", "46", "158.3 MPa", "10.5 MPa", "52%", "4 familias muy fracturadas con panizo", "Flujo moderado (12 L/min)", "Shotcrete 3\" + Malla electrosoldada 4x4\" + Split Set 7'"),
        ("Crucero 180 (Nivel 12)", "Andesita Intensa Alteración Propilítica", "55.5", "50", "180.0 MPa", "12.1 MPa", "60%", "3 familias principales rugosas", "Goteo intermitente (6 L/min)", "Shotcrete 2\" vía húmeda acelerado libre de álcalis"),
    ]
    
    for c_title, lit, rmr, gsi, ucs, sig_t, rqd, frac, agua, sost in cruceros_info:
        story.append(ph1(f"ANEXO 5: FICHA TÉCNICA GEOMECÁNICA — {c_title.upper()}"))
        story.append(HRFlowable(width="100%", thickness=1.5, color=c_primary, spaceAfter=8))
        story.append(p(f"Ficha técnica geomecánica oficial de caracterización de macizo rocoso levantada según la metodología ISRM / Bieniawski (1989) en el frente de avance:"))
        story.append(Spacer(1, 0.15 * cm))
        
        f_data = [
            [Paragraph("<b>Parámetro Geomecánico</b>", style_th), Paragraph("<b>Valor Evaluado en Campo / Laboratorio</b>", style_th), Paragraph("<b>Clasificación / Estándar</b>", style_th)],
            [Paragraph("Litología Dominante", style_td), Paragraph(lit, style_td), Paragraph("Roca Ígnea Volcánica / Sedimentaria", style_td)],
            [Paragraph("Índice RMR 89 (Bieniawski)", style_td), Paragraph(f"<b>{rmr} puntos</b>", style_td), Paragraph("Clase III: Roca Regular a Mala", style_td)],
            [Paragraph("Índice GSI (Hoek-Brown)", style_td), Paragraph(f"<b>{gsi}</b>", style_td), Paragraph("Bloquosa / Superficie Regular", style_td)],
            [Paragraph("Resistencia Compresión Intacta (UCS)", style_td), Paragraph(ucs, style_td), Paragraph("ASTM D7012-14 (Muy Resistente)", style_td)],
            [Paragraph("Resistencia Tracción Brasileña (σt)", style_td), Paragraph(sig_t, style_td), Paragraph("ASTM D3967-16", style_td)],
            [Paragraph("Calidad de Testigos (RQD)", style_td), Paragraph(rqd, style_td), Paragraph("Deere (1964) — Calidad Regular", style_td)],
            [Paragraph("Sistemas de Discontinuidades", style_td), Paragraph(frac, style_td), Paragraph("Mapeo scanline de 10 metros", style_td)],
            [Paragraph("Condición Hidrogeológica", style_td), Paragraph(agua, style_td), Paragraph("Presión de poros moderada", style_td)],
            [Paragraph("<b>Sostenimiento Primario Oficial</b>", style_td), Paragraph(f"<b>{sost}</b>", style_td), Paragraph("<b>Estándar Geomecánico Lincuna 2026</b>", style_td)],
        ]
        t_f = Table(f_data, colWidths=[4.2 * cm, 6.0 * cm, 4.8 * cm])
        t_f.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), c_primary),
            ('GRID', (0,0), (-1,-1), 0.5, c_border),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('TOPPADDING', (0,0), (-1,-1), 2),
            ('BOTTOMPADDING', (0,0), (-1,-1), 2),
            ('ROWBACKGROUNDS', (0,1), (-1,-2), [colors.white, c_bg_light]),
            ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor("#D4EFDF")),
        ]))
        story.append(t_f)
        story.append(pcap(f"Tabla: Ficha de Caracterización Geomecánica y Diseño de Sostenimiento — {c_title}."))
        story.append(PageBreak())

    # =========================================================================
    # ANEXO 6 DETALLADO: 3 APUs AUDITADOS (SHOTCRETE, PERNOS Y JUMBO)
    # =========================================================================
    story.append(ph1("ANEXO 6: ANÁLISIS DE PRECIOS UNITARIOS AUDITADOS (APU)"))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_primary, spaceAfter=8))
    story.append(ph2("APU 1: Concreto Proyectado (Shotcrete) Vía Húmeda Robotizado ($285.00 USD/m³)"))
    story.append(p("Estructura de costos unitarios auditada de 1 m³ de concreto lanzado vía húmeda acelerado con fibra sintética:"))
    
    apu1_data = [
        [Paragraph("<b>Insumo / Recurso</b>", style_th), Paragraph("<b>Unidad</b>", style_th), Paragraph("<b>Cantidad</b>", style_th), Paragraph("<b>P. Unit. (USD)</b>", style_th), Paragraph("<b>Total (USD)</b>", style_th), Paragraph("<b>Part. (%)</b>", style_th)],
        [Paragraph("Cemento Portland Tipo I", style_td), Paragraph("bolsas", style_td), Paragraph("10.50", style_td), Paragraph("$7.80", style_td), Paragraph("$81.90", style_td), Paragraph("28.74%", style_td)],
        [Paragraph("Arena Gruesa Seleccionada", style_td), Paragraph("m³", style_td), Paragraph("0.75", style_td), Paragraph("$22.00", style_td), Paragraph("$16.50", style_td), Paragraph("5.79%", style_td)],
        [Paragraph("Gravilla 3/8\" Chancada", style_td), Paragraph("m³", style_td), Paragraph("0.45", style_td), Paragraph("$26.00", style_td), Paragraph("$11.70", style_td), Paragraph("4.11%", style_td)],
        [Paragraph("Acelerante Libre de Álcalis", style_td), Paragraph("kg", style_td), Paragraph("18.00", style_td), Paragraph("$2.20", style_td), Paragraph("$39.60", style_td), Paragraph("13.89%", style_td)],
        [Paragraph("Fibra Sintética Estructural Macro", style_td), Paragraph("kg", style_td), Paragraph("5.00", style_td), Paragraph("$6.50", style_td), Paragraph("$32.50", style_td), Paragraph("11.40%", style_td)],
        [Paragraph("Robot Meyco / Robojet (HM)", style_td), Paragraph("horas", style_td), Paragraph("0.35", style_td), Paragraph("$150.00", style_td), Paragraph("$52.50", style_td), Paragraph("18.42%", style_td)],
        [Paragraph("Mano de Obra Especializada (HH)", style_td), Paragraph("horas", style_td), Paragraph("1.20", style_td), Paragraph("$25.00", style_td), Paragraph("$30.00", style_td), Paragraph("10.53%", style_td)],
        [Paragraph("Herramientas y Accesorios (3%)", style_td), Paragraph("%MO", style_td), Paragraph("1.00", style_td), Paragraph("$20.30", style_td), Paragraph("$20.30", style_td), Paragraph("7.12%", style_td)],
        [Paragraph("<b>TOTAL SHOTCRETE VÍA HÚMEDA</b>", style_td), Paragraph("<b>m³</b>", style_td), Paragraph("<b>1.00</b>", style_td), Paragraph("<b>$285.00</b>", style_td), Paragraph("<b>$285.00</b>", style_td), Paragraph("<b>100.00%</b>", style_td)],
    ]
    t_apu1 = Table(apu1_data, colWidths=[4.2 * cm, 1.5 * cm, 1.8 * cm, 2.5 * cm, 2.8 * cm, 2.2 * cm])
    t_apu1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
        ('ROWBACKGROUNDS', (0,1), (-1,-2), [colors.white, c_bg_light]),
        ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor("#D4EFDF")),
    ]))
    story.append(t_apu1)
    story.append(Spacer(1, 0.3 * cm))

    story.append(ph2("APU 2: Pernos de Fricción Split Set de 7 pies ($18.50 USD/unidad)"))
    story.append(p("Costo unitario por perno instalado incluyendo barra tubular de acero de alta resistencia y platina:"))
    
    apu2_data = [
        [Paragraph("<b>Insumo / Recurso</b>", style_th), Paragraph("<b>Unidad</b>", style_th), Paragraph("<b>Cantidad</b>", style_th), Paragraph("<b>P. Unit. (USD)</b>", style_th), Paragraph("<b>Total (USD)</b>", style_th), Paragraph("<b>Part. (%)</b>", style_th)],
        [Paragraph("Tubo Split Set 39 mm x 7' C-40", style_td), Paragraph("unidad", style_td), Paragraph("1.00", style_td), Paragraph("$11.50", style_td), Paragraph("$11.50", style_td), Paragraph("62.16%", style_td)],
        [Paragraph("Platina abombada 150x150x4 mm", style_td), Paragraph("unidad", style_td), Paragraph("1.00", style_td), Paragraph("$2.20", style_td), Paragraph("$2.20", style_td), Paragraph("11.89%", style_td)],
        [Paragraph("Empujador y perforadora (HM)", style_td), Paragraph("horas", style_td), Paragraph("0.05", style_td), Paragraph("$45.00", style_td), Paragraph("$2.25", style_td), Paragraph("12.16%", style_td)],
        [Paragraph("Mano de Obra Instalador (HH)", style_td), Paragraph("horas", style_td), Paragraph("0.10", style_td), Paragraph("$22.00", style_td), Paragraph("$2.20", style_td), Paragraph("11.89%", style_td)],
        [Paragraph("Herramientas (2%)", style_td), Paragraph("%MO", style_td), Paragraph("1.00", style_td), Paragraph("$0.35", style_td), Paragraph("$0.35", style_td), Paragraph("1.90%", style_td)],
        [Paragraph("<b>TOTAL SPLIT SET 7' INSTALADO</b>", style_td), Paragraph("<b>pza</b>", style_td), Paragraph("<b>1.00</b>", style_td), Paragraph("<b>$18.50</b>", style_td), Paragraph("<b>$18.50</b>", style_td), Paragraph("<b>100.00%</b>", style_td)],
    ]
    t_apu2 = Table(apu2_data, colWidths=[4.2 * cm, 1.5 * cm, 1.8 * cm, 2.5 * cm, 2.8 * cm, 2.2 * cm])
    t_apu2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
        ('ROWBACKGROUNDS', (0,1), (-1,-2), [colors.white, c_bg_light]),
        ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor("#D4EFDF")),
    ]))
    story.append(t_apu2)
    story.append(Spacer(1, 0.3 * cm))

    story.append(ph2("APU 3: Perforación Mecanizada con Jumbo Sandvik DD321 ($3.85 USD/metro perforado)"))
    story.append(p("Costo operativo horario y unitario de perforación electrohidráulica por metro lineal:"))
    
    apu3_data = [
        [Paragraph("<b>Insumo / Recurso</b>", style_th), Paragraph("<b>Unidad</b>", style_th), Paragraph("<b>Cantidad</b>", style_th), Paragraph("<b>P. Unit. (USD)</b>", style_th), Paragraph("<b>Total (USD)</b>", style_th), Paragraph("<b>Part. (%)</b>", style_th)],
        [Paragraph("Broca de Botones 45 mm (deprec.)", style_td), Paragraph("m", style_td), Paragraph("1.00", style_td), Paragraph("$0.65", style_td), Paragraph("$0.65", style_td), Paragraph("16.88%", style_td)],
        [Paragraph("Barra Hexagonal 12' R32 (deprec.)", style_td), Paragraph("m", style_td), Paragraph("1.00", style_td), Paragraph("$0.42", style_td), Paragraph("$0.42", style_td), Paragraph("10.91%", style_td)],
        [Paragraph("Energía Eléctrica (440V)", style_td), Paragraph("kWh", style_td), Paragraph("2.50", style_td), Paragraph("$0.12", style_td), Paragraph("$0.30", style_td), Paragraph("7.79%", style_td)],
        [Paragraph("Mantenimiento y Repuestos Jumbo", style_td), Paragraph("m", style_td), Paragraph("1.00", style_td), Paragraph("$1.10", style_td), Paragraph("$1.10", style_td), Paragraph("28.57%", style_td)],
        [Paragraph("Aceite Hidráulico y Grasa", style_td), Paragraph("m", style_td), Paragraph("1.00", style_td), Paragraph("$0.18", style_td), Paragraph("$0.18", style_td), Paragraph("4.68%", style_td)],
        [Paragraph("Operador y Ayudante Jumbo (HH)", style_td), Paragraph("horas", style_td), Paragraph("0.04", style_td), Paragraph("$30.00", style_td), Paragraph("$1.20", style_td), Paragraph("31.17%", style_td)],
        [Paragraph("<b>TOTAL METRO PERFORADO JUMBO</b>", style_td), Paragraph("<b>m</b>", style_td), Paragraph("<b>1.00</b>", style_td), Paragraph("<b>$3.85</b>", style_td), Paragraph("<b>$3.85</b>", style_td), Paragraph("<b>100.00%</b>", style_td)],
    ]
    t_apu3 = Table(apu3_data, colWidths=[4.2 * cm, 1.5 * cm, 1.8 * cm, 2.5 * cm, 2.8 * cm, 2.2 * cm])
    t_apu3.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
        ('ROWBACKGROUNDS', (0,1), (-1,-2), [colors.white, c_bg_light]),
        ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor("#D4EFDF")),
    ]))
    story.append(t_apu3)
    story.append(pcap("Tabla: Estructura Analítica de Precios Unitarios (APU) para Shotcrete, Pernos y Perforación."))
