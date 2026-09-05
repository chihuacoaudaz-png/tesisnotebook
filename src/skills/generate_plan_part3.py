# -*- coding: utf-8 -*-
"""
PLAN DE TESIS OFICIAL UNI FIGMM - PARTE 3: MARCO CONCEPTUAL Y METODOLOGÍA
Estructura según PLAN DE TESIS (1).docx:
- MARCO CONCEPTUAL (Glosario enciclopédico de 45+ términos)
- METODOLOGÍA:
  - TIPO Y DISEÑO DE LA INVESTIGACIÓN (Enfoque con tabla comparativa, Alcance, Diseño)
  - UNIDAD DE ANÁLISIS
  - ETAPAS DE LA INVESTIGACIÓN (Recolección, Procesamiento, Análisis de datos)
"""

from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, Image, PageBreak, HRFlowable

def append_plan_part3(story, p, pb, peq, ph1, ph2, ph3, pcap, style_th, style_td, style_code, colors, c_primary, c_border, c_bg_light, cm):
    # MARCO CONCEPTUAL
    story.append(ph1("MARCO CONCEPTUAL"))
    story.append(HRFlowable(width="100%", thickness=1.0, color=c_primary, spaceAfter=8))
    
    conceptos = [
        ("Aceleración Lateral Dinámica", "Aceleración tangencial inducida en las partículas del macizo rocoso como consecuencia de la propagación de ondas de choque de corte y tracción durante la detonación."),
        ("Agente Autónomo (AI Agent)", "Entidad de software basada en modelos de lenguaje y reglas formales que percibe su entorno operativo, razona sobre restricciones físicas y ejecuta acciones de diseño para alcanzar objetivos específicos sin intervención humana continua."),
        ("Algoritmo de Auto-Tajeo Espacial", "Procedimiento computacional determinístico que optimiza la posición espacial y la carga de los taladros de ayuda en el núcleo de una excavación subterránea para garantizar una distribución homogénea de energía."),
        ("Alivio Central (Taladro Escariado)", "Taladro no cargado de gran diámetro (102 mm) perforado en el centro del arranque que proporciona la superficie libre inicial requerida para la expansión volumétrica de la roca."),
        ("Área de Sección Nominal", "Superficie teórica de diseño de la labor subterránea delimitada por las especificaciones de planeamiento minero (19.04 m² para la sección baúl de 4.50 m × 4.50 m)."),
        ("Arranque en Cuatro Cuadrantes", "Geometría de corte de barrenos paralelos dispuestos en cuadrados concéntricos alrededor del alivio central que detonan secuencialmente para aperturar la cavidad primaria."),
        ("Bases de Datos Operacionales", "Conjuntos estructurados de registros diarios de mina correspondientes a metros perforados, avance lineal, consumo de explosivos, horómetros de jumbos y volumen de shotcrete."),
        ("Burden Práctico (Bp)", "Distancia geométrica perpendicular más corta medida desde un barreno cargado hasta la superficie libre más cercana hacia la cual se proyectará el material volado."),
        ("Celdas de Voronoi", "Partición matemática del espacio euclidiano donde cada región contiene todos los puntos más cercanos a un barreno específico que a cualquier otro, utilizada para calcular el factor de carga puntual."),
        ("Compuerta de Calidad Geomecánica", "Restricción física inviolable impuesta en el software agéntico que impide aprobar cualquier diseño de malla si la presión efectiva en pared supera la resistencia compresiva ($P_{te} > UCS$)."),
        ("Concreto Proyectado (Shotcrete) Vía Húmeda", "Mezcla de cemento Portland, áridos seleccionados, agua, microsílice, aditivos superplastificantes y fibra estructural lanzada neumáticamente a alta velocidad sobre las paredes de la excavación."),
        ("Desacoplamiento de Carga", "Relación geométrica entre el diámetro de la columna de explosivo y el diámetro del barreno ($d_c / d_h < 1.0$), utilizada para amortiguar el pulso de presión hidrodinámica transmitido a la roca."),
        ("Diseño Cuasiexperimental Longitudinal", "Esquema de contrastación científica en el cual se evalúan mediciones cuantitativas repetidas en una misma unidad de análisis antes y después de aplicar un tratamiento tecnológico."),
        ("Distancia Punto a Malla (Cloud-to-Mesh / C2M)", "Distancia euclidiana tridimensional calculada en software de fotogrametría entre cada vértice de la nube de puntos LIDAR y la superficie poligonal del sólido 3D de diseño."),
        ("Ecuación de Estado de Jones-Wilkins-Lee (JWL)", "Formulación termodinámica empírica que describe la presión de expansión isentrópica generada por los gases de detonación de un explosivo condensado."),
        ("Efecto Arco (Rock Arching)", "Fenómeno mecánico mediante el cual un macizo rocoso competente transfiere los esfuerzos litostáticos alrededor de una cavidad excavada hacia los hastiales sin colapsar."),
        ("Eficiencia de Avance Lineal", "Relación porcentual entre la longitud efectiva de avance longitudinal lograda tras el disparo y la longitud total perforada de los barrenos ($Avance / H_p \\times 100$)."),
        ("Emulsión Matriz Encartuchada", "Explosivo industrial resistente al agua constituido por una emulsión de microgotas de nitrato de amonio dispersas en una fase continua de hidrocarburos, sensibilizada mediante microesferas de vidrio."),
        ("Escáner Láser Terrestre 3D (LIDAR)", "Instrumento optoelectrónico de medición topográfica que emite pulsos láser de alta frecuencia para capturar millones de coordenadas espaciales tridimensionales (x, y, z) de la labor minera."),
        ("Espaciamiento Práctico (Sp)", "Distancia lineal entre barrenos contiguos pertenecientes a una misma fila o sección de voladura."),
        ("Exponente Adiabático (Gamma)", "Relación entre los calores específicos a presión y volumen constante de los gases de detonación ($\gamma \approx 3.0$ en emulsiones)."),
        ("Factor de Carga Lineal (ql)", "Masa de material explosivo activo contenida por cada metro lineal de longitud de barreno ($kg/m$)."),
        ("Factor de Fijación de Gustafsson (f)", "Coeficiente empírico adimensional que cuantifica la resistencia adicional al despegue de la roca en barrenos de arrastre debido a la fricción de la solera y la gravedad ($f = 1.45$)."),
        ("Factor de Media Caña (Half-Cast Factor / HCF)", "Porcentaje de la longitud total de las trazas visibles de los barrenos de contorno que permanecen intactas en la roca tras la voladura respecto a la longitud perforada teórica."),
        ("Factor de Potencia (qp)", "Cantidad de energía o masa de explosivo utilizada por unidad de volumen o masa de roca excavada ($kg/m^3$ o $kg/t$)."),
        ("Frentes de Avance Horizontal", "Labores subterráneas de desarrollo y preparación (cruceros, galerías, rampas) excavadas en dirección predominantemente subhorizontal."),
        ("Índice RMR 89 de Bieniawski", "Sistema de clasificación geomecánica que evalúa la calidad del macizo rocoso mediante la suma ponderada de seis parámetros de campo y laboratorio."),
        ("Iterative Closest Point (ICP)", "Algoritmo computacional de alineamiento espacial que minimiza iterativamente el error cuadrático medio entre dos nubes de puntos 3D superpuestas."),
        ("Jumbo Electrohidráulico", "Equipo mecanizado autopropulsado equipado con brazos articulados y perforadoras hidráulicas pesadas para perforar frentes subterráneos con alta precisión geométrica."),
        ("Línea Base Operacional", "Conjunto de indicadores históricos cuantitativos de perforación, voladura, costos y sobrerotura medidos con anterioridad a la implementación del sistema agéntico."),
        ("Malla de Perforación y Voladura", "Distribución geométrica espacial, inclinación, longitud y diámetro de los barrenos en el frente de disparo."),
        ("Model Context Protocol (MCP)", "Protocolo de comunicación abierto y estandarizado que permite a los modelos de inteligencia artificial interactuar de forma segura con herramientas externas, algoritmos y bases de datos."),
        ("Modelo de Holmberg-Persson", "Metodología analítica determinística para el cálculo de mallas de voladura subterránea en frentes de avance basada en criterios de daño por velocidad pico de partícula."),
        ("Nube de Puntos 3D", "Conjunto masivo de coordenadas tridimensionales capturadas mediante escaneo láser que representan fielmente la geometría superficial de la cavidad minera."),
        ("Presión de Detonación Chapman-Jouguet (Pt)", "Presión hidrodinámica máxima instantánea alcanzada en el plano sónico de término de la reacción química del explosivo."),
        ("Presión Efectiva Desacoplada en Pared (Pte)", "Presión estática y dinámica transmitida a las paredes del barreno tras la expansión radial de los gases de detonación en el espacio anular."),
        ("Prueba t-Student Pareada", "Prueba estadística paramétrica que determina si existe una diferencia estadísticamente significativa entre las medias de dos grupos de mediciones relacionadas (pre-test vs post-test)."),
        ("Red Team Agéntico (Agente Escéptico)", "Módulo autónomo de supervisión programado para identificar fallas, inconsistencias matemáticas y violaciones de restricciones geomecánicas en el diseño propuesto."),
        ("Resistencia a la Compresión Uniaxial (UCS)", "Esfuerzo axial compresivo máximo que puede soportar una probeta cilíndrica de roca intacta antes de fracturarse según la norma ASTM D7012-14."),
        ("Resistencia a la Tracción Brasileña (Sigma-t)", "Esfuerzo de tracción indirecto máximo soportado por un disco de roca intacta sometido a compresión diametral diametral según ASTM D3967-16."),
        ("Rimado de Corte", "Operación de ensanchamiento mecánico de uno o más barrenos centrales en el arranque para crear una cavidad vacía de alivio."),
        ("Sobrerotura (Overbreak)", "Volumen o porcentaje de roca excavada en exceso por fuera del límite geométrico teórico proyectado para la sección de la labor subterránea."),
        ("Tamaño del Efecto de Cohen (d)", "Métrica estadística estandarizada que cuantifica la magnitud real del impacto de un tratamiento experimental independientemente del tamaño de muestra."),
        ("Velocidad de Detonación (VOD)", "Velocidad a la cual se propaga la onda de choque exotérmica a lo largo de la columna de explosivo ($m/s$)."),
        ("Velocidad Pico de Partícula (PPV)", "Velocidad máxima alcanzada por una partícula del macizo rocoso al ser perturbada por las ondas sísmicas inducidas por la detonación ($mm/s$)."),
    ]

    for term, desc in conceptos:
        story.append(pb(f"<b>{term}:</b> {desc}"))
    story.append(Spacer(1, 0.3 * cm))

    # METODOLOGÍA
    story.append(ph1("METODOLOGÍA"))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_primary, spaceAfter=8))
    
    story.append(ph2("TIPO Y DISEÑO DE LA INVESTIGACIÓN"))
    story.append(Spacer(1, 0.15 * cm))

    # Enfoque de la investigación
    story.append(ph3("Enfoque de la investigación"))
    story.append(p("La presente investigación se desarrollará bajo un <b>enfoque cuantitativo</b>, caracterizado por la medición objetiva, rigurosa y numérica de variables físicas (presión en pared de barreno, velocidad pico de partícula, factor de potencia, volumen excavado y coordenadas 3D) y el análisis inferencial mediante pruebas estadísticas paramétricas. A continuación, se presenta la contrastación formal entre el enfoque cualitativo y el enfoque cuantitativo según los estándares metodológicos de la UNI FIGMM:"))
    
    enfoque_data = [
        [Paragraph("<b>Características</b>", style_th), Paragraph("<b>Investigación cualitativa</b>", style_th), Paragraph("<b>Investigación cuantitativa (Presente Estudio)</b>", style_th)],
        [Paragraph("Percepción de la realidad", style_td), Paragraph("Subjetiva. Incluyente.", style_td), Paragraph("<b>Objetiva. Excluyente de sesgos personales.</b>", style_td)],
        [Paragraph("Razonamiento", style_td), Paragraph("Inductivo. Genera hipótesis exploratorias.", style_td), Paragraph("<b>Deductivo. Contrasta y valida hipótesis causales.</b>", style_td)],
        [Paragraph("Recolección de datos", style_td), Paragraph("Entrevistas abiertas, observaciones cualitativas no estructuradas.", style_td), Paragraph("<b>Mediciones instrumentadas con escáner láser 3D LIDAR, bases de datos operacionales y ensayos normalizados ASTM.</b>", style_td)],
        [Paragraph("Análisis de datos", style_td), Paragraph("Análisis temático, discurso, categorías narrativas.", style_td), Paragraph("<b>Estadística descriptiva e inferencial (pruebas t-Student, ANOVA, cálculo de d de Cohen y p-valores).</b>", style_td)],
        [Paragraph("Naturaleza de resultados", style_td), Paragraph("Descriptiva contextual, comprensión de fenómenos individuales.", style_td), Paragraph("<b>Generalizable, replicable, determinística y basada en leyes físicas de la hidrodinámica de detonación.</b>", style_td)],
        [Paragraph("Finalidad primordial", style_td), Paragraph("Interpretar percepciones y significados sociales.", style_td), Paragraph("<b>Demostrar relaciones de causalidad ($X \\to Y$) y cuantificar la reducción de sobrerotura y sobrecostos.</b>", style_td)],
        [Paragraph("Control de variables", style_td), Paragraph("Bajo o nulo control experimental en entorno natural.", style_td), Paragraph("<b>Riguroso control de variables mediante compuertas de calidad físicas ($P_{te} \\le UCS$) y algoritmos deterministicos.</b>", style_td)],
    ]
    t_enf = Table(enfoque_data, colWidths=[3.2 * cm, 5.0 * cm, 7.8 * cm])
    t_enf.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_bg_light]),
    ]))
    story.append(t_enf)
    story.append(pcap("Tabla: Comparativa Metodológica entre Investigación Cualitativa y Cuantitativa (Estándar UNI FIGMM)."))
    story.append(Spacer(1, 0.2 * cm))

    # Alcance de la investigación
    story.append(ph3("Alcance de la investigación"))
    story.append(p("El alcance del proyecto será de nivel <b>explicativo y correlacional-cuantitativo</b>. Es explicativo porque determina y demuestra los mecanismos físicos de causalidad que originan la sobre-excavación en labores subterráneas (sobrepresión por encima del $UCS$, confinamiento excesivo en el corte y falta de paralelismo) y valida el mecanismo mediante el cual el desacoplamiento hidrodinámico y el auto-tajeo espacial erradican dicho daño. Es correlacional porque establece el grado de relación matemática entre variables independientes (factor de desacoplamiento, relación de burden, factor de potencia) y variables dependientes (porcentaje de sobrerotura, factor de media caña y costos de shotcrete)."))
    story.append(Spacer(1, 0.15 * cm))

    # Diseño de la investigación
    story.append(ph3("Diseño de la investigación"))
    story.append(p("Se adoptará un <b>diseño cuasiexperimental longitudinal de tipo pre-test / post-test con grupo de control temporal</b>:"))
    story.append(peq("$$G: \\quad O_1 \\quad \\longrightarrow \\quad X \\quad \\longrightarrow \\quad O_2$$"))
    story.append(p("Donde $G$ representa los frentes de avance en la U.E.A. Lincuna, $O_1$ representa la línea base histórica de 30 voladuras convencionales evaluadas con escáner 3D (pre-test), $X$ representa la intervención tecnológica mediante la implementación del Sistema Agéntico Autónomo y la malla optimizada de 47 taladros, y $O_2$ representa la medición post-intervención en 30 voladuras instrumentadas."))
    story.append(Spacer(1, 0.2 * cm))

    # UNIDAD DE ANÁLISIS
    story.append(ph2("UNIDAD DE ANÁLISIS"))
    story.append(p("La unidad de análisis está constituida por los <b>frentes de avance horizontal mecanizado en cruceros de exploración y galerías de extracción en sección tipo baúl de 4.50 m de ancho por 4.50 m de altura</b> pertenecientes a los Niveles 4, 6, 8, 10 y 12 de la U.E.A. Lincuna, perforados en macizo rocoso volcánico Tipo III-B/IV-A con jumbos Sandvik DD321 y barras de 12 pies."))
    story.append(Spacer(1, 0.2 * cm))

    # ETAPAS DE LA INVESTIGACIÓN
    story.append(ph2("ETAPAS DE LA INVESTIGACIÓN"))
    story.append(Spacer(1, 0.15 * cm))

    story.append(ph3("Recolección de datos"))
    story.append(p("La recolección de información primaria y secundaria se estructurará a partir de cinco fuentes operacionales de datos reales:"))
    story.append(pb("<b>1. Registros de Avances (`1. BD AVANCES.xlsx`):</b> Registro sistemático de longitud perforada, avance efectivo lineal y volumen excavado."))
    story.append(pb("<b>2. Reportes Diarios de Voladura (`2. REPORTE DE VOLADURA  2026.xlsx`):</b> Detalle de taladros cargados, tipo de emulsión (22/32 mm), accesorios de detonación no eléctrica y factor de potencia."))
    story.append(pb("<b>3. Base de Datos de Jumbos (`3. BD TL JUMBOS 2026.xlsx`):</b> Presiones de percusión (180 bar), rotación (55 bar), velocidad de penetración (1.85 m/min) y desgaste de brocas de 45 mm."))
    story.append(pb("<b>4. Base de Datos de Limpieza (`5. BD-SCOOP 2026.xlsx`):</b> Tiempos de ciclo de carguío y acarreo con scooptramps Cat R1600 y volquetes dumper."))
    story.append(pb("<b>5. Base de Datos de Sostenimiento (`6. BD SOSTENIMIENTO METALICO.xlsx`):</b> Consumo cúbico de shotcrete vía húmeda robotizado y número de pernos Split Set instalados."))
    story.append(Spacer(1, 0.15 * cm))

    story.append(ph3("Procesamiento de la información"))
    story.append(p("El procesamiento de datos se desarrollará mediante el siguiente flujo computacional:"))
    story.append(pb("<b>Fase A (Ingesta y Limpieza de Datos):</b> Scripts en Python para consolidar variables geomecánicas y operacionales."))
    story.append(pb("<b>Fase B (Ejecución del Agente Solver):</b> Cálculo analítico del modelo de Holmberg-Persson en 5 secciones y generación de coordenadas (X, Y)."))
    story.append(pb("<b>Fase C (Auditoría del Red Team):</b> Verificación de compuertas de seguridad ($P_{te} \le UCS$)."))
    story.append(pb("<b>Fase D (Procesamiento 3D LIDAR):</b> Filtrado SOR, alineamiento ICP y cálculo de distancia punto a malla (C2M) en CloudCompare."))
    story.append(Spacer(1, 0.15 * cm))

    story.append(ph3("Análisis de la información"))
    story.append(p("El análisis inferencial comprenderá la aplicación de la prueba t-Student para muestras pareadas, la prueba t de 1 muestra contra la meta operacional ($\le 5.0\%$), el Análisis de Varianza (ANOVA) entre los 5 cruceros de prueba, el modelamiento de curvas granulométricas en Split-Desktop y la formulación del flujo de caja descontado proyectado a 5 años."))
    story.append(Spacer(1, 0.3 * cm))
