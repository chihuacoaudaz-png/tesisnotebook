# CAPÍTULO II: MARCO TEÓRICO Y CONCEPTUAL

---

## 2.1. Antecedentes de la Investigación

### 2.1.1. Antecedentes Internacionales
1. **Holmberg, R., & Persson, P. A. (1980 / 1999) – *Design of Tunnel Perimeter and Damage Zone in Crystalline Rocks*, Suecia:**  
   Esta investigación fundacional desarrolló el modelo matemático de diseño de voladuras en túneles subterráneos dividiendo la sección de excavación en cinco zonas de confinamiento diferenciado (corte, arrastre, tajeo, hastiales y corona). Establecieron las ecuaciones semianalíticas para la concentración lineal de carga ($q$), el burden crítico y la presión de detonación desacoplada. En ensayos en túneles de roca granítica en Suecia, la aplicación del modelo redujo la zona de daño perimétrico inducido por choque de $1.20\text{ m}$ a menos de $0.25\text{ m}$, estableciendo la condición de contorno de que la presión efectiva en la pared del taladro ($P_{te}$) no debe exceder la resistencia a la compresión uniaxial ($\sigma_c$) del macizo rocoso.
2. **Hustrulid, W., & Lu, W. (2018) – *Control of Perimeter Damage in Hard Rock Underground Excavations*, Colorado School of Mines, EE. UU.:**  
   Los autores investigaron los mecanismos de fracturamiento dinámico en labores subterráneas mecanizadas comparando la voladura convencional acoplada contra técnicas de precorte (*pre-splitting*) y amortiguamiento (*smooth blasting*) con relaciones de desacoplamiento $2:1$. Concluyeron que el factor de desacoplamiento geométrico reduce la amplitud de la onda de choque en más del $70\%$, transfiriendo la energía remanente a una presión cuasiestática de gases que propaga fracturas orientadas exclusivamente entre taladros periféricos adyacentes, logrando factores de media caña (*Half-Cast Factor*) superiores al $80\%$ en rocas competentes.
3. **Marchioni, A. (2021) – *3D Laser Scanning and Automated Overbreak Quantification in Deep Underground Mining*, Universidad de Bolonia / CSIRO Australia:**  
   Esta tesis doctoral implementó un sistema de escaneo láser tridimensional (*LIDAR*) y fotogrametría digital para mapear en tiempo real la geometría post-voladura en galerías subterráneas profundas. La investigación demostró que los métodos de diseño estático presentan una tasa de error de sobre-excavación del $25\%$ al $40\%$ debido a la falta de adaptación a la heterogeneidad del macizo, y propuso algoritmos de optimización paramétrica que lograron reducir la sobrerotura al $6.2\%$ con ahorros anuales de $\$2.1\text{M USD}$ en consumo de concreto proyectado.

### 2.1.2. Antecedentes Nacionales
1. **Compañía Minera Poderosa S.A. – Chauca, J., & Medina, E. (2022) – *Optimización de la Voladura de Contorno para la Reducción de la Sobrerotura en Labores Subterráneas*, Pataz, La Libertad:**  
   En frentes de avance de $3.0\text{ m} \times 3.0\text{ m}$ en roca volcánica-intrusiva (RMR $50-60$), la unidad minera presentaba sobreroturas históricas del $28.5\%$. Mediante la reformulación de la malla perimétrica con cartuchos de emulsión de $22\text{ mm}$ (Exsacorte) en taladros de $41\text{ mm}$ y la reconfiguración del corte en 4 cuadrantes con alivio central de $102\text{ mm}$, lograron reducir la sobrerotura media al $7.2\%$. Esto generó una reducción en el factor de potencia de $2.35\text{ kg/m}^3$ a $1.72\text{ kg/m}^3$ y un ahorro operativo verificado de $\$1.85\text{ Millones de USD}$ en reducción de shotcrete y horas de acarreo con scooptramps.
