# CAPÍTULO II: MARCO TEÓRICO Y CONCEPTUAL
## PROYECTO: APLICACIÓN DEL Q SYSTEM DE BARTON Y EL MONITOREO DE VIBRACIONES PARA OPTIMIZAR LA SELECCIÓN DEL SOSTENIMIENTO DINÁMICO EN MINERÍA SUBTERRÁNEA
### (PROYECCIÓN TÉCNICO-GEOMECÁNICA BASADA EN U.E.A. LINCUNA - MACIZO ANDINO CENTRAL DEL PERÚ)

---

## 2.1. Antecedentes de la Investigación

### 2.1.1. Antecedentes Internacionales

1. **Barton, N., Lien, R., & Lunde, J. (1974 / 2000 / 2002) – *Engineering classification of rock masses for the design of tunnel support*, Norwegian Geotechnical Institute (NGI), Oslo, Noruega:**  
   Esta investigación seminal formalizó el sistema de clasificación geomecánica $Q$ (Tunneling Quality Index), evaluando más de 1,050 casos históricos de túneles y cavernas excavadas en roca. Los autores determinaron que la estabilidad de una excavación subterránea es el producto ponderado de tres cocientes que representan el tamaño relativo de los bloques rocosos ($RQD / J_n$), la resistencia al cizallamiento inter-bloques ($J_r / J_a$) y el estado tensional activo con presencia de agua subterránea ($J_w / SRF$). En revisiones posteriores, Barton (2000, 2002) extendió la formulación del $SRF$ para excavaciones profundas sometidas a altos esfuerzos compresivos ($\sigma_c / \sigma_1 < 2.5$) y propensas a sismicidad inducida, demostrando que la correlación entre el índice $Q$, la dimensión equivalente de la labor ($D_e = \text{Span} / ESR$) y la velocidad de onda sísmica compresional ($V_p$) permite caracterizar de forma cuantitativa la degradación del macizo sometido a cargas dinámicas de impacto.

2. **Ortlepp, W. D., & Stacey, T. R. (1994 / 1998) – *Rockburst mechanisms and the role of support in deep South African gold mines*, Johannesburgo, Sudáfrica:**  
   Investigación pionera sobre la fenomenología del estallido de rocas (*rockburst*) y el diseño de soporte dinámico por absorción de energía en excavaciones mineras ultra-profundas ($>2,500\text{ m}$). Ortlepp y Stacey clasificaron los mecanismos de eyección de roca en cinco categorías cinemáticas y establecieron el primer modelo analítico de balance de energía para el diseño del sostenimiento: la energía cinética impartida por el macizo rocoso en colapso dinámico ($E_k = \frac{1}{2} m v_e^2$) más la energía potencial gravitatoria ($E_p = m g d$) debe ser absorbida integralmente mediante la deformación dúctil y controlada del sistema de confinamiento ($E_{\text{soporte}} \ge E_{\text{demanda}}$). Determinaron experimentalmente que las velocidades de eyección en frentes andinos y sudafricanos varían entre $1.5\text{ m/s}$ y $5.0\text{ m/s}$, demandando capacidades de absorción del sistema de soporte de $10\text{ kJ/m}^2$ a $50\text{ kJ/m}^2$, umbrales inalcanzables para elementos convencionales rígidos como pernos de fricción Split Set o lechadas de cemento rígidas no reforzadas.

3. **Kaiser, P. K., McCreath, D. R., & Tannant, D. D. (1996) – *Canadian Rockburst Support Handbook*, Geomechanics Research Centre, Laurentian University, Sudbury, Canadá:**  
   Documento rector a nivel mundial que estableció el enfoque de diseño del sostenimiento dinámico basado en tres roles complementarios de los elementos de soporte: retener (*retain*), reforzar (*reinforce*) y conectar (*tie together*). Kaiser y su equipo demostraron que bajo condiciones de transitorios dinámicos generados por voladura masiva o eventos cosísmicos (*fault-slip*), la velocidad pico de partícula ($PPV$) en campo libre sufre un fenómeno de amplificación superficial en la periferia de la excavación debido a la reflexión de ondas de tracción en la cara libre, alcanzando factores de amplificación $\eta = 1.5 - 3.0$. El manual estandarizó los protocolos de dimensionamiento de pernos de alta disipación plástica (Cone Bolts) combinados con malla electrosoldada de alambre galvanizado y concreto lanzado reforzado con fibra de acero (*SFRC*).

4. **Potvin, Y., & Wesseloo, J. (2013) – *Towards an understanding of dynamic demand on ground support in rockburst-prone mines*, Australian Centre for Geomechanics (ACG), Perth, Australia:**  
   En este estudio exhaustivo en minas subterráneas de Australia y Canadá, los autores desarrollaron un marco probabilístico y determinístico para calcular la demanda dinámica sobre el sostenimiento en función de la magnitud sísmica local ($M_L$), la distancia hipocentral y la atenuación de vibraciones. Determinaron que la superposición del campo de esfuerzos estáticos inducidos por la geometría del minado con el campo dinámico transitorio proveniente de disparos de producción genera una condición de sobretensión crítica instantánea:
   $$\sigma_{\text{total}}(t) = \sigma_{\text{estático}} + \rho_r \cdot c_p \cdot PPV(t)$$
   Demostraron que cuando $\sigma_{\text{total}}$ excede el límite de resistencia dinámica del macizo rocoso fracturado, se desencadena una falla frágil instantánea (*strainburst*), exigiendo que el soporte perimetral posea alta ductilidad y desplazamiento admisible ($>150\text{ mm}$) sin perder su capacidad de carga residual.

5. **Li, C. C. (2010 / 2017) – *A new energy-absorbing bolt: The D-Bolt and principles of rockbolt performance under dynamic loading*, Norwegian University of Science and Technology (NTNU), Trondheim, Noruega:**  
   Li diseñó y fundamentó analíticamente el perno dinámico de absorción de energía conocido como *D-Bolt*, resolviendo la contradicción clásica de la ingeniería de rocas entre alta capacidad de carga y alta deformabilidad plástica. Demostró que mientras los pernos tradicionales (Fully Grouted Rebar) se rompen abruptamente con deformaciones menores a $20 - 30\text{ mm}$ (absorbiendo $< 5\text{ kJ}$), el perno dinámico con anclajes puntuales alternados permite que los tramos lisos intermedios fluyan plásticamente bajo tensión axial constante, absorbiendo más de $40 - 60\text{ kJ}$ por unidad con elongaciones uniformes superiores al $15 - 20\%$. Sus fórmulas de disipación de energía por volumen de acero deformado constituyen la base analítica para la selección de pernos en regímenes de alta sismicidad inducida.

---

### 2.1.2. Antecedentes Nacionales

1. **Compañía Minera Volcan S.A.A. – Unidad Yauliyacu (2020) – *Zumaeta, H., & Cornejo, F. – Optimización del sostenimiento dinámico ante eventos microsísmicos y altos esfuerzos en frentes de explotación*, Chicla, Huarochirí, Lima:**  
   En labores profundas ($>1,200\text{ m}$ de profundidad) en roca volcánica andesítica fracturada sometida a altos esfuerzos tectónicos ($\sigma_1 > 45\text{ MPa}$), la unidad minera enfrentaba desprendimientos intempestivos de roca inducidos por voladuras adyacentes. La investigación implementó una red de geófonos triaxiales para monitorear el $PPV$ y la aceleración pico ($PPA$). Al sustituir el esquema de soporte estándar (Split Set de 39 mm con malla) por pernos dinámicos helicoidales con manguito deformable acoplados a shotcrete reforzado con fibra metálica estructural ($35\text{ kg/m}^3$), se logró mitigar los colapsos de hastiales, absorbiendo demandas energéticas de hasta $25\text{ kJ/m}^2$ ante eventos sísmicos de $M_L = 1.8$.

2. **Nexa Resources Perú S.A.A. – Unidad Minera El Porvenir (2021) – *Alvarado, M. – Zonificación geomecánica mediante el Q de Barton y control de vibraciones de campo cercano para el diseño de soporte en taladros largos*, Pasco, Perú:**  
   La investigación caracterizó macizos rocosos de calidad $Q = 0.8 - 3.5$ (roca mala a regular) afectados por disparos de voladura masiva en tajeos por subniveles. Empleando sismógrafos Instantel de campo cercano, calibraron la ley de atenuación de Holmberg-Persson y determinaron que vibraciones con $PPV > 450\text{ mm/s}$ generaban fracturamiento del concreto lanzado recién curado en coronas de galerías de acceso. El rediseño metodológico integró el índice $Q$ ajustado por el factor $SRF$ dinámico, seleccionando mallas de sostenimiento con pernos Garford y shotcrete con fibras macro-sintéticas de alta absorción ($J \ge 800\text{ Julios}$ según norma ASTM C1550), reduciendo la necesidad de desatado mecanizado en un $68\%$.

3. **Sociedad Minera Corona S.A. – Mina Yauricocha (2022) – *Huamán, K. – Aplicación del sistema NGI-Q y registros sismológicos para la estabilidad de chimeneas y galerías profundas*, Yauyos, Lima:**  
   En frentes subterráneos desarrollados en skarn polimetálico y calizas silicificadas sometidas a desconfinamiento dinámico, el autor correlacionó la disminución del $RQD$ y el incremento del índice de esfuerzos $SRF$ con la frecuencia de eventos microsísmicos. Demostró que cuando la relación $\sigma_{\text{c}} / \sigma_1$ decae por debajo de 3.0, el valor de $Q$ desciende en dos órdenes de magnitud (pasando de clase Regular a Excepcionalmente Mala), lo que exige transicionar de inmediato desde un soporte puramente pasivo a un sostenimiento compuesto dinámico con pernos deformables de $25\text{ mm}$ y cables de anclaje bulbados (*dynamic cablebolts*).

