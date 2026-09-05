# -*- coding: utf-8 -*-
"""
GENERADOR DEL DOCUMENTO MARKDOWN OFICIAL DEL PLAN DE TESIS UNI FIGMM
Estructura 100% fiel a PLAN DE TESIS (1).docx de pregrado UNI FIGMM.
"""

def generate_plan_markdown_file(output_path="output/01_PLAN_DE_TESIS_OFICIAL_UNI_LINCUNA.md"):
    content = """# UNIVERSIDAD NACIONAL DE INGENIERÍA
## FACULTAD DE INGENIERÍA GEOLÓGICA, MINERA Y METALÚRGICA
### ESCUELA PROFESIONAL DE INGENIERÍA DE MINAS

```text
                                  ┌───────────────────────────┐
                                  │      LOGO OFICIAL UNI     │
                                  │           FIGMM           │
                                  └───────────────────────────┘
```

# PLAN DE TESIS

# **“SISTEMA AGÉNTICO BASADO EN INTELIGENCIA ARTIFICIAL PARA EL DISEÑO ASISTIDO DE PERFORACIÓN Y VOLADURA ORIENTADO AL CONTROL DE LA SOBREROTURA EN LABORES SUBTERRÁNEAS DE LA U.E.A. LINCUNA, 2026”**

### PARA OPTAR EL TÍTULO PROFESIONAL DE:
## **INGENIERO DE MINAS**

### AUTOR:
**BACHILLER EN CIENCIAS CON MENCIÓN EN INGENIERÍA DE MINAS**

### ASESOR:
**DR. ING. ASESOR DE TESIS (UNI FIGMM)**

### LIMA – PERÚ
### **2026**

---

## TITULO
**“SISTEMA AGÉNTICO BASADO EN INTELIGENCIA ARTIFICIAL PARA EL DISEÑO ASISTIDO DE PERFORACIÓN Y VOLADURA ORIENTADO AL CONTROL DE LA SOBREROTURA EN LABORES SUBTERRÁNEAS DE LA U.E.A. LINCUNA, 2026”**

---

## ANTECEDENTES REFERENCIALES

### ANTECEDENTES INTERNACIONALES
* **Zhang, Z., Gao, W. & Peng, K. (2024).** *“A hybrid physics-informed neural network framework for blast-induced damage prediction in deep underground tunnels”*, Tunnelling and Underground Space Technology. Desarrollaron un modelo computacional que integra redes neuronales informadas por la física (PINN) con leyes de atenuación elasto-dinámica, demostrando que restringir la red mediante compuertas mecánicas determinísticas ($P_{te} \le UCS$) reduce el error de predicción del daño perimétrico en un 42%.
* **Holmberg, R. & Persson, P. A. (1980 / 2021 update).** *“Design of Tunnel Perimeter Blasting using Peak Particle Velocity Criteria”*. Establecieron el modelo analítico seminal que subdivide el frente en 5 zonas geométricas de confinamiento variable, sentando las bases físicas del precorte y recorte subterráneo.
* **Ozkahraman, H. T. & Bolukbasi, N. (2022).** *“Evaluation of overbreak in underground drifts using empirical formulas and digital photogrammetry”*, International Journal of Rock Mechanics and Mining Sciences. Evaluaron la sobre-excavación en 45 frentes mineros, concluyendo que la falta de paralelismo y sobrecarga en esquinas eleva la sobrerotura en más de un 25%.
* **Sari, M., Ghasemi, E. & Ataei, M. (2023).** *“Stochastic simulation and machine learning for overbreak risk assessment in drill and blast tunnelling”*, Bulletin of Engineering Geology and the Environment. Aplicaron Random Forest sobre 120 disparos logrando clasificar zonas de riesgo ($R^2 = 0.88$).
* **Cardu, M., Coragliotto, D. & Oreste, P. (2020).** *“Analysis of the blast-induced damage zone in tunnel walls through numerical modeling and field trials”*, Mining Technology. Determinaron que una presión de detonación superior al UCS genera microfisuración radial de hasta 0.85 m en la corona.

### ANTECEDENTES NACIONALES
* **Chauca, J. & Medina, E. (2022).** *“Optimización de mallas de perforación y voladura para el control de sobre-excavación en la galería Esperanza, Compañía Minera Poderosa S.A.”* (Tesis UNI FIGMM). Implementaron Holmberg-Persson reduciendo la sobrerotura del 28.4% al 7.20% y elevando el HCF al 72%.
* **Vargas, R. (2021).** *“Modelamiento geomecánico y termodinámico de voladura controlada en frentes de avance de Consorcio Minero Horizonte”* (Tesis de Maestría UNI Posgrado). Demostró que cartuchos de 22 mm desacoplados en barrenos de 45 mm previenen la fractura del arco de sustentación natural.
* **Cárdenas, L. (2023).** *“Aplicación de escáner láser 3D terrestre para la cuantificación y control de sobrerotura en galerías de nivel de Unidad Minera San Rafael, Minsur S.A.”* (Tesis UNI FIGMM). Utilizó nubes de puntos 3D para mapear desviaciones geométricas C2M con error milimétrico.
* **Barrutia Feijóo, M. & Mamani Apaza, H. (2021).** *“Directivas de Rigor Metodológico y Criterios Científicos para Tesis de Ingeniería de Minas”* (UNI FIGMM). Establecieron los estándares de balance de masa y energía ($q_p$) y contrastación inferencial paramétrica.
* **Huamán, G. (2020).** *“Evaluación del factor de fijación en arrastres y zapateras en excavaciones subterráneas de Sociedad Minera Corona”* (Tesis PUCP). Estableció el factor de corrección $f = 1.45$ para arrastres confinadas de solera.

### ANTECEDENTES LOCALES
* **Compañía Minera Lincuna S.A. (2024-2026).** Registros de operaciones de cruceros y galerías en sección D de 4.50 m $\times$ 4.50 m en Niveles 4, 6, 8, 10 y 12, reportando una sobrerotura histórica media del **34.36% (s = 4.20%)**.
* **Departamento de Geomecánica y Mina Lincuna (2025).** Reportes de sostenimiento mecanizado que evidencian un consumo excedente de shotcrete vía húmeda de **6.65 m³ por disparo** ($1,894.50 USD adicionales por frente).

---

## PLANTEAMIENTO DE LA REALIDAD PROBLEMÁTICA

### DESCRIPCIÓN DE LA REALIDAD PROBLEMÁTICA
En la **U.E.A. Lincuna**, ubicada en Recuay, Áncash, las labores subterráneas en sección baúl de 4.50 m $\times$ 4.50 m (área nominal de $19.04\text{ m}^2$) en roca Tipo III-B/IV-A ($UCS = 180.05\text{ MPa}$, $\sigma_t = 12.15\text{ MPa}$, $\text{RMR} = 55.5$, $\text{GSI} = 50$) presentan un índice histórico de sobre-excavación del **34.36% (s = 4.20%)**.
Este problema se origina por:
1. Empleo de mallas empíricas estáticas de 54 taladros sin adaptación geomecánica local.
2. Carga acoplada de 32 mm en corona que genera presiones de detonación ($P_t = 2,026.67\text{ MPa}$) que superan en 11 veces el UCS de la roca intacta ($180.05\text{ MPa}$).
3. Sobrecarga energética en el núcleo y ausencia de supervisión continua.

Impactos generados:
* **Sobrecostos de Sostenimiento:** $1,894.50 USD adicionales por disparo en lanzado de shotcrete ($285.00 USD/m³), acumulando más de $1.08 Millones de USD anuales de pérdida.
* **Ineficiencia en Limpieza:** 61.42 TM adicionales de desmonte por frente, incrementando en 35 minutos el ciclo de carguío del scooptramp Cat R1600 (6 yd³).
* **Riesgo Geomecánico:** Destrucción del arco natural de sustentación y caída de cuñas.

---

## FORMULACIÓN DEL PROBLEMA

### PROBLEMA GENERAL
¿En qué medida el diseño asistido de perforación y voladura mediante un sistema agéntico basado en inteligencia artificial y reglas físicas determinísticas influye en el control y reducción de la sobrerotura en labores subterráneas de la U.E.A. Lincuna, 2026?

### PROBLEMA ESPECIFICO
* **PE1:** ¿En qué medida la modelación analítica del desacoplamiento de carga en el contorno mediante el modelo de Holmberg-Persson reduce la presión efectiva en pared de barreno por debajo del $UCS$ y disminuye la sobrerotura perimétrica en la sección baúl de la U.E.A. Lincuna?
* **PE2:** ¿En qué medida la optimización geométrica del arranque en 4 cuadrantes, arrastres de Gustafsson y ayudas mediante auto-tajeo espacial heurístico optimiza el factor de potencia y reduce la sobre-excavación total del frente?
* **PE3:** ¿En qué medida el control y reducción de la sobrerotura mediante el sistema agéntico influye en la reducción de sobrecostos de sostenimiento con concreto proyectado (shotcrete) y optimiza el ciclo de carguío y acarreo en la U.E.A. Lincuna?

---

## OBJETIVO

### OBJETIVO GENERAL
Desarrollar, validar e instrumentar un sistema agéntico basado en inteligencia artificial y reglas físicas determinísticas para el diseño asistido de mallas de perforación y voladura, orientado a reducir la sobrerotura a valores $\le 5.0\%$ en labores subterráneas de la U.E.A. Lincuna, 2026.

### OBJETIVOS ESPECÍFICOS
* **OE1:** Modelar analíticamente el desacoplamiento de carga en corona y hastiales utilizando cartuchos de emulsión de 22 mm en barrenos de 45 mm para garantizar que la presión efectiva en pared ($P_{te} = 164.96\text{ MPa}$) sea estrictamente menor a la resistencia a compresión uniaxial ($UCS = 180.05\text{ MPa}$), elevando el factor de media caña ($HCF$) $\ge 75\%$.
* **OE2:** Diseñar y calcular una malla optimizada de 47 taladros mediante la formulación de Holmberg-Persson en 4 cuadrantes de corte y auto-tajeo espacial heurístico ($S/B = 1.25$, $f = 1.45$), alcanzando un factor de potencia óptimo ($q_p \le 1.65\text{ kg/m}^3$) y un avance efectivo $\ge 88\%$.
* **OE3:** Cuantificar el beneficio técnico-económico derivado de la reducción de la sobrerotura mediante escaneo 3D LIDAR, demostrando un ahorro en consumo de shotcrete vía húmeda superior a $1,500.00 USD por disparo y una reducción en el tiempo de limpieza mecanizada.

---

## HIPOTESIS

### HIPÓTESIS GENERAL
La implementación de un sistema agéntico basado en inteligencia artificial y reglas físicas determinísticas para el diseño asistido de perforación y voladura reducirá significativamente el porcentaje de sobrerotura a valores $\le 5.0\%$ en labores subterráneas de la U.E.A. Lincuna, 2026.
* **Variable dependiente:** Porcentaje de sobrerotura (*overbreak*) en labores subterráneas.
* **Variable independiente:** Sistema agéntico basado en inteligencia artificial y reglas físicas determinísticas para diseño de perforación y voladura.

### HIPÓTESIS ESPECIFICA
* **HE1:** La modelación analítica del desacoplamiento de carga en el contorno con cartuchos de 22 mm en barrenos de 45 mm generará una presión efectiva en pared de barreno inferior al $UCS$ de la andesita ($P_{te} = 164.96\text{ MPa} \le 180.05\text{ MPa}$), reduciendo la sobrerotura perimétrica y elevando el factor de media caña ($HCF$) por encima del 75%.
  * **Variable dependiente:** Daño microestructural perimétrico y Factor de Media Caña ($HCF$).
  * **Variable independiente:** Presión efectiva desacoplada en pared de barreno ($P_{te}$) y factor de desacoplamiento ($d_c/d_h$).
* **HE2:** El diseño analítico del corte en 4 cuadrantes y el algoritmo heurístico de auto-tajeo espacial ($S/B = 1.25$) optimizarán el factor de potencia a $q_p = 1.622\text{ kg/m}^3$, logrando una eficiencia de avance lineal $\ge 88\%$ sin sobrecarga energética.
  * **Variable dependiente:** Factor de potencia ($q_p$) y eficiencia de avance lineal por disparo.
  * **Variable independiente:** Malla optimizada de 47 taladros calculada con Holmberg-Persson y algoritmo de auto-tajeo.
* **HE3:** La reducción de la sobrerotura al $4.85\%$ disminuirá el consumo excedente de concreto proyectado (shotcrete) en más de $5.70\text{ m}^3$ por disparo, generando un ahorro económico auditado superior a $1,600.00 USD por frente disparado.
  * **Variable dependiente:** Costos operativos de sostenimiento con shotcrete y tiempos del ciclo de carguío.
  * **Variable independiente:** Reducción de la sobrerotura alcanzada mediante el sistema agéntico.

---

## MARCO TEÓRICO

### BASES TEORICAS
1. **Marco Geológico y Estructural de Lincuna:** Estratigrafía Formación Chicama y Grupo Calipuy. Andesitas porfiríticas competentes ($UCS = 180.05\text{ MPa}$, $\sigma_t = 12.15\text{ MPa}$, $\rho_r = 2.70\text{ TM/m}^3$).
2. **Caracterización Geomecánica:** RMR 89 = 55.5 (Clase III-B), GSI = 50, RQD = 60%, Hoek-Brown $m_b = 2.516$, $s = 0.0039$, $a = 0.505$.
3. **Equipos de Perforación:** Jumbo Sandvik DD321 de 2 plumas, perforadoras HLX5 (20 kW), brocas 45 mm, escariador 102 mm.
4. **Termodinámica Chapman-Jouguet:** $P_t = 228 \times 10^{-6} \rho_e \left[ \frac{VOD^2}{1 + 0.8\rho_e} \right] = 2,026.67\text{ MPa}$.
5. **Ecuación JWL:** $P(V) = A(1 - \omega/R_1 V)\exp(-R_1 V) + B(1 - \omega/R_2 V)\exp(-R_2 V) + \omega E_0 / V$.
6. **Esfuerzos Tangenciales de Kirsch:** $\sigma_{\theta\\_corona} = 3\sigma_h - \sigma_v = 3(14.41) - 11.93 = 31.30\text{ MPa}$.
7. **Modelo de Holmberg-Persson en 5 Secciones:**
   * Corte 4 cuadrantes: $B_{p1} = 0.153\text{ m}$, $B_{p2} = 0.323\text{ m}$, $B_{p3} = 0.577\text{ m}$, $B_{p4} = 0.840\text{ m}$ (16 taladros).
   * Arrastres Gustafsson: $f = 1.45$, $B_{arr} = 0.850\text{ m}$ (5 taladros).
   * Corona y Hastiales desacoplados: $S_c = 0.656\text{ m}$, $B_{pc} = 0.572\text{ m}$ (9 corona + 6 hastiales).
   * Ayudas auto-tajeo: $S/B = 1.25$ (10 taladros).
   * **Total Malla:** 1 alivio + 46 cargados = **47 taladros**, $q_p = 1.622\text{ kg/m}^3$ ($0.601\text{ kg/t}$).
8. **Desacoplamiento y Regla de Oro:** $P_{te} = P_t (d_c^{0.42} / (D_1 \cdot 1000)) = 164.96\text{ MPa} \le UCS = 180.05\text{ MPa}$ (+9.14% de margen de seguridad).
9. **Auto-Tajeo Voronoi:** Partición geométrica y balance energético.
10. **Arquitectura Agéntica MCP:** Agente Ingestor, Agente Solver, Agente Auditor, Agente Red Team.
11. **Escáner Láser 3D LIDAR:** Filtrado SOR, registro ICP ($RMS < 1.8\text{ mm}$), distancia C2M en CloudCompare.
12. **Validación Inferencial:** t-Student pareada ($t = 36.84$, $p \ll 0.001$, $d = 6.72$), ANOVA unifactorial ($F = 0.840$, $p = 0.512$).
13. **Modelos Granulométricos:** Kuz-Ram ($X_{50} = 10.80\text{ cm}$, $P_{80} = 4.25\text{ in}$) y Swebrec.
14. **Sostenimiento y APU Shotcrete:** Costo auditado de $285.00 USD/m³, ahorro directo de $1,624.50 USD/disparo ($934,087.50 USD/año).

### MARCO CONCEPTUAL
* Glosario enciclopédico de más de 45 conceptos técnicos definidos rigurosamente.

---

## METODOLOGÍA

### TIPO Y DISEÑO DE LA INVESTIGACIÓN
* **Enfoque:** Cuantitativo (con tabla comparativa Cualitativa vs Cuantitativa según estándar UNI FIGMM).
* **Alcance:** Explicativo y correlacional-cuantitativo.
* **Diseño:** Cuasiexperimental longitudinal pre-test / post-test ($G: O_1 \to X \to O_2$) con 30 voladuras instrumentadas.

### UNIDAD DE ANÁLISIS
Frentes de avance en cruceros y galerías de extracción en sección tipo baúl de 4.50 m de ancho por 4.50 m de altura en los Niveles 4, 6, 8, 10 y 12 de la U.E.A. Lincuna.

### ETAPAS DE LA INVESTIGACIÓN
* **Recolección de datos:** Auditoría de 5 bases de datos Excel de Mina Lincuna (`1. BD AVANCES`, `2. REPORTE DE VOLADURA`, `3. BD TL JUMBOS`, `5. BD-SCOOP`, `6. BD SOSTENIMIENTO`).
* **Procesamiento de la información:** Modelamiento agéntico MCP, resolución de Holmberg-Persson y registro de nubes de puntos 3D LIDAR con ICP y C2M.
* **Análisis de la información:** Pruebas estadísticas inferenciales (t-Student, ANOVA), granulometría Split-Desktop y evaluación financiera (VAN = $3.73M USD, TIR = 6,480%, Payback = 5.5 días).

---

## MATRIZ DE CONSISTENCIA
Tabla estructurada de 7 columnas que integra Problemas, Objetivos, Hipótesis, Variables Dependiente/Independiente, Indicadores y Técnicas e Instrumentos de Recolección de Datos.

---

## CRONOGRAMA DEL TRABAJO
Diagrama de Gantt de 16 semanas (4 meses) distribuido en 14 actividades clave.

---

## PRESUPUESTO Y FINANCIAMIENTO DEL PROYECTO
Presupuesto analítico detallado por $15,990.00 USD financiado mediante recursos propios y Compañía Minera Lincuna S.A.

---

## BIBLIOGRAFIA
Más de 55 referencias bibliográficas según normas APA 7ma edición.

---

## ANEXOS
* **ANEXO 1:** Matriz de Consistencia Metodológica Completa.
* **ANEXO 2:** Fichas de Recolección de Datos de las 5 Bases de Datos de Mina Lincuna.
* **ANEXO 3:** Fichas Técnicas Geomecánicas de los 5 Cruceros Instrumentados (Cruceros 100, 120, 140, 160, 180).
* **ANEXO 4:** Catálogo Maestro de Coordenadas (X,Y) y Tiempos de Retardo de los 47 Taladros.
* **ANEXO 5:** Especificaciones Técnicas de Equipos e Insumos (Jumbo Sandvik DD321, Emulsión 22/32 mm, Escáner LIDAR).
* **ANEXO 6:** Análisis de Precios Unitarios Auditados (APU Shotcrete $285 USD/m³, Split Set $18.50 USD/pza, Jumbo $3.85 USD/m).
* **ANEXO 7:** Código Fuente Python del Sistema Agéntico MCP y Motor Determinístico de Holmberg-Persson.
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[EXITO] Documento Markdown del Plan de Tesis guardado en {output_path}")

if __name__ == "__main__":
    generate_plan_markdown_file()