2. **Consorcio Minero Horizonte S.A. – Vargas, R. (2021) – *Implementación del Modelo Holmberg en Frentes de Avance Mecanizados*, Parcoy, La Libertad:**  
   La investigación evaluó el impacto de sustituir mallas empíricas tradicionales por el modelo físico-matemático de Holmberg en galerías de $3.5\text{ m} \times 3.5\text{ m}$ en roca Tipo III-B. La optimización del espaciamiento en corona ($S_c = 0.55\text{ m}$) y el control de desviación de perforación redujeron el índice de sobre-excavación del $31.2\%$ al $5.8\%$, incrementando el avance lineal por disparo del $82\%$ al $94\%$ de la longitud de barra y disminuyendo el costo de sostenimiento en un $62.5\%$.
3. **Minsur S.A. – Unidad Minera San Rafael – Cárdenas, L. (2023) – *Control de Dilución y Daño Perimétrico en Rampas y Cruceros de Gran Sección*, Puno:**  
   En labores mecanizadas de gran envergadura ($4.5\text{ m} \times 4.5\text{ m}$ con jumbos electrohidráulicos Sandvik DD321), se evaluó el sobrecosto generado por el daño inducido en los hastiales. Mediante la aplicación de voladura de contorno amortiguada con espaciamientos calculados en función de la resistencia a la tracción del macizo ($\sigma_t$), se redujo la sobre-excavación de $36.0\%$ a $6.1\%$, logrando un factor de media caña del $78\%$ y evitando la sobrecarga en el circuito de transporte con camiones dumper de 20 TM.

### 2.1.3. Antecedentes Locales
1. **Perez Guia, R. (2024, UNI FIGMM) – *Optimización de Parámetros de Perforación y Voladura con el Método de Holmberg en Frentes de Avance*, Tesis de Titulación UNI, Lima:**  
   Desarrolló un algoritmo computacional base en Python para calcular los cuadrantes de corte, arrastres y contorno en frentes subterráneos. Si bien demostró la viabilidad del cálculo determinístico, la investigación dejó abierta la limitación del posicionamiento manual de los taladros de tajeo y la necesidad de una arquitectura agéntica interactiva que integre la supervisión geomecánica en tiempo real y la cuantificación económica del ciclo de shotcrete.

---

## 2.2. Bases Teóricas y Físico-Matemáticas

### 2.2.1. Termodinámica de Explosivos y Mecánica de Fracturamiento Dinámico
La fragmentación de la roca por voladura es un fenómeno físico no lineal de alta velocidad termodinámica que involucra tres fases sucesivas:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                   MECÁNICA DINÁMICA DE LA DETONACIÓN EN ROCA                             │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────┘
                                                     │
     ┌───────────────────────────────────────────────┼───────────────────────────────────────────────┐
     ▼                                               ▼                                               ▼