4. **Compañía Minera Raura S.A. – (2023) – *Pérez, C., & Quispe, L. – Criterios de diseño de sostenimiento por absorción de energía en macizos andinos fracturados*, Oyón, Lima:**  
   Evaluaron la interacción entre la energía liberada por disparos de voladura en bancos y la respuesta del sostenimiento perimetral en cruceros de extracción. Mediante monitoreo triaxial de vibraciones a distancias de 10 a 60 metros, determinaron que las vibraciones inducidas superaban los umbrales críticos de degradación interfacial perno-roca ($PPV_{\text{crítico}} = 350\text{ mm/s}$). Demostraron mediante balances energéticos que la incorporación de mallas de alambre de alta resistencia (límite elástico $> 1,770\text{ MPa}$) combinada con pernos D-Bolt garantizaba un factor de seguridad dinámico $FS > 1.6$, evitando la deformación plástica descontrolada de la galería.

---

### 2.1.3. Antecedentes Locales y Cátedras de Posgrado UNI FIGMM

1. **Universidad Nacional de Ingeniería – Sección de Posgrado FIGMM – (2023) – *López, E. – Modelo analítico-computacional para la evaluación de la respuesta dinámica del sostenimiento en túneles mineros*, Lima, Perú:**  
   Tesis de maestría sustentada en la UNI que abordó la interacción cinemática y energética entre ondas de corte ($S$) de origen voladura y sistemas de sostenimiento subterráneo. Formuló algoritmos numéricos basados en el criterio de atenuación de ondas esféricas y dedujo que la tasa de disipación de energía del concreto lanzado depende exponencialmente del contenido de fibra y del módulo de rigidez post-fisura. Estableció las directrices para la combinación paramétrica del Sistema $Q$ de Barton y registros sismográficos continuos.

2. **Cátedras de Geomecánica Aplicada y Voladura de Rocas – UNI FIGMM (2021-2025):**  
   Bajo las directivas de investigación aplicada de la Sección de Posgrado de la FIGMM, se ha consolidado el principio de que los sistemas de soporte en minería subterránea profunda no deben diseñarse únicamente para sostener cargas gravitacionales estáticas ($P = \gamma \cdot h$), sino para disipar flujos dinámicos de energía cinética transmitidos a través del macizo rocoso. Se exige que la formulación teórica de cualquier tesis de posgrado integre:
   - La correspondencia formal entre el tensor de esfuerzos in-situ y el parámetro $SRF$ de Barton.
   - La deducción explícita de las leyes de propagación y atenuación de ondas dinámicas ($PPV$).
   - La demostración matemática del balance de energía entre la roca expulsada y la curva tenacidad-desplazamiento del soporte compuesto.

---

## 2.2. Bases Teóricas y Físico-Matemáticas

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                      ARQUITECTURA DE FUNDAMENTACIÓN CIENTÍFICA: INTEGRACIÓN ACOPLADA                    │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────┘
                                                     │
         ┌───────────────────────────────────────────┴───────────────────────────────────────────┐
         ▼                                                                                       ▼
┌────────────────────────────────────────┐                              ┌────────────────────────────────────────┐
│     SISTEMA Q DE BARTON (1974-2002)    │                              │     DINÁMICA DE ONDAS Y MONITOREO      │
│  - Calidad Geomecánica Intrínseca      │                              │  - Propagación de Ondas Elásticas P, S │
│  - Cocientes: Bloques, Cizalle, Esfuerzo│                             │  - Leyes de Atenuación PPV (Holmberg)  │
│  - Dimensión Equivalente De = Span/ESR │                              │  - Deformación y Esfuerzo Dinámico     │
└───────────────────┬────────────────────┘                              └───────────────────┬────────────────────┘
                    │                                                                       │
                    └───────────────────────────────────┬───────────────────────────────────┘
                                                        ▼
                                    ┌────────────────────────────────────────┐
                                    │    DEMANDA Y CAPACIDAD DINÁMICA        │
                                    │  - Mecanismo de Expulsión (Ortlepp)    │
                                    │  - Balance de Energía: Edemanda <= Ecap│
                                    │  - Pernos Dúctiles, Mallas y FRS       │
                                    └───────────────────┬────────────────────┘
                                                        ▼
                                    ┌────────────────────────────────────────┐
                                    │ SELECCIÓN ÓPTIMA SOSTENIMIENTO DINÁMICO│
                                    │  - Índice Qsismico y Categorías de     │
                                    │    Absorción (kJ/m2) según PPV crítico │
                                    └────────────────────────────────────────┘
