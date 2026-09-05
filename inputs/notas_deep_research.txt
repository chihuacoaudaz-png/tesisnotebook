# Guía Metodológica y Marco Investigativo para Tesis de Posgrado (UNI - FIGMM)

## 1. Fundamentos y Estilo de Redacción Académica UNI
Las tesis de la **Sección de Posgrado de la Facultad de Ingeniería Geológica, Minera y Metalúrgica (FIGMM - UNI)** exigen un enfoque de investigación científica cuantitativa, aplicada y tecnológica, caracterizado por:
* **Tono y Estilo:** Tercera persona impersonal, rigor técnico-científico, formulación matemática explícita y trazabilidad total de datos.
* **Coherencia Lógica:** Correspondencia biunívoca entre problemas, objetivos e hipótesis.
* **Formato de Citas:** Estilo APA 7ma edición / IEEE según la especialidad de posgrado.

---

## 2. Matriz de Consistencia Metodológica (Modelo UNI / Metodología Dra. Rosario Martínez)
La matriz de consistencia es el núcleo rector del proyecto de tesis. Garantiza la coherencia interna de la investigación.

| Problemas | Objetivos | Hipótesis | Variables e Indicadores | Metodología |
| :--- | :--- | :--- | :--- | :--- |
| **Problema General (PG):**<br>¿De qué manera [Variable Independiente] influye/optimiza [Variable Dependiente] en [Unidad de Estudio / Yacimiento]? | **Objetivo General (OG):**<br>Determinar/Optimizar la influencia de [Variable Independiente] sobre [Variable Dependiente] en [Unidad de Estudio]. | **Hipótesis General (HG):**<br>La aplicación/integración de [Variable Independiente] optimiza significativamente [Variable Dependiente] en [Unidad de Estudio]. | **Variable Independiente ($X$):**<br>- Dimensión 1: [Parámetros de Diseño]<br>  - Indicador: Burden, Espaciamiento, Taco (m)<br>- Dimensión 2: [Energía / Explosivo]<br>  - Indicador: Factor de Potencia ($kg/m^3$, $kg/t$)<br><br>**Variable Dependiente ($Y$):**<br>- Dimensión 1: [Distribución Granulométrica]<br>  - Indicador: Tamaño medio $X_{50}$, Pasante $P_{80}$ (cm / in)<br>- Dimensión 2: [Rendimiento Operativo]<br>  - Indicador: Sobretamaños (Boulders %), Rendimiento de Carguío ($t/h$) | **Tipo de Investigación:**<br>Aplicada / Tecnológica.<br><br>**Nivel:**<br>Explicativo - Correlacional / Cuasi-experimental.<br><br>**Diseño:**<br>Cuasi-experimental o No experimental longitudinal.<br><br>**Población:**<br>Total de voladuras ejecutadas en el periodo de estudio.<br><br>**Muestra:**<br>Muestreo censal o probabilístico de voladuras instrumentadas.<br><br>**Técnicas e Instrumentos:**<br>Fotogrametría / Análisis de imágenes, Software de simulación, Modelos Machine Learning (XGBoost, ANN, Random Forest). |
| **Problemas Específicos (PE):**<br>PE1: ¿Cómo influyen los parámetros geomecánicos en...?<br>PE2: ¿Cuál es el desempeño del modelo empírico vs ML en...?<br>PE3: ¿Cuál es el impacto económico en los costos de carguío y acarreo? | **Objetivos Específicos (OE):**<br>OE1: Caracterizar los parámetros geomecánicos de...<br>OE2: Desarrollar y evaluar el modelo predictivo (Kuz-Ram vs ML)...<br>OE3: Evaluar el impacto técnico-económico en los procesos aguas abajo... | **Hipótesis Específicas (HE):**<br>HE1: Los parámetros geomecánicos condicionan significativamente...<br>HE2: El modelo basado en ML presenta una precisión ($R^2 > 0.90$, menor RMSE) superior al modelo empírico tradicional...<br>HE3: La optimización de la fragmentación reduce los costos unitarios de carguío y chancado en un X%... | | |

---

## 3. Matriz de Operacionalización de Variables
Desglosa las variables desde su conceptualización teórica hasta su medición empírica en mina.