┌───────────────────────────────┐   ┌───────────────────────────────┐   ┌───────────────────────────────┐
│     FASE 1: ONDA DE CHOQUE    │   │  FASE 2: REFLEXIÓN Y TRACCIÓN │   │   FASE 3: EXPANSIÓN DE GASES  │
│  - Detonación Supersónica     │   │  - Onda compresional P llega  │   │  - Gases a alta T (> 3000 K)  │
│  - Presión Chapman-Jouguet    │   │    a la cara libre / alivio.  │   │    y P (> 1000 MPa).          │
│  - Microfisuramiento radial   │   │  - Refleja como onda de       │   │  - Cuña hidrostática en       │
│    inmediato al taladro.      │   │    tracción (Hopkinson).      │   │    grietas y desplazamiento.  │
└───────────────────────────────┘   └───────────────────────────────┘   └───────────────────────────────┘
```

1. **Estado de Detonación de Chapman-Jouguet (C-J):**  
   Al iniciarse el cebo detonante, una onda de choque viaja a través de la columna de explosivo a una velocidad de detonación supersónica ($\text{VOD} = 4000 - 5500\text{ m/s}$). En el plano de Chapman-Jouguet, la reacción química es instantánea, transformando el sólido en gases a temperaturas superiores a $3000\text{ K}$ y presiones extremas de detonación ($P_t$), modeladas por la ecuación hidrodinámica:
   $$P_t = 228 \times 10^{-6} \cdot \rho_e \cdot \frac{\text{VOD}^2}{1 + 0.8\rho_e} \quad [\text{MPa}]$$
   Donde $\rho_e$ es la densidad del explosivo en $\text{g/cm}^3$ y $\text{VOD}$ es la velocidad de detonación en $\text{m/s}$.
2. **Generación de la Zona Plástica y Ondas Compresionales ($P$):**  
   Si el explosivo está acoplado ($D_c = D_1$), la presión en la pared del taladro ($P_{te} \approx P_t / 2$) supera por varios órdenes de magnitud la resistencia dinámica de la roca ($\sigma_c$), triturando la matriz mineral en una zona plástica adyacente y emitiendo ondas elásticas de compresión esféricas/cilíndricas hacia el macizo.
3. **Reflexión de Ondas de Tracción y Efecto Hopkinson:**  
   Al incidir la onda compresional sobre una cara libre (taladro de alivio o perímetro de labor previa), se refleja como una onda de tracción ($S$). Dado que las rocas poseen una resistencia a la tracción ($\sigma_t$) que apenas representa entre el $5\%$ y $10\%$ de su resistencia compresiva ($\sigma_c$), la onda reflejada genera fracturamiento por *spalling* (descascaramiento dinámico).
4. **Presión Cuasiestática y Acción de Cuña de los Gases:**  
   Los gases de explosión a alta presión penetran en la red de microfisuras radiales abiertas por la onda de choque, actuando como una cuña hidráulica que expande los bloques y los desplaza hacia el espacio libre disponible.

### 2.2.2. Mecánica de la Voladura de Contorno: Precorte (*Pre-splitting*) vs. Recorte Amortiguado (*Smooth Blasting*)
Para evitar la sobre-excavación y la degradación del macizo rocoso en la periferia de la labor, la energía de los taladros de corona y hastiales debe ser rigurosamente desacoplada:

* **Mecanismo de Desacoplamiento de Carga:**  
  Al emplear un cartucho de explosivo de menor diámetro ($D_{cc} = 22\text{ mm}$) dentro de un taladro de mayor diámetro ($D_1 = 45\text{ mm}$), se genera un colchón de aire anular que amortigua el impacto de la onda de choque, reduciendo la presión efectiva en la pared del taladro ($P_{te}$) según la ley de expansión adiabática:
  $$P_{te} = P_t \cdot \left(\frac{D_{cc}^{0.42}}{D_1 \cdot 1000}\right) \quad [\text{MPa}]$$
* **Condición de Contorno de No Destrucción Microestructural:**  
  Para garantizar que no se induzca daño microestructural ni desprendimiento incontrolado de roca, se exige la condición de seguridad:
  $$P_{te} \le \sigma_c \quad (164.96\text{ MPa} \le 180.05\text{ MPa})$$
* **Cálculo del Espaciamiento en Corona ($S_c$) y Hastiales ($S_h$):**  
  El espaciamiento perimétrico óptimo para generar una línea continua de fractura por tracción pura entre taladros sin romper hacia el exterior se determina mediante:
  $$S_c = D_1 \cdot \frac{P_{te} + \sigma_t}{\sigma_t} \quad [\text{m}]$$
  Y el burden teórico asociado se calcula con la relación clásica de voladura controlada:
  $$B_{tc} = \frac{S_c}{0.8} \quad [\text{m}]$$

### 2.2.3. Deducción Matemática Integral del Modelo de Holmberg-Persson (5 Secciones)

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                   SECCIONES DEL MODELO DE HOLMBERG-PERSSON                               │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────┘
                                                     │
     ┌───────────────────────┬───────────────────────┼───────────────────────┬───────────────────────┐
     ▼                       ▼                       ▼                       ▼                       ▼
┌──────────────┐       ┌──────────────┐       ┌──────────────┐       ┌──────────────┐       ┌──────────────┐
│  SECCIÓN 1   │       │  SECCIÓN 2   │       │  SECCIÓN 3   │       │  SECCIÓN 4   │       │  SECCIÓN 5   │
│   ARRANQUE   │       │   ARRASTRES  │       │    CORONA    │       │  HASTIALES   │       │ AUTO-TAJEO Y │
│ (4 Cuadran.) │       │ (Gustafsson) │       │ (Precorte)   │       │ (Amortiguad) │       │    AYUDAS    │
└──────────────┘       └──────────────┘       └──────────────┘       └──────────────┘       └──────────────┘
```