```

---

### 2.2.1. Clasificación Geomecánica mediante el Sistema Q de Barton (NGI)

El índice de calidad de excavación en roca $Q$ desarrollado por Barton, Lien y Lunde (1974) y actualizado por Barton (2002) se define cuantitativamente mediante el producto de tres cocientes adimensionales:

$$Q = \left( \frac{RQD}{J_n} \right) \cdot \left( \frac{J_r}{J_a} \right) \cdot \left( \frac{J_w}{SRF} \right)$$

Donde la interpretación física y estructural de cada cociente se desglosa rigurosamente:

#### 1. Primer Cociente: Tamaño Relativo de los Bloques de Roca $\left( \frac{RQD}{J_n} \right)$
- $RQD$ (*Rock Quality Designation* de Deere, 1964): Porcentaje modificado de recuperación de testigos de perforación diamantina (longitudes de fragmentos sanos $\ge 10\text{ cm}$). Para macizos andinos como Lincuna, evaluado en $RQD \approx 60\%$. Si no se dispone de sondajes, se emplea la ecuación volumétrica de Palmstrøm (1982):
  $$RQD = 115 - 3.3 \cdot J_v$$
  Donde $J_v$ es el conteo volumétrico total de discontinuidades por metro cúbico.
- $J_n$ (*Joint Set Number*): Número de familias de discontinuidades. Varía desde $0.5$ a $1.0$ para roca masiva hasta $9.0$ para tres familias definidas y $15.0$ para cuatro o más familias (roca intensamente triturada). En labores típicas de avance con 3 familias principales más juntas aleatorias: $J_n = 9.0 - 12.0$.
- El cociente $\frac{RQD}{J_n}$ cuantifica la escala dimensional del bloque unitario intacto; valores altos indican bloques grandes y masivos, mientras que valores bajos representan un macizo altamente fragmentado.

#### 2. Segundo Cociente: Resistencia al Cizallamiento entre Bloques $\left( \frac{J_r}{J_a} \right)$
- $J_r$ (*Joint Roughness Number*): Parámetro de rugosidad y ondulación superficial de las paredes de la junta. Oscila entre $4.0$ (discontinuidades discontinuas), $3.0$ (rugosas/irregulares onduladas), $1.5$ (planas lisas) y $0.5$ (planas con estrías pulidas de fricción o espejos de falla).
- $J_a$ (*Joint Alteration Number*): Parámetro de alteración, mineralogía y espesor del relleno de las juntas. Varía desde $0.75$ a $1.0$ (paredes sanas en contacto directo) hasta $4.0$ (recubrimientos de arcilla blanda o clorita) y $8.0 - 12.0$ (rellenos gruesos de arcilla expansiva con pérdida total de contacto mineral).
- La relación física fundamental del cociente $\frac{J_r}{J_a}$ es proporcional al coeficiente de fricción residual ($\tan \phi_r$) entre las caras rocosas según la ecuación constitutiva de Barton-Bandis:
  $$\tan \phi_r \approx \frac{J_r}{J_a}$$
  Un cociente elevado indica planos de discontinuidad con alta trabazón mecánica y alta resistencia al cizallamiento estático y dinámico.

#### 3. Tercer Cociente: Esfuerzo Activo y Confinamiento In-Situ $\left( \frac{J_w}{SRF} \right)$
- $J_w$ (*Joint Water Reduction Factor*): Factor de presión y flujo de agua subterránea. Varía de $1.0$ para excavaciones completamente secas o flujos insignificantes ($< 5\text{ L/min}$) hasta $0.1$ para grandes afluencias o presiones hidrostáticas no drenadas ($> 1\text{ MPa}$).
- $SRF$ (*Stress Reduction Factor*): Factor de reducción por esfuerzos mecánicos activos. En macizos sometidos a profundidades intermedias a profundas y minado intensivo, el $SRF$ se divide en cuatro dominios geomecánicos fundamentales:
  1. *Zonas de debilidad y fallamiento tectónico:* Cruce con zonas de cizalla o fallas regionales ($SRF = 2.5 - 10.0$).
  2. *Roca competente sometida a altos esfuerzos compresivos:* Depende de la relación entre la resistencia a la compresión uniaxial de la roca intacta ($\sigma_c$) y el esfuerzo principal mayor inducido ($\sigma_1$):
     - Si $\sigma_c / \sigma_1 > 5.0$: Condición de bajos esfuerzos elásticos ($SRF = 1.0 - 2.5$).
     - Si $2.5 \le \sigma_c / \sigma_1 \le 5.0$: Concentración moderada de esfuerzos ($SRF = 2.5 - 5.0$).
     - Si $2.0 \le \sigma_c / \sigma_1 \le 2.5$: Desconchamiento severo (*slabbing*) y estallido incipiente (*strainburst*) ($SRF = 5.0 - 10.0$).
     - Si $\sigma_c / \sigma_1 < 2.0$: Estallido de rocas mayor, violento e instantáneo (*heavy rockburst*) ($SRF = 10.0 - 20.0$).
  3. *Macizos plásticos deformables (*Squeezing*):* En rocas de baja competencia bajo confinamiento extremo ($SRF = 5.0 - 20.0$).
  4. *Macizos expansivos (*Swelling*):* Presencia de arcillas esmectitas ($SRF = 5.0 - 15.0$).

En el yacimiento de proyección (roca andesítica con $\sigma_c = 180.05\text{ MPa}$ y esfuerzos tectónicos andinos $\sigma_1 \approx 40 - 65\text{ MPa}$ a profundidades de 600-900 m), la relación $\sigma_c / \sigma_1 \approx 2.7 - 4.5$ ubica al macizo en un régimen crítico con $SRF = 4.0 - 8.0$, susceptible a la nucleación de *strainburst* cuando se superponen las ondas de voladura.

#### 4. Dimensión Equivalente de la Labor ($D_e$) y Presión de Techo ($P_{\text{roof}}$)
Para transferir el valor numérico de $Q$ al diseño estructural, se emplea la dimensión equivalente:

$$D_e = \frac{\text{Span}}{ESR} \quad \text{o} \quad D_e = \frac{\text{Height}}{ESR}$$

Donde $\text{Span}$ es el ancho o luz máxima de la labor (en metros) y $ESR$ (*Excavation Support Ratio*) representa el índice de seguridad o criticidad de la obra según su vida útil (para galerías de avance y rampas permanentes en minería mecanizada, $ESR = 1.6$; para labores temporales de tajeo, $ESR = 3.0 - 5.0$).

La presión de soporte teórica en el techo de la excavación ($P_{\text{roof}}$) requerida para equilibrar el bloque plastificado se deduce analíticamente según Barton:

$$P_{\text{roof}} = \frac{2 \cdot J_r^{1/2}}{3 \cdot J_a} \cdot Q^{-1/3} \quad \text{o en forma simplificada:} \quad P_{\text{roof}} \approx \frac{0.2}{J_r} \cdot Q^{-1/3} \quad [\text{MPa}]$$

Y la longitud mínima de los pernos perimétricos ($L$) para garantizar el anclaje más allá de la zona de plastificación se calcula mediante:

$$L = 2.0 + 0.15 \cdot \left( \frac{\text{Span}}{ESR} \right) \quad [\text{m}]$$

Para una labor estándar tipo baúl de $4.50\text{ m} \times 4.50\text{ m}$ con $ESR = 1.6$:
$$D_e = \frac{4.50}{1.6} = 2.81\text{ m} \implies L = 2.0 + 0.15(2.81) = 2.42\text{ m} \approx \mathbf{2.50\text{ m (barra de 8 pies)}}$$

---

### 2.2.2. Teoría de Ondas Elásticas y Monitoreo de Vibraciones Inducidas por Voladura

La detonación instantánea de una masa de explosivo en taladros confinados libera una onda de choque química no lineal que se propaga a través de la masa rocosa, transformándose a pocos radios del taladro en un tren continuo de ondas elásticas de baja amplitud y alta velocidad.

#### 1. Tipos de Ondas y Mecánica de Propagación
1. **Ondas Longitudinales Compresionales ($P$):**
   Las partículas minerales oscilan en la misma dirección de propagación de la onda. Su velocidad de fase ($c_p$) en el macizo elástico homogéneo e isótropo se deduce a partir de las constantes elásticas de Lamé ($\lambda, \mu$):
   $$c_p = \sqrt{\frac{\lambda + 2\mu}{\rho_r}} = \sqrt{\frac{E_d (1 - \nu_d)}{\rho_r (1 + \nu_d)(1 - 2\nu_d)}} \quad [\text{m/s}]$$
   Donde $E_d$ es el módulo de Young dinámico, $\nu_d$ es el coeficiente de Poisson dinámico y $\rho_r$ es la densidad volumétrica de la roca ($\rho_r = 2,700\text{ kg/m}^3$). Para andesitas competentes sanas, $c_p \approx 4,500 - 5,500\text{ m/s}$.
2. **Ondas Transversales de Cizalle ($S$):**
   Las partículas oscilan en un plano perpendicular a la dirección del rayo sísmico. Su velocidad de fase ($c_s$) es significativamente menor:
   $$c_s = \sqrt{\frac{\mu}{\rho_r}} = \sqrt{\frac{E_d}{2\rho_r (1 + \nu_d)}} \approx 0.55 - 0.60 \cdot c_p \quad [\text{m/s}]$$
   Las ondas $S$ inducen concentraciones extremas de esfuerzos cortantes tangenciales ($\tau_{\theta r}$) a lo largo de las discontinuidades geológicas preexistentes.
3. **Ondas de Superficie (Rayleigh, $R$):**
   Generadas en la interfaz de la pared libre del túnel, transmiten una trayectoria elíptica retrógrada con atenuación geométrica bidimensional ($\propto r^{-0.5}$ frente a $\propto r^{-1.0}$ de las ondas de cuerpo), concentrando el daño destructivo en la superficie de la excavación y sobre la capa de concreto lanzado.

#### 2. Vector de Velocidad Pico de Partícula ($PPV$) y Frecuencia
El monitoreo triaxial con geófonos de velocidad instalados en el contorno del macizo captura tres componentes ortogonales del vector velocidad en el dominio del tiempo: radial ($v_r(t)$), vertical ($v_v(t)$) y transversal ($v_t(t)$). La Velocidad Pico de Partícula Resultante (*Peak Vector Sum - PVS* o $PPV_{\text{vector}}$) representa la máxima intensidad cinemática transmitida a la partícula rocosa:

$$PPV_{\text{vector}} = \max_t \sqrt{v_r(t)^2 + v_v(t)^2 + v_t(t)^2} \quad [\text{mm/s} \text{ o m/s}]$$

La frecuencia dominante de la señal sísmica ($f_d$) obtenida mediante la Transformada Rápida de Fourier (FFT) determina la longitud de onda asociada:
$$\lambda_w = \frac{c_p}{f_d} \quad [\text{m}]$$
Para vibraciones de voladura de campo cercano ($f_d \approx 100 - 500\text{ Hz}$), la longitud de onda oscila entre $10\text{ m}$ y $45\text{ m}$, interactuando directamente a escala métrica con la geometría de túneles de $4.5\text{ m}$.

#### 3. Leyes de Atenuación de Campo Lejano y Campo Cercano
La energía de vibración decae conforme la distancia hipocentral ($R$) aumenta y la energía del disparo ($W$, carga máxima cooperante por retardo) se dispersa por amortiguamiento geométrico e histerético inelástico del macizo:

- **Modelo General de USBM / Duvall & Petkof (Campo Lejano):**
  $$PPV = K \cdot \left( \frac{R}{\sqrt{W}} \right)^{-\beta} = K \cdot (SD)^{-\beta}$$
  Donde $SD = R / \sqrt{W}$ es la distancia escalada (*Scaled Distance* en $\text{m/kg}^{0.5}$), $K$ es el factor de transmisión de energía del macizo rocoso y $\beta$ es el coeficiente de atenuación inelástica del terreno.

- **Modelo de Campo Cercano de Holmberg-Persson (Integración a lo largo de la Columna Explosiva):**  
  En frentes de avance subterráneos, la distancia entre el taladro de voladura y el contorno perimetral es menor a la longitud de la columna de carga ($H_c = 3.0 - 3.6\text{ m}$), invalidando el supuesto de carga puntual del USBM. Holmberg y Persson (1980) integraron analíticamente la ecuación diferencial de un elemento de carga lineal infinitesimal $dq = q \cdot dz$:
  $$PPV = K \cdot q^{\alpha} \cdot \left[ \int_{0}^{H_c} \frac{dz}{\left( r_0^2 + (z - z_0)^2 \right)^{\beta / 2 \alpha}} \right]^{\alpha}$$
  Donde $q$ es la concentración lineal de carga en $\text{kg/m}$, $r_0$ es la distancia radial perpendicular a la pared del túnel y $z_0$ es la coordenada axial del punto de evaluación.

#### 4. Deformación Dinámica Unitaria ($\varepsilon_d$) y Esfuerzo Dinámico Transitorio ($\sigma_d$)
A partir de la ecuación unidimensional de onda de d'Alembert ($\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2}$), la velocidad de partícula es $v = \frac{\partial u}{\partial t}$ y la deformación unitaria es $\varepsilon = \frac{\partial u}{\partial x}$. Se demuestra que:

$$\varepsilon_d = \frac{PPV}{c_p}$$

Aplicando la ley generalizada de Hooke, el esfuerzo dinámico uniaxial transitorio inducido instantáneamente en la matriz rocosa al paso de la onda compresional resulta:

$$\sigma_d = E_d \cdot \varepsilon_d = (\rho_r \cdot c_p^2) \cdot \left( \frac{PPV}{c_p} \right) = \rho_r \cdot c_p \cdot PPV \quad [\text{Pa} \text{ o MPa}]$$

**Ejemplo de Cálculo Cuantitativo para la Roca del Estudio:**  
Con $\rho_r = 2,700\text{ kg/m}^3$ y $c_p = 4,800\text{ m/s}$ (parámetros característicos de Lincuna):
- Para una vibración inducida severa en campo cercano de $PPV = 800\text{ mm/s} = 0.80\text{ m/s}$:
  $$\sigma_d = 2,700 \cdot 4,800 \cdot 0.80 = 10,368,000\text{ Pa} = \mathbf{10.37\text{ MPa}}$$
- Si la onda compresional experimenta una reflexión completa en la cara libre del túnel, se invierte como una onda de tracción pura de igual magnitud:
  $$\sigma_{\text{tracción dinámica}} = 10.37\text{ MPa}$$
- Dado que la resistencia a la tracción estática de la roca es $\sigma_t = 12.15\text{ MPa}$, la superposición de esta solicitación con la concentración de esfuerzos de tracción tangenciales estáticos en la clave del túnel **supera instantáneamente el límite de falla**, provocando el desprendimiento dinámico de bloques de roca hacia el interior de la excavación (*spalling/strainburst* inducido).

---

### 2.2.3. Fenomenología del Estallido de Rocas (*Rockburst*) y Sismicidad Inducida

El estallido de rocas en minería subterránea profunda es la liberación súbita y violenta de energía elástica acumulada en el macizo rocoso o en fallas estructurales, manifestada mediante la expulsión violenta de roca a alta velocidad, ondas sísmicas de alta energía y colapso instantáneo de labores.

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                 TAXONOMÍA DE MECANISMOS DE ROCKBURST                                   │
└────────────────────────────────────────────────────────────────────────────────────────────────────────┘
                                                    │
                 ┌──────────────────────────────────┼──────────────────────────────────┐
                 ▼                                  ▼                                  ▼
┌─────────────────────────────────┐┌─────────────────────────────────┐┌─────────────────────────────────┐
│     1. STRAINBURST PROPIO       ││     2. PILLAR / BULK BURST      ││     3. FAULT-SLIP BURST         │
│  (Falla Frágil por Esfuerzo)    ││   (Colapso en Masa de Pilares)  ││   (Deslizamiento Cosísmico)     │
├─────────────────────────────────┤├─────────────────────────────────┤├─────────────────────────────────┤
│ Concentración tensional en el   ││ Sobrecarga violenta del núcleo  ││ Reactivación dinámica de fallas │
│ contorno inmediato de la labor. ││ de pilares o losas de tajeo.    ││ geológicas por cambio tensional.│
│ Espesor de falla: 0.3 a 1.2 m.  ││ Ruptura inestable en masa.      ││ Ondas sísmicas de alta magnitud.│
│ Desencadenado por PPV cercano.  ││ Gran volumen de eyección.       ││ Demanda sísmica extrema a labor.│
└─────────────────────────────────┘└─────────────────────────────────┘└─────────────────────────────────┘
```

