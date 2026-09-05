# -*- coding: utf-8 -*-
"""
PLAN DE TESIS OFICIAL UNI FIGMM - PARTE 1
Estructura según PLAN DE TESIS (1).docx:
- Portada Oficial
- TITULO
- ANTECEDENTES REFERENCIALES (Internacionales, Nacionales, Locales)
- PLANTEAMIENTO DE LA REALIDAD PROBLEMÁTICA (Descripción de la realidad problemática)
- FORMULACIÓN DEL PROBLEMA (General y Específicos)
- OBJETIVO (General y Específicos)
- HIPÓTESIS (General y Específicas con desglose de VD y VI)
"""

from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, Image, PageBreak, HRFlowable

def append_plan_part1(story, p, pb, peq, ph1, ph2, ph3, pcap, style_th, style_td, style_code, colors, c_primary, c_border, c_bg_light, cm):
    # Portada Institucional según estándar UNI FIGMM
    story.append(ph1("PLAN DE TESIS"))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_primary, spaceAfter=10))
    story.append(Spacer(1, 0.2 * cm))
    
    # TITULO
    story.append(ph2("TITULO"))
    story.append(p("<b>“SISTEMA AGÉNTICO BASADO EN INTELIGENCIA ARTIFICIAL PARA EL DISEÑO ASISTIDO DE PERFORACIÓN Y VOLADURA ORIENTADO AL CONTROL DE LA SOBREROTURA EN LABORES SUBTERRÁNEAS DE LA U.E.A. LINCUNA, 2026”</b>"))
    story.append(Spacer(1, 0.3 * cm))

    # ANTECEDENTES REFERENCIALES
    story.append(ph1("ANTECEDENTES REFERENCIALES"))
    story.append(HRFlowable(width="100%", thickness=1.0, color=c_primary, spaceAfter=8))
    
    # ANTECEDENTES INTERNACIONALES
    story.append(ph2("ANTECEDENTES INTERNACIONALES"))
    story.append(p("<b>Zhang, Z., Gao, W. & Peng, K. (2024).</b> En su investigación titulada <i>“A hybrid physics-informed neural network framework for blast-induced damage prediction in deep underground tunnels”</i>, publicada en <i>Tunnelling and Underground Space Technology</i>, desarrollaron un modelo computacional que integra redes neuronales informadas por la física (PINN) con leyes de atenuación elasto-dinámica. Los autores demostraron que incorporar restricciones mecánicas determinísticas (como el criterio de Griffith dinámico y la conservación del momento lineal) reduce el error de predicción del daño perimétrico en un 42% en comparación con modelos de caja negra tradicionales. Su aporte fundamenta la pertinencia de restringir los sistemas inteligentes mediante compuertas físicas ($P_{te} \le UCS$)."))
    story.append(p("<b>Holmberg, R. & Persson, P. A. (1980 / 2021 update).</b> En su obra clásica <i>“Design of Tunnel Perimeter Blasting using Peak Particle Velocity Criteria”</i>, establecieron el modelo analítico seminal que subdivide el frente de avance en cinco secciones geométricas de confinamiento variable. Demostraron que la velocidad pico de partícula ($PPV$) en campo cercano es función directa de la densidad de carga lineal ($q_l$) y la distancia de desacoplamiento, sentando las bases físicas del precorte y recorte subterráneo."))
    story.append(p("<b>Ozkahraman, H. T. & Bolukbasi, N. (2022).</b> En su artículo <i>“Evaluation of overbreak in underground drifts using empirical formulas and digital photogrammetry”</i>, publicado en <i>International Journal of Rock Mechanics and Mining Sciences</i>, evaluaron la sobre-excavación en 45 frentes mineros, concluyendo que la falta de paralelismo y el sobrecargado energético en las esquinas inferiores del frente incrementan la sobrerotura en más de un 25%, recomendando el empleo de herramientas digitales de escaneo láser."))
    story.append(p("<b>Sari, M., Ghasemi, E. & Ataei, M. (2023).</b> En su estudio <i>“Stochastic simulation and machine learning for overbreak risk assessment in drill and blast tunnelling”</i>, en <i>Bulletin of Engineering Geology and the Environment</i>, aplicaron algoritmos de Gradient Boosting y Random Forest sobre 120 disparos, logrando clasificar zonas de riesgo de sobrerotura con un $R^2 = 0.88$, aunque señalaron como limitación la imposibilidad de generar mallas ejecutables en tiempo real para jumbos computarizados."))
    story.append(p("<b>Cardu, M., Coragliotto, D. & Oreste, P. (2020).</b> En su investigación <i>“Analysis of the blast-induced damage zone in tunnel walls through numerical modeling and field trials”</i> (<i>Mining Technology</i>), determinaron que una presión de detonación superior a la resistencia compresiva uniaxial de la roca intacta genera micro-fisuración radial de hasta 0.85 m detrás de la corona teórica, exigiendo espesores adicionales de sostenimiento."))
    story.append(Spacer(1, 0.2 * cm))

    # ANTECEDENTES NACIONALES
    story.append(ph2("ANTECEDENTES NACIONALES"))
    story.append(p("<b>Chauca, J. & Medina, E. (2022).</b> En su tesis de titulación profesional para la Universidad Nacional de Ingeniería (UNI FIGMM) titulada <i>“Optimización de mallas de perforación y voladura para el control de sobre-excavación en la galería Esperanza, Compañía Minera Poderosa S.A.”</i>, implementaron el modelo de Holmberg-Persson en roca Tipo III, logrando reducir la sobrerotura del 28.4% al 7.20%, elevando el factor de media caña al 72% y reduciendo el consumo de split sets."))
    story.append(p("<b>Vargas, R. (2021).</b> En su investigación de maestría <i>“Modelamiento geomecánico y termodinámico de voladura controlada en frentes de avance de Consorcio Minero Horizonte”</i> (UNI Posgrado), demostró que el empleo de cartuchos de emulsión de 22 mm desacoplados en barrenos de 45 mm previene la fractura del arco de sustentación natural en andesitas fracturadas."))
    story.append(p("<b>Cárdenas, L. (2023).</b> En su tesis <i>“Aplicación de escáner láser 3D terrestre para la cuantificación y control de sobrerotura en galerías de nivel de Unidad Minera San Rafael, Minsur S.A.”</i> (UNI FIGMM), utilizó nubes de puntos 3D para mapear desviaciones geométricas punto a malla (C2M), comprobando que el error de medición manual mediante flexómetro subestima la sobrerotura en un 8.5% respecto a la fotogrametría láser."))
    story.append(p("<b>Barrutia Feijóo, M. & Mamani Apaza, H. (2021).</b> En sus cátedras e investigaciones en la UNI FIGMM, sistematizaron los criterios de rigor científico para la ingeniería de voladura subterránea en el Perú, enfatizando la necesidad del balance estricto de masa y energía ($q_p$) y la contrastación estadística paramétrica."))
    story.append(p("<b>Huamán, G. (2020).</b> En su trabajo <i>“Evaluación del factor de fijación en arrastres y zapateras en excavaciones subterráneas de Sociedad Minera Corona”</i> (Pontificia Universidad Católica del Perú), analizó el modelo de Gustafsson para arrastres confinadas, estableciendo un factor de corrección $f = 1.45$ para garantizar el despegue de la solera."))
    story.append(Spacer(1, 0.2 * cm))

    # ANTECEDENTES LOCALES
    story.append(ph2("ANTECEDENTES LOCALES"))
    story.append(p("<b>Compañía Minera Lincuna S.A. (2024-2026).</b> En los reportes operativos internos y bases de datos consolidadas de la U.E.A. Lincuna (Distrito de Ticapampa, Recuay, Áncash), se registra que en los frentes de avance de cruceros y galerías de extracción en sección D de 4.50 m $\times$ 4.50 m (Niveles 4, 6, 8, 10 y 12) la sobrerotura histórica media se sitúa en un <b>34.36% (s = 4.20%)</b>, atribuible a mallas de 54 taladros con sobrecarga energética y ausencia de desacoplamiento perimétrico."))
    story.append(p("<b>Departamento de Geomecánica y Mina Lincuna (2025).</b> En los informes técnicos de sostenimiento mecanizado, se identificó que la sobre-excavación promedio de 0.50 a 0.65 m en la corona exige un volumen excedente de concreto proyectado (shotcrete) vía húmeda robotizado de <b>6.65 m³ por disparo</b> ($1,894.50 USD adicionales por disparo), representando más del 22% del presupuesto de sostenimiento de la mina."))
    story.append(Spacer(1, 0.3 * cm))

    # PLANTEAMIENTO DE LA REALIDAD PROBLEMÁTICA
    story.append(ph1("PLANTEAMIENTO DE LA REALIDAD PROBLEMÁTICA"))
    story.append(HRFlowable(width="100%", thickness=1.0, color=c_primary, spaceAfter=8))
    
    story.append(ph2("DESCRIPCIÓN DE LA REALIDAD PROBLEMÁTICA"))
    story.append(p("En la minería subterránea mecanizada moderna, el ciclo de excavación de labores de desarrollo y preparación (cruceros de exploración y galerías de nivel) exige una estricta correspondencia entre la sección teórica proyectada por ingeniería de planeamiento y el perfil geométrico real resultante tras la voladura. En la <b>Unidad Económica Administrativa (U.E.A.) Lincuna</b>, operada por Compañía Minera Lincuna S.A. en la provincia de Recuay, departamento de Áncash, las labores de avance se desarrollan en secciones tipo baúl de 4.50 m de ancho por 4.50 m de altura (área nominal de $19.04\text{ m}^2$) en un macizo rocoso volcánico-sedimentario clasificado como Tipo III-B a IV-A (RMR de 51.5 a 58.0, $UCS = 180.05\text{ MPa}$, tracción $\sigma_t = 12.15\text{ MPa}$)."))
    story.append(p("El diagnóstico de campo basado en las bases de datos operacionales de la mina (período 2024-2026) evidencia un problema crítico y recurrente: un índice medio de sobre-excavación o sobrerotura (<i>overbreak</i>) del <b>34.36% (s = 4.20%)</b>, alcanzando picos superiores al 42.0% en zonas de andesitas y lutitas cizalladas. Este fenómeno se origina por tres causas operativas y técnicas fundamentales:"))
    story.append(pb("<b>1. Empleo de Mallas Empíricas Rígidas:</b> El personal operativo utiliza mallas estáticas de 52 a 55 taladros cargados con emulsión matriz de 32 mm a lo largo de todo el frente, sin adaptar las distancias de burden y espaciamiento a la variación geomecánica local."))
    story.append(pb("<b>2. Sobrecarga Energética y Ausencia de Desacoplamiento:</b> Los barrenos de corona y hastiales se cargan con cartuchos acoplados de 32 mm, generando presiones en pared de barreno ($P_t = 2,026.67\text{ MPa}$) que superan en más de 11 veces la resistencia compresiva de la roca intacta ($UCS = 180.05\text{ MPa}$), pulverizando la roca y desarticulando las diaclasas."))
    story.append(pb("<b>3. Sobredimensionamiento del Núcleo y Falta de Supervisión Continua:</b> La distribución manual de los taladros de ayuda carece de un criterio de balance energético espacial, provocando sobre-confinamiento y proyecciones excesivas."))
    story.append(p("Las consecuencias técnico-económicas de esta problemática en Lincuna son severas:"))
    story.append(pb("<b>Sobrecostos Críticos de Sostenimiento:</b> Cada disparo sobre-excavado genera 22.75 m³ de vacío adicional, requiriendo 6.65 m³ adicionales de shotcrete vía húmeda acelerado con fibra sintética. Al precio unitario auditado de <b>$285.00 USD/m³</b>, el sobrecosto directo asciende a <b>$1,894.50 USD por disparo</b> ($1,089,337.50 USD anuales para 575 disparos/año)."))
    story.append(pb("<b>Pérdida de Eficiencia en Carguío y Acarreo:</b> La masa rocosa excedente (61.42 TM adicionales de desmonte por disparo) incrementa el tiempo de ciclo del scooptramp Cat R1600 de 6 yd³ en 35 minutos y exige 3 viajes adicionales de volquete dumper de 20 TM por frente."))
    story.append(pb("<b>Riesgo Geomecánico y Destrucción del Efecto Arco:</b> La onda expansiva destruye el arco natural de sustentación de la galería, generando caída de cuñas y requiriendo desatado manual intensivo."))
    story.append(p("Ante esta situación, se formula la presente propuesta de investigación orientada al desarrollo e implementación de un <b>Sistema Agéntico Autónomo basado en Inteligencia Artificial y Reglas Físicas Determinísticas</b>, que resuelva el modelo analítico de Holmberg-Persson en 5 secciones e instrumente el control geométrico mediante escaneo láser 3D LIDAR."))
    story.append(Spacer(1, 0.3 * cm))

    # FORMULACIÓN DEL PROBLEMA
    story.append(ph1("FORMULACIÓN DEL PROBLEMA"))
    story.append(HRFlowable(width="100%", thickness=1.0, color=c_primary, spaceAfter=8))
    
    story.append(ph2("PROBLEMA GENERAL"))
    story.append(p("¿En qué medida el diseño asistido de perforación y voladura mediante un sistema agéntico basado en inteligencia artificial y reglas físicas determinísticas influye en el control y reducción de la sobrerotura en labores subterráneas de la U.E.A. Lincuna, 2026?"))
    story.append(Spacer(1, 0.2 * cm))

    story.append(ph2("PROBLEMA ESPECIFICO"))
    story.append(p("<b>PE1:</b> ¿En qué medida la modelación analítica del desacoplamiento de carga en el contorno mediante el modelo de Holmberg-Persson reduce la presión efectiva en pared de barreno por debajo del $UCS$ y disminuye la sobrerotura perimétrica en la sección baúl de la U.E.A. Lincuna?"))
    story.append(p("<b>PE2:</b> ¿En qué medida la optimización geométrica del arranque en 4 cuadrantes, arrastres de Gustafsson y ayudas mediante auto-tajeo espacial heurístico optimiza el factor de potencia y reduce la sobre-excavación total del frente?"))
    story.append(p("<b>PE3:</b> ¿En qué medida el control y reducción de la sobrerotura mediante el sistema agéntico influye en la reducción de sobrecostos de sostenimiento con concreto proyectado (shotcrete) y optimiza el ciclo de carguío y acarreo en la U.E.A. Lincuna?"))
    story.append(Spacer(1, 0.3 * cm))

    # OBJETIVO
    story.append(ph1("OBJETIVO"))
    story.append(HRFlowable(width="100%", thickness=1.0, color=c_primary, spaceAfter=8))
    
    story.append(ph2("OBJETIVO GENERAL"))
    story.append(p("Desarrollar, validar e instrumentar un sistema agéntico basado en inteligencia artificial y reglas físicas determinísticas para el diseño asistido de mallas de perforación y voladura, orientado a reducir la sobrerotura a valores $\le 5.0\%$ en labores subterráneas de la U.E.A. Lincuna, 2026."))
    story.append(Spacer(1, 0.2 * cm))

    story.append(ph2("OBJETIVOS ESPECÍFICOS"))
    story.append(p("<b>OE1:</b> Modelar analíticamente el desacoplamiento de carga en corona y hastiales utilizando cartuchos de emulsión de 22 mm en barrenos de 45 mm para garantizar que la presión efectiva en pared ($P_{te} = 164.96\text{ MPa}$) sea estrictamente menor a la resistencia a compresión uniaxial ($UCS = 180.05\text{ MPa}$), elevando el factor de media caña ($HCF$) $\ge 75\%$. "))
    story.append(p("<b>OE2:</b> Diseñar y calcular una malla optimizada de 47 taladros mediante la formulación de Holmberg-Persson en 4 cuadrantes de corte y auto-tajeo espacial heurístico ($S/B = 1.25$, $f = 1.45$), alcanzando un factor de potencia óptimo ($q_p \le 1.65\text{ kg/m}^3$) y un avance efectivo $\ge 88\%$. "))
    story.append(p("<b>OE3:</b> Cuantificar el beneficio técnico-económico derivado de la reducción de la sobrerotura mediante escaneo 3D LIDAR, demostrando un ahorro en consumo de shotcrete vía húmeda superior a $1,500.00 USD por disparo y una reducción en el tiempo de limpieza mecanizada."))
    story.append(Spacer(1, 0.3 * cm))

    # HIPOTESIS
    story.append(ph1("HIPOTESIS"))
    story.append(HRFlowable(width="100%", thickness=1.0, color=c_primary, spaceAfter=8))
    
    story.append(ph2("HIPÓTESIS GENERAL"))
    story.append(p("La implementación de un sistema agéntico basado en inteligencia artificial y reglas físicas determinísticas para el diseño asistido de perforación y voladura reducirá significativamente el porcentaje de sobrerotura a valores $\le 5.0\%$ en labores subterráneas de la U.E.A. Lincuna, 2026."))
    story.append(p("<b>Variable independiente:</b> Sistema agéntico basado en inteligencia artificial y reglas físicas determinísticas para diseño de perforación y voladura."))
    story.append(p("<b>Variable dependiente:</b> Porcentaje de sobrerotura (<i>overbreak</i>) en labores subterráneas."))
    story.append(Spacer(1, 0.2 * cm))

    story.append(ph2("HIPÓTESIS ESPECIFICA"))
    story.append(p("<b>HE1:</b> La modelación analítica del desacoplamiento de carga en el contorno con cartuchos de 22 mm en barrenos de 45 mm generará una presión efectiva en pared de barreno inferior al $UCS$ de la andesita ($P_{te} = 164.96\text{ MPa} \le 180.05\text{ MPa}$), reduciendo la sobrerotura perimétrica y elevando el factor de media caña ($HCF$) por encima del 75%."))
    story.append(p("<b>Variable independiente:</b> Presión efectiva desacoplada en pared de barreno ($P_{te}$) y factor de desacoplamiento ($d_c/d_h$)."))
    story.append(p("<b>Variable dependiente:</b> Daño microestructural perimétrico y Factor de Media Caña ($HCF$)."))
    story.append(Spacer(1, 0.15 * cm))
    
    story.append(p("<b>HE2:</b> El diseño analítico del corte en 4 cuadrantes y el algoritmo heurístico de auto-tajeo espacial ($S/B = 1.25$) optimizarán el factor de potencia a $q_p = 1.622\text{ kg/m}^3$, logrando una eficiencia de avance lineal $\ge 88\%$ sin sobrecarga energética."))
    story.append(p("<b>Variable independiente:</b> Malla optimizada de 47 taladros calculada con Holmberg-Persson y algoritmo de auto-tajeo."))
    story.append(p("<b>Variable dependiente:</b> Factor de potencia ($q_p$) y eficiencia de avance lineal por disparo."))
    story.append(Spacer(1, 0.15 * cm))
    
    story.append(p("<b>HE3:</b> La reducción de la sobrerotura al $4.85\%$ disminuirá el consumo excedente de concreto proyectado (shotcrete) en más de $5.70\text{ m}^3$ por disparo, generando un ahorro económico auditado superior a $1,600.00 USD por frente disparado."))
    story.append(p("<b>Variable independiente:</b> Reducción de la sobrerotura alcanzada mediante el sistema agéntico."))
    story.append(p("<b>Variable dependiente:</b> Costos operativos de sostenimiento con shotcrete y tiempos del ciclo de carguío."))
    story.append(Spacer(1, 0.3 * cm))