#### 1. Sección de Corte (Arranque de 4 Cuadrantes en Cuadrado Progresivo)
* **Taladro de Alivio Equivalente ($D_v$):**
  Para $n$ taladros de alivio de diámetro $D_2$:
  $$D_v = D_2 \cdot \sqrt{n} \quad [\text{m}]$$
* **Avance Máximo Teórico ($I$):**
  $$I = 0.15 + 34.1 \cdot D_v - 39.4 \cdot D_v^2 \le 0.95 \cdot H_p \quad [\text{m}]$$
* **Constante de Roca Sueca ($C$) mediante Fórmula de Ashby:**
  $$C_e = \frac{0.56 \cdot \rho_r \cdot \tan\left(\frac{\text{GSI} + 15}{2}\right)}{\left(\frac{115 - \text{RQD}}{3.3}\right)^{1/3}} \implies C = 0.878 \cdot C_e + 0.0052$$
* **Error Total de Perforación ($F$):**
  $$F = \alpha \cdot H_p + \beta \quad [\text{m}]$$
* **Primer Cuadrante ($k=1$):**
  El burden teórico ($B_{t1}$) se deduce resolviendo la raíz positiva de la ecuación de equilibrio de energía:
  $$B_{t1}^2 - D_v B_{t1} + \frac{D_v^2}{4} - \left[\frac{q_1 \cdot S_{\text{ANFO}} \cdot 0.4 \cdot D_v^{1.5}}{55 \cdot D_1 \cdot C}\right]^2 = 0$$
  $$B_{p1} = B_{t1} - F \implies A_1 = B_{p1} \cdot \sqrt{2} \quad [\text{m}]$$
* **Cuadrantes Sucesivos ($k=2, 3, 4$):**
  $$A_k = \left(B_{p(k-1)} + \frac{A_{k-1}}{2} - F\right) \cdot \sqrt{2} \quad [\text{m}]$$
  $$B_{tk} = 8.8 \times 10^{-2} \cdot \sqrt{\frac{A_k \cdot q_1 \cdot S_{\text{ANFO}}}{D_1 \cdot C}} \implies B_{pk} = B_{tk} - F$$
  $$A_k = \left(B_{pk} + \frac{A_{k-1}}{2}\right) \cdot \sqrt{2} \quad [\text{m}]$$

#### 2. Sección de Arrastres (Taladros de Piso)
Los taladros de arrastre deben vencer el confinamiento de la gravedad y la fricción de la masa rocosa hacia arriba, por lo que Gustafsson asigna un factor de fijación $f = 1.45$ y relación $S/B = 1.0$:
$$C_{\text{arrastre}} = C + \frac{0.07}{B_{p4}} \quad [\text{para } B_{p4} < 1.4\text{ m}]$$
$$B_{ta} = 0.9 \cdot \sqrt{\frac{q_1 \cdot S_{\text{ANFO}}}{C_{\text{arrastre}} \cdot f \cdot 1.0}} \le 0.6 \cdot H_p$$
$$B_{pa} = B_{ta} - H_p \cdot \sin(\phi_{\text{realce}}) - F \quad [\text{m}]$$
$$N_{ta} = \operatorname{int}\left(\frac{W + 2 H_p \sin\phi}{B_{ta}} + 1\right)$$

#### 3. Sección de Corona y Hastiales
Desarrollada en la sección 2.2.2 con carga desacoplada ($q_{ce} = 0.380\text{ kg/m}$), verificando $P_{te} \le \sigma_c$.

#### 4. Sección de Auto-Tajeo y Ayudas (Algoritmo Heurístico)
En el área remanente anular entre la apertura del 4to cuadrante ($A_4 = 2.069\text{ m}$) y el contorno ($W = 4.50\text{ m}$, $H = 4.50\text{ m}$), los taladros de destrozo se distribuyen con relación $S/B = 1.25$ y $f = 1.45$:
$$B_{p,\text{tajeo}} = 0.9 \cdot \sqrt{\frac{q_1 \cdot S_{\text{ANFO}}}{C \cdot 1.45 \cdot 1.25}} - F = 0.750\text{ m}$$
$$S_{p,\text{tajeo}} = 1.25 \cdot B_{p,\text{tajeo}} = 0.938\text{ m}$$