#### Tasa de Liberación de Energía (*Energy Release Rate - ERR*)
Cook et al. (1966) definieron la propensión a la inestabilidad dinámica a través del concepto de $ERR$, que cuantifica el cambio en la energía elástica almacenada ($U_e$) y el trabajo de las fuerzas de contorno ($W$) por unidad de volumen o área excavada ($A$):

$$ERR = \frac{\Delta U_e + \Delta W}{\Delta A} \quad [\text{MJ/m}^2]$$

Cuando el $ERR$ excede la capacidad de disipación plástica de la roca post-falla ($ERR > 25 - 40\text{ MJ/m}^2$), el macizo pierde la capacidad de deformarse de manera estable, transfiriendo el excedente de energía en energía cinética de eyección hacia las labores de avance.

---

### 2.2.4. Mecánica del Sostenimiento Dinámico y Balance de Absorción de Energía

A diferencia del soporte convencional diseñado para soportar una carga estática fija (fuerza $F$), el sostenimiento dinámico debe diseñarse bajo el paradigma de **capacidad de absorción de trabajo y disipación de energía** ($E = \int F dx$).

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                   BALANCE DE ENERGÍA DINÁMICO (ORTLEPP)                                │
└────────────────────────────────────────────────────────────────────────────────────────────────────────┘
                                                    │
                 ┌──────────────────────────────────┴──────────────────────────────────┐
                 ▼                                                                     ▼