| Variable | Tipo de Variable | Definición Conceptual | Definición Operacional | Dimensiones | Indicadores | Escala / Unidad | Fuente / Instrumento |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Diseño y Energía de Voladura** | Independiente ($X$) | Conjunto de parámetros geométricos y termodinámicos aplicados al macizo rocoso para su fragmentación. | Medición de la malla de perforación, propiedades del explosivo y distribución de carga en el taladro. | 1. Parámetros Geométricos<br>2. Parámetros de Carga | - Burden ($B$)<br>- Espaciamiento ($S$)<br>- Longitud de taco ($T$)<br>- Factor de carga ($q$) | Métrico (m)<br>Métrico (m)<br>Métrico (m)<br>$kg/m^3$ o $kg/t$ | Reportes de perforación, inclinometría, balance de masa explosiva. |
| **Calidad del Macizo Rocoso** | Interviniente ($Z$) | Características intrínsecas mecánicas y estructurales del macizo antes de la detonación. | Cuantificación geomecánica mediante índices y ensayos de laboratorio. | 1. Resistencia de roca intacta<br>2. Estructura y discontinuidades | - UCS (MPa)<br>- RMR / GSI<br>- RQD (%)<br>- Espaciamiento de juntas ($J_s$) | Escala continua (MPa)<br>Puntaje (0 - 100)<br>Porcentaje (%)<br>Métrico (m) | Mapeo geomecánico, ensayos triaxiales/compresión simple, televiewer. |
| **Fragmentación de Roca ($P_{80}$)** | Dependiente ($Y$) | Distribución dimensional de los fragmentos de roca resultantes de la voladura. | Curva granulométrica pasante acumulada evaluada en la pila de voladura mediante algoritmos de visión artificial y modelos predictivos. | 1. Tamaño representativo<br>2. Uniformidad | - Diámetro $X_{50}$<br>- Tamaño pasante $P_{80}$<br>- Índice de uniformidad ($n$)<br>- % de bolones / finos | Milímetros / Pulgadas<br>Milímetros / Pulgadas<br>Adimensional<br>Porcentaje (%) | Análisis granulométrico digital (Split-Engineering / WipFrag), registros de chancadora primaria. |

---

## 4. Estructura Canónica de Tesis de Posgrado UNI (FIGMM)

### Carátula / Portada Institucional
* Universidad Nacional de Ingeniería - Escuela de Posgrado.
* Título de la Tesis (preciso, delimitado, indicando variables y unidad de estudio).
* Grado académico optado: *Maestro en Ciencias con mención en Ingeniería de Minas* / *Doctor en Ingeniería de Minas*.

### Capítulo I: Planteamiento del Problema
1.1. Descripción de la realidad problemática (Contexto operativo y brecha tecnológica en la unidad minera).  
1.2. Formulación del problema (Problema general y específicos).  
1.3. Justificación de la investigación (Técnica, económica, metodológica, social y ambiental).  
1.4. Delimitación y limitaciones del estudio (Espacial, temporal y conceptual).  
1.5. Objetivos de la investigación (General y específicos).  

### Capítulo II: Marco Teórico y Referencial
2.1. Antecedentes de la investigación (Internacionales y Nacionales - últimos 5 años).  
2.2. Bases teóricas y científicas (Mecánica de fragmentación, modelos empíricos Kuz-Ram/KCO/Swebrec, Machine Learning, Visión Artificial).  
2.3. Definición de términos básicos (Glosario conceptual riguroso).  

### Capítulo III: Hipótesis, Variables y Operacionalización
3.1. Hipótesis (General y específicas).  
3.2. Identificación y clasificación de variables (Independiente, Dependiente, Intervinientes).  
3.3. Matriz de operacionalización de variables.  
3.4. Matriz de consistencia lógica.  

### Capítulo IV: Metodología de la Investigación
4.1. Tipo, nivel y enfoque de investigación.  
4.2. Diseño de la investigación.  
4.3. Población, muestra y criterios de selección.  
4.4. Técnicas, instrumentos y equipos de recolección de datos.  
4.5. Procedimiento de captura y preprocesamiento de datos (Limpieza, normalización, análisis exploratorio).  
4.6. Metodología de modelamiento / Machine Learning (Arquitecturas, validación cruzada, métricas $R^2$, RMSE, MAE, análisis SHAP).  

### Capítulo V: Resultados, Contrastación y Discusión
5.1. Presentación y análisis descriptivo de datos geomecánicos y de voladura.  
5.2. Resultados del modelamiento predictivo y comparativa de modelos.  
5.3. Prueba y contrastación de hipótesis estadísticas.  
5.4. Discusión de resultados (Contraste con antecedentes y modelos clásicos).  
5.5. Evaluación técnica y económica del impacto en mina.  

### Conclusiones y Recomendaciones
* Conclusiones numeradas alineadas estrictamente a cada uno de los objetivos específicos y general.
* Recomendaciones operativas para la mina y para futuras líneas de investigación científica.

### Referencias Bibliográficas y Anexos
* Formato APA 7ma / IEEE.
* Anexos: Matriz de consistencia completa, certificados de calibración de instrumentos, base de datos depurada, scripts de código fuente/algoritmos.