### 2.2.4. Fundamentación Epistemológica de Sistemas Agénticos Determinísticos vs. Machine Learning
En la ingeniería de excavaciones subterráneas, la seguridad estructural y la vida humana dependen de que las leyes de la geomecánica no sean violadas. Los modelos de *Machine Learning* tradicionales (ANN, SVM, XGBoost) operan como aproximadores estadísticos de caja negra:
1. Son propensos a **alucinaciones y extrapolaciones no físicas** cuando los parámetros del frente caen fuera del dominio de entrenamiento.
2. No ofrecen **trazabilidad causal directa** para auditoría forense ante un colapso estructural o disparo fallido.

Por el contrario, la **Inteligencia Artificial Agéntica Basada en Reglas Físicas y Orquestación Modular de Herramientas (*Deterministic Agentic AI*)**:
* Garantiza determinismo y reproducibilidad matemática: cada taladro tiene una justificación causal explícita basada en ecuaciones de Navier-Stokes, Chapman-Jouguet y Holmberg.
* Incorpora compuertas de calidad (*Quality Gates*) con agentes auditores y escépticos (*Red Team*) que verifican $P_{te} \le \sigma_c$ antes de liberar cualquier diseño a mina.

---

## 2.3. Marco Conceptual Extenso (Glosario Enciclopédico Especializado)

1. **Geomecánica de Rocas:**  
   Disciplina de la ingeniería que estudia el comportamiento mecánico, el estado tensional y las deformaciones del macizo rocoso sometido a campos de esfuerzos naturales o inducidos por excavaciones mineras. En minería subterránea, proporciona los criterios cuantitativos para el dimensionamiento de labores y la selección de sostenimiento.
2. **Rock Mass Rating (RMR de Bieniawski, 1989):**  
   Sistema geomecánico de clasificación geomecánica empírica que cuantifica la calidad de un macizo rocoso mediante la ponderación de cinco parámetros básicos: resistencia de la roca intacta (UCS), RQD, espaciamiento de discontinuidades, condición de las discontinuidades (rugosidad, apertura, relleno) y presencia de agua subterránea, con un factor de ajuste por orientación de juntas. Su valor oscila de 0 a 100 puntos.
3. **Geological Strength Index (GSI de Hoek & Brown):**  
   Índice cuali-cuantitativo que caracteriza las condiciones estructurales del macizo rocoso (desde masivo hasta intensamente desintegrado) y las condiciones superficiales de las discontinuidades (desde muy buenas hasta muy pobres). Es fundamental para calcular los parámetros de resistencia del criterio de falla no lineal de Hoek-Brown.
4. **Rock Quality Designation (RQD de Deere):**  
   Medida porcentual de la calidad de recuperación de testigos de perforación diamantina, calculada como la sumatoria de longitudes de fragmentos de testigo intacto mayores o iguales a 10 cm dividida entre la longitud total de la corrida perforada. Representa el grado de competencia y fracturamiento primario del macizo.
5. **Resistencia a la Compresión Uniaxial ($\sigma_c$ / UCS):**  
   Tensión normal máxima que soporta una probeta cilíndrica de roca intacta sometida a compresión axial sin confinamiento lateral antes de experimentar la falla por cizalle o fractura frágil. Es el parámetro base de dureza y competencia rocosa.
6. **Resistencia a la Tracción ($\sigma_t$):**  
   Tensión máxima que resiste la roca intacta bajo solicitaciones de tracción directa o indirecta (ensayo brasileño). En rocas duras, su magnitud representa aproximadamente entre un $5\%$ y $10\%$ del UCS, siendo la propiedad que gobierna el fracturamiento por ondas reflejadas.
7. **Módulo de Young ($E_i$):**  
   Parámetro elástico que representa la pendiente de la curva esfuerzo-deformación lineal de la roca intacta antes del régimen plástico. Define la rigidez y la capacidad del macizo para redistribuir los esfuerzos inducidos alrededor de la excavación.