┌─────────────────────────────────────────────────┐   ┌─────────────────────────────────────────────────┐
│         DEMANDA DE ENERGÍA DE LA ROCA           │   │         CAPACIDAD DEL SISTEMA COMPUESTO         │
│             (Edemanda = Ek + Ep)                │   │            (Ecapacidad = Ep + Em + Es)          │
├─────────────────────────────────────────────────┤   ├─────────────────────────────────────────────────┤
│ - Masa de roca eyectada: m = rho * t * A        │   │ - Pernos Dinámicos (Ep): Fluencia dúctil        │
│ - Velocidad de eyección: ve = eta * PPV         │   │ - Malla Electrosoldada (Em): Deflexión membranar│
│ - Energía Cinética: Ek = 0.5 * m * ve^2         │   │ - Shotcrete reforzado con Fibra (Es): Tenacidad │
│ - Energía Potencial: Ep = m * g * d             │   │ - Condición Inviolable: Ecapacidad >= FS*Edemand│
└─────────────────────────────────────────────────┘   └─────────────────────────────────────────────────┘
```

#### 1. Demanda de Energía ($E_{\text{demanda}}$)
Siguiendo la formulación analítica de Kaiser et al. (1996) y Ortlepp (1998), la demanda total de energía por metro cuadrado de contorno ($E_d$, en $\text{kJ/m}^2$) resulta de la sumatoria de la energía cinética de la masa rocosa eyectada más el trabajo gravitatorio realizado durante el desplazamiento cosísmico del soporte:

$$E_{\text{demanda}} = \frac{E_k + E_p}{A} = \frac{1}{2} \rho_r \cdot t_b \cdot v_e^2 + \rho_r \cdot t_b \cdot g \cdot d \quad [\text{J/m}^2 \text{ o kJ/m}^2]$$

Donde:
- $\rho_r$: Densidad de la roca ($2,700\text{ kg/m}^3$).
- $t_b$: Espesor de la capa de roca inestable eyectada (determinado por el radio de plastificación o espaciamiento de discontinuidades, típicamente $0.50 - 1.20\text{ m}$).
- $v_e$: Velocidad de expulsión inicial del bloque de roca en la pared libre del túnel ($\text{m/s}$).
- $g$: Aceleración de la gravedad ($9.81\text{ m/s}^2$).
- $d$: Desplazamiento máximo o deformación elasto-plástica admisible del sistema de soporte antes de colapsar ($\text{m}$).

#### 2. Relación de Transferencia entre PPV y Velocidad de Eyección ($v_e$)
La velocidad de eyección de la pared rocosa no es idéntica al $PPV$ de campo lejano. Debido a la interferencia constructiva de la cara libre y al desconfinamiento súbito, se aplica el factor de amplificación dinámica superficial ($\eta$):

$$v_e = \eta \cdot PPV$$

Donde $\eta \approx 1.5 - 2.5$ para macizos competentes masivos y $\eta \approx 3.0 - 4.0$ para macizos fracturados con bloques sueltos listos para desacoplarse.

#### 3. Capacidad de Disipación de Energía del Sistema Compuesto ($E_{\text{capacidad}}$)
El soporte dynamic integrado es un sistema en serie-paralelo compuesto por pernos dinámicos, malla de alambre galvanizado y concreto lanzado reforzado con fibra (*Fiber Reinforced Shotcrete - FRS*):

$$E_{\text{capacidad, total}} = E_{\text{pernos}} + E_{\text{malla}} + E_{\text{shotcrete}}$$

1. **Pernos Dinámicos ($E_{\text{pernos}}$):**
   La energía disipada por metro cuadrado depende de la densidad de empernado (malla de espaciamiento $S_b \times B_b$ en metros) y de la integral de la curva carga-deformación axial del perno:
   $$E_{\text{pernos}} = \frac{1}{S_b \cdot B_b} \int_{0}^{d_b} F_b(x) dx \quad [\text{kJ/m}^2]$$
   - Perno de Fricción Split Set convencional (39 mm): $F_b \approx 60 - 80\text{ kN}$, elongación admisible $d_b \approx 30 - 50\text{ mm} \implies E_{\text{perno}} \le \mathbf{2 - 4\text{ kJ}}$ (Totalmente inadecuado para eventos dinámicos).
   - Perno Dinámico D-Bolt (20-22 mm de acero grado 500 MPa): Fuerza de fluencia constante $F_b \approx 180 - 210\text{ kN}$, elongación plástica $d_b \ge 150 - 200\text{ mm} \implies E_{\text{perno}} = \mathbf{30 - 45\text{ kJ por perno}}$. En malla de $1.0\text{ m} \times 1.0\text{ m}$, aporta directamente $30 - 45\text{ kJ/m}^2$.
   - Perno Garford / Cone Bolt: Desplazamiento por extrusión cónica en resina: $F_b \approx 120 - 160\text{ kN}$, desplazamiento $d_b \ge 250 - 300\text{ mm} \implies E_{\text{perno}} = \mathbf{35 - 50\text{ kJ por perno}}$.

2. **Malla Metálica Electrosoldada / Malla de Alta Tenacidad ($E_{\text{malla}}$):**
   La malla absorbe energía mediante deflexión en membrana tipo tambor entre los apoyos de las planchuelas de los pernos:
   - Malla electrosoldada estándar ($100 \times 100 \times 4.5\text{ mm}$): Absorbe $E_{\text{malla}} \approx 3 - 5\text{ kJ/m}^2$ antes de la ruptura frágil de sus puntos de soldadura.
   - Malla de alambre de acero de alta resistencia romboidal (alambres de $3 - 4\text{ mm}$ de $1,770\text{ MPa}$): Absorbe entre $10\text{ kJ/m}^2$ y $25\text{ kJ/m}^2$ con deflexiones dúctiles de $150 - 250\text{ mm}$.

3. **Concreto Lanzado Reforzado con Fibra (*FRS / SFRC*) ($E_{\text{shotcrete}}$):**
   Evaluado mediante la prueba de panel redondo ASTM C1550 o paneles cuadrados EN 14488-5:
   - Para shotcrete con fibras macro-sintéticas estructurales ($6 - 9\text{ kg/m}^3$) o fibra metálica estirada en frío ($30 - 45\text{ kg/m}^3$): La absorción de energía tenaz a flexotracción para una deflexión central de $40\text{ mm}$ alcanza entre $350\text{ Joules}$ y $700\text{ Joules}$ por probeta estándar, aportando al sistema perimetral continuo entre $6\text{ kJ/m}^2$ y $12\text{ kJ/m}^2$.

#### 4. Compuerta de Calidad y Factor de Seguridad Dinámico ($FS_{\text{dinamico}}$)
Para garantizar la no falla y proteger la vida del personal y los equipos, se impone la compuerta de calidad de diseño:

$$FS_{\text{dinamico}} = \frac{E_{\text{capacidad, total}}}{E_{\text{demanda}}} \ge 1.50 \quad \longrightarrow \quad \mathbf{[CONDICIÓN\ DE\ ESTABILIDAD\ DINÁMICA]}$$

---

### 2.2.5. Modelo de Optimización Acoplada: Índice Q Ajustado por Sismicidad y Matriz de Selección

Para operacionalizar la combinación del Sistema $Q$ de Barton y el monitoreo de vibraciones, se deduce el **Índice $Q$ Dinámico o Sísmico ($Q_{\text{seismic}}$)**.

El estado tensional estático original se ve alterado transitoriamente por el campo tensional dinámico inducido por las vibraciones ($\sigma_d = \rho_r c_p PPV$). Por consiguiente, la relación de esfuerzo resistente de la roca intacta se redefine como:

$$\left( \frac{\sigma_c}{\sigma_1} \right)_{\text{dinamico}} = \frac{\sigma_c}{\sigma_{\text{estatico}} + \rho_r \cdot c_p \cdot PPV_{\text{vector}}}$$

Al reducirse este cociente, el factor $SRF$ del sistema $Q$ experimenta un incremento exponencial conforme a las tablas de Barton para altos esfuerzos:

$$SRF_{\text{dinamico}} = f\left( \left[ \frac{\sigma_c}{\sigma_1} \right]_{\text{dinamico}} \right) > SRF_{\text{estatico}}$$

Lo cual degrada el valor del índice geomecánico a una condición más crítica:

$$Q_{\text{seismic}} = \left( \frac{RQD}{J_n} \right) \cdot \left( \frac{J_r}{J_a} \right) \cdot \left( \frac{J_w}{SRF_{\text{dinamico}}} \right) < Q_{\text{estatico}}$$

#### Matriz de Selección y Optimización del Sostenimiento Dinámico

Integrando el valor resultante de $Q_{\text{seismic}}$, la dimensión equivalente de la labor ($D_e$) y el umbral de $PPV$ medido o proyectado en el frente, se formula la matriz de decisión cuantitativa:

| Categoría de Diseño | Rango $PPV_{\text{vector}}$ (mm/s) | Rango $Q_{\text{seismic}}$ | Demanda Energética ($kJ/m^2$) | Esquema de Sostenimiento Dinámico Optimizado |
| :---: | :---: | :---: | :---: | :--- |
| **Categoría I: Estático / Transición** | $< 150\text{ mm/s}$ | $Q \ge 4.0$ (Roca Buena/Regular) | $< 5\text{ kJ/m}^2$ | Pernos helicoidales con resina ($L=2.4\text{ m}$, malla $1.2\text{ m} \times 1.2\text{ m}$) + Malla electrosoldada estándar + Shotcrete simple $e=5\text{ cm}$. |
| **Categoría II: Dinámico Moderado** | $150 - 350\text{ mm/s}$ | $1.0 \le Q < 4.0$ (Roca Regular/Pobre) | $5 - 15\text{ kJ/m}^2$ | Pernos D-Bolt o helicoidales dúctiles ($L=2.4\text{ m}$, malla $1.0\text{ m} \times 1.0\text{ m}$) + Malla electrosoldada reforzada + Shotcrete FRS ($e=7.5\text{ cm}$, $400\text{ J}$ a $40\text{ mm}$). |
| **Categoría III: Dinámico Pesado** | $350 - 600\text{ mm/s}$ | $0.1 \le Q < 1.0$ (Roca Muy Pobre) | $15 - 35\text{ kJ/m}^2$ | Pernos D-Bolt / Garford ($L=2.5\text{ m}$, malla $0.8\text{ m} \times 0.8\text{ m}$) + Malla romboidal de alta tenacidad $1,770\text{ MPa}$ + Shotcrete FRS ($e=10\text{ cm}$, $\ge 600\text{ J}$ ASTM C1550) + Planchuelas semiesféricas deformables. |
| **Categoría IV: Dinámico Extremo (Rockburst)** | $> 600\text{ mm/s}$ | $Q < 0.1$ (Extremadamente Pobre) | $> 35\text{ kJ/m}^2$ ($\ge 50\text{ kJ/m}^2$) | Sistema de doble contención: Pernos dinámicos D-Bolt ($L=2.5\text{ m}$) intercalados con Cables dinámicos bulbados desacoplados ($L=5.0 - 6.0\text{ m}$) + Malla de alta tenacidad encadenada con cable lacing ($\phi = 12\text{ mm}$) + Shotcrete FRS doble capa ($e=12 - 15\text{ cm}$, $> 800\text{ J}$). |

---

## 2.3. Marco Conceptual Extenso (Glosario Enciclopédico Especializado)

A continuación, se desarrolla el glosario de términos fundamentales de la investigación, estructurado bajo el estándar normativo de **mínimo dos párrafos continuos por concepto**: el primero enfocado en su definición teórico-científica y autor de referencia, y el segundo en su contextualización operacional y función causal en la mina subterránea.

---

### 1. Sistema Q de Barton (Tunneling Quality Index - NGI)
El Sistema $Q$ es una clasificación geomecánica empírico-analítica de macizos rocosos desarrollada en 1974 por Nick Barton, Robert Lien y John Lunde en el Instituto Geotécnico Noruego (NGI), diseñada para estimar los requerimientos de sostenimiento en excavaciones subterráneas. El índice se expresa en una escala logarítmica que oscila entre $0.001$ (roca excepcionalmente mala) y $1,000$ (roca excepcionalmente buena), calculándose mediante el producto de tres cocientes que representan el tamaño medio de bloques de roca, la resistencia al corte residual entre las paredes de las discontinuidades y el estado tensional activo combinado con el factor hidráulico subterráneo.

En el marco operativo de la minería subterránea andina (con proyección en labores mecanizadas de Lincuna), el Sistema $Q$ actúa como la variable independiente geomecánica rectora. Su determinación permite zonificar cuantitativamente cruceros y rampas en función de su calidad competente, identificando tramos donde el macizo rocoso experimenta altos factores de esfuerzo ($SRF$) propensos al estallido de rocas, y suministrando la base paramétrica para calibrar la demanda estática y dinámica que el sistema de soporte debe equilibrar.

---

### 2. Rock Quality Designation (RQD de Deere)
El $RQD$ es un parámetro cuantitativo de evaluación geomecánica introducido por Don U. Deere en 1964, definido como el porcentaje acumulado de testigos de perforación diamantina intactos de longitud mayor o igual a $10\text{ cm}$ recuperados en una corrida de sondeo, respecto a la longitud total perforada. Constituye el numerador del primer cociente del Sistema $Q$ de Barton y representa el grado de fragmentación, fracturamiento primario y competencia elástica de la matriz rocosa, siendo un estándar adoptado universalmente por la Sociedad Internacional de Mecánica de Rocas (ISRM) y la norma ASTM D6032.

En frentes de avance subterráneos donde no se dispone de perforaciones diamantinas continuas, el $RQD$ se determina indirectamente en la labor mediante el recuento volumétrico de discontinuidades ($J_v$). En la labor de estudio (andesitas y dacitas con $RQD \approx 60\%$), este indicador condiciona la capacidad del macizo para redistribuir el campo de esfuerzos inducido; un $RQD$ bajo indica bloques pequeños susceptibles de desacoplarse como proyectiles ante la incidencia de una onda de vibración de alta aceleración.

---

### 3. Índice de Familias de Juntas ($J_n$)
El parámetro $J_n$ (*Joint Set Number*) del Sistema $Q$ cuantifica la complejidad estructural y el grado de libertad cinemática del macizo rocoso mediante la valoración numérica de las familias o sets de diaclasas presentes. Sus valores oscilan de $0.5 - 1.0$ para macizos prácticamente masivos sin discontinuidades, pasando por $9.0$ para macizos con tres familias ortogonales definidas, hasta $15.0$ para rocas intensamente diaclasadas con cuatro o más familias, y $20.0$ para roca completamente triturada tipo brecha tectónica.

En la excavación de túneles mineros, el $J_n$ controla directamente el mecanismo de falla en el contorno. La presencia de 3 familias ortogonales intersecadas por fallas locales genera diedros y cuñas rocosas tetraédricas con susceptibilidad de desprendimiento gravitacional inmediato; en régimen dinámico, una mayor cantidad de familias facilita la disipación dispersiva de ondas de compresión pero genera múltiples superficies de reflexión de tracción que aceleran la eyección de fragmentos.

---

### 4. Coeficiente de Rugosidad de Juntas ($J_r$)
El parámetro $J_r$ (*Joint Roughness Number*) evalúa la textura morfológica, rugosidad milimétrica y ondulación a escala métrica de las superficies de discontinuidad del macizo rocoso. Valores de $J_r = 4.0$ representan juntas rugosas y onduladas discontinuas que impiden el desplazamiento sin fracturación de asperezas, mientras que valores descendentes ($J_r = 1.5$ para juntas lisas o $0.5$ para espejos de falla) describen planos con pérdida total de trabazón mecánica.

Operacionalmente, $J_r$ determina la resistencia al cizallamiento dinámico ante ondas sísmicas transversales ($S$). Planos de estratificación o diaclasamiento con $J_r$ bajo ubicados en la corona de la labor actúan como planos de deslizamiento preferencial cuando la onda de voladura imparte una aceleración transversal, requiriendo que los pernos de sostenimiento suministren una elevada fuerza de confinamiento normal para incrementar la fricción aparente en la interfaz.

---

### 5. Coeficiente de Alteración de Juntas ($J_a$)
El parámetro $J_a$ (*Joint Alteration Number*) cuantifica el grado de intemperismo químico, desintegración mineralógica y naturaleza reológica del material de relleno alojado entre las paredes rocosas de la discontinuidad. La escala de Barton asigna valores de $J_a = 0.75 - 1.0$ a paredes de roca sana en contacto mineral íntimo sin rellenos, mientras que la presencia de arcillas expansivas (esmectitas/montmorillonitas) o talco incrementa el parámetro a $J_a = 8.0 - 12.0$.

En yacimientos polimetálicos subterráneos como Lincuna, donde la circulación hidrotermal y aguas ácidas alteran los contactos de veta y cajas encajonantes, un $J_a$ elevado reduce drásticamente el coeficiente de fricción inter-bloques ($\tan \phi_r \approx J_r / J_a$). En eventos sísmicos o disparos masivos, las juntas con alto $J_a$ sufren una pérdida instantánea de rigidez cortante (*slip*), desencadenando eyecciones de roca incluso a niveles moderados de vibración de voladura.

---

### 6. Factor de Reducción por Esfuerzos (Stress Reduction Factor - SRF)
El $SRF$ es el parámetro del Sistema $Q$ que pondera la influencia del estado tensional y las sobrecargas mecánicas en la estabilidad del túnel. Evalúa el confinamiento tensional mediante la relación entre la resistencia compresiva uniaxial de la roca intacta ($\sigma_c$) y el esfuerzo principal mayor inducido ($\sigma_1$); a medida que esta relación cae por debajo de $2.5$, el $SRF$ se incrementa desde valores normales de $1.0$ hasta $10.0$ o $20.0$, reflejando una condición crítica de plastificación violenta y estallido de rocas.

En labores profundas del centro del Perú, el $SRF$ es el parámetro más dinámico y sensible de la clasificación geomecánica. La excavación de galerías altera el campo tensional virgen, concentrando esfuerzos tangenciales en la periferia de la labor; la ocurrencia de disparos de voladura induce un pulso tensional transitorio adicional ($\sigma_d$) que reduce drásticamente la relación efectiva $(\sigma_c / \sigma_1)_{\text{dinamico}}$, elevando el $SRF$ y degradando la calidad aparente del macizo a categorías que exigen soporte dinámico de absorción pesada.

---

### 7. Dimensión Equivalente ($D_e$) y Excavation Support Ratio (ESR)
La Dimensión Equivalente ($D_e$) es una formulación dimensional introducida por Barton para relacionar el vano o altura libre de la labor subterránea con el grado de seguridad y permanencia requerido para la obra, definido como $D_e = \text{Span} / ESR$. El coeficiente $ESR$ asigna valores más altos a excavaciones temporales con baja presencia humana ($ESR = 3.0 - 5.0$) y valores más estrictos a túneles permanentes, galerías de acarreo principal o cavernas de infraestructura crítica ($ESR = 1.0 - 1.6$).

En el dimensionamiento del sostenimiento en mina, la combinación paramétrica de $Q$ y $D_e$ sobre la carta empírica de Grimstad y Barton determina la longitud óptima de pernos y el espesor del concreto lanzado. Para labores de sección baúl de $4.5\text{ m} \times 4.5\text{ m}$ con $ESR = 1.6$ ($D_e = 2.81\text{ m}$), esta relación garantiza que los pernos dinámicos alcancen una profundidad de anclaje de al menos $2.4\text{ m}$, garantizando la fijación en el macizo elástico competente ubicado más allá del halo de fractura perimétrica inducida por voladura.

---

### 8. Velocidad Pico de Partícula (Peak Particle Velocity - PPV)
La Velocidad Pico de Partícula ($PPV$) es la máxima velocidad cinemática instantánea experimentada por una partícula del macizo rocoso al ser alcanzada y perturbada por un tren de ondas elásticas generado por una detonación de voladura o por un evento cosísmico de fracturamiento. Se cuantifica mediante sismógrafos triaxiales que registran componentes radial, vertical y transversal, expresándose en milímetros por segundo ($\text{mm/s}$) o metros por segundo ($\text{m/s}$), y constituye la métrica estándar internacional para correlacionar vibraciones con el umbral de daño en excavaciones.

En el control del sostenimiento dinámico, el $PPV$ es la variable independiente operativa fundamental. Existe una relación directa entre el $PPV$ en la cara libre de la labor y la deformación unitaria inducida ($\varepsilon_d = PPV / c_p$); niveles de $PPV$ que excedan los $350 - 450\text{ mm/s}$ causan la rotura por tracción del concreto lanzado en proceso de fraguado y el cizallamiento interfacial del anclaje de pernos rígidos, marcando la frontera técnica donde la mina debe transicionar obligatoriamente hacia elementos dinámicos deformables.

---

### 9. Aceleración Pico de Partícula (Peak Particle Acceleration - PPA)
La Aceleración Pico de Partícula ($PPA$) es la primera derivada temporal del vector velocidad de partícula ($a(t) = dv/dt$), expresada comúnmente en múltiplos de la aceleración gravitacional ($g = 9.81\text{ m/s}^2$). Representa la tasa de cambio cinemático instantáneo transmitido al macizo rocoso y gobierna la magnitud de las fuerzas inerciales de cuerpo ($F_{\text{inercial}} = m \cdot PPA$) que actúan sobre bloques potencialmente inestables en el techo y hastiales de la labor.

En el diseño de soporte de contención (mallas y concreto lanzado), el $PPA$ gobierna la primera fracción de segundo de un estallido de rocas. Aceleraciones que superan $2.0 - 5.0\text{ g}$ vencen instantáneamente la adherencia interfacial del shotcrete sobre la roca limpia y provocan la falla por cizallamiento en el perímetro de las planchuelas de los pernos si la malla no cuenta con una tenacidad de deformación dúctil suficiente para disipar el choque inicial.

---

### 10. Frecuencia Dominante de Vibración ($f_d$)
La Frecuencia Dominante ($f_d$) es la frecuencia espectral que concentra la mayor densidad de energía en el sismograma de vibración, obtenida mediante la transformación matemática al dominio de Fourier (FFT). Se mide en Hertz ($\text{Hz}$) y define, en conjunto con la velocidad de propagación de onda de la roca ($c_p$), la longitud de onda física ($\lambda = c / f$) del frente de perturbación sísmica.

En la ingeniería de voladuras de avance, las detonaciones en campo cercano generan altas frecuencias dominantes ($100 - 600\text{ Hz}$), asociadas a longitudes de onda cortas que coinciden con las dimensiones geométricas de la sección del túnel ($4.5\text{ m}$). Esta coincidencia dimensional induce fenómenos de difracción y resonancia local en la periferia de la excavación, incrementando el desgarramiento de roca y demandando un sistema de soporte continuo que evite la fragmentación del contorno.

---

### 11. Ley de Atenuación de Holmberg-Persson
La Ley de Atenuación de Holmberg-Persson (1980) es un modelo físico-matemático desarrollado específicamente para voladuras en túneles subterráneos, que supera la limitación del modelo de carga puntual de la USBM mediante la integración continua de la energía liberada a lo largo de una columna cilíndrica de explosivo. Su ecuación semianalítica permite predecir el $PPV$ en cualquier punto perimétrico del túnel en función de la concentración lineal de carga ($q$), el diámetro del barreno, la geometría de retardo y las constantes de atenuación elástica del macizo ($K, \alpha, \beta$).

En la optimización del sostenimiento dinámico, este modelo permite modelar el campo de vibraciones inducido taladro por taladro durante el avance del crucero. Conocer el $PPV$ previsto en la corona y hastiales permite delimitar la zona de daño perimétrico donde la roca intacta se fracturará inevitablemente, dimensionando la longitud del perno para que sobrepase dicha zona y asegurando que el soporte dynamic mantenga su anclaje en roca sana.

---

### 12. Deformación Dinámica Unitaria ($\varepsilon_d$)
La Deformación Dinámica Unitaria ($\varepsilon_d$) es la relación infinitesimal de cambio dimensional que experimenta un volumen rocoso sometido al paso de una onda sísmica de compresión o tracción, deducida a partir de la mecánica de medios continuos como el cociente entre la velocidad pico de partícula y la velocidad de onda del macizo ($\varepsilon_d = PPV / c_p$). Es una magnitud adimensional fundamental para evaluar si la perturbación inducida supera el límite elástico del macizo.

En la práctica geomecánica, la deformación unitaria dinámica impone una elongación transitoria forzada en la roca y en los elementos de sostenimiento instalados. Si la deformación dinámica supera la capacidad elástica del acero convencional (típicamente $\varepsilon_{\text{cedencia}} \approx 0.002$), los pernos rígidos plastifican prematuramente o se rompen; el perno dinámico, al poseer capacidades de deformación plástica superiores al $15 - 20\%$ ($\varepsilon > 0.15$), tolera múltiples ciclos de deformación dinámica sin degradación estructural.

---

### 13. Esfuerzo Dinámico Transitorio ($\sigma_d$)
El Esfuerzo Dinámico Transitorio ($\sigma_d$) es la tensión mecánica uniaxial adicional inducida instantáneamente en el medio rocoso por el frente de onda compresional o de tracción, proporcional al producto de la densidad de la roca, la velocidad de onda acústica y el $PPV$ ($\sigma_d = \rho_r \cdot c_p \cdot PPV$). Se expresa en MegaPascales ($\text{MPa}$) y se superpone algebraicamente al tensor de esfuerzos estáticos preexistente alrededor de la excavación.

En el control de la sobrerotura y selección de soporte, este parámetro explica el mecanismo de falla por desconchamiento dinámico (*spalling*). Cuando una onda compresional de $10\text{ MPa}$ inducida por voladuras masivas incide en la superficie libre de un túnel, se refleja como una onda de tracción de magnitud similar; dado que la resistencia a la tracción de la roca ($\sigma_t$) en Lincuna es de apenas $12.15\text{ MPa}$, la sobrepresión dinámica destruye instantáneamente la cohesión de la corona, exigiendo que el soporte dinámico actúe como un elemento de confinamiento superficial activo.

---

### 14. Estallido de Rocas (Rockburst)
El estallido de rocas (*rockburst*) es un fenómeno de inestabilidad geomecánica violenta e intempestiva caracterizado por la fracturación instantánea y eyección a gran velocidad de grandes masas de roca desde la periferia de una excavación subterránea hacia el vacío de la labor, acompañado de la emisión de ondas sísmicas de alta energía y severo daño estructural. Ocurre predominantemente en macizos rocosos frágiles, elásticos y de alta resistencia (como andesitas, granitos o cuarcitas) sometidos a estados tensionales extremos que exceden la resistencia última del macizo.

En la unidad minera objeto del estudio, la profundización de las operaciones por debajo de niveles de $600\text{ m}$ incrementa la probabilidad de ocurrencia de estallidos de roca inducidos por disparos de avance o desquinche. Diseñar un sostenimiento para mitigar este fenómeno exige descartar esquemas rígidos tradicionales y dimensionar sistemas de contención dúctiles capaces de absorber el impacto inercial y cinemático de la masa eyectada sin desprenderse del macizo competente.

---

### 15. Estallido por Concentración de Esfuerzos (Strainburst)
El *strainburst* es una categoría específica de estallido de rocas originada por la concentración excesiva de esfuerzos tangenciales compresivos inducidos en el perímetro inmediato de la excavación, la cual supera la resistencia compresiva residual de la roca intacta, provocando una fractura frágil superficial súbita por pandeo (*buckling*) y expulsión en lajas (*slabs*). Su espesor de daño típicamente oscila entre $0.3\text{ m}$ y $1.2\text{ m}$ desde la superficie del túnel.

Operativamente, el *strainburst* es el tipo de estallido más frecuente en cruceros y frentes de avance andinos y suele ser detonado intempestivamente por el paso de las ondas de vibración de una voladura cercana ($PPV$). El sistema de sostenimiento dinámico optimizado con pernos deformables y concreto lanzado reforzado con fibra restringe el desconfinamiento lateral de las lajas rocosas, suprimiendo el pandeo inicial y evitando la expulsión violenta hacia la labor.

---

### 16. Sismicidad Inducida por Minado
La sismicidad inducida es la respuesta cinemática y dinámica del macizo rocoso ante las perturbaciones tensionales generadas por la actividad humana de excavación, vaciado de tajeos y voladuras masivas en el subsuelo. Se clasifica sismológicamente desde eventos microscópicos de fracturamiento intergranular ($M_L < 0$) hasta grandes sismos cosísmicos por reactivación de fallas geológicas regionales ($M_L \ge 2.0 - 3.5$), registrados mediante redes de monitoreo microsísmico subterráneo con geófonos y acelerómetros.

En la gestión geomecánica de una unidad minera, el monitoreo continuo de la tasa de sismicidad inducida y su correlación con las voladuras permite anticipar las zonas del yacimiento sometidas a sobre-esfuerzos críticos. Esta información alimenta la calibración dinámica del parámetro $SRF$ en el Sistema $Q$ de Barton, permitiendo que la selección del sostenimiento dinámico se actualice en tiempo real conforme el frente de minado avanza hacia dominios de mayor peligro sísmico.

---

### 17. Sostenimiento Dinámico
El sostenimiento dinámico es un sistema de fortificación subterránea diseñado específicamente para absorber energía cinética y deformación inelástica severa impartida por el macizo rocoso en colapso violento o sometido a trenes de ondas de voladura, manteniendo la integridad del confinamiento y el gálibo operativo de la labor. Se diferencia del soporte convencional en que su criterio de diseño no es la capacidad de carga estática puntual en toneladas, sino su capacidad de disipación de trabajo mecánico medida en Kilojulios por metro cuadrado ($\text{kJ/m}^2$).

En el núcleo de esta tesis, el sostenimiento dinámico constituye la variable dependiente de optimización. La integración del Sistema $Q$ y el monitoreo de vibraciones permite seleccionar la combinación óptima de elementos (pernos dinámicos, mallas de alta resistencia y shotcrete con fibra) para responder con un factor de seguridad dinámico $FS \ge 1.5$ a la demanda energética específica del frente, evitando el sobrecosto de sobre-fortificar zonas estables o el riesgo letal de sub-dimensionar labores expuestas a sismicidad.

---

### 18. Capacidad de Absorción de Energía ($kJ/m^2$)
La Capacidad de Absorción de Energía ($E_{\text{capacidad}}$) es la integral del área bajo la curva carga-deformación ($E = \int F dx$) desarrollada por un elemento o sistema compuesto de sostenimiento durante su deformación hasta el punto de rotura o desplazamiento admisible, normalizada comúnmente por metro cuadrado de superficie expuesta ($\text{kJ/m}^2$). Cuantifica la cantidad de trabajo mecánico que el sistema puede disipar antes de perder su capacidad resistente.

En la ingeniería de rocas moderna, la absorción de energía es el indicador de rendimiento cuantitativo por excelencia para mitigar estallidos de roca. De acuerdo a las demandas calculadas para las vibraciones de voladura y profundidades de la labor de estudio ($15 - 35\text{ kJ/m}^2$), el sistema de fortificación debe seleccionar pernos y mallas cuya respuesta plástica garantice disipar este volumen energético con deformaciones controladas ($< 150 - 200\text{ mm}$), preservando la integridad de los equipos y del personal.

---

### 19. Perno Dinámico de Absorción de Energía (D-Bolt)
El *D-Bolt* es un perno de anclaje de roca de absorción de energía patentado por Charlie C. Li (2010), fabricado con una barra de acero corrugado de alta ductilidad que contiene una serie de anclajes mecánicos puntuales estampados a lo largo de su longitud, separados por tramos lisos recubiertos o desacoplados del mortero de inyección. Al ocurrir una deformación dinámica en el macizo, el mortero sostiene firmemente los anclajes puntuales, forzando a que los tramos lisos intermedios fluyan plásticamente bajo tensión axial uniforme.

En la selección de soporte de la labor, el D-Bolt representa la tecnología de vanguardia para reemplazar a los pernos helicoidales rígidos convencionales en frentes sometidos a vibraciones intensas ($PPV > 350\text{ mm/s}$). Cada D-Bolt de $22\text{ mm}$ es capaz de elongarse más de $150\text{ mm}$ disipando entre $35\text{ kJ}$ y $45\text{ kJ}$ de energía cinética por unidad, asegurando que ante una eyección súbita de la corona el perno no se corte en los labios de la junta.

---

### 20. Perno Deformable Cone Bolt
El *Cone Bolt* es un perno dinámico desarrollado originalmente en Sudáfrica por el Chamber of Mines Research Organization (COMRO) y perfeccionado por la Universidad Laurentian de Canadá, compuesto por una barra lisa de acero que posee un cono ensanchado forjado en su extremo distal alojado dentro de una cápsula de resina o lechada de cemento. Ante la tracción dinámica ejercida por la roca en expansión, el cono es forzado a penetrar y extrudirse a través de la masa de resina, generando una resistencia a la fricción constante con desplazamientos de más de $200 - 300\text{ mm}$.

Operacionalmente en minería mecanizada, el Cone Bolt aporta una de las mayores capacidades de absorción de energía del mercado ($\ge 40\text{ kJ}$ por unidad), siendo ideal para frentes de avance con condiciones de *strainburst* extremo. Su interacción mecánica garantiza que el perno trabaje a una fuerza constante sin sufrir concentración de tensiones en la planchuela, transmitiendo la carga de manera distribuida hacia la malla de contención perimetral.

---

### 21. Concreto Lanzado Reforzado con Fibra (Fiber Reinforced Shotcrete - FRS)
El *FRS* es un material compuesto estructural constituido por una matriz de mortero proyectada neumáticamente a alta velocidad, adicionada homogéneamente con fibras discontinuas de acero estirado en frío o macro-fibras sintéticas de poliolefina de alta tenacidad. Su propiedad distintiva es la tenacidad a la flexotracción post-fisuración, la cual impide la propagación incontrolada de grietas mediante el cosido mecánico de las fibras que cruzan el plano de fisura, absorbiendo energía elasto-plástica residual.

En el sostenimiento dinámico, el FRS actúa como la primera línea de contención perimetral, impidiendo el desconfinamiento inicial de la roca y distribuyendo las tensiones de eyección hacia los pernos dinámicos. Su capacidad de disipación se certifica mediante la prueba de absorción de energía en paneles circulares (ASTM C1550) o cuadrados (EN 14488-5); para las condiciones proyectadas de la tesis, se exige un shotcrete de ductilidad Clase A ($> 600 - 800\text{ Joules}$ a $40\text{ mm}$ de deflexión central), evitando el colapso frágil ante el impacto de vibraciones de voladura.

---

### 22. Malla Metálica de Alta Resistencia (High-Tensile Steel Mesh)
La malla de alta resistencia es una membrana flexible de soporte superficial fabricada con alambres de acero de alta aleación trenzados romboidalmente con resistencias a la tracción superiores a $1,770\text{ MPa}$ (tales como las mallas Geobrugg Tecco o Minax). A diferencia de las mallas electrosoldadas tradicionales que fallan por corte en los puntos de soldadura rígida ante deformaciones dinámicas menores a $50\text{ mm}$, la malla de alambre trenzado de alta resistencia tolera deformaciones de membrana superiores a $200\text{ mm}$ absorbiendo más de $15 - 25\text{ kJ/m}^2$.

En galerías sometidas a eventos sísmicos y voladura cercana, esta malla se instala en contacto directo con la roca o sobre una capa base de shotcrete, anclada mediante planchuelas semiesféricas deformables y pernos dinámicos. Su función operacional es retener la masa de roca desintegrada tras el estallido (*containment*), formando una bolsa deformable que evita la caída de escombros hacia la calzada de tránsito de vehículos y personal.

---

### 23. Velocidad de Eyección de Bloques ($v_e$)
La Velocidad de Eyección ($v_e$) es la velocidad cinemática lineal con la que un bloque de roca desprendido es lanzado desde la pared o techo de la excavación hacia el espacio libre de la galería como consecuencia de un estallido de rocas o del desconfinamiento dinámico provocado por voladuras adyacentes. Se cuantifica mediante análisis fotogramétrico de alta velocidad, registros sismológicos forenses o balances analíticos de impulso, oscilando típicamente entre $1.5\text{ m/s}$ y $5.0\text{ m/s}$.

En el dimensionamiento del soporte por balance de energía, $v_e$ es la variable más crítica puesto que la demanda de energía cinética crece con el cuadrado de su valor ($E_k \propto v_e^2$). La velocidad de eyección resulta de la amplificación del $PPV$ superficial ($\eta \cdot PPV$); por ende, monitorear y mitigar el $PPV$ mediante mallas de voladura controlada en frentes de avance reduce drásticamente la velocidad de expulsión, disminuyendo la demanda que debe disipar el sostenimiento dinámico.

---

### 24. Factor de Amplificación Dinámica Superficial ($\eta$)
El Factor de Amplificación Dinámica ($\eta$) es un coeficiente adimensional que relaciona la velocidad de partícula registrada en la pared libre de una excavación subterránea ($PPV_{\text{superficie}}$) con la velocidad pico de partícula medida en el macizo virgen continuo a cierta distancia (*campo libre*, $PPV_{\text{campo libre}}$), definido analíticamente como $\eta = PPV_{\text{superficie}} / PPV_{\text{campo libre}}$. Se origina por la interferencia constructiva de ondas reflejadas en la cara libre y el desconfinamiento elástico del contorno del túnel, tomando valores típicos de $\eta \approx 1.5 - 3.5$.

En el protocolo de cálculo de sostenimiento dinámico, omitir el factor de amplificación $\eta$ conduce a un peligroso sub-dimensionamiento del sistema. El subagente geomecánico debe multiplicar el $PPV$ proyectado por este factor para calcular la verdadera velocidad de eyección ($v_e$), garantizando que el diseño dinámico contemple las máximas fuerzas inerciales y energéticas que experimentará la capa de shotcrete y los pernos instalados en la periferia de la labor.

---

### 25. Tasa de Liberación de Energía (Energy Release Rate - ERR)
La Tasa de Liberación de Energía ($ERR$) es un parámetro geomecánico computacional desarrollado por N.G.W. Cook en Sudáfrica, definido como la cantidad neta de energía de deformación elástica disipada o liberada por unidad de superficie o volumen de roca excavada al avanzar el minado subterráneo ($\text{MJ/m}^2$). Refleja la concentración del estado tensional alrededor de las labores y constituye el indicador predictivo clásico del potencial destructivo de eventos microsísmicos.

En la planificación y diseño de frentes de avance minero, un incremento del $ERR$ por encima de umbrales críticos ($> 30\text{ MJ/m}^2$) señala la transición desde una condición de desprendimiento gravitacional estable a un régimen inestable propenso a estallidos de roca. Cuando el modelo numérico o las mediciones de convergencia registran altos valores de $ERR$, el sistema geomecánico debe acoplar el índice $Q$ ajustado por sismicidad e incrementar la capacidad de absorción de energía del sostenimiento perimetral.

---

### 26. Rigidez Dinámica del Macizo Rocoso
La Rigidez Dinámica ($K_d$) es la relación entre el incremento de esfuerzo dinámico aplicado y la deformación elástica resultante en el macizo sometido a solicitaciones cíclicas o transitorias de alta velocidad de carga, directamente vinculada con el módulo de Young dinámico ($E_d = \rho_r \cdot c_p^2 \cdot \frac{(1+\nu_d)(1-2\nu_d)}{1-\nu_d}$). A velocidades de deformación de voladura ($\dot{\varepsilon} = 10^0 - 10^2\text{ s}^{-1}$), el módulo dinámico de la roca es entre un $20\%$ y $50\%$ superior al módulo estático ($E_{\text{estático}}$).

En el análisis de transferencia de energía entre la voladura y el sostenimiento, la rigidez dinámica determina la cantidad de energía absorbida internamente por la matriz rocosa versus la cantidad transmitida a la superficie del túnel. Un macizo andesítico rígido como el de Lincuna transmite el pulso de choque casi sin atenuación interna, transportando el $PPV$ con alta energía destructiva hacia el perímetro del túnel y requiriendo un sostenimiento con pernos de alta ductilidad que eviten la falla por sobrecarga frágil.

---

### 27. Factor de Seguridad Dinámico ($FS_{\text{dinamico}}$)
El Factor de Seguridad Dinámico ($FS_{\text{dinamico}}$) es el cociente adimensional entre la capacidad total de absorción de energía disipativa del sistema compuesto de soporte ($E_{\text{capacidad}}$) y la demanda total de energía cinética y gravitacional transmitida por la masa de roca expulsada ($E_{\text{demanda}}$), definido formalmente como $FS_{\text{dinamico}} = E_{\text{capacidad}} / E_{\text{demanda}}$.

En la metodología de diseño sismorresistente en minería subterránea, se exige un $FS_{\text{dinamico}} \ge 1.50$ para validar la compuerta de calidad de una labor permanente o de avance mecanizado. Un factor inferior a $1.0$ representa colapso violento seguro y ruptura catastrófica del sostenimiento ante una voladura o sismo, mientras que un factor en el rango $1.0 \le FS < 1.5$ califica al soporte en estado de deformación plástica crítica con riesgo de falla residual ante réplicas subsecuentes.

---

### 28. Efecto Kaiser y Memoria Tensional del Macizo
El Efecto Kaiser es el fenómeno geomecánico por el cual un macizo rocoso sometido a esfuerzos compresivos cíclicos no emite actividad acústica ni microsísmica apreciable hasta que el nivel de esfuerzo aplicado excede el máximo nivel de esfuerzo de compresión previamente experimentado en su historia geológica o minera. Representa la memoria tensional intrínseca de la roca y se mide mediante emisión acústica ultrasónica en laboratorio o geófonos en mina.

En labores subterráneas sometidas a ciclos repetidos de perforación y voladura, el Efecto Kaiser gobierna la nucleación del daño acumulativo. Cuando un nuevo disparo de voladura genera una vibración cuyo esfuerzo dinámico transitorio supera el umbral histórico memorizado por el macizo, el efecto se anula y la roca inicia una microfisuración acelerada que degrada el $RQD$ y el $SRF$, exigiendo que el soporte dinámico controle la dilatancia perimetral en cada disparo de avance.

---

### 29. Atenuación Histerética Inelástica
La Atenuación Inelástica o Histerética es el mecanismo disipativo interno por el cual parte de la energía mecánica de las ondas sísmicas de voladura se transforma irreversiblemente en calor debido a la fricción interna en microgrietas, deformación viscoelástica de minerales y presencia de fluidos en los poros de la roca. Se cuantifica matemáticamente a través del factor de calidad sísmica ($Q_{\text{sismico}}$ o factor de amortiguamiento $\zeta = 1 / 2Q$).

En el monitoreo de vibraciones para la calibración de leyes de campo cercano, la atenuación inelástica es el parámetro que complementa a la dispersión geométrica esférica. En rocas volcánicas andesíticas moderadamente fracturadas ($Q \approx 2 - 4$), la atenuación de altas frecuencias ($> 300\text{ Hz}$) ocurre en los primeros 10 a 20 metros de recorrido, lo que implica que las labores adyacentes a menos de $15\text{ m}$ del disparo reciben el choque de ondas no atenuadas con máximo potencial destructivo para el sostenimiento perimetral.

---

### 30. Desacoplamiento Mecánico de Pernos de Anclaje
El Desacoplamiento Mecánico es la técnica de ingeniería geomecánica mediante la cual se anula intencionalmente la adherencia interfacial continua entre la barra de acero del perno y la lechada de cemento o cartucho de resina en tramos específicos de la columna, empleando fundas plásticas lisas, grasas lubricantes o resinas deformables. Su objetivo es evitar que la barra de acero concentre deformaciones extremas en el punto donde una discontinuidad individual se abre o desliza, distribuyendo la deformación axial uniformemente a lo largo de toda la longitud desacoplada.

En el diseño de pernos para sostenimiento dinámico (como en variantes de D-Bolts o cables dinámicos), el desacoplamiento es el principio que permite alcanzar grandes desplazamientos admisibles ($> 150 - 250\text{ mm}$) sin inducir la rotura prematura del acero por cizalle o tracción concentrada. Al permitir que el perno fluya en un volumen mayor de metal, se maximiza la integral de disipación de energía ($E = \int F dx$), garantizando que el sistema mantenga una fuerza de retención activa mientras el túnel experimenta la convergencia dinámica inducida por voladura.
