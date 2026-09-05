# CAPÍTULO I: PLANTEAMIENTO DEL ESTUDIO

---

## 1.1. Planteamiento de la Realidad Problemática

### 1.1.1. Contexto Operacional y Diagnóstico en la U.E.A. Lincuna
La Unidad Económica Administrativa (U.E.A.) Lincuna, operada por la Compañía Minera Lincuna S.A., se localiza en el distrito de Ticapampa, provincia de Recuay, departamento de Áncash, dentro de la franja polimetálica de la Cordillera Negra en el centro-norte del Perú. La operación explota cuerpos mineralizados y estructuras vetiformes complejas con contenidos de plomo, plata, zinc y cobre mediante métodos de minado subterráneo mecanizado y semimecanizado, tales como el Corte y Relleno Ascendente mecanizado y el banqueo por subniveles (*Sublevel Stoping*).

Para el acceso, preparación y desarrollo de los bloques de explotación, la unidad minera ejecuta un programa intensivo de excavaciones subterráneas lineales horizontales, principalmente cruceros de extracción (*cross-cuts*), galerías de nivel, chimeneas de ventilación y rampas de acceso. Estas labores se diseñan geométricamente bajo una **Sección D (tipo baúl con arco rebajado)** con dimensiones nominales de **4.50 metros de ancho por 4.50 metros de altura** y una flecha de arco de corona de **1.25 metros**, totalizando un área neta teórica de excavación de **$19.04\text{ m}^2$** y un perímetro nominal de **$16.12\text{ m}$**.

La excavación se realiza mediante perforación mecanizada utilizando jumbos electrohidráulicos de dos brazos equipados con barras de perforación de 12 pies ($3.66\text{ m}$), alcanzando una longitud de taladro efectiva de $3.48\text{ m}$ por disparo (equivalente al 95% de la longitud de barra). El macizo rocoso encajonante en los frentes de avance corresponde predominantemente a secuencias volcánicas y sedimentarias hidrotermalizadas clasificadas geomecánicamente en la categoría **Roca Regular a Mala (Tipo III-B a IV-A)**, caracterizadas por un Índice de Calidad de la Roca (**RQD**) medio del $60.0\%$, un Índice de Resistencia Geológica (**GSI**) de $50.0$, y una valoración **RMR de Bieniawski (1989)** de **$55.5\text{ puntos}$**, con una Resistencia a la Compresión Uniaxial de la roca intacta ($\sigma_c$ o UCS) de **$180.05\text{ MPa}$**, resistencia a la tracción ($\sigma_t$) de **$12.15\text{ MPa}$** y una densidad media de **$2.70\text{ TM/m}^3$**.

### 1.1.2. La Problemática de la Sobrerotura (*Overbreak*) y Limitaciones de los Diseños Empíricos
A pesar de la alta competencia de la roca intacta (UCS = 180.05 MPa), los registros operativos históricos y las evaluaciones mediante escaneo láser tridimensional (*LIDAR / 3D Cavity Auto-Scanning*) revelan que los frentes de avance en la U.E.A. Lincuna presentan un índice medio de **sobrerotura (*overbreak*) del $34.36\%$** con respecto a la sección teórica de diseño.

Este fenómeno de sobre-excavación sistemática se origina por el uso de **mallas de perforación y voladura empíricas y estáticas**, diseñadas con reglas heurísticas tradicionales o tablas fijas de mina que no consideran la respuesta dinámica y tensorial del macizo rocoso frente a la detonación de explosivos de alta energía. Específicamente, se identifican las siguientes deficiencias en el diseño convencional:

1. **Sobrecarga de Energía en el Arranque y Cuadrantes Interiores:** La distribución empírica no modula la apertura progresiva de las caras libres. Al utilizar taladros de alivio insuficientes o mallas de corte sobredimensionadas, la roca experimenta confinamiento extremo, generando deformaciones plásticas y ondas de choque hiper-concentradas que propagan fracturas radiales descontroladas hacia los hastiales y la corona.
2. **Ausencia de Voladura Controlada Desacoplada en el Contorno:** En la corona y hastiales se utilizan explosivos de alta densidad y alto VOD acoplados o pobremente amortiguados. La presión de detonación generada supera ampliamente la resistencia dinámica a la tracción y compresión del macizo, provocando la apertura de las discontinuidades naturales y el desprendimiento de bloques rocosos más allá del límite teórico de excavación.
3. **Distribución Manual y Deficiente de los Taladros de Tajeo (*Stoping*):** La asignación empírica del espaciamiento y burden en los taladros de destrozo deja áreas sub-rotas que concentran la energía o sobre-densifica taladros en zonas críticas, induciendo fracturamiento secundario en las paredes de la labor.
4. **Desviaciones de Perforación y Falta de Ajuste Geométrico:** La falta de un cálculo automatizado que compense el error de emboquillado ($\beta = 20\text{ mm}$) y la desviación angular ($\alpha = 10\text{ mm/m}$) agrava la divergencia de los taladros periféricos hacia el exterior del perfil de diseño.

### 1.1.3. Impacto Técnico, Operacional, Económico y de Seguridad
La sobre-excavación del $34.36\%$ representa una masa crítica de consecuencias operacionales y financieras directas e indirectas para la U.E.A. Lincuna:

```
                                    ÁRBOL DE CAUSAS Y EFECTOS DE LA SOBREROTURA
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                 EFECTOS FINALES                                                  │
│  - Sobrecosto millonario anual (> $2.5M USD en shotcrete y acarreo).                                             │
│  - Reducción del avance lineal mensual y estrangulamiento del ciclo de minado.                                  │
│  - Incremento del riesgo de atrapamiento y accidentes por desprendimiento de roca en coronas dañadas.           │
└─────────────────────────────────────────────────────────▲────────────────────────────────────────────────────────┘
                                                          │
┌─────────────────────────────────────────────────────────┴────────────────────────────────────────────────────────┐
│                                              EFECTOS DIRECTOS EN MINA                                            │
│  - Sobre-excavación de 22.75 m³ de roca adicional por disparo (88.96 m³ real vs. 66.21 m³ teórico).              │
│  - Sobrecosto de sostenimiento: $7,639.50 USD adicionales por disparo en lanzado de shotcrete ($516.58 USD/m³). │
│  - Sobrecarga en equipos de limpieza: Mayor número de pases de scooptramp (6 yd³) y camiones dumper (20 TM).     │
│  - Dilución del mineral en labores de preparación y desestabilización del macizo rocoso (microfisuramiento).   │
└─────────────────────────────────────────────────────────▲────────────────────────────────────────────────────────┘
                                                          │
┌─────────────────────────────────────────────────────────┴────────────────────────────────────────────────────────┐
│                                                  CAUSA PRINCIPAL                                                 │
│       Inadecuado diseño y dimensionamiento de mallas de perforación y voladura subterránea en roca Tipo III-B     │
│                 basado en reglas empíricas estáticas y sin desacoplamiento controlado perimétrico                │
└─────────────────────────────────────────────────────────▲────────────────────────────────────────────────────────┘
                                                          │
┌─────────────────────────────────────────────────────────┴────────────────────────────────────────────────────────┐
│                                                CAUSAS ESPECÍFICAS                                                │
│  1. Incompatibilidad entre la presión efectiva de taladro (Pte) y la resistencia geomecánica (UCS = 180.05 MPa).│
│  2. Cálculo manual no optimizado del corte en 4 cuadrantes y ausencia de algoritmo heurístico para tajeo.        │
│  3. Inexistencia de un sistema inteligente de diseño asistido que recalcule mallas según variabilidad del macizo.│
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

* **Sobrecosto de Sostenimiento por Concreto Lanzado (*Shotcrete*):**
  Para una sección nominal de $19.04\text{ m}^2$ con un avance de $3.48\text{ m}$, el volumen teórico por disparo es de **$66.21\text{ m}^3$** ($178.77\text{ TM}$). Con una sobrerotura del $34.36\%$, el volumen real excavado alcanza **$88.96\text{ m}^3$** ($240.19\text{ TM}$), generando un excedente de **$22.75\text{ m}^3$** de cavidad irregular por disparo. Debido a los estándares geomecánicos de la unidad (roca Tipo III-B), esta sobre-cavidad debe ser perfilada y rellenada con *shotcrete* vía húmeda robotizado a un costo unitario de **$\$516.58\text{ USD/m}^3$**. Considerando un factor de llenado geométrico del $65\%$, el sobrecosto directo de shotcrete asciende a **$\$7,639.50\text{ USD por disparo}$**. Para un programa anual de $2,000\text{ metros}$ de desarrollo ($\approx 575\text{ disparos}$), el sobrecosto exclusivo de shotcrete supera los **$\$4.39\text{ Millones de USD}$**.
* **Sobrecosto en Limpieza y Transporte Subterráneo:**
  Las $61.42\text{ TM}$ adicionales de desmonte por disparo obligan a incrementar el número de ciclos de acarreo con equipos *scooptramp* de $6.0\text{ yd}^3$ y camiones volquetes de bajo perfil (*dumpers*) de $20\text{ TM}$, incrementando el consumo de diésel, desgaste de neumáticos, horas-máquina y retrasando el ciclo operativo de ventilación y desatado en más de $1.5\text{ horas por guardia}$.
* **Riesgo Crítico de Seguridad Geomecánica:**
  El sobre-fracturamiento inducido por voladuras no controladas destruye el "arco natural de soporte" de la excavación (*rock arching effect*), generando "planchones" y cuñas inestables en la corona que elevan el riesgo de desprendimiento de rocas, principal causa de accidentes fatales y de alta severidad en la minería subterránea peruana.

### 1.1.4. Cuadro Comparativo: Situación Actual Convencional vs. Situación Futura con Sistema Agéntico

| Variable / Parámetro Operacional | Situación Actual (Diseño Empírico Convencional) | Situación Futura (Sistema Agéntico Asistido Holmberg + Auto-Tajeo) | Delta de Mejora / Impacto Técnico-Económico |
| :--- | :--- | :--- | :--- |
| **Metodología de Diseño de Malla** | Tablas estáticas empíricas en hojas de cálculo no integradas. | Sistema agéntico multi-rol basado en motor físico determinístico y auto-tajeo geométrico. | Trazabilidad física 1:1, adaptación paramétrica y cero dependencia de recetas fijas. |
| **Control de Presión en Contorno ($P_{te}$)** | Cartuchos de alta densidad acoplados ($P_{te} > 500\text{ MPa} \gg \text{UCS}$). | Carga desacoplada ($22\text{ mm}$ en taladro de $45\text{ mm}$) verificando $P_{te} = 164.96\text{ MPa} \le \text{UCS}$ ($180.05\text{ MPa}$). | Eliminación del daño microestructural por choque y preservación de la roca intacta. |
| **Distribución de Taladros de Tajeo** | Posicionamiento visual aproximado por el operador jumbero. | Algoritmo heurístico de auto-tajeo ($S/B = 1.25$, $f = 1.45$) con coordenadas $(x,y)$ exactas. | Cobertura volumétrica uniforme, fragmentación homogénea y eliminación de áreas sub-rotas. |
| **Índice de Sobrerotura (*Overbreak*)** | **$34.36\%$** (Media histórica de campo). | **$\le 5.00\%$** (Validación mediante modelo analítico e inferencial). | **Reducción neta absoluta de $29.36\%$ de sobre-excavación.** |
| **Volumen de Roca Rota por Disparo** | $88.96\text{ m}^3$ ($240.19\text{ TM}$). | $69.52\text{ m}^3$ ($187.70\text{ TM}$). | Reducción de $19.44\text{ m}^3$ ($52.49\text{ TM}$) de sobre-excavación por disparo. |
| **Consumo de Shotcrete por Disparo** | $14.79\text{ m}^3$ ($\$7,639.50\text{ USD}$ en sobreconsumo). | $2.15\text{ m}^3$ (Consumo nominal proyectado según diseño). | **Ahorro directo de $\approx \$6,500\text{ USD}$ por disparo en sostenimiento.** |
| **Factor de Potencia Global** | $1.85 - 2.10\text{ kg/m}^3$ (Sobrecarga de explosivo). | $1.622\text{ kg/m}^3$ ($0.601\text{ kg/t}$). | Optimización energética y menor emisión de gases nitrosos y CO. |
| **Factor de Media Caña (*Half-Cast Factor*)** | $< 15\%$ (Paredes rugosas y fracturadas). | $> 75\%$ (Trazas de taladros visibles en corona y hastiales). | Incremento de la autosoporte del macizo y máxima estabilidad geomecánica. |

---

## 1.2. Formulación del Problema

### 1.2.1. Problema General (PG)
¿De qué manera el desarrollo y aplicación de un sistema agéntico basado en inteligencia artificial y reglas físicas determinísticas optimiza el diseño asistido de perforación y voladura para el control efectivo de la sobrerotura en las labores subterráneas de la U.E.A. Lincuna, 2026?

### 1.2.2. Problemas Específicos (PE)
* **Problema Específico 1 (PE1):**  
  ¿De qué manera la caracterización geomecánica y la formulación físico-matemática del desacoplamiento de cargas mediante el modelo de Holmberg-Persson reducen la presión efectiva de taladro por debajo de la resistencia a la compresión uniaxial ($\sigma_c$) en la corona y hastiales de la labor?
* **Problema Específico 2 (PE2):**  
  ¿En qué medida el desarrollo de un algoritmo heurístico de auto-tajeo para la distribución geométrica de taladros de destrozo y ayudas en secciones baúl optimiza el factor de potencia y elimina las zonas de confinamiento y sub-rotura?
* **Problema Específico 3 (PE3):**  
  ¿Cuál es el impacto técnico-económico y de seguridad que genera la reducción de la sobrerotura al límite meta ($\le 5\%$) en los costos unitarios de sostenimiento con *shotcrete* y en los tiempos de ciclo del carguío mecanizado en la U.E.A. Lincuna?

---

## 1.3. Justificación de la Investigación

### 1.3.1. Justificación Teórica
La investigación aporta a la ingeniería de minas y geomecánica subterránea al integrar la teoría de detonación de Chapman-Jouguet, la mecánica de propagación de ondas de choque en macizos rocosos fracturados (Ashby, 1987) y el modelo matemático de Holmberg-Persson para excavaciones en 5 secciones con arquitecturas modernas de **Inteligencia Artificial Agéntica Basada en Reglas y Orquestación de Herramientas (*Tool-Calling / Deterministic Agentic AI*)**.

A diferencia de los modelos de Machine Learning convencionales (cajas negras como Redes Neuronales densas o Gradient Boosting) que carecen de interpretabilidad física y pueden generar predicciones no acotadas catastróficas en voladura, esta propuesta fundamenta su gobernanza en leyes físicas inviolables ($P_{te} \le \sigma_c$, relaciones de amortiguamiento de Gustafsson y condiciones de contorno de corte). Se genera un marco teórico reproducible que demuestra cómo la IA agéntica puede gobernar motores de cálculo determinístico para resolver problemas no lineales de ingeniería estructural.

### 1.3.2. Justificación Metodológica
Desde la perspectiva metodológica, la tesis establece un estándar cuantitativo, experimental-longitudinal y reproducible para el diseño de voladuras subterráneas en la UNI FIGMM. Se estructuran **Skills modulares ejecutables en Python** para la ingesta de datos multimodales, resolución matemática de Holmberg, auto-tajeo espacial y auditoría inferencial de consistencia lógica mediante pruebas de $t$-Student. Esto supera la brecha de los proyectos académicos tradicionales basados en cálculos manuales aproximados, proporcionando un entorno algorítmico auditable y transferible a cualquier operación minera subterránea.

### 1.3.3. Justificación Práctica y Operacional
En el plano operacional, el sistema agéntico entrega a la superintendencia de mina y al departamento de geomecánica de Minera Lincuna una herramienta computacional interactiva capaz de generar en segundos el patrón de perforación óptimo con coordenadas $(x,y)$ exactas para cada taladro, tablas de carga, tipos de explosivo, número de cartuchos y secuencia de retardo según la variación geomecánica del frente. Se elimina la improvisación del trazo manual y se garantiza la repetibilidad técnica del disparo.

### 1.3.4. Justificación Económica y de Seguridad
La justificación económica es contundente:
* Para una proyección de avance anual de **$2,000\text{ metros}$** de desarrollo lineal ($\approx 575\text{ disparos}$ de $3.48\text{ m}$ de avance efectivo), la reducción de la sobrerotura del **$34.36\%$ al $\le 5.00\%$** representa evitar la sobre-excavación de **$11,178\text{ m}^3$** de roca estéril.
* Esto genera un **ahorro directo consolidado de $\$3.75\text{ Millones de USD}$ en consumo de concreto lanzado (*shotcrete*)**, más de **$\$350,000\text{ USD}$ en costos operativos de carguío y acarreo mecanizado (diésel, llantas y mantenimiento de scooptramps/dumpers)** y una reducción del $25\%$ en la dilución del mineral en labores de preparación.
* En seguridad, el incremento del factor de media caña (*Half-Cast Factor*) al $\ge 75\%$ preserva el macizo rocoso intacto, disminuyendo drásticamente el riesgo de accidentes laborales por caída de rocas y asegurando la estabilidad a largo plazo de las galerías principales.

---

## 1.4. Delimitación y Alcance del Estudio

* **Delimitación Espacial:** La investigación se circunscribe a las labores de desarrollo horizontal (cruceros de nivel y galerías de avance de sección D $4.50\text{ m} \times 4.50\text{ m}$) de la U.E.A. Lincuna, ubicada en el distrito de Ticapampa, provincia de Recuay, departamento de Áncash, Perú.
* **Delimitación Temporal:** Los datos de caracterización geomecánica, registros de disparo, escaneos láser 3D y costos operativos corresponden al periodo anual 2026.
* **Delimitación Operacional y Geomecánica:** El estudio abarca frentes de avance emplazados en dominios estructurales de calidad geomecánica Tipo III-B a IV-A (RMR $45 - 60$, GSI $40 - 55$, UCS $100 - 200\text{ MPa}$). Quedan expresamente excluidas zonas con fallamientos geológicos mayores regionales no atribuibles a efectos de voladura.

---

## 1.5. Objetivos de la Investigación

### 1.5.1. Objetivo General (OG)
Desarrollar y evaluar un sistema agéntico basado en inteligencia artificial y reglas físicas determinísticas para el diseño asistido de perforación y voladura, orientado a controlar y reducir la sobrerotura a un valor meta menor o igual al **$5.0\%$** en las labores subterráneas de la U.E.A. Lincuna, 2026.

### 1.5.2. Objetivos Específicos (OE)
* **Objetivo Específico 1 (OE1):**  
  Modelar y calcular la malla de perforación y desacoplamiento de carga perimétrica mediante las ecuaciones de Holmberg-Persson, asegurando que la presión efectiva de taladro ($P_{te}$) sea estrictamente menor o igual a la resistencia compresiva uniaxial ($\sigma_c = 180.05\text{ MPa}$) de la roca encajonante.
* **Objetivo Específico 2 (OE2):**  
  Desarrollar e implementar un algoritmo heurístico de auto-tajeo espacial que calcule el área remanente y posicione de forma equidistante y optimizada los taladros de destrozo y ayudas en secciones baúl de $4.5\text{ m} \times 4.5\text{ m}$.
* **Objetivo Específico 3 (OE3):**  
  Evaluar el impacto técnico, económico y de seguridad derivado de la reducción de la sobrerotura en la disminución de costos de *shotcrete* y en la optimización del ciclo de acarreo mecanizado en la U.E.A. Lincuna.