8. **Relación de Poisson ($\nu$):**  
   Cociente entre la deformación transversal unitaria y la deformación axial unitaria en un espécimen rocoso bajo esfuerzo uniaxial. Determina la magnitud de la expansión lateral y la presión de confinamiento elástico.
9. **Sobrerotura (*Overbreak*):**  
   Volumen o porcentaje de roca excavada que excede la línea de contorno perimétrico proyectada en el plano de diseño de la labor. Se produce por la propagación descontrolada de fracturas hacia el macizo encajonante, generando sobrecostos severos de limpieza y sostenimiento.
10. **Factor de Media Caña (*Half-Cast Factor* / HCF):**  
    Porcentaje visible de las trazas cilíndricas de los taladros de contorno en la corona y hastiales de la labor tras la voladura. Constituye el principal indicador empírico de la calidad de la voladura controlada; valores $> 75\%$ indican ausencia de daño perimétrico.
11. **Burden Teórico ($B_t$) y Práctico ($B_p$):**  
    El burden teórico es la distancia perpendicular máxima desde el eje del taladro cargado hacia la cara libre más cercana para lograr la rotura completa de la roca. El burden práctico resulta de restar al valor teórico los errores de perforación ($\alpha H_p + \beta$).
12. **Espaciamiento ($S$):**  
    Distancia geométrica entre taladros consecutivos pertenecientes a una misma fila o sección de voladura. Su relación con el burden ($S/B$) controla la interacción de las ondas de choque y la uniformidad de fragmentación.
13. **Taco de Sellado ($T$):**  
    Columna de material inerte (detritos de perforación, arcilla o tapones mecánicos) colocada en el cuello del taladro sobre la columna de explosivo. Su función es confinar los gases de detonación para maximizar el empuje y evitar el efecto "bocazo".
14. **Desacoplamiento Energético:**  
    Técnica que consiste en utilizar cartuchos de explosivo de diámetro significativamente menor al diámetro del taladro ($D_{cc} < D_1$), dejando un espacio anular de aire que amortigua el choque dinámico y reduce la presión de pared.
15. **Velocidad de Detonación (VOD):**  
    Velocidad lineal a la que la onda de reacción exotérmica supersónica se propaga a través de la columna continua de explosivo. Gobierna la potencia rompedora y la presión de choque emitida.
16. **Presión de Detonación de Chapman-Jouguet ($P_t$):**  
    Presión hidrodinámica en el frente de reacción de la columna de explosivo inmediatamente detrás de la onda de choque. Es función directa de la densidad del explosivo y del cuadrado de su VOD.
17. **Presión Efectiva de Taladro ($P_{te}$):**  
    Presión neta ejercida por los gases y la onda de choque en la interfaz de la pared rocosa del taladro tras el efecto de amortiguamiento del desacoplamiento anular.
18. **Voladura de Precorte (*Pre-splitting*):**  
    Técnica de voladura controlada en la que los taladros perimétricos estrechamente espaciados con cargas desacopladas se detonan antes que los taladros de producción, creando una fractura continua que aísla el macizo de las ondas de choque subsiguientes.
19. **Recorte Amortiguado (*Smooth Blasting*):**  
    Técnica de contorno en la que los taladros perimétricos desacoplados se detonan en la última posición de la secuencia de retardo, perfilando la cavidad final hacia el espacio libre ya abierto por el tajeo y arrastres.
20. **Concreto Lanzado (*Shotcrete* Vía Húmeda):**  
    Mortero o concreto proyectado neumáticamente a alta velocidad sobre la superficie rocosa mediante equipos robotizados, adicionado con fibras metálicas/sintéticas y acelerantes de fraguado para formar una membrana estructural de soporte.
21. **Sistema Agéntico Autónomo (*Agentic AI*):**  
    Arquitectura computacional de inteligencia artificial compuesta por agentes especializados que interactúan entre sí, ejecutan herramientas determinísticas en código (*Skills*) y operan bajo bucles cerrados de autocorrección sin depender de cajas negras opacas.
22. **Heurística de Auto-Tajeo:**  
    Algoritmo geométrico y computacional que evalúa el polígono espacial remanente entre el corte y el contorno de una labor subterránea, distribuyendo automáticamente los taladros de destrozo con relaciones de burden y espaciamiento físicamente equilibradas.
