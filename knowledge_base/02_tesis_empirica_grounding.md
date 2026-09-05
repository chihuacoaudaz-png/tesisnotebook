# CONTENIDO DE TESIS DE REFERENCIA: tesis_referencia.docx

Universidad Nacional de Ingeniería
Facultad de
Para obtener el título profesional de Ingeniero de Minas
Elaborado por
0009-0000-8288-357X
Asesor
0000-0003-1078-4155
LIMA – PERÚ
Dedicatoria
Dedico este trabajo a mis padres, por su amor, apoyo y sacrificio constante. A mi hermana, por su compañía y siempre estar a mi lado. Y a mis mentores, por guiarme con sabiduría y paciencia. Gracias a todos por ser parte fundamental de este logro.
Agradecimientos
Quiero expresar mi más profundo agradecimiento a mi madrina de promoción, Arq. Eva Arias de Sologuren, presidenta ejecutiva de la Compañía Minera Poderosa, por darme a mí y a toda mi promoción la oportunidad de realizar nuestras prácticas profesionales durante seis meses. Su generosidad al abrir las puertas de la compañía y permitirnos vivir una experiencia tan enriquecedora ha sido clave en mi crecimiento profesional. Gracias por confiar en nosotros y por mostrarnos con su liderazgo el valor de la dedicación y el trabajo en equipo en el mundo de la minería.
A los ingenieros a cargo de la Unidad Minera Santa María, les agradezco sinceramente por su paciencia, conocimientos y por brindarme la confianza necesaria para desempeñar mis funciones. Cada uno de ustedes me enseñó lecciones valiosas, tanto técnicas como humanas, que dijeron posible la realización de este trabajo. Gracias por guiarme y darme la oportunidad de poner en práctica lo aprendido.
Resumen
Este trabajo de investigación analiza el impacto de la optimización de las mallas de perforación para voladuras de precorte en las labores de avance y desarrollo en minas subterráneas. La hipótesis sostiene que un diseño adecuado de las mallas optimizadas reducirá la sobrerotura a un máximo del 5%, lo que disminuirá los costos de sostenimiento y el tiempo de planificación. Para lograrlo, se desarrolló un software de automatización en Python, utilizando el entorno IDE Spyder, que calcula y diseña mallas de perforación de manera rápida y precisa, eliminando errores humanos y reduciendo el tiempo de cálculo.
El método de investigación consistió en comparar los resultados obtenidos con una malla de perforación convencional frente a una optimizada para voladuras de precorte, evaluando su impacto en la sobrerotura, los costos operativos y el tiempo invertido en el diseño. Los resultados mostraron una reducción de la sobrerotura del 34.36% al 3.33%, lo que mejoró la eficiencia de las voladuras. Además, se observó una disminución en el costo unitario de las actividades de voladura y sostenimiento con shotcrete, resultando en un ahorro total de 169,654.23 dólares para un proyecto de 2 km.
En conclusión, la implementación de la malla optimizada y el software de automatización mejoraron significativamente la seguridad, eficiencia y rentabilidad de las operaciones mineras, destacando la importancia de las tecnologías avanzadas en la optimización de los procesos de perforación y voladura en minería subterránea.
Palabras clave — Mallas de perforación, sobrerotura, costos de sostenimiento, voladura de precorte, software de automatización, Python.
Abstract
This thesis analyses the impact of optimising drill meshes for pre-cut blasting in advancement and development works in underground mines. The hypothesis holds that an adequate design of the optimised meshes will reduce over-breaking to a maximum of 5%, which will decrease maintenance costs and planning time. To achieve this, an automation software was developed in Python, using the Spyder IDE environment, which calculates and designs drill meshes quickly and accurately, eliminating human errors and reducing calculation time.
The research method consisted of comparing the results obtained with a conventional drill mesh versus one optimised for pre-cut blasting, evaluating their impact on over-breaking, operating costs and time spent on design. The results showed a reduction in over-breaking from 34.36% to 3.33%, which improved blasting efficiency. In addition, a decrease in the unit cost of shotcrete blasting and support activities will be observed, resulting in a total savings of $169,654.23 for a 2 km project.
In conclusion, the implementation of the optimized grid and automation software significantly improved the safety, efficiency, and profitability of mining operations, highlighting the importance of advanced technologies in optimizing drilling and blasting processes in underground mining.
Keywords — Drill grids, overburden, support costs, pre-cut blasting, automation software, PythonKeywords.
Tabla de Contenido
Pág.
Resumen	v
Abstract	vi
Introducción	xv
Capítulo I. Parte introductoria del trabajo	1
1.1	Generalidades	1
1.2	Descripción del problema de investigación	1
1.2.1	Problema general	2
1.2.2	Problema especifico	2
1.3	Objetivos del estudio	3
1.3.1	Objetivo general	3
1.3.2	Objetivos específicos	3
1.4	Justificación.	3
1.5	Hipótesis y operacionalización de variables	4
1.5.1	Hipótesis general	4
1.5.2	Hipótesis especifica	4
1.6	Antecedentes investigativos	5
1.6.1	Antecedentes internacionales	5
1.6.2	Antecedentes nacionales	5
1.6.3	Antecedentes locales	7
Marcos teórico y conceptual	9
2.1	Marco teórico	9
2.1.1	Sobrerotura en minería subterránea	9
2.1.2	Sostenimiento en minería subterránea	10
2.1.3	Mecanismo de fragmentación de la roca	14
2.1.4	Criterio de diseño de malla de perforación para voladura controlada	17
2.1.5	Optimización en el diseño y cálculo de mallas de perforación: Modelo matemáticollllll lllllllllllllllde Holmberg	19
2.1.6	Programación con Python	31
2.2	Marco conceptual	43
Capítulo III. Desarrollo del trabajo de investigación	47
3.1	Metodología	47
3.1.1	Tipo y diseño de la investigación	47
3.1.2	Unidad de análisis	48
3.1.3	Etapas de la investigación	59
Capítulo IV. Análisis e interpretación de resultados	98
4.1	Análisis de resultados	98
4.1.1	Comparación de resultados de la sobrerotura	98
4.1.2	Comparación de resultados de costos operativos de interés	98
4.2	Contrastación de la hipótesis	99
4.2.1	Sobrerotura	99
4.2.2	Costo de sostenimiento	101
4.3	Discusión de resultados	103
Conclusiones	104
Recomendaciones	105
Referencias bibliográficas	106
Anexos	108
Lista de Tablas
Pág.
Tabla 1  : Valores de factor de fijación y relación (S/B) de los tajeos	28
Tabla 2  : Valores de factor de fijación y relación (S/B) del contorno	29
Tabla 3  : Comandos constructores de datos	32
Tabla 4  : Tipos de operadores	32
Tabla 5  : Métodos de cadenas	33
Tabla 6  : Caracteres de escape	34
Tabla 7  : Métodos de listas	35
Tabla 8  : Métodos de Tuplas	35
Tabla 9  : Métodos de conjuntos	36
Tabla 10: Métodos de diccionarios	37
Tabla 11: Métodos de la biblioteca Math	40
Tabla 12: Métodos de la biblioteca Matplotlib	41
Tabla 13: Métodos de la biblioteca NumPy	42
Tabla 14: Métodos de la biblioteca Pandas	42
Tabla 15: Ruta vía terrestre	49
Tabla 16: Ruta vía aérea	49
Tabla 17: Parámetros geomecánicos en la unidad de análisis	53
Tabla 18: Parámetros de la emulsión emulnor 5000	58
Tabla 19: Parámetros de la emulsión Famecorte e20	58
Tabla 20: Parámetros de interés en la actividad unitaria de perforación en la etapalllllll llllllllllllllllllll preliminar	64
Tabla 21: Parámetros de interés en la actividad unitaria de voladura en la etapalllllll lllllllllllllllllllllpreliminar	64
Tabla 22: Parámetros de interés en la actividad unitaria de perforación aplicando la mallallllll llllllllllllllllll de perforación optimizada	96
Tabla 23: Parámetros de interés en la actividad unitaria de voladura aplicando la mallallllllll lllllllllllllllllllllde perforación optimizada	96
Lista de Figuras
Pág.
Figura 1  : Imagen representativa de la sobrerotura	9
Figura 2  : Minas de carbón usando madera para sostenimiento	10
Figura 3  : Cimbras instaladas en una mina subterránea	11
Figura 4  : Perno Helicoidal	12
Figura 5  : Perno Split Set	12
Figura 6  : Rollos de mallas electrosoldada	13
Figura 7  : Robot lanzando shotcrete a la pared de una labor minera	14
Figura 8  : Gráfica que diferencia el comportamiento de un explosivo según su velocidadllllllll llllllllllllllllllll de detonación en el tiempo	15
Figura 9  : Tipos de fisuramiento en las cercanías del taladro	16
Figura 10: Zonas de la cuña de fracturamiento debido a la reflexión de las ondas delllllll llllllllllllllllllllllchoque	16
Figura 11: Funcionalidad de las ondas de tensión para la generación de zonaslllllll llllllllllllllllllllllformadoras del plano de rotura	17
Figura 12: Fases de las voladuras controladas en minería subterránea	19
Figura 13: Secciones de trabajo para la obtención de la malla de perforación	19
Figura 14: Gráfica de relación entre la profundidad del taladro y el diámetro del taladrollllllll llllllllllllllllllll vacío….	20
Figura 15: Representación de las cuatro secciones de corte	21
Figura 16: Comportamiento de la voladura respecto a la relación del burden y el diámetrollllll llllllllllllllllllll del taladro vacío	22
Figura 17: Grafica para el cálculo del burden máximo según la concentración lineal y elllllll llllllllllllllllllll diámetro del taladro vacío	24
Figura 18: Gráfico de la afectación del burden debido a la desviación de la perforación	25
Figura 19: Representación gráfica de los taladros de arrastre con realce, espaciamientolllllll llllllllllllllllllll practico y burden máximo	27
Figura 20: Representación del código condicional con la palabra clave “if”	37
Figura 21: Representación del código multicondicional	38
Figura 22: Representación del uso del bucle “while” con la palabra clave “break”	38
Figura 23: Representación del uso del bucle “for” con la palabra clave “break”	39
Figura 24: Representación de la creación de una función básica en Python	39
Figura 25: Representación de la utilización de la recursión de funciones en Python	39
Figura 26: Foto satelital de la Unidad de Producción Santa María	49
Figura 27: Columna estratigráfica regional	50
Figura 28: Columna estratigráfica local	52
Figura 29: Representación geométrica de la labor de la unidad de análisis	54
Figura 30: Scooptramp modelo R1600G de 6 yardas cúbicas	54
Figura 31: Scayler de la marca EPAUS, modelo S8 853	55
Figura 32: Small Bolter 99 de la marca Resemin	56
Figura 33: Robot de la marca Putmeister, modelo Wetkret 4	56
Figura 34: Mixer marca Perkins, modelo Huron 4	56
Figura 35: Jumbo de la marca Epiroc, modelo Boomer S10D	57
Figura 36: Accesorios de voladura y explosivos utilizados	58
Figura 37: Representación gráfica de la CR NW del nivel 2350	59
Figura 38: Almacenamiento en listas de datos tomados en campo	60
Figura 39: Concatenación de listas	60
Figura 40: Código para cálculo de sobrerotura	61
Figura 41: Código para obtención de parámetros estadísticos	61
Figura 42: Gráfica que representa la sobrerotura en la etapa preliminar	62
Figura 43: Malla utilizada en la etapa preliminar	63
Figura 44: Código para importar bibliotecas	65
Figura 45: Código para solicitar datos geométricos de la labor	65
Figura 46: Código para solicitar el largo del taladro con el que se desee trabajar	66
Figura 47: Código de ajuste de avance	66
Figura 48: Código para obtener el numero de taladros vacíos	68
Figura 49: Código de solicitud de parámetros de la roca	68
Figura 50: Código para el cálculo de la constante de roca sueca	69
Figura 51: Código para calcular el burden ideal, según Holmberg	70
Figura 52: Código para corroborar que la concentración e carga lineal sea mayor alllllllll llllllllllllllllllllllmínimo	72
Figura 53: Código para obtener el burden especifico del explosivo del mercado	74
Figura 54: Código para obtener los parámetros del primer cuadrante	75
Figura 55: Código para obtener los parámetros de los cuadrantes restantes	77
Figura 56: Código parea corroborar que la concentración de carga lineal del explosivollllllll llllllllllllllllllllllno sea mayor al máximo	78
Figura 57: Código para calcular el burden teórico de los taladros de arrastre	79
Figura 58: Código para obtener los parámetros de los taladros de arrastre	80
Figura 59: Código para corroborar la buena elección del explosivo de contorno	81
Figura 60: Código para obtener los parámetros de sección de contorno	82
Figura 61: Código para obtener los parámetros de los taladros de los hastiales	83
Figura 62: Código para graficar la estructura inicial de la labor	84
Figura 63: Código para dibujar los taladros en la corona	85
Figura 64: Código para graficar los taladros de arrastre	86
Figura 65: Código para graficar los taladros de los hastiales	87
Figura 66: Código para dibujar los taladros de la sección de corte	88
Figura 67: Código para dibujar la gradiente	89
Figura 68: Código para dibujar el taladro de alivio equivalente	90
Figura 69: Código para imprimir mensajes de interés en la grafica de la malla	90
Figura 70: Código para crear las tablas de interés que almacenan los parámetros de lasllllllll llllllllllllllllllll secciones calculadas	91
Figura 71: Código para representar las tablas en el documento PDF	91
Figura 72: Representación gráfica de la malla que otorgo el software	92
Figura 73: Representación gráfica de los parámetros de los taladros de corte	92
Figura 74: Representación gráfica de los parámetros de los taladros de la corona	93
Figura 75: Representación gráfica de los parámetros de los taladros del arrastre	93
Figura 76: Representación gráfica de los parámetros de los taladros en los hastiales	93
Figura 77: Representación de grafica de la malla de perforación optimizada	94
Figura 78: Código que muestra el almacenamiento de los datos obtenidos al aplicar lalllllll llllllllllllllllllllllmalla de perforación optimizada	95
Figura 79: Representación gráfica de la evolución de la sobrerotura al aplicar la malla de perforación optimizada	95
Figura 80: Precio unitario de voladura aplicando la nueva malla de perforaciónlllllllll llllllllllllllllllllllllloptimizada	96
Figura 81: Precio unitario de perforación aplicando la nueva malla de perforaciónlllllllll llllllllllllllllllllll optimizada	97
Figura 82: Representación gráfica de comparación de sobrerotura en las dos etapas	98
Figura 83: Grafica de la distribución normal del t de student para comprobar hipótesis..101
Figura 84: Grafica de la distribución normal del t de student para comprobar hipótesis..102
Introducción
El presente trabajo de investigación está estructurado en cuatro capítulos:
El capítulo I expone los problemas derivados de la sobrerotura en las labores mineras subterráneas y su impacto en el aumento de los costos de sostenimiento. Basándose en investigaciones previas, se propone una solución a través de la implementación de una malla de perforación optimizada, respaldada por el modelo matemático de Holmberg.
El capítulo II presenta el marco teórico y conceptual, en el que se explican los conceptos básicos relacionados con la sobrerotura, el sostenimiento, las metodologías de voladuras controladas y el modelo matemático de Holmberg para la elaboración de mallas de perforación optimizadas. También se incluyen los fundamentos necesarios para la programación en Python.
El capítulo III detalla la metodología de investigación, la unidad de análisis en la que se aplicó el cambio de malla de perforación. Se describe la recolección y procesamiento de la información, así como el análisis de la situación preliminar de la mina antes de la implementación de la nueva malla. Además, se explica el desarrollo del software de automatización para el diseño de mallas de perforación para voladuras de precorte y los resultados obtenidos tras su aplicación.
El Capítulo IV analiza los resultados obtenidos, subrayando la reducción de la sobrerotura al 3.33%, lo que representa una disminución del 31.06% en comparación con los valores previos a la aplicación de la nueva malla. También se destaca la disminución de 243.13 dólares por disparo en los costos de sostenimiento, así como un ahorro total de 250.24 dólares por disparo al considerar las tres actividades unitarias (perforación, voladura y sostenimiento). Estos resultados demuestran la efectividad de la implementación de la malla de perforación optimizada-
Finalmente, se incluyen las conclusiones, recomendaciones, referencias bibliográficas y anexos utilizados en este trabajo de investigación.
Capítulo I. Parte introductoria del trabajo
1.1	Generalidades
La minería subterránea enfrenta constantemente retos asociados con la seguridad y la eficiencia operativa, especialmente en lo que respecta a la perforación y voladura de rocas. Uno de los problemas más comunes es la sobrerotura, que se refiere al exceso de material fracturado debido a un mal diseño de las mallas de perforación, lo que afecta tanto la estabilidad de las labores como los costos operativos. En este contexto, la optimización de las mallas de perforación se ha convertido en un aspecto clave para mejorar la eficiencia y reducir los costos de sostenimiento, especialmente en labores de desarrollo y avance, donde la calidad del diseño es fundamental para minimizar la sobrerotura y el uso excesivo de insumos como el shotcrete.
La presente tesis se enfoca en la implementación de un software de automatización, desarrollado en Python utilizando el entorno IDE Spyder, para el diseño y cálculo de mallas de perforación optimizadas para voladuras de precorte en minas subterráneas. Este software permite reducir el tiempo de cálculo y diseño de las mallas, eliminando errores humanos y optimizando los procesos en un entorno operativo complejo.
A través de la comparación de resultados obtenidos con mallas de perforación convencionales frente a las optimizadas, esta investigación evalúa su impacto en la reducción de la sobrerotura, la mejora de la eficiencia en la perforación y voladura, y los ahorros significativos en los costos operativos. La automatización y la optimización en el diseño de las mallas no solo contribuyen a la reducción de costos, sino que también favorecen la seguridad y sostenibilidad a largo plazo de las operaciones mineras subterráneas.
1.2	Descripción del problema de investigación
En las minas subterráneas, uno de los principales problemas que afectan la eficiencia en las labores de perforación y voladura es la sobrerotura, especialmente en la zona de la corona durante los trabajos de perforación. Esta sobreexcavación, que puede alcanzar entre el 15% y el 20%, genera una inestabilidad significativa en las labores. La sobrerotura no solo representa un riesgo para la seguridad de los trabajadores, sino que también incrementa los costos operacionales debido al uso ineficiente de recursos como la mano de obra y los equipos. Este fenómeno, por lo tanto, tiene un impacto directo en la productividad y la rentabilidad de las operaciones mineras (Vidal, 2020).
Un problema estrechamente vinculado con la sobrerotura es el alto consumo de shotcrete, necesario para estabilizar las paredes de la mina afectadas por la sobreexcavación. Este material, empleado en grandes cantidades, incrementa los costos de sostenimiento de la mina, afectando negativamente la rentabilidad de las operaciones. La necesidad de aplicar shotcrete de manera continua para mitigar los efectos de la sobrerotura obliga a la empresa a destinar recursos adicionales, lo que incrementa los costos operacionales y afecta la eficiencia de las operaciones (Baltazar, 2023).
Además, otro de los principales desafíos que enfrenta la mina es la lentitud en el proceso de diseño de mallas de perforación. Este proceso, mayormente realizado de forma manual, implica cálculos complejos y una gran inversión de tiempo. La falta de un sistema automatizado para el diseño de mallas genera retrasos significativos, afectando la eficiencia general de las operaciones. La ausencia de herramientas adecuadas para generar los diseños en tiempo real contribuye a que los cálculos se realicen de manera lenta y, en algunos casos, sin el sustento teórico técnico necesario. Esto podría comprometer la efectividad de las voladuras y aumentar la probabilidad de sobrerotura (Jimenes, 2021).
1.2.1	Problema general
¿En qué medida un mal diseño y cálculo de la malla de perforación incrementa la sobrerotura de las labores de avance y desarrollo?
1.2.2	Problema especifico
¿En qué medida el incremento de la sobrerotura eleva los costos de sostenimiento mediante el lanzado de shotcrete en las labores de avance y desarrollo?
¿En qué medida la falta de un software de automatización de diseño y cálculo de mallas de perforación optimizadas aumenta el tiempo empleado para realizar esta actividad?
1.3	Objetivos del estudio
1.3.1	Objetivo general
Reducir la sobrerotura a un máximo de 5% en las labores de avance y desarrollo de las minas subterráneas.
1.3.2	Objetivos específicos
Reducir los costos de sostenimiento por lanzado de shotcrete en las labores de avance y desarrollo de las minas subterráneas.
Reducir el tiempo empleado en la realización del diseño y cálculo de mallas de perforación optimizadas en las labores de avance y desarrollo de las minas subterráneas.
1.4	Justificación.
El presente trabajo se justifica por la necesidad de optimizar los procesos de perforación y voladura en la unidad de análisis, específicamente debido al exceso de sobrerotura identificado en las labores de minería. Esta sobrerotura ha generado diversos problemas operativos, como inestabilidad en las labores, incremento de los costos operacionales y mayor riesgo para la seguridad de los trabajadores. Ante estos desafíos, se propone el desarrollo de un software de automatización para el cálculo y diseño de mallas de perforación optimizadas, basado en el modelo matemático de Holmberg, específicamente diseñado para voladuras de precorte.
El uso de este software ofrecerá tres soluciones principales que beneficiarán directamente las operaciones mineras. En primer lugar, al optimizar el diseño de la malla de perforación, se logrará reducir significativamente la sobrerotura, lo que mejora la estabilidad de las labores y minimiza los riesgos asociados a la voladura. En segundo lugar, al disminuir la sobrerotura, se reducirán los costos de sostenimiento, ya que el área de aplicación de shotcrete será menor. Esto se traduce en un menor consumo de este material, reduciendo los costos asociados a su aplicación. Finalmente, la automatización del cálculo y diseño de mallas permitirá reducir considerablemente el tiempo invertido en esta tarea, eliminando los errores humanos que pueden surgir durante el proceso manual de cálculos. Esto no solo incrementará la eficiencia operativa, sino que también garantizará un diseño más preciso y consistente, contribuyendo a una mayor efectividad en las voladuras y reduciendo aún más el riesgo de sobrerotura
1.5	Hipótesis y operacionalización de variables
1.5.1	Hipótesis general
Un diseño y cálculo de las mallas de perforación optimizada permitirá reducir la sobrerotura a un máximo del 5% en las labores de avance y desarrollo.
Variable dependiente:
Sobrerotura.
Variable independiente:
Diseño y cálculo de las mallas de perforación optimizada.
1.5.2	Hipótesis especifica
La reducción de la sobrerotura permitirá disminuir los costos de sostenimiento por lanzado shotcrete en las labores de avance y desarrollo.
Variable dependiente:
Costos de sostenimiento por lanzado de shotcrete.
Variable independiente:
Sobrerotura.
La creación de un software de automatización de diseño y cálculo de mallas de perforación optimizadas reducirá el tiempo empleado para realizar esta tarea.
Variable dependiente:
Tiempo empleado para realizar mallas de perforación optimizadas.
Variable independiente:
Software de automatización de diseño y cálculo de mallas de perforación optimizadas.
Se adjunta la matriz de consistencia en el Anexo (8).
1.6	Antecedentes investigativos
1.6.1	Antecedentes internacionales
Zúñiga G. (2019) en su estudio “Control de calidad topológico de los objetos espaciales a través de la automatización con Python en el proceso de validación de la información” identifica que al realizar el control de calidad de las bases de datos geográficos del Ecuador manualmente es una tarea exhaustiva, además genera demoras y errores significativos, para ello el propone un software de automatización del control topológico con ayuda de los scripts de Python, utilizando esta herramienta no solo se agiliza la realización de la tarea si no que reduce los errores en el cálculo hasta en un 80% según los estudios que realizo en Santa Lucía, lo cual evidencia el beneficio que presenta automatizar tareas pesadas.
Persson P. et al (1993) en su libro “Rock Blasting and Explosives Engineering” detalla en la sección de diseño de voladuras, el modelo matemático de Holmberg, el cual considera indicadores como la calidad de la roca circundante, el explosivo que se utiliza tanto en el contorno como en las demás secciones y la necesidad de avance del túnel con la finalidad de diseñar y calcular parámetros de la malla de perforación para la voladura, optimizando la distribución de energía, la fragmentación, diseño de la malla de perforación y minimiza daños a la roca remanente. Este método a pesar de ser engorroso al calcular es uno de los más utilizados en las minas subterráneas.
1.6.2	Antecedentes nacionales
Jimenez A. (2021) “Automatización del modelo matemático Holmberg para el cálculo y diseño de mallas de perforación en frentes de desarrollo” toma como unidad de análisis a la galería 710 SE del prospecto Monserrat, en la cual se optimiza la malla de perforaron con ayuda del modelo matemático de Holmberg y automatiza este proceso utilizando el lenguaje de programación orientado a objetos VBA, además utiliza la interfaz ActiveX  de AutoCAD para visualizar el diseño de la malla de perforación, obteniendo una reducción en el tiempo de realización de esta tarea y de fácil manejo para el usuario.
Ticona S. (2024) “Aplicación del método de Holmberg para la optimización de la malla de perforación y voladura en minería en rocas del Grupo Pucará 2023” evidencia como el modelo matemático de Holmberg optimiza el diseño y cálculo de la malla de perforación, ya que, al aplicarlo presenta una mejora en el avance de 11%, una reducción en el factor de carga del 9%, una reducción en el costo de avance del 12% y una reducción de numero taladros cargados de 43 a 41, logrando así mayor productividad en la unidad minera.
Carrasco P. (2015) “Aplicación del método de Holmberg para optimizar la malla de perforación y voladura en la unidad Parcoy – CIA. Consorcio Minero Horizonte S.A.” aplica el modelo matemático de Holmberg donde optimiza la malla de perforación obteniendo resultados satisfactorios como el incremento de la eficiencia a un 92% con un avance de 3.6m, la sobrarotura se redujo a un 7.92% el cual está dentro de los estándares establecidos por la mina y se minimizó el factor de carga a 1.73 kg/m3, con la cual se pudo reducir los costos operativos.
Mostacero E. et al (2017) “Optimización del diseño de perforación y voladura, para reducir costos en labores de avance en la mina Santa María – Poderosa S.A.” utilizó el modelo matemático de Holmberg para optimizar la malla de perforación en la unidad Santa María de la CIA. Minera Poderosa, debido a que realizaban un avance de 1.46 m/disparo frente a 1.55 m/disparo que era lo programado, obteniendo como resultado luego de la aplicación del modelo, un avance de 1.65m/disparo. También se obtuvieron resultados significativos en la reducción del costo operativo que fue de 328.82 $/m a 282.37 $/m, lo cual equivale a un ahorro de 55,188.12 $/año proyecto.
Quezada W. (2017) “ Optimización de perforación y voladura aplicando el modelo matemático de Holmberg en frente de 3.5m*3.5m en roca tipo II veta Papagayo, mina Poderosa, 2017” aplica el modelo matemático de Holmberg debido a la presencia de una baja eficiencia, consumo excesivo de explosivos, aceros de perforación y disparos fallidos, se pudo optimizar la malla con la finalidad de obtener resultados beneficiosos como el incremento de avance de 1.43 m a 1.7 m, reducción del factor de carga a 0.83kg/Tn el cual se encuentra dentro de los estándares requeridos y una reducción significativa en los disparos fallidos ( 2 disparos cortados, 0.8 soplados y 0.5 anillados por mes en promedio). Finalmente se presentó una reducción en los costos operativos de 715.55 US$/m a 536.31 US$/m, menor consumos de explosivo y aceros de perforación.
Ttica E. (2018) “Diseño de malla de perforación y voladura según Holmberg, para reducir los costos unitarios en la cortada SW nivel 2760. Contrata minera ARCA. S.A.C.- Unidad de producción Santa María – CIA. Minera Poderosa S.A., 2017” utiliza el modelo matemático de Holmberg para optimizar la malla de perforación y voladura en su área de trabajo esto debido a que presentaban excesivos costos, mala fragmentación y una sobrerotura por encima del estándar, los resultados de la aplicación del modelo en esta unidad fueron los siguientes: reducción de cantidad de taladros de 51 a 49, disminución del costo de perforación de 94.45 US$/m a 83.47 US$/m, reducción del factor de carga de 24.65 kg/m a 20.21 kg/m, reducción del costo de voladura de 103.29 US$/m a 86.02 US$/m y presentaron un incremento en el avance de 1.45m a 1.58m.
Sulcacondor J. (2018) “Optimización de operaciones unitarias de perforación y voladura mediante voladura controlada en labores horizontales en la CIA. Minera Poderosa S.A.” aplica el modelo de matemático de Holmberg en la cortada SW del nivel 2760 con el criterio de voladura controlada (smooth blasting) en la cual se obtuvo una disminución de sobrerotura de 15% al 0%, conllevando una disminución en los costos de perforación de 103 US$/m a 83.47 US$ y los costos de voladura de 103.29 US$/m a 86.02 US$/m, además de la reducción del factor de carga en un 18% y la eficiencia de avance se incrementó de 1.45 m a 1.58 m.
1.6.3	Antecedentes locales
Acero A. (2021) “Propuesta de una malla de perforación y voladura para labores de avances” explica que el diseño de una malla de perforación y voladura optimizada en minería subterránea demuestra una mejora significativa en el avance lineal, aumentando la eficiencia del 79% al 95% en secciones de 4,0 m x 4,0 m, lo que representa un incremento del 16%. Además, se logró reducir la sobrerotura en las paredes de la sección, mejorando la estabilidad de los hastiales y la corona, lo que aumentó la seguridad en las labores mineras. El factor de carga del explosivo disminuyó de 2.33 kg/m³ a 1.47 kg/m³, optimizando el uso de recursos y reduciendo costos operativos.
Valenzuela B. (1995) “Desarrollo de software para ser aplicado a las operaciones mineras unitarias de perforación y voladura” aplica un sistema de automatización para optimizar los procesos de perforación y voladura en minería, lo que mejora la eficiencia al reducir tiempos y costos. El software permite ajustar parámetros de perforación y diseñar disparos más efectivos, logrando una mejor fragmentación de la roca y reduciendo la necesidad de voladuras secundarias. Esto contribuye a una mayor estabilidad en las paredes de la sección, reduciendo costos operativos y mejorando el rendimiento en avance y aprovechamiento de recursos, todo basado en datos reales de una unidad minera.
Orihuela J. (1992) “Aplicación de voladuras controladas en minería subterránea y tunelaría” explica que las voladuras convencionales en excavaciones subterráneas generan varios problemas, como grandes daños a la estructura rocosa, lo que se traduce en altos costos de sostenimiento, mayor material disparado de lo planificado, mayor dilución, costos de extracción incrementados y mayor tiempo de desatado de rocas. Para mitigar estos efectos negativos, el autor propone el uso de voladuras controladas, una técnica que permite reducir la sobreexcavación y promover el auto sostenimiento. Estas voladuras controladas no solo disminuyen los costos operativos, sino que también mejoran la seguridad en las operaciones subterráneas.
Marcos teórico y conceptual
2.1	Marco teórico
2.1.1	Sobrerotura en minería subterránea
La sobrerotura en la minería subterránea es un fenómeno que se presenta tras la voladura, cuando la sección real ostenta mayor dimensión que la sección planificada, el material fragmentado en exceso comparado con el material fragmentado deseado se identifica como sobrerotura.
Figura 1
Imagen representativa de la sobrerotura.
Nota: El grafico resalta la zona roja como la sobrerotura de la sección planificada. Fuente propia.
Matemáticamente la sobrerotura se puede expresar mediante la siguiente fórmula:
(1)
Si no se controla la sobrerotura, las operaciones mineras pueden suplir de muchas deficiencias, entre la cuales tenemos: inestabilidad estructural del macizo rocoso circundante, incremento en los costos de sostenimiento, interrupciones en el ciclo de minado, aumento de riesgo de accidentes, etc. El MINEM enfatiza en sus regulaciones aplicar buenas prácticas en el diseño y ejecución de voladuras para mitigar riesgos y optimizar la estabilidad del macizo rocoso (DS N.º 024-2016-EM), entonces se puede mitigar o reducir la sobrerotura si es que se tiene un diseño de malla de perforación adecuada, sin embargo, para ostentar ello se deben tener en cuenta factores como la calidad de roca circundante, el tipo de explosivo que se desea utilizar, técnicas de voladura controlada y una supervisión constante, con este cuidado la sobrerotura disminuye aumentando la eficiencia en la realización de tareas y la productividad de la unidad minera.
2.1.2	Sostenimiento en minería subterránea
Debido a los constantes accidentes presentados a lo largo de la historia en las minas subterráneas una de las áreas más desarrolladas e implementadas actualmente es el área de geomecánica el cual se encarga del estudio y supervisión del sostenimiento de las labores subterráneas. Son distintos los tipos de sostenimiento que se utilizan en las minas subterráneas esto depende de las condiciones geomecánicas y geoestructurales que presenta la roca, entre ellas tenemos:
2.1.2.1	Sostenimiento con uso de madera. El sostenimiento con madera se utilizaba desde la edad media (alrededor del sigo X), cuando las primeras minas se desarrollaban en Europa, esto debido a su fácil disponibilidad con las cual formaban andamios y soportes dentro de las minas. Conforme las minas subterráneas se fueron sofisticando más y profundizaban en los cuerpos mineralógicos era necesario crear blocks de madera donde se utilizaba barricas de madera, vigas de madera y andamiajes, con ello asegurar el avance y seguridad de la labor, sin embargo, este método en la actualidad es mal visto por los constantes incendios que se generaban en las minas de carbón y también en algunas minas con alta presencia de pirita.
Figura 2
Minas de carbón usando madera para sostenimiento.
Nota: fuente https://images.app.goo.gl/iFMib5iMBrU56Tc28 (Diario digital Ultima Hora)
2.1.2.2	Sostenimiento con uso de metales. A mediados del siglo XIX, las labores que presentaban las minas subterráneas eran más complicadas de manejar, las cargas que soportaban eran cada vez más pesadas y las calidades de roca en el interior de la mina estaban más dañadas, es por ello que se optó por el uso de cerchas y arcos metálicos para crear las famosas cimbras lo cual fue una útil herramienta de sostenimiento para esa época, en la actualidad se usan muy poco debido a su alto costo y su afectación con el medio ambiente.
Figura 3
Cimbras instaladas en una mina subterránea.
Nota: fuente https://images.app.goo.gl/bdfmyBscMqSAGkdk8 (Guia sobre control geotécnico en minería subterránea, pág. 9)
2.1.2.3	Sostenimiento moderno. En la actualidad los principales métodos de sostenimiento que se utilizan son pernos de anclaje, mallas electrosoldadas y concreto lanzado (shotcrete); los cuales han presentado resultados satisfactorios para labores con larga vida, generan seguridad y confianza al trabajador para su desarrollo laboral.
2.1.2.3.1	Pernos de anclaje. Se utilizan para aportar tensión a bancos sueltos hacia un sistema más estable, el cual ayuda principalmente a prevenir el deslizamiento de rocas, existen distintos tipos de pernos de rocas según su necesidad:
Pernos Helicoidal: Este perno ostenta un cuerpo en forma de espiral el cual proporciona un agarre mucho más efectivo entre los cuerpos rocosos para proporcionar mayor estabilidad, se complementan con inyecciones de resina y cemento.
Figura 4
Perno Helicoidal.
Nota: fuente https://images.app.goo.gl/JsgPujqjqGNF4Gs57 (Sistemas de Anclaje, DSI Underground)
Pernos Split Set: Es una alternativa al perno helicoidal, pero con un costo mucho más barato debido a que se utilizan para labores con mejor calidad de roca y no necesitan mucho agarre.
Figura 5
Perno Split Set.
Nota: fuente https://images.app.goo.gl/ht7mCox7c91SjbR18 (Pernos para piedra, Internacional Rollforms, INC)
Pernos Swellex: Son pernos que ostentan la misma forma del Split set, pero se utiliza cuando la condición de roca circundante está muy fragmentada, este perno se infla con ayuda de aire comprimido y compacta los fragmentos de la roca remanente.
2.1.2.3.2	Mallas electrosoldadas. Es un tipo de malla soldada formada de varillas de acero que están unidas mediante el proceso de soldadura eléctrica en forma de rejilla, a pesar de que ostentan una resistencia considerable, son muy flexibles y previenen la caída de bancos, se instalan con ayuda de pernos de anclaje y complementan la sostenibilidad en las minas subterráneas.
Figura 6
Rollos de mallas electrosoldada.
Nota: fuente https://images.app.goo.gl/dhPQ4kEqnvnHVopB7 (Categoría mallas electrosoldadas, Aceros Arequipa)
2.1.2.3.3	Concreto lanzado (shotcrete). El shotcrete es una clase de sostenimiento versátil altamente utilizado en la minería subterránea, es una combinación de cemento, agua, arena y aditivos (acelerante de fraguado, retardantes y plastificantes) que es proyectado con ayuda de aire comprimido a las paredes las labores subterráneas, el shotcrete puede presentar resistencia de 25 a 45 MPa. El método de lanzado también ha ido evolucionando a lo largo del tiempo, actualmente las minas ostentan robots que reducen desperdicios y optimizan el lanzado de shotcrete, tal como se muestra en la figura.
Figura 7
Robot lanzando shotcrete a la pared de una labor minera.
Nota: fuente https://images.app.goo.gl/E3sbi2Jkm7ipN9GVA (Concreto lanzado, Zika Colombia)
Para calcular la necesidad de shotcrete se presenta la siguiente relación matemática:
(2)
2.1.3	Mecanismo de fragmentación de la roca
Cuando al explosivo se le aplica una abrupta cantidad de energía superior a la energía química que atrae sus moléculas, estas se separan hasta conseguir un estado más estable, en este proceso se liberan principalmente gran cantidad de gases y energía mecánica en forma de ondas de presión, a este comportamiento se le conoce como reacción exotérmica. Sin embargo, no todos los explosivos reflejan los mismos resultados, esto se debe a que la velocidad de detonación en algunos es muy lenta y en otros es muy rápido, aquí se diferencian tres tipos de reacciones.
Combustión: Es una reacción exotérmica de oxidación, su velocidad de denotación es menor a 1 m/s y se puede observar a simple vista en forma de llama.
Deflagración: Es una reacción subsónica, debido a que su velocidad de detonación es mayor a la de la combustión, pero menor a la velocidad del sonido, esta reacción genera una onda de presión de  atmosferas, por ello se le confunde con una explosión.
Detonación: Es una reacción supersónica, ya que su velocidad de detonación supera la velocidad del sonido (entre 1500 a 9000 m/s) generando ondas de choque con altos gradientes de presión y temperatura, utilizables para la fragmentación de roca en minería.
Figura 8
Gráfica que diferencia el comportamiento de un explosivo según su velocidad de detonación en el tiempo.
Nota: fuente Perforación y voladura de rocas en minería (p.66), de A. Bernaola, J. Castilla y F. Herrera, 2013.
La fragmentación de rocas se lleva a cabo principalmente por dos comportamientos que se realizan en la detonación de un explosivo.
En la primera fase, la onda de choque generada por la reacción exotérmica, con gran velocidad de detonación, representando el 10% de la energía total del explosivo, genera un fisuramiento radial donde se presentan distintas zonas como se en observa en la imagen.
Figura 9
Tipos de fisuramiento en las cercanías del taladro
Nota: fuente Perforación y voladura de rocas en minería (p.133), de A. Bernaola, J. Castilla y F. Herrera, 2013.
Cuando existe una cara libre las ondas de choque se reflejan creando un esfuerzo de tracción que facilitan la creación grietas y aumenta la ampliación del radio fisurado.
La segunda fase es cuando los gases liberados por esta reacción impulsan a los fragmentos creados por lo primera fase en dirección a la cara libre, incrementando así la abertura según como se observa en la siguiente figura.
Figura 10
Zonas de la cuña de fracturamiento debido a la reflexión de las ondas de choque.
Nota: fuente Perforación y voladura de rocas en minería (p.134), de A. Bernaola, J. Castilla y F. Herrera, 2013.
2.1.4	Criterio de diseño de malla de perforación para voladura controlada
La voladura convencional frecuentemente afecta estructuralmente a las paredes y techo de las labores subterráneas generando inestabilidad, desprendimiento de bancos en un corto plazo y sobrerotura fuera de los estándares, para este problema se creó el criterio de voladura controlada que consiste en el uso de cargas explosivas de baja energía y perforación taladros cercanos entre sí, para crear un plano de rotura que limite la superficie final de la labor.
La voladura controlada también rige su fragmentación en el contorno por esfuerzos de la onda de choque y acción de gases de expansión, pero  cuando los taladros se encuentran cercanos la interacción de las ondas de choque no solo generan las grietas radiales a lo largo del taladro, sino también producen esfuerzos de tracción perpendiculares al plano axial favoreciendo la propagación de grietas radiales en la dirección de corte proyectado, posteriormente estas grietas se agrandan con la interacción de los gases del explosivo generando un plano de rotura definido.
Figura 11
Funcionalidad de las ondas de tensión para la generación de zonas formadoras del plano de rotura.
Nota: fuente Manual práctico de voladura (5ta ed.) (p. 252), de EXSA Soluciones Exactas, s.f.
Para considerar una voladura como controlada en minería subterránea se deben cumplir las siguientes condiciones:
Perforación: Diámetro de taladros de producción igual al diámetro de taladros de contorno, al perforar los taladros se debe mantener el paralelismo de acuerdo con el diseño del plano de rotura, el emboquillado no debe superar desviaciones de 0.1 a 0.15m en el fondo, el espaciamiento debe ser menor que el burden debido a que su relación debe estar en el rango de (0.5-0.8).
Carga explosiva: Se deben usar explosivos de baja energía y velocidad, la carga debe estar desacoplada al taladro en una relación de 2:1, para facilitar la creación del plano de rotura se pueden intercalar taladros vacíos como guía entre los taladros con explosivo.
Carga en el fondo: Es necesario la utilización de un explosivo potente para el cebado con la finalidad de asegurar el arranque y evitar que se formen tacos en el fondo del taladro después de la voladura.
Disparo: El disparo de los taladros del contorno deben ser simultaneo, sin embargo, si el perímetro es grande se puede realizar en un máximo de dos o tres etapas con un retardo corto.
A lo largo de los años se han creado distintas técnicas, en su mayoría para casos particulares, pero existen dos técnicas genéricas en las minas subterráneas, las cuales se definirán a continuación.
2.1.4.1	Voladura de precorte. Consiste en formar un plano de fractura antes de disparar la voladura principal, mediante taladros de bajo diámetro, cercanos entre sí, y con cargas explosivas de baja energía, desacoplados y disparados simultáneamente.
2.1.4.2	Voladura de recorte. Consiste en realizar la voladura de una fila de taladros cercanos y con cargas desacopladas después de la voladura de producción.
Figura 12
Fases de las voladuras controladas en minería subterránea.
Nota: fuente Manual práctico de voladura (5ta ed.) (p. 270), de EXSA Soluciones Exactas, s.f.
2.1.5	Optimización en el diseño y cálculo de mallas de perforación: Modelo matemático de Holmberg
El modelo matemático de Holmberg, diseñado para simplificar los cálculos, divide el frente en cinco secciones, etiquetadas de A a E, como se muestra en la figura siguiente. Cada una de estas secciones tiene un enfoque específico para su cálculo.
Figura 13
Secciones de trabajo para la obtención de la malla de perforación.
Nota: fuente Manual de perforación y voladura de rocas (p. 309), de Instituto Tecnológico GeoMinero de España, s.f.
Donde:
A: Sección de corte.
B: Sección de ayudas de hastiales.
C: Sección de ayudas de corona.
D: Sección de contorno.
E: Sección de arrastres.
2.1.5.1	Avance por disparo. El primer paso en el modelo de Holmberg consiste en calcular el avance necesario por disparo. Es claro que se puede lograr un mayor ahorro si se obtiene un disparo completo. Por esta razón, Holmberg, en sus estudios, presenta un gráfico que ilustra la relación entre la dimensión el diámetro del taladro vacío (cara libre) para el avance requerido. Este cálculo debe garantizar una efectividad en el avance mínimo del 95%, considerando que el corte será de cuatro secciones.
Figura 14
Gráfica de relación entre la profundidad del taladro y el diámetro del taladro vacío.
Nota: fuente Manual de perforación y voladura de rocas (p. 310), de Instituto Tecnológico GeoMinero de España, s.f.
La ecuación que describe la profundidad del taladro, H, puede expresarse de la siguiente manera.
(3)
El avance  es representado con el  de la profundidad del taladro, según la siguiente ecuación:
(4)
Estas dos ecuaciones son aplicables siempre y cuando la desviación en la perforación no supere el 2%, lo que garantiza que el proceso se mantenga dentro de un margen de error aceptable para la precisión requerida.
Cuando no se cuenta con el diámetro adecuado del taladro vacío necesario para alcanzar el avance requerido por la ecuación (3), es necesario realizar perforaciones adicionales. Estas perforaciones adicionales se representan como un taladro vacío equivalente, lo que permite ajustar el proceso de perforación para cumplir con los parámetros de avance establecidos. Esta equivalencia se expresa mediante la siguiente ecuación.
(5)
Donde  representa el diámetro del taladro equivalente, que corresponde a la combinación de varios taladros vacíos de menor diámetro que el requerido.
2.1.5.2	Arranque de cuatro secciones. El diseño geométrico general de una sección de corte, que incluye cuatro secciones con barrenos paralelos, se ilustra en la figura siguiente.
Figura 15
Representación de las cuatro secciones de corte.
Nota: fuente Manual de perforación y voladura de rocas (p. 310), de Instituto Tecnológico GeoMinero de España, s.f.
La distancia entre el taladro vacío equivalente central y los taladros de la primera sección no debe exceder de "“”  para asegurar una fragmentación eficiente y una adecuada liberación de la roca (Langefors y Kilhstrom, 1963). Es importante destacar que las condiciones de fragmentación pueden variar considerablemente según el tipo de explosivo utilizado, las características específicas de la roca y la distancia entre el barreno cargado y el vacío.
Cuando el burden es mayor a “” el ángulo de salida se vuelve demasiado reducido, lo que provoca una deformación plástica de la roca entre los dos taladros. Incluso si el burden es menor que “”, pero la concentración de carga es demasiado alta, puede ocurrir la sinterización de la roca fragmentada, lo que resulta en un fallo en el arranque tal como se presenta en la siguiente imagen. Por esta razón, se recomienda calcular el burden tomando en cuenta lo siguiente:
(6)
Figura 16
Comportamiento de la voladura respecto a la relación del burden y el diámetro del taladro vacío
Nota: fuente Manual de perforación y voladura de rocas (p. 310), de Instituto Tecnológico GeoMinero de España, s.f.
Cuando la desviación de perforación supera el 1%, es necesario considerar el factor de error de perforación para ajustar los valores del burden. El error de perforación se representa mediante la siguiente fórmula:
(7)
Donde:
EP: Error de perforación (m).
∝: Desviación angular (m/m).
I: Profundidad de los taladros (m).
: Error de emboquille (m)
Por lo tanto, el burden práctico (el burden aplicado en el campo) queda determinado por la siguiente ecuación:
(8)
La concentración de carga lineal se calcula a partir de la siguiente expresión:
(9)
Donde:
: Concentración lineal de carga (kg/m)
: Diámetro de perforación (m)
: Diámetro del taladro vacío (m)
: Burden
: Constante de roca
: Potencia relativa en peso del explosivo referida al ANFO
Sin embargo, los valores de concentración lineal están limitados debido a la variedad restringida de explosivos disponibles en el mercado. Generalmente, se selecciona un explosivo cuyo valor de concentración lineal esté lo más cerca posible al calculado mediante la ecuación (9). No obstante, existen dos métodos adicionales para obtener un cálculo más preciso. El primero consiste en utilizar la gráfica propuesta por Holmberg, que establece la relación entre el diámetro del taladro vacío equivalente, la concentración lineal de carga y el burden práctico, tal como se muestra en la siguiente figura. El segundo método, más complejo, implica despejar el burden de la ecuación 3 una vez conocida la concentración de carga lineal del explosivo a utilizar, y resolver la ecuación de quinto grado resultante.
Figura 17
Grafica para el cálculo del burden máximo según la concentración lineal y el diámetro del taladro vacío.
Nota: fuente Manual de perforación y voladura de rocas (p. 311), de Instituto Tecnológico GeoMinero de España, s.f.
Para calcular el resto de las secciones, se asume que ya existen huecos rectangulares de anchura  y que se conocen las concentraciones de carga lineal El valor del burden se calcula utilizando la siguiente fórmula:
(10)
Cuando se presenta un error de perforación, como se observa en la siguiente figura, la superficie libre Ah difiere de la distancia Ah' en la primera sección, como se muestra en la siguiente figura, lo que implica que:
(11)
Figura 18
Gráfico de la afectación del burden debido a la desviación de la perforación.
Nota: fuente Manual de perforación y voladura de rocas (p. 311), de Instituto Tecnológico GeoMinero de España, s.f.
Al sustituir este valor en la ecuación (10), se obtiene el siguiente resultado:
(12)
Este valor debe ajustarse considerando la desviación de los taladros para obtener el burden práctico.
(13)
Existen algunas limitaciones respecto a  las cuales deben cumplirse de la siguiente manera:
(14)
Si no se cumple la condición anterior, se provocará una deformación plástica en la roca. Para corregir este problema, es necesario ajustar la concentración de carga lineal utilizando la siguiente ecuación:
(15)
Si no se cumple la restricción de deformación plástica, lo más adecuado es elegir un explosivo de menor potencia para mejorar la fragmentación. Asimismo, el ángulo de apertura debe ser inferior a 1.6 radianes (90°), ya que, de lo contrario, el arranque deja de tener la forma de corte en cuatro secciones. Esto significa que:
(16)
Gustafsson (1973), sugiere que el burden para cada sección se calcule con:
(17)
Una regla general para determinar el número de secciones es que la longitud del lado de la última sección, Ah, no debe ser mayor que la raíz cuadrada del avance. El método para calcular las demás secciones es el mismo que se aplica para la segunda sección. La longitud del retacado se puede calcular utilizando la siguiente ecuación:
(18)
Para el cálculo del número de cartuchos utilizados en los taladros de la sección de corte se utiliza la siguiente ecuación.
(19)
Donde
Lc: Longitud de carga (m)
: Peso neto del explosivo (kg)
2.1.5.3	Cálculo de sección de arrastres. Para calcular el burden de los taladros de arrastre dispuestos en fila, se emplea la misma relación utilizada en la voladura de bancos en la minería a cielo abierto, considerando que la altura del banco corresponde a la profundidad de avance de la labor.
(20)
Donde:
= Factor de fijación, generalmente se toma 1.45 para tener en cuenta el efecto gravitacional y el tiempo de retardo entre taladros.
=Relación entre espaciamiento y el burden, Se suele tomar igual a 1.
= Constante de roca corregida
En los taladros de arrastre, es fundamental tener en cuenta el ángulo de realce “γ” o inclinación necesaria para asegurar un hueco adecuado que permita a la perforadora realizar el emboquille del próximo disparo. Para un avance de 3 metros, un ángulo de 3°, equivalente a 5 cm/m, es generalmente suficiente, aunque esto dependerá, por supuesto, de las características específicas del equipo utilizado.
El número de taladros vendrá dado por:
(21)
Donde:
: ancho de la labor (m).
: ángulo de realce (°)
Figura 19
Representación gráfica de los taladros de arrastre con realce, espaciamiento practico y burden máximo
Nota: fuente Manual de perforación y voladura de rocas (p. 313), de Instituto Tecnológico GeoMinero de España, s.f.
El espaciamiento práctico para los taladros del rincón esta dado por la siguiente expresión.
(22)
El burden práctico “” se obtiene a partir de la siguiente ecuación.
(23)
El taco en los taladros de arrastre son los mismos que en la sección de corte.
(24)
La concentración de carga en el fondo es la misma que se utilizó en sección de corte.
(25)
La altura de carga en el fondo se calcula mediante la siguiente formula.
(26)
Para el cálculo del número de cartuchos en el fondo del taladro tenemos la siguiente expresión.
(27)
Donde:
: Longitud del cartucho (m)
La concentración de carga en las columnas de los taladros de arrastres se obtiene mediante la siguiente ecuación:
(28)
La altura de carga en la columna se calcula mediante la siguiente formula.
(29)
Para el cálculo del número de cartuchos en la columna tenemos la siguiente expresión.
(30)
2.1.5.4	Cálculo de sección de tajeo. El método para calcular el esquema de los taladros del tajeo es similar al utilizado para los de arrastre, con la única diferencia de que se aplican valores diferentes para el factor de fijación y la relación espaciamiento/burden.
Tabla 1
Valores de factor de fijación y relación (S/B) de los tajeos.
Nota: fuente Manual de perforación y voladura de rocas (p. 314), de Instituto Tecnológico GeoMinero de España, s.f.
La concentración de carga en la columna, para ambos tipos de taladros, debe ser la mitad de la concentración de carga en el fondo.
2.1.5.5	Cálculo de la sección de contorno. En caso de que en la excavación no se utilice la voladura controlada, los esquemas se calculan de acuerdo con lo indicado para los taladros de arrastre con los siguientes valores:
Tabla 2
Valores de factor de fijación y relación (S/B) del contorno.
Nota: fuente Manual de perforación y voladura de rocas (p. 314), de Instituto Tecnológico GeoMinero de España, s.f.
Siendo la concentración de la carga en el fondo.
En el caso que se tenga que realizar voladuras controladas se debe analizar la presión de taladro que ejerce cada uno del explosivo mediante la siguiente expresión.
(31)
Entonces la presión del taladro efectiva está dada por la siguiente ecuación.
(32)
Se debe verificar que la presión efectiva del taladro sea inferior al esfuerzo de compresión de la roca circundante, para evitar que ésta se vea afectada y así obtener una sección con una sobrerotura mínima.
La concentración de carga lineal mínima se obtiene de la siguiente expresión.
(33)
La concentración lineal del explosivo se calcula utilizando la siguiente ecuación, la cual debe ser comparada con la concentración mínima establecida. Para que el cálculo sea válido, la concentración obtenida debe ser superior a la concentración mínima requerida.
(34)
Es crucial asegurarse de que el explosivo tenga, como mínimo, la concentración de carga lineal efectiva necesaria para evitar disparos fallidos y lograr un contorno uniforme, sin taladros soplados.
El espaciamiento en el corno se calcula mediante la siguiente formula.
(35)
Para el cálculo de burden teórico en el contorno se calcula con la siguiente ecuación.
(36)
El burden practico se calcula mediante la siguiente expresión.
(37)
En el contorno no es indispensable colocar el taco, sin embargo, para asegurar que los gases de la explosión no escapen se deberá considerar un taco como en la sección de corte.
(38)
La longitud de carga en la columna del taladro este dado por la siguiente formula.
(39)
Para el cálculo del número de taladros se debe calcular primero la longitud de arco el cual está determinado mediante la siguiente ecuación.
(40)
Para luego obtener del número taladro mediante la siguiente formula.
(41)
Finalmente, se obtiene el número de cartuchos por taladro mediante la siguiente expresión.
(42)
2.1.6	Programación con Python
Python es un lenguaje de programación lanzada al público en 1991 por Guido Van Rossum, creada para desarrollo web, resolución de matemáticas complejas, para crear aplicaciones web, softwares para crear flujos de trabajo, gestionar grandes cantidades de datos, etc. Python es un lenguaje con sintaxis simple similar al idioma inglés y orientada a objetos el cual permite tener un sistema más completo y sofisticado.
2.1.6.1	Fundamentos de Python.
2.1.6.1.1	Variables. Las variables son todo aquello que se le coloca valor de datos.
Criterio de nombre:
Pueden empezar con una letra o “_”, no números ni símbolos, las mayúsculas distinguen variables y no puede ser una “palabra clave”.
Variable de salida y entrada: “Print” :
Es el comando para reflejar en el terminal algún comentario, tabla, imagen, etc. “Input” es el comando para solicitar datos al usuario.
Variables locales:
Toda variable debe estar definida, si está definida en código libre todos los códigos pendientes tomaran su valor, si se le asigna un valor dentro de un código especifico solo tomara ese valor en esa parte del código, sin embargo, si se necesita globalizar su valor para todos los códigos consiguientes se tendrá que usar antes la palabra clave “global”.
2.1.6.1.2	Datos. Se presenta en el siguiente cuadro con los comandos constructores que forman los tipos de datos que maneja Python.
Tabla 3
Comandos constructores de datos.
Nota: Adaptado de “Métodos de cadena”, por W3Schools, 2024, recuperado de https://www.w3schools.com/python/python_strings_methods.asp.
2.1.6.1.3	Operadores en Python. En Python existen distintos tipos de operadores que realizan operaciones entre variables y valores, en el siguiente recuadro observaremos que tipos de operadores maneja Python.
Tabla 4
Tipos de operadores.
Nota: Adaptado de “Operadores de Python”, por W3Schools, 2024, recuperado de https://www.w3schools.com/python/python_operators.asp.
2.1.6.1.4	Clases de Python.
Cadenas:
Son caracteres que están encerrados entre comillas y representan un matriz de bytes que reflejan caracteres unicode.
Dentro de las propiedades más importantes de las cadenas tenemos:
La ubicación de sus caracteres se realiza escribiendo la variable y posterior a ello “[a, b]”; siendo “a” el espacio de inicio del carácter y “b” el espacio final
La función “len()” indica la cantidad de caracteres que ostenta la cadena.
Los métodos más elementales que se utilizan se presentan en la siguiente tabla:
Tabla 5
Métodos de cadenas.
Nota: Adaptado de “Operadores de Python”, por W3Schools, 2024, recuperado de https://www.w3schools.com/python/python_strings_methods.asp.
Si se desea colocar una variable, operación, lista, función, tupla, diccionario, etc., dentro de una descripción salida se puede usar el comando de formato de cadena que se observa mediante la siguiente forma:
Los “caracteres de espacios” pueden reflejar un mensaje mucho más claro para el usuario en el terminal, en la siguiente tabla se presentan con la descripción de la funcionalidad de cada uno.
Tabla 6
Caracteres de escape.
Nota: Adaptado de “Caracteres de escape”, por W3Schools, 2024, recuperado de https://www.w3schools.com/python/python_strings_escape.asp.
Listas:
Son clases que almacenan gran cantidad de datos en una sola variable, son ordenados porque están indexados, se pueden cambiar, agregar o retirar elementos y permite tener duplicados.
Dentro de sus principales propiedades de las listas tenemos:
La función “len()” indica la cantidad de valores que tiene la lista.
Para acceso a los elementos de las listas se realiza de la misma forma que en las cadenas.
Para ampliar elemento se debe utilizar “lista.append()”.
Para unir dos listas se debe utilizar “lista1.extend(lista2)”.
Para eliminar elementos de la lista se utiliza “remove(“”)” cuando se indica que elemento se quiere eliminas, “pop(1)” cuando se conoce la posición mediante el índice, se utiliza la palabra clave “del” si es que se quiere eliminar la lista y se usa “lista.clear” para dejar la lista vacía.
Para crear listas de forma rápida y con poco código se debe escribir la siguiente función:.
La “condición” funciona como un filtro para los datos que quieras que pasen a la “expresión” en el cual se puede colocar condiciones de como quieres que se presenten los datos.
Los métodos más elementales que se utilizan en las listas son las siguientes:
Tabla 7
Métodos de listas.
Nota: Adaptado de “Métodos de listas”, por W3Schools, 2024, recuperado de https://www.w3schools.com/python/python_lists_methods.asp.
Tuplas:
Es una clase almacenadora de datos ordenados porque sus elementos están indexados, es inalterable debido a que no se pueden cambiar sus elementos, agregar o eliminar elementos y permite tener duplicados.
Las propiedades principales de la tupla son:
Se cuenta los elementos del conjunto con el código “len()”.
Para cambiar, eliminar y agregar valores de la tupla se debe convertir a lista, realizar la acción y cambiarlo a tupla.
Para recorrer tuplas se deben usar funciones iterables “for”, “range” y “while”.
Para unir tuplas se debe usar el operador suma.
Los métodos más usados en las tuplas se presentan en el siguiente cuadro.
Tabla 8
Métodos de Tuplas.
Nota: Adaptado de “Métodos de tuplas”, por W3Schools, 2024, recuperado de https://www.w3schools.com/python/python_tuples_methods.asp.
Conjuntos:
Los conjuntos son clases que almacenan datos, no está ordenada por lo que sus elementos no tienen índice, es inmutable debido a que no se pueden cambiar sus elementos, pero si agregar y eliminar, y no acepta duplicados.
Dentro de las propiedades fundamentales de los conjuntos tenemos:
Dentro del conjunto “true” y “1” son el mismo valor.
Dentro del conjunto “false” y “0” son el mismo valor.
Para obtener la cantidad de elemento también se utiliza el código “len()”.
Para agregar elementos se utiliza el código “set.add(elemento)” y  “set.update(tuple)”.
Para eliminar elementos se usan los siguientes códigos: “remove”, “discard”, “pop”, “clear” y la palabra clave “del”.
Para interactuar con sus elementos solo se usa el bucle “for”.
Los métodos más importantes de los conjuntos se observan en el siguiente cuadro.
Tabla 9
Métodos de conjuntos.
Nota: Adaptado de “Unir conjuntos”, por W3Schools, 2024, recuperado de https://www.w3schools.com/python/python_sets_join.asp.
Son clases que se utilizan para almacenar datos en pares “clave:valor” el cual es ordenado, modificable pero no permite duplicados.
Entre las propiedades más importantes de los diccionarios tenemos:
Para determinar la cantidad de elementos de un diccionario se el código “len()”.
Su código constructor es “dict()”.
Se puede acceder al valor sabiendo la clave con el código “thisdict.get(clave)”.
Al usar el código “dict.key()” devolverá una lista con todas las claves.
Al usar el código “dict.values()” devolverá una lista con todos los valores.
Para eliminar elementos del diccionario se utiliza el código “pop()”, “clear()” o la palabra clave “del”.
Solo se puede recorrer el diccionario con el bucle “for”.
Los métodos mas importantes de los diccionarios se muestran en la siguiente tabla.
Tabla 10
Métodos de diccionarios.
Nota: Adaptado de “Métodos de diccionario de Python”, por W3Schools, 2024, recuperado de https://www.w3schools.com/python/python_dictionaries_methods.asp.
2.1.6.1.5	Condicionales en Python. Python permite trabajar con funciones condicionales mediante la palabra clave “if”, las condiciones se rigen bajo los operadores de comparación (== , != , > , < , >= , <=) lo cuales funcionan como filtros, es importante utilizar la sangría para diferenciar el nivel donde se encuentra, tal como se observa en la siguiente imagen.
Python permite trabajar con funciones condicionales mediante la palabra clave “if”, las condiciones se rigen bajo los operadores de comparación (== , != , > , < , >= , <=) lo cuales funcionan como filtros, es importante utilizar la sangría para diferenciar el nivel donde se encuentra, tal como se observa en la siguiente imagen.
Figura 20
Representación del código condicional con la palabra clave “if”.
Nota: Adaptado de “Si… de lo contrario, Python”, por W3Schools, 2024, recuperado de https://www.w3schools.com/python/python_conditions.asp.
Si la condición de la palabra clave “if” no es verdadera se pueden añadir mas condiciones mediante la palabra clave “elif”, sin embargo, si ninguna de estas condiciones es verdadera se usa la palabra clave “else”, tal como se muestra en la siguiente imagen.
Figura 21
Representación del código multicondicional.
Nota: Adaptado de “Si… de lo contrario, Python”, por W3Schools, 2024, recuperado de https://www.w3schools.com/python/python_conditions.asp.
2.1.6.1.6	Bucles en Python. Cuando se quiere realizar tareas repetitivas Python tiene las palabras clave “for” y “while” los cuales cumplen la misma función, pero con métodos distintos.
Con la palabra clave “while” se realiza un bucle continuo hasta que la condición presentada sea falsa, y si se necesita romper el buble antes, se utiliza la palabra clave “break”.
Figura 22
Representación del uso del bucle “while” con la palabra clave “break”
Nota: Adaptado de “Bucle while de Python”, por W3Schools, 2024, recuperado de  https://www.w3schools.com/python/python_while_loops.asp.
El bucle “for” se utiliza para iterar sobre una secuencia (lista, diccionario, tupla, conjunto o cadena), cuando presenta un error se puede utilizar la palabra clave “pass” para que el código no se interrumpa.
Figura 23
Representación del uso del bucle “for” con la palabra clave “break”
Nota: Adaptado de “Bucles for de Python”, por W3Schools, 2024, recuperado de https://www.w3schools.com/python/python_for_loops.asp.
Una función es un bloque de código que solo se ejecuta cuando se coloca su nombre, estos ostentan argumentos que se colocan dentro del paréntesis de la función, para que las variables dentro de la función tomen el valor que el usuario coloca.
Figura 24
Representación de la creación de una función básica en Python
Nota: Adaptado de “Funciones de Python”, por W3Schools, 2024, recuperado de https://www.w3schools.com/python/python_functions.asp.
La recursión en Python es un concepto en el que una función se llama a sí misma para resolver un problema. Este enfoque es útil cuando un problema puede dividirse en subproblemas similares que se resuelven de manera repetitiva.
Al utilizar recursión, la función realiza una serie de llamadas a sí misma, cada vez con parámetros modificados, hasta que se alcanza una condición de terminación. Esta condición es crucial para evitar que la función se llame infinitamente.
Figura 25
Representación de la utilización de la recursión de funciones en Python.
Nota: Adaptado de “Funciones de Python”, por W3Schools, 2024, recuperado de https://www.w3schools.com/python/python_functions.asp.
2.1.6.2	Bibliotecas de Python.
2.1.6.2.1	Math. Es una librería estándar de Python que proporciona acceso a funciones matemáticas básicas. Está diseñada para realizar operaciones matemáticas que son comunes en el desarrollo de aplicaciones científicas y de ingeniería, como funciones trigonométricas, exponenciales, logaritmos y operaciones algebraicas. Math se utiliza principalmente cuando necesitamos hacer cálculos de alto rendimiento y precisión con valores numéricos simples.
Aunque no incluye funciones de álgebra lineal avanzadas ni matrices, es ideal para operaciones matemáticas simples. Su eficiencia es uno de sus principales puntos fuertes, ya que las funciones están escritas en “C”, lo que las hace muy rápidas.
Algunos de sus métodos más importantes son:
Tabla 11
Métodos de la biblioteca Math
Nota: Adaptado de “Modulo de Matemáticas”, por W3Schools, 2024, recuperado de https://www.w3schools.com/python/module_math.asp.
2.1.6.2.2	Matplotlib. Es una biblioteca poderosa para la visualización de datos en Python. Su módulo principal, pyplot, permite crear gráficos 2D y algunas visualizaciones 3D de manera rápida y sencilla. Esta librería es ampliamente utilizada en ciencia de datos, análisis estadístico, ingeniería y cualquier campo que requiera mostrar información de manera gráfica.
Uno de sus mayores beneficios es su flexibilidad y compatibilidad con otros paquetes como NumPy, lo que permite crear gráficos a partir de arreglos numéricos. También es compatible con otros entornos gráficos como Jupyter Notebook, facilitando la creación de gráficos interactivos.
Algunos de sus métodos más importantes son:
Tabla 12
Métodos de la biblioteca Matplotlib.
Nota: fuente https://matplotlib.org/stable/users/index.html (página web de Matplotlib)
2.1.6.2.3	NumPy. Es una de las bibliotecas más utilizadas en Python para el cálculo numérico. Su principal ventaja es la manipulación eficiente de grandes volúmenes de datos numéricos a través de sus arreglos multidimensionales (ndarrays).
Estos arreglos son mucho más rápidos y eficientes que las listas estándar de Python. NumPy también proporciona una gran variedad de funciones matemáticas, estadísticas y algebraicas para operar sobre estos arreglos de forma eficiente.
Además, NumPy es la base para muchas otras bibliotecas científicas en Python, como SciPy y pandas, lo que lo convierte en un componente esencial del ecosistema de ciencia de datos.
Algunos de sus métodos más importantes son:
Tabla 13
Métodos de la biblioteca NumPy.
Nota: fuente https://numpy.org/doc/ (página web de NumPy documention).
2.1.6.2.4	Pandas. Es una biblioteca fundamental para el análisis de datos en Python. Proporciona dos estructuras de datos clave: Series y DataFrame. La Series es una estructura unidimensional que puede almacenar cualquier tipo de dato, mientras que el DataFrame es bidimensional, similar a una tabla o hoja de cálculo, lo que lo hace ideal para trabajar con datos tabulares.
Uno de los grandes beneficios de pandas es su capacidad para manejar datos faltantes, realizar operaciones de filtrado y agrupación, y combinar múltiples fuentes de datos en una sola estructura. Esta biblioteca es utilizada ampliamente en análisis de datos, limpieza de datos y manipulación de grandes volúmenes de información.
Algunos de sus métodos más importantes son:
Tabla 14
Métodos de la biblioteca Pandas.
Nota: fuente https://pandas.pydata.org/ (Pagina web de Pandas).
2.2	Marco conceptual
Geomecánica: Ciencia que estudia el comportamiento de las rocas y su interacción con las estructuras subterráneas en minería. Se enfoca en cómo las fuerzas externas, como las cargas y las voladuras, afectan la estabilidad de las excavaciones subterráneas, optimizando los procesos de extracción y garantizando la seguridad en las operaciones mineras.
Acelerante: Aditivo utilizado en el concreto lanzado para acelerar el proceso de fraguado. En minería, este material mejora la seguridad al permitir que el concreto adquiera resistencia rápidamente, facilitando el sostenimiento y la estabilización de túneles y otras excavaciones subterráneas.
Explosivo: Sustancia química empleada en minería para generar una reacción exotérmica controlada que facilita la fragmentación de la roca. Los explosivos liberan una gran cantidad de energía de forma rápida, lo que permite la ruptura de la roca de manera eficiente y controlada.
Reacción: Proceso químico que ocurre durante la detonación de un explosivo. Dependiendo de la velocidad de la reacción (combustión, deflagración o detonación), esta influye en la efectividad y el control de la voladura, impactando directamente en la fragmentación de la roca.
Fisuramiento: Formación de grietas o fracturas en la roca debido a la acción de las ondas de choque generadas durante la detonación de explosivos. El fisuramiento reduce la resistencia de la roca, permitiendo su fragmentación más fácil y controlada.
Gases: Subproductos de la detonación de los explosivos. Los gases liberados, como productos de combustión, generan una presión elevada que impulsa los fragmentos de roca y facilita su fragmentación.
Reflexión: Comportamiento de las ondas de choque cuando encuentran una superficie libre, como la cara de la roca o una cavidad. La reflexión contribuye a la creación de grietas y mejora la eficiencia de la voladura.
Burden: Distancia entre los taladros de perforación y la cara libre de la roca. Este parámetro es fundamental para el diseño de las voladuras controladas, ya que determina la cantidad de energía necesaria para fragmentar la roca de manera eficiente y segura.
Taladro: Hueco o cavidad realizada en la roca mediante perforadora, que servirá para almacenar los explosivos utilizados en una voladura. La precisión en la perforación es clave para la correcta colocación de los explosivos y la seguridad de la operación minera.
Interacción: Comportamiento entre las ondas de choque generadas por los explosivos y las fracturas preexistentes en la roca. Esta interacción facilita la propagación de las fracturas en la dirección deseada, optimizando la fragmentación de la roca.
Espaciamiento: Distancia entre los taladros de perforación en una voladura controlada. Este factor debe ser calculado correctamente para garantizar la eficiencia y seguridad de la voladura, logrando una fragmentación adecuada sin causar problemas en la estabilidad de la roca.
Emboquillado: Alineación y desviación de los taladros respecto al fondo del agujero. El emboquillado adecuado asegura la correcta colocación de los explosivos, lo cual es esencial para una voladura controlada y efectiva.
Desacoplamiento: Técnica que consiste en dejar un espacio entre la carga explosiva y las paredes del taladro, lo cual facilita la creación de un plano de rotura y optimiza la fragmentación controlada de la roca.
Cebado: Colocación de explosivos de alta potencia en el fondo del taladro para asegurar el inicio adecuado de la voladura. El cebado es esencial para evitar formaciones no deseadas en la roca y garantizar que la voladura comience de forma efectiva.
Cartuchos: Unidades de explosivo que se colocan dentro de los taladros. El número de cartuchos a utilizar depende de la longitud del taladro y de la cantidad de explosivo requerido para realizar una voladura eficaz.
Presión: Fuerza generada por los gases de la detonación en el interior del taladro. En voladuras controladas, es importante que la presión no exceda el esfuerzo de compresión de la roca circundante, para evitar daños indeseados y garantizar una fragmentación eficiente.
Python: Lenguaje de programación de alto nivel, interpretado y de propósito general, utilizado en minería y diversas aplicaciones tecnológicas. Su sintaxis clara y legible lo hace accesible para desarrollar programas que faciliten la automatización y análisis de datos en minería.
Recursión: Técnica en programación donde una función se llama a sí misma para resolver un problema más pequeño. En minería, se puede utilizar en la resolución de problemas complejos relacionados con simulaciones o cálculos en cadenas de procesos repetitivos.
Módulo: Conjunto de funciones y variables en un archivo, que organiza el código en Python. En minería, los módulos permiten reutilizar código en simulaciones, análisis de datos o control de voladuras, facilitando la programación.
Biblioteca: Conjunto de módulos predefinidos que proporcionan funciones específicas sin necesidad de escribir el código desde cero. En minería, bibliotecas como NumPy, pandas o matplotlib se utilizan para procesar datos y generar informes visuales de operaciones.
Argumento: Valor que se pasa a una función cuando se llama. En aplicaciones mineras, los argumentos pueden incluir parámetros como las características de los taladros, explosivos o el tipo de roca, permitiendo ejecutar cálculos específicos para la voladura.
Parámetro: Variable definida en una función que recibe los valores de los argumentos. Los parámetros permiten personalizar la ejecución de funciones para diferentes escenarios en la minería, como ajustar las variables de diseño de una voladura.
Método: Función asociada a un objeto en programación orientada a objetos. En minería, los métodos pueden manipular objetos como los cálculos de voladura, simulaciones de fragmentación o análisis de estructuras subterráneas.
Constructor: Método especial en Python que se invoca cuando se crea un objeto de una clase. En minería, los constructores pueden ser utilizados para inicializar objetos como voladuras o simulaciones, preparando sus datos y configuraciones iniciales.
Herencia: En programación orientada a objetos, es el principio que permite que una clase derive características de otra. En minería, la herencia podría aplicarse a programas que modelan diferentes tipos de voladuras o estructuras, heredando funcionalidades comunes de una clase base.
Polimorfismo: Capacidad de una función o método para manejar diferentes tipos de datos. En minería, se puede usar polimorfismo para crear programas que ajusten dinámicamente las simulaciones de voladuras o el análisis de datos según las características de la roca o los explosivos.
Encapsulamiento: Es el principio que oculta la implementación interna de una clase y solo expone la interfaz necesaria para interactuar con ella. En minería, el encapsulamiento se utiliza para mantener la integridad de los datos y garantizar la seguridad y eficiencia en los cálculos y simulaciones.
Capítulo III. Desarrollo del trabajo de investigación
3.1	Metodología
3.1.1	Tipo y diseño de la investigación
3.1.1.1	Enfoque de la investigación.  El presente trabajo de investigación adopta un enfoque caracterizado por una percepción objetiva y excluyente de la realidad, basada en un razonamiento deductivo. Se contrasta la hipótesis con el objetivo de comprobar, confirmar y reducir variables, orientándose hacia la obtención de resultados precisos. Este enfoque sigue un principio de verdad particularizada, estable y predeterminada, centrado en las similitudes observadas. La perspectiva del investigador es externa, adoptando una visión objetiva, mientras que la causalidad se fundamenta en antecedentes específicos. Por lo tanto, esta investigación sigue una tendencia cuantitativa.
3.1.1.2	Alcance de la investigación. El alcance de esta investigación es de naturaleza explicativa, ya que se enfoca en identificar y analizar las causas que originan la sobrerotura en las labores de avance y desarrollo en minas subterráneas, así como los costos elevados de sostenimiento asociados a este fenómeno. El estudio no se limita a describir el problema, sino que tiene como objetivo explicar cómo la implementación de un software de automatización para el diseño y cálculo de mallas optimizadas puede reducir tanto la sobrerotura como el tiempo requerido para realizar estas tareas.
Asimismo, se analiza cómo la minimización de la sobrerotura puede contribuir a la reducción de los costos de sostenimiento en las labores mineras. En este sentido, el enfoque explicativo busca comprender las relaciones causales entre el diseño de la malla de perforación, la sobrerotura y los costos asociados al sostenimiento, así como el impacto de la automatización del proceso de diseño de mallas de perforación optimizadas.
3.1.1.3	Diseño de la investigación. El presente trabajo de investigación sigue un diseño experimental, ya que busca analizar las relaciones causales entre diferentes variables en el proceso de voladura y el diseño de mallas de perforación en las labores de avance y desarrollo en minería subterránea. En un diseño experimental, el investigador manipula una o más variables independientes para observar sus efectos en las variables dependientes. En este caso, la variable independiente es el diseño y cálculo de las mallas de perforación optimizadas, mientras que las variables dependientes son la sobrerotura, los costos de sostenimiento (en particular el uso de shotcrete), y el tiempo invertido en el proceso de diseño de las mallas.
El objetivo principal de este diseño es determinar si la optimización del diseño de mallas de perforación puede reducir la sobrerotura a un nivel aceptable, a la vez que disminuye los costos asociados al sostenimiento y el tiempo dedicado a la planificación de las perforaciones. Para ello, se realizan intervenciones controladas y sistemáticas, como el análisis de una diferente configuración de malla y la aplicación de tecnologías para automatizar su diseño. Este enfoque experimental permite controlar variables externas y aislar el impacto específico de las mallas optimizadas en los resultados obtenidos, lo cual es esencial para validar las hipótesis planteadas y establecer conclusiones sólidas basadas en evidencias cuantitativas.
3.1.2	Unidad de análisis
La unidad de análisis en la que se centrará el estudio corresponde a la cortada CR NW, ubicada en el nivel 2350 de la Unidad de Producción Santa María de la mina Poderosa. A continuación, se detallarán los aspectos fundamentales necesarios para llevar a cabo su análisis.
3.1.2.1	Ubicación. La unidad que se analiza se localiza en la mina subterránea de Compañía Minera Poderosa, ubicada en el distrito y provincia de Pataz, dentro del departamento de La Libertad, Perú. Esta unidad se encuentra a unos 360km de Trujillo, a una altitud que varía entre los 2050 y 3200 metros sobre el nivel del mar.
La mina cubre un área de 78,674 hectáreas, con 147 concesiones mineras y tres de beneficio. La ubicación está en el flanco noreste de la cordillera de los Andes, dentro del Batolito de Pataz, cerca del río Marañón, sus coordenadas geográficas son 7°45’56.94” S y 77° 34’ 51.27” O.
Figura 26
Foto satelital de la Unidad de Producción Santa María
Nota: fuente Google Earth Pro.
3.1.2.2	Accesibilidad.
El acceso a la unidad de análisis se puede realizar a través de dos rutas principales:
Tabla 15
Ruta vía terrestre
Nota: fuente propia.
Tabla 16
Ruta vía aérea
Nota: fuente propia.
3.1.2.3	Geología.
3.1.2.3.1	Geología regional. Las formaciones rocosas en esta área están vinculadas a la evolución estratigráfica y estructural de la cordillera oriental del norte del Perú, que se compone de tres ciclos geológicos: Precámbrico, Hercínico y Andino.
En el ciclo Precámbrico, se encuentran esquistos y filitas del Complejo Marañón, con una serie volcánica del Cambriano en las capas superiores. El ciclo Hercínico está representado por las secuencias turbidíticas de la formación Contaya, mientras que al comienzo del Carbonífero surge una sedimentación continental conocida como el grupo Ambo. Al final del Paleozoico, una fase epirogénica da lugar al depósito molásico del grupo Mitu, de edad Permo-Triásico. Finalmente, el ciclo Andino se caracteriza por la sedimentación de calizas Pucará del Triásico-Jurásico, seguido de areniscas Goyllarisquizga del Cretácico Inferior, calizas Crisnejas del Cretácico Medio y las capas rojas de la formación Chota del Cretácico Superior.
Este contexto geológico establece las bases para la exploración minera en la región, contribuyendo al entendimiento del potencial aurífero del área.
Figura 27
Columna estratigráfica regional
Nota: fuente compañía minera Poderosa S.A.
3.1.2.3.2	Geología local. La geología del distrito de Pataz se distingue por una clara tendencia estructural hacia el nor-noroeste, definida principalmente por fallas regionales, contactos geológicos y un extenso batolito de Pataz. A continuación, se detallan los principales componentes geológicos presentes en esta región.
Complejo Marañón: Este complejo está conformado mayoritariamente por filitas y esquistos. En los taladros realizados en la zona de Santa Filomena, se ha observado un origen volcánico félsico del esquisto cuarzoso-sericítico, el cual representa el componente predominante del Complejo Marañón en esta área.
Formación Vijus: Esta formación se compone de areniscas volcániclásticas metamorfizadas con predominancia félsica. Los estratos son de poca potencia, con granulometrías que varían entre fina y media. Una de las principales unidades de la formación Vijus está en contacto fallado con el Complejo Marañón al norte del distrito de Pataz, específicamente en la zona conocida como Paraíso. Otra unidad de menor extensión se encuentra al oeste del distrito. Cabe destacar que no se registran afloramientos de la Formación Vijus en el tramo entre el lineamiento este de Tingo y el lineamiento de Cedro, en la parte central del distrito.
Formación Contaya: Compuesta por areniscas, limolitas y lodolitas silicoclásticas metamorfizadas (también conocidas como pizarras), esta formación presenta estratos de mediana a alta potencia. Además, contiene pequeñas proporciones de areniscas volcánicas félsicas. La mayor extensión de la Formación Contaya se encuentra al norte del lineamiento de Paraíso y entre los lineamientos de Tingo y Suyubamba. En las zonas donde entra en contacto con el batolito de Pataz, se observa un metamorfismo de contacto que transforma las rocas meta-sedimentarias en hornfels, con potencias que pueden superar varias decenas de metros.
Formación Atahualpa: Esta nomenclatura corresponde a las rocas volcánicas félsicas que se encuentran sobre la Formación Contaya, en la región norte del lineamiento francés. Estas rocas presentan una apariencia similar a la de la Formación Vijus, lo que sugiere que las rocas volcánicas félsicas podrían representar una repetición de esta última formación.
Formación Lavasen: Esta secuencia, que abarca desde el Mioceno hasta el Plioceno, está constituida por rocas volcánicas de composición félsica e intermedia, depósitos piroclásticos y rocas sedimentarias volcánicas.
Rocas intrusivas: El batolito de Pataz tiene un ancho aún desconocido, con su contacto situado por debajo de la Formación Lavasen. A partir de los afloramientos, se infiere que el batolito se extiende en dirección nor-noroeste a lo largo de una distancia que no supera los 100 km. Su componente principal es la granodiorita de grano medio, aunque también se encuentran proporciones menores de diorita, cuarzo-diorita, tonalita y monzogranito.
Figura 28
Columna estratigráfica local
Nota: fuente compañía minera Poderosa S.A.
Información geomecánica. Los parámetros geomecánicos correspondientes al tipo de roca presente en la cortada de la Unidad de Producción Santa María han sido proporcionados por el área de Geomecánica. A continuación, se presentan los valores obtenidos para las rocas en este lugar de estudio:
Tabla 17
Parámetros geomecánicos en la unidad de análisis
Nota: fuente compañía minera Poderosa S.A.
3.1.2.5	Geometría de la labor. Las labores de desarrollo en la Unidad de Producción Santa María corresponden al tipo D, con variabilidad dependiendo del arco de flecha (fl) que se desee aplicar. Las dimensiones utilizadas para las labores de desarrollo y avance, que son permanentes, oscilan entre 3.5 y 4.5 metros. Sin embargo, la labor en la que se está trabajando presenta dimensiones de 4.5 x 4.5 metros y una gradiente del 0%.
Las cunetas se ejecutan manualmente con herramientas como pico y pala. A continuación, se presenta la geometría de la labor en la figura siguiente.
Figura 29
Representación geométrica de la labor de la unidad de análisis.
Nota: fuente propia.
3.1.2.6	Ciclo de Minado.
3.1.2.6.1	Limpieza. Como primera tarea del día, se lleva a cabo la limpieza de la labor, la cual se realiza después de esperar el tiempo establecido tras la voladura, con el fin de permitir la eliminación de los gases presentes en la zona. Para realizar esta tarea, se utiliza un scooptramp modelo R1600G de 6 yardas cúbicas, marca Ferreyros, tal como se muestra en la figura. Este equipo se encarga de transportar el material hacia un SCAM (Sistema de Carga Automática de Material), para su posterior traslado fuera de la mina.
Figura 30
Scooptramp modelo R1600G de 6 yardas cúbicas
Nota: fuente https://www.ferreyros.com.pe/equipo/cargador-de-bajo-perfil-r1600h/?parent=1879.
3.1.2.6.2	Desquinchado de roca. Una vez finalizada la limpieza de la labor, se procede a verificar que todos los bancos suspendidos en el techo y las paredes estén completamente sueltos y seguros. Para esta tarea, se utiliza un scayler, debido a las dimensiones de la labor. En la unidad de análisis, se empleó un scayler de la marca EPAUS, modelo S8 853, como se ilustra en la imagen siguiente. Este equipo lleva a cabo la tarea en un tiempo promedio de 1 hora.
Figura 31
Scayler de la marca EPAUS, modelo S8 853
Nota: fuente https://mtirental.com.pe/producto/sacaler-paus-s8-853/.
3.1.2.6.3	Sostenimiento. El sostenimiento en la labor se lleva a cabo utilizando el Small Bolter 99 de la marca Resemin, el cual se encarga de realizar un sostenimiento temporal.
Este proceso incluye la instalación de malla electrosoldada junto con pernos de anclaje, lo que garantiza la estabilidad inicial del área. Posteriormente, se proyecta el shotcrete mediante un robot de la marca Putmeister, modelo Wetkret 4, que es alimentado por un mixer de la marca Perkins, modelo Huron 4.
Luego de la proyección, se espera un tiempo aproximado de 22 minutos para permitir el secado adecuado antes de continuar con las demás tareas unitarias. Los equipos mencionados se encuentran ilustrados en las siguientes figuras.
Figura 32
Small Bolter 99 de la marca Resemin
Nota: fuente https://www.resemin.com/index.php?route=product/product&product_id=77.
Figura 33
Robot de la marca Putmeister, modelo Wetkret 4
Nota: fuente https://www.interempresas.net/Mineria/Articulos/228455-Putzmeister-expande-su-gama-de-equipos-para-proyeccion-de-hormigon.html.
Figura 34
Mixer marca Perkins, modelo Huron 4
Nota: fuente http://www.mlorenzana.com/products/mining/mixers/huron-4/8.
3.1.2.6.4	Perforación. Para la tarea unitaria de perforación, se emplea un perforador eléctrico debido a la considerable fuerza que se requiere para trabajar en frentes de gran dimensión. En este caso, se utiliza un Jumbo de la marca Epiroc, modelo Boomer S10D, como se ilustra en la figura. Este equipo es capaz de realizar un taladro de 12 pies aproximadamente cada 3 minutos, optimizando el tiempo de perforación en función de las características del frente de trabajo.
Figura 35
Jumbo de la marca Epiroc, modelo Boomer S10D
Nota: fuente https://www.epiroc.com/es-ar/products/drill-rigs/face-drill-rigs/boomer-s1.
3.1.2.6.5	Voladura. La tarea de voladura se realiza de manera manual. En cuanto a los materiales utilizados, estos provienen del proveedor Famesa. Para los frentes de desarrollo, se emplean como explosivos las emulsiones Emulnor 5000 y 300, mientras que para el contorno se utiliza la emulsión Famecorte E20.
Además, se utiliza cordón detonante de 5 g, mecha rápida de ignición Z-18 y detonadores no eléctricos Fanel y detonador ensamblado. Es importante señalar que no se emplea mecha de seguridad en este proceso. Todos estos elementos están ilustrados en la imagen siguiente.
Figura 36
Accesorios de voladura y explosivos utilizados.
Nota: fuente https://www.famesaexplosivos.com/.
Además, los parámetros relacionados con los explosivos se presentan en las siguientes tablas
Tabla 18
Parámetros de la emulsión emulnor 5000
Nota: fuente https://www.famesaexplosivos.com/producto/emulnor/ (ficha técnica).
Tabla 19
Parámetros de la emulsión Famecorte e20
Nota: fuente https://www.famesaexplosivos.com/producto/famecorte-e-20/ (ficha técnica).
3.1.3	Etapas de la investigación
3.1.3.1	Recolección de datos.  La metodología de recolección de datos en este estudio fue diseñada para obtener información precisa que permitiera calcular la sobrerotura, actualizar precios unitarios de voladura y perforación en la Unidad Minera Santa María y obtener parámetros de calidad de roca y del explosivo a usar que solicita el modelo matemático de Holmberg para optimizar la malla de perforación.
Para calcular la sobrerotura, se llevaron a cabo mediciones en campo en la CR NW del nivel 2350 de la unidad minera, utilizando un distanciómetro. Se tomó como referencia la dirección de la labor, midiendo cada tres metros la distancia desde el centro de la labor hasta los hastiales derecho e izquierdo, y también se registró la altura de la labor. No obstante, se identificó la presencia de un SCAM en la labor, lo que impidió realizar el cálculo de la sobrerotura en esa área específica. Además, la sección inicial de la labor presentaba una forma cónica, motivo por el cual esta zona fue excluida del cálculo. Es importante destacar que este estudio se centró en las mediciones de la sobrerotura en las secciones con dimensiones de 4.5 x 4.5 metros, tal como se muestra en la siguiente figura.
Figura 37
Representación gráfica de la CR NW del nivel 2350
Nota: fuente propia.
En relación con los precios unitarios de perforación, voladura y sostenimiento, estos fueron obtenidos directamente de la Unidad Minera en formato Excel, tal como se detalla en los Anexo (1), (2) y (3), se llevó a cabo una supervisión continua de las actividades, registrando de manera precisa la cantidad de materiales empleados en cada operación. Estos datos fueron anotados en el cuaderno de campo, lo que permitió actualizar los precios unitarios tras la implementación de la malla de perforación optimizada.
Finalmente, para obtener los datos sobre la calidad de la roca, se coordinó con el área de mecánica de rocas, mientras que las especificaciones de los explosivos se obtuvieron a partir de las fichas técnicas disponibles en la página web del distribuidor, todos estos datos se observan en las tablas (17), (18) y (19).
3.1.3.2	Procesamiento de la información. Para el cálculo de la sobrerotura, se desarrolló un software utilizando el IDE Spyder y el lenguaje de programación Python. En este software, los datos fueron almacenados en variables de tipo "lista", lo que permitió una gestión eficiente y organizada de la información, tal como se ilustra en la figura siguiente.
Figura 38
Almacenamiento en listas de datos tomados en campo.
Nota: fuente propia.
Se concatenaron las listas con la misma descripción (izquierda, derecha o altura), mediante el operador “+”, como se muestra en la siguiente figura, con el objetivo de reducir la cantidad de variables necesarias durante el cálculo de la sobrerotura.
Figura 39
Concatenación de listas
Nota: fuente propia.
Dado que la labor planificada tiene dimensiones de 4.5 x 4.5 m, la sección planificada tendrá un área de 20.25 m². A continuación, se procederá a calcular el área de la sección real con ayuda de las listas previamente mencionadas, lo cual permitirá determinar la sobrerotura mediante la aplicación de la ecuación (3).
Para ello, se creará inicialmente una lista vacía denominada "SobreRoturaA2", que almacenará los valores de sobrerotura correspondientes a las secciones de donde se extrajeron los datos. Posteriormente, se definirá un bucle "for" con un iterable "i", el cual tomará los valores desde cero hasta el número total de elementos en la lista "A2Altura", menos uno, gracias al comando “range(len(A2Altura))”. Dentro de este bucle, se ejecutará la fórmula correspondiente para calcular la sobrerotura, y el resultado se almacenará en la variable "SRA2". Finalmente, los valores calculados de "SRA2" se agregarán a la lista "SobreRoturaA2" utilizando el método "append", como se ilustra en la figura siguiente.
Figura 40
Código para cálculo de sobrerotura
Nota: fuente propia.
Posteriormente, para obtener los datos estadísticos, utilizaremos la biblioteca NumPy, que nos permitirá realizar los cálculos necesarios de manera eficiente. Los códigos para obtener estos resultados se presentan en la siguiente imagen.
Figura 41
Código para obtención de parámetros estadísticos
Nota: fuente propia.
En relación con los precios unitarios, se procederá a actualizar el precio unitario de perforación modificando el número de taladros a utilizar. Para el precio unitario de voladura, se ajustará la cantidad de agentes de voladura necesarios. En cuanto al precio unitario de sostenimiento, este se mantendrá sin cambios, ya que la tarea a realizar no sufrirá alteraciones. Una vez actualizados los precios unitarios, se llevará a cabo un análisis de costos, en el que se sumarán los precios unitarios multiplicados por su respectivo factor de uso: en el caso de perforación, el factor será de 1 disparo; para voladura, el factor también corresponderá a un disparo, mientras que, en el caso de sostenimiento, el factor estará determinado por el volumen de shotcrete lanzado en metros cúbicos.
Finalmente, los parámetros relacionados con la calidad de la roca y las especificaciones de los explosivos utilizados serán incorporados al software, lo que permitirá obtener la malla de perforación optimizada mediante el método de Holmberg.
3.1.3.3	Análisis de la información.
3.1.3.3.1	Estado preliminar. En la Unidad de Producción Santa María, el estándar de sobrerotura para las labores de desarrollo debe ser, como máximo, del 10%. Sin embargo, al analizar los datos, se observó una sobrerotura promedio del 34.6%, como se muestra en la siguiente imagen. Estos resultados evidencian una ineficiente utilización de los recursos, lo que indica la necesidad de revisar y optimizar los procesos para mejorar estos resultados.
Figura 42
Gráfica que representa la sobrerotura en la etapa preliminar
Nota: fuente propia.
La sobrerotura conlleva una serie de problemas, siendo el principal el uso excesivo de shotcrete en las labores mineras, lo cual incrementa considerablemente el costo de la creación de la labor.
Entonces, al tener una sobrerotura del 34.6%, obtenemos una longitud real promedio de 5.22m, sustituyendo los valores en la ecuación (1), tal como se muestra en la siguiente expresión.
Y con un avance promedio de disparo de 2.95 m, podemos calcular la cantidad de shotcrete necesaria utilizando la ecuación (2).
Dado que el precio unitario del shotcrete es de 516.58 USD/m³ lanzado tal como se muestra en el Anexo (3), se estaría incurriendo en un costo excesivo de 1,952.54 USD por cada disparo. Al sumarle los demás costos asociados, se vuelve insostenible la construcción de la labor de desarrollo.
Este elevado gasto resalta la necesidad de revisar el diseño de la malla de perforación, el cual, en el campo, se identificó como inadecuado, ya que no cumplía con los estándares establecidos. El maestro de obra realizaba el diseño según su propio criterio, como se puede observar en la siguiente figura.
Figura 43
Malla utilizada en la etapa preliminar
Nota: fuente propia.
En esta malla se lograron identificar los parámetros de perforación y voladura, los cuales están detallados en las siguientes tablas.
Tabla 20
Parámetros de interés en la actividad unitaria de perforación en la etapa preliminar
Nota: fuente propia.
Tabla 21
Parámetros de interés en la actividad unitaria de voladura en la etapa preliminar
Nota: fuente propia.
3.1.3.3.2	Elaboración del software de automatización de cálculo y diseño de malla de perforación para voladura de precorte en Python. Debido a la complejidad en el cálculo de mallas de perforación optimizadas, es fundamental utilizar herramientas tecnológicas que optimicen este proceso, minimicen errores en los cálculos y mejoren los resultados operativos. Por esta razón, se optó por desarrollar un software para el diseño y cálculo de mallas de perforación optimizada para voladura de precorte, basado en el modelo matemático de Holmberg, debido al alto índice de sobrerotura que presenta la labor.
Para el desarrollo de este software, se optó por utilizar el IDE Spyder y el lenguaje de programación Python. Se emplearon diversas bibliotecas para facilitar los cálculos y la visualización de datos: "math" para realizar cálculos matemáticos básicos, "numpy" para operaciones matemáticas avanzadas, "pandas" para organizar y presentar los resultados en tablas, y "matplotlib" para graficar la malla de perforación. Estas bibliotecas se activan mediante el comando “import”, como se muestra en la siguiente figura.
Figura 44
Código para importar bibliotecas
Nota: fuente propia.
Para iniciar con el diseño y cálculo de la malla de perforación, es crucial comprender la geometría de la labor a realizar. En este caso, se emplea un diseño de tipo D, para ello iniciaremos solicitando al usuario los datos geométricos del ancho y alto de la labor, así como la flecha de arco mediante el comando "input". Sin embargo, este último valor no puede ser mayor que la mitad del ancho de la labor ni menor o igual a cero. Para garantizar que se ingrese un valor válido, utilizamos un bucle "while" controlado por una variable indexada, "a", que inicialmente toma el valor cero. Dentro del bucle, se solicita al usuario que ingrese el valor de la flecha de arco, que se almacena en la variable "fl". Luego, "a" pasa por un comando condicional que evalúa si el valor ingresado está dentro del rango permitido. Si el valor no es válido, el flujo pasa al comando "else", que muestra un mensaje indicando que el valor debe estar dentro del intervalo especificado. El bucle se repetirá hasta que se ingrese un valor válido, momento en el cual la variable indexada "a" pasará por el comando "break", terminando el bucle tal como se muestra en la siguiente imagen.
Figura 45
Código para solicitar datos geométricos de la labor
Nota: fuente propia.
Para calcular el número de taladros vacíos de alivio que deben ubicarse en el centro de la malla, se solicita al usuario, mediante el comando "input", la longitud de la barra de perforación en pies, la cual ya ha sido multiplicada por su factor de convergencia. Este valor se almacena en la variable "LT", como se muestra en la imagen siguiente.
Figura 46
Código para solicitar el largo del taladro con el que se desee trabajar
Nota: fuente propia.
Es importante destacar que la longitud del taladro no representa el avance real que se logrará en la voladura. Este valor debe ajustarse teniendo en cuenta la eficiencia de perforación de 0.85 y el factor de avance de 0.95 propuesto por Holmberg los cuales están representados por las variables “Hp” e “I” respectivamente, como se ilustra en la imagen siguiente.
Figura 47
Código de ajuste de avance
Nota: fuente propia.
Según la ecuación (3), Holmberg propone que el avance depende del diámetro del taladro vacío. Si se requiere un avance mayor y no se dispone taladros con diámetros más grandes, se puede utilizar la ecuación (5) para obtener un taladro vacío de diámetro equivalente. Para implementar este cálculo, se desarrolló un bucle animado con dos secciones: una principal y una subsección, utilizando comandos “while”.
En la primera sección, el bucle se controla con la variable de indexación "i" que toma un valor precedente igual a 1. Este bucle tiene como objetivo obtener información del usuario mediante el comando "input", preguntando si dispone de una broca rimadora. La respuesta se almacena en la variable "z". El iterador "i" pasa por los comandos condicionales donde se evalúa la respuesta y se verificar si cumple con alguna de las opciones válidas. Si la respuesta no es válida, el flujo pasa al comando "else", el cual muestra un mensaje indicándole al usuario que ingrese una respuesta valida. Este proceso se repite hasta que el usuario proporcione una respuesta correcta, momento en el cual la variable de indexación “i” podrá acceder a uno de los comandos condicionales donde se le solicitara datos de las dimensiones de sus brocas según la respuesta que almacenó en la variable “z”.
Una vez ingresados los datos de la broca, se inicia la subsección del bucle animado, utilizando el bucle "while", controlado por la variable de indexación "n", que comienza con un valor inicial de 1. Este bucle interrumpe la ejecución del bucle principal, controlado por la variable "i", hasta que el nuevo bucle interno termine su proceso. Antes de iniciar el bucle, se define la variable "H" con un valor inicial de cero, lo cual es necesario para que la variable "n" pueda acceder al comando condicional.
Dentro del bucle, la variable indexada "n" ejecuta un único comando condicional que calcula el valor de la variable "Dv", el diámetro de taladro equivalente. Este valor depende de "n", que representa el número de taladros vacíos. El valor calculado de "Dv" se reemplaza en la siguiente ecuación, lo que genera un nuevo valor para "H". Al mismo tiempo, la variable "n" se incrementa en 1. El bucle continuará repitiéndose hasta que se encuentre un valor de "n" que haga que "H" sea mayor que "I". En ese punto, el flujo se redirige al comando "else", donde se resta 1 al valor de "n", ya que la última operación fue incrementarle uno, posteriormente el programa imprime el número de taladros vacíos necesarios, representada por la variable indexada “n”, mediante el comando "print". A continuación, el flujo pasa al comando "break", que finaliza el bucle controlado por "n" y permite que el bucle controlado por "i" continúe.
Dado que "i" ya ha pasado por un comando condicional, su flujo omite el resto de las condiciones y salta directamente al siguiente "break", lo que culmina el bucle animado. Tal como se presenta en la siguiente imagen.
Figura 48
Código para obtener el numero de taladros vacíos
Nota: fuente propia.
Antes de proceder con el arranque de las cuatro secciones, de acuerdo con el modelo de Holmberg, se requiere la recopilación de datos sobre la calidad de la roca para garantizar la correcta aplicación de sus ecuaciones sin inconvenientes. Para ello, se empleará el comando "input", que permitirá la introducción de los valores necesarios de manera interactiva, tal como se ilustra en la figura siguiente.
Figura 49
Código de solicitud de parámetros de la roca
Nota: fuente propia.
En cuanto a la constante de roca sueca, se debe calcular primero el consumo específico del explosivo utilizando la siguiente ecuación
(43)
Donde:
: Densidad de la roca
Para luego calcular la constante de roca sueca mediante la siguiente ecuación
(44)
Donde
: Consumo especifico de explosivo
Este cálculo se automatiza en el software tal como se presenta en la siguiente imagen. En este contexto, la variable "Ce" representa el consumo específico del explosivo, mientras que "C" a la constante de roca sueca.
Figura 50
Código para el cálculo de la constante de roca sueca
Nota: fuente propia.
Para iniciar el proceso del cálculo de arranque por cuatro secciones, es importante recordar que el método de Holmberg no se aplica para desviación de perforación mayores al 2%, para cual si la desviación es mayor a 1% lo óptimo para que la voladura salga con una buena fragmentación y no se presenten voladuras plásticas o sinterizadas se deben cumplir  y para menores a 1% pero mayores a 0.5% la condición más optima es la que se presenta en la ecuación (6).
Para representar ello en Python, se creó un bucle while con una variable de indexación “i” cuyo valor inicial es cero, en primer lugar se le solicita al usuario que coloque el porcentaje de desviación de perforación con el que trabajara, que puede ir de 0.5 a 2 %, en donde se abren dos comandos condicionales dependiendo en que intervalo se encuentra la respuesta, si esta no se encuentra en ningún rango de los condicionales, la variable indexada pasara al comando “else” el cual con el comando “print” le indicará al usuario que coloque una desviación válida, entonces la variable “i” volverá a correr el bucle hasta que coloque un porcentaje valido, una vez colocado se solicitara mediante el comando “input” la desviación angular y el error de emboquille para que la variable “F”, que representa el error de perforación en la ecuación (7), tome valor junto al burden teórico ideal representado por la variable “BT10”, posterior a esto se encuentra una sentencia “break” el cual termina el bucle while, tal como se muestra en la siguiente figura.
Figura 51
Código para calcular el burden ideal, según Holmberg
Nota: fuente propia.
Una vez determinado el burden teórico, se procede a calcular la concentración mínima de carga lineal que debe tener nuestro explosivo, lo cual asegura una cara libre adecuada para las detonaciones subsecuentes.
Dado que resulta difícil encontrar un explosivo en el mercado presente un valor igual de concentración de carga lineal a la mínima requerida para el burden ideal, el proceso a seguir consiste en verificar inicialmente que la concentración del explosivo disponible en el mercado sea superior a la mínima establecida para asegurar el arranque. La concentración de carga lineal del explosivo de mercado se calcula mediante la siguiente ecuación.
(45)
Después, se procederá a calcular el burden teórico específico para el primer cuadrante, resolviendo la ecuación de quinto grado obtenida al despejar la variable del burden en la ecuación de concentración de carga lineal. Este paso puede llevarse a cabo de manera eficiente utilizando la biblioteca NumPy en Python.
Una vez obtenido el burden teórico, se procederá a calcular los valores de los parámetros necesarios de los cuadrantes. No sin antes tener en cuenta la restricción de carga lineal máxima, que establece que la carga lineal del explosivo debe ser inferior al valor calculado en el segundo cuadrante mediante la siguiente ecuación:
(46)
Todo este proceso se codifica mediante un bucle animado que consta de una sección principal y dos subsecciones. La sección principal, que utiliza un bucle while con la variable de indexación “m” iniciada en 1, se emplea para verificar que no se exceda la concentración de carga lineal máxima, lo cual se explicará más adelante. La variable indexada “m” interactúa con una subsección que también contiene un bucle while con la variable de indexación “i”, iniciada en 1. Esta subsección bloquea la sección principal e inicia un proceso donde se evalúa, mediante un comando condicional, si el diámetro “D1” del taladro de producción previamente solicitado es menor o igual a 31.8mm. Si no es así, se pasa al bloque “else”.
En ambos bloques (if y else), se solicitarán los parámetros del explosivo mediante el comando “input". En el bloque “if”, se calcula la concentración de carga lineal mínima necesaria mediante la siguiente ecuación.
(47)
En el bloque “else”, se utilizará la ecuación (9), cuyos resultados se almacenarán en la variable “q10”. Luego, se calculará la concentración de carga lineal del explosivo de mercado utilizando la ecuación (45), y el resultado se guardará en la variable “q1”. Posteriormente, se evaluará, mediante un comando condicional, si la concentración lineal del explosivo de mercado es mayor que la concentración mínima requerida. Si es así, se imprimirá un mensaje con el comando “print”, indicando que el explosivo tiene una concentración de carga lineal superior a la mínima. En este caso, se ejecutará el comando “break” para finalizar la subsección del bucle while de la variable indexada “i”.
Si la concentración del explosivo no cumple con el requisito mínimo, se pasará al bloque “else”, donde se imprimirá un mensaje de error con el comando “print”, informando al usuario sobre el problema. Esto permitirá que el bucle se repita, dando la oportunidad al usuario de intentar con otro explosivo hasta que se logre cumplir con la concentración mínima de carga lineal exigida, tal como se muestra en la siguiente imagen.
Figura 52
Código para corroborar que la concentración e carga lineal sea mayor al mínimo
Nota: fuente propia.
Al culminar la subsección, la variable de indexación "m" retoma su flujo y pasa por un comando condicional que, de manera similar a lo explicado previamente, separa las acciones según el valor del diámetro “D1”. En primer lugar, se define una lista con los coeficientes de la ecuación obtenida al despejar el burden en las ecuaciones (47) y (9). Posteriormente, se crea una función llamada "resolver_ecuación" utilizando la palabra clave “def”, a la que se le pasa como argumento la lista "Coeficientes". Dentro de esta función, se obtiene las soluciones de la ecuación mediante el comando “np.roots” de la biblioteca NumPy, el cual devuelve una lista denominada "soluciones" que contiene todas las raíces de la ecuación, tanto reales como complejas. Para obtener únicamente las soluciones reales y positivas, se utiliza una compresión de lista que recorre la lista "soluciones". La condición de la compresión es que la parte imaginaria de la solución sea cero, lo cual se verifica utilizando “np.isreal”, y que la parte real de la solución sea mayor que cero, mediante “sol.real > 0”. Aquellas soluciones que cumplen ambas condiciones se extrae su parte real utilizando “sol.real”. y se almacenan en la lista "soluciones_reales_positivas". Finalmente, la lista de soluciones reales positivas se imprime en el terminal mediante el comando “return”.
Además, se define una función denominada "encontrar_valor_mas_cercano" mediante la palabra clave “def”, la cual toma como argumentos una lista de números y un número objetivo. Dentro de esta función, se utiliza la función “min()”, que devuelve el valor mínimo de un iterable, en este caso, de la lista proporcionada. Sin embargo, el objetivo no es encontrar el valor más pequeño en términos de magnitud, sino el valor más cercano al número dado.
Para lograr esto, se hace uso del parámetro “key” de la función “min()”, que permite especificar una función personalizada que definirá cómo comparar los elementos de la lista. Esta función personalizada es una función anónima (lambda), lambda x: abs (x - numero), que toma un valor x de la lista y calcula la distancia entre x y el número objetivo (numero). La distancia se calcula utilizando abs(x - numero), que devuelve el valor absoluto de la diferencia entre ambos números. De esta manera, se obtiene la distancia entre x y numero, sin considerar si la diferencia es positiva o negativa, garantizando que siempre se calcule la magnitud de la diferencia.
A continuación, se crea la lista “BT1_soluciones”, la cual se asigna al resultado de la función "resolver_ecuación", pasando como argumento la lista “Coeficientes” previamente definida. Posteriormente, se genera la “lista BT1_solucion”, que se obtiene mediante la llamada a la función "encontrar_valor_mas_cercano", utilizando como argumentos la “lista BT1_soluciones” y el valor “BT10”. De este modo, se obtiene el valor más cercano a “BT10” dentro de la lista de soluciones. Finalmente, el valor calculado se asigna a la variable “BT1”, tomando como valor el resultado almacenado en “BT1_solucion”, tal como se ilustra en la figura.
Figura 53
Código para obtener el burden especifico del explosivo del mercado
Nota: fuente propia.
Una vez obtenido el valor del burden teórico para el explosivo del mercado seleccionado, se procede al cálculo del burden práctico utilizando la ecuación (8), y el resultado se almacena en la variable “BP1”. A continuación, se calcula la apertura del primer cuadrante mediante la ecuación (11), y su valor se guarda en la variable “A1”. Seguidamente, se determina el taco aplicando la ecuación (18), y el valor resultante se almacena en la variable “T1”. De igual manera, se calcula la longitud de carga en el primer cuadrante y el resultado se almacena en la variable “L1”. Además, se obtiene el número de cartuchos del explosivo a utilizar, mediante la ecuación (19), y se guarda en la variable “N1”.
Todos estos valores calculados se almacenarán en listas, en donde se irán agregando los datos de los siguientes cuadrantes.
Cabe señalar que, en la lista de aperturas “Lista_A”, se añade un valor inicial de cero debido al método de obtención de las aperturas en los siguientes cuadrantes, lo cual se explicará más adelante.
Todos estos cálculos y sus correspondientes valores se ilustran en la siguiente figura.
Figura 54
Código para obtener los parámetros del primer cuadrante
Nota: fuente propia.
Para los cuadrantes restantes, se inicia la segunda subsección, la cual contiene un bucle “while” con la variable de indexación “i”, cuyo valor inicial será cero.
Además, se define la variable “BP”, que tomará el valor de “BP1”, y se crea una lista vacía “lista_q2”.
También se define la variable “Ah”, la cual tendrá el mismo valor que la apertura “A1” del primer cuadrante. Este bucle, controlado por “i”, interrumpe el flujo de la variable “m”.
En primer lugar, se calcularán los valores de las aperturas dejadas de los siguientes cuadrantes, que se almacenan en la variable “Ak”. El valor de “Ak” será igual al burden práctico más los valores de la lista “Lista_A” según la iteración de “i”. Cabe recordar que el primer valor de esta lista es 0, como se explicó previamente. Siguiendo el modelo de Holmberg, se resta el error de perforación a este valor y se multiplica por la raíz cuadrada del mismo. Posteriormente, se utiliza la ecuación (10) para calcular el burden teórico, y el valor obtenido se almacenará en la variable “BT”. De igual manera, se calculará el burden práctico, identificado con la variable “BP”, utilizando la ecuación (8).
Luego, se procederá al cálculo del nuevo valor de la apertura en el cuadrante mediante la ecuación representada en el software y su valor se almacenará en la variable “Ah”. También se calculará el taco utilizando la ecuación (18), y el resultado se guardará en la variable “T2”. Además, se calculará la longitud de carga en el segundo cuadrante como se realizó previamente y el resultado se almacenará en la variable “LC2”. Finalmente, se determinará el número de cartuchos requeridos, calculado a partir de la ecuación (19), y el valor obtenido se almacenará en la variable “N2”.
Una vez calculados estos parámetros, el flujo de la variable de indexación “i” continuará con el cálculo de la concentración máxima que debe tener el explosivo en cada cuadrante, según la ecuación (46), para evitar voladuras plásticas. Este valor se almacenará en la variable “q2”, y se añadirá a la lista “Lista_q2” mediante el comando “append”().
Según el modelo de Holmberg, el número de cuadrantes que se pueden obtener está limitado por la condición de que la apertura no puede ser mayor que la raíz cuadrada del avance. Por lo tanto, se implementa un comando condicional que verifica esta condición.
Mientras la condición de Holdmerg se cumpla, los datos se seguirán añadiendo a las listas previamente creadas y el bucle continuará con la variable indexada “i”, incrementando su valor en cada iteración.
Cuando la condición de Holmberg ya no se cumpla, se ejecutará el bloque “else”, en el cual se elimina el primer valor (0) de la lista “Lista_A” utilizando el comando “pop()”, ya que este valor se añadió inicialmente solo para poder calcular la primera apertura dejada por el primer cuadrante. Después de esto, la variable indexada “i” saldrá del bucle con el comando “break”, y de esta manera se culmina la segunda subsección. El flujo de la variable “m” continuará a partir de este punto.
Figura 55
Código para obtener los parámetros de los cuadrantes restantes
Nota: fuente propia.
Como se mencionó en la sección principal, la variable de indexación “m” se utiliza para asegurar que la concentración de carga lineal del explosivo no supere el valor máximo permitido, con el fin de evitar voladuras plásticas. Por ello, “m” pasa por un comando condicional que valida la correcta inscripción del explosivo. En el bloque “if”, se verifica si la concentración de carga lineal es mayor que el valor máximo permitido. Si esta condición se cumple, el comando “print” muestra un mensaje indicando que la concentración de carga lineal es excesiva, y el bucle animado se repite para permitir que el usuario ajuste los parámetros del explosivo y realice un nuevo intento.
Si la concentración de carga lineal está dentro de los límites permitidos, el flujo del programa avanza al bloque “else”, donde se ejecuta un comando “break”, finalizando así el bucle animado. Posteriormente, se imprime el rango en el cual se encuentra la concentración de carga lineal del explosivo seleccionado. Además, se indica la cantidad de cuadrantes que se han generado en el proceso, tal como se muestra en la siguiente figura.
Figura 56
Código parea corroborar que la concentración de carga lineal del explosivo no sea mayor al máximo
Nota: fuente propia.
Una vez definidas las cuatro secciones de arranque, se procede a automatizar los taladros de arrastre. El primer paso consiste en calcular el burden teórico para lo cual es necesario definir ciertos parámetros previos. En primer lugar, se establece el factor de fijación, representado por la variable "f", con un valor de 1.45. Además, se define la relación de espaciamiento y burden, indicada por la variable "rela_esp_burd", que tiene un valor de 1. También se debe considerar la constante de roca corregida, cuyo valor depende del último burden práctico del arranque, es decir, el correspondiente a la cuarta sección.
Para calcular la constante de roca corregida, se implementa un comando condicional. La condición consiste en que el último valor de la lista que almacena los burden prácticos del arranque, representado por la variable "List_BP[-1]", debe ser mayor o igual a 1.4. Si esta condición se cumple, la constante de roca corregida se ajusta sumando 0.05 a la constante de roca sueca, representada previamente con la variable “C”. En caso contrario, en el bloque "else", la constante de roca corregida se determina sumando a la constante de roca sueca “C” la relación de 0.07 y el último burden práctico del arranque.
Con la constante de roca corregida ya definida, se procede a calcular el burden teórico de los arrastres mediante la ecuación (20), el cual se almacena en la variable "BTA". No obstante, es importante tener en cuenta la restricción de Gustafsson, que establece que el burden teórico de los arrastres no debe superar los seis décimos del avance. Para ello, se implementa un comando condicional que verifica si el valor obtenido para el burden teórico es mayor que los seis décimos del avance. En caso afirmativo, el valor del burden teórico se ajusta y toma el valor de seis décimos del avance, tal como se indica en la figura correspondiente.
Figura 57
Código para calcular el burden teórico de los taladros de arrastre
Nota: fuente propia.
Posteriormente, se solicita al usuario, mediante el comando "input", el ángulo de realce con el objetivo de calcular el número de taladros de arrastre teórico, el cual se determina utilizando la ecuación (21) y se representa mediante la variable "NTA". A continuación, se calcula el espaciamiento teórico mediante la siguiente ecuación.
(45)
El cual se denota por la variable "STA". Seguidamente, se calcula el espaciamiento práctico, el cual se obtiene a través de la ecuación (22) y se representa por la variable "SPA". De manera similar, se calcula el burden práctico mediante la ecuación (23), representado por la variable "BPA".
En cuanto al taladro, se considera que presenta una carga en el fondo diferente a la carga de columna. La longitud de carga de fondo se calcula utilizando la ecuación (26), y se denota por la variable "HFA". Además, la concentración de carga lineal en el fondo, representada por la variable "qfa", será igual a la carga en el arranque, de acuerdo con la ecuación (25). El número de cartuchos utilizados en el fondo se determina mediante la ecuación (27), y la variable asociada es "NFA".
Para la columna, se calcula la altura de carga de columna utilizando la ecuación (29), y se representa por la variable "HCA". La concentración de carga lineal en la columna se obtiene mediante la ecuación (28) y se denota por la variable "qca". El número de cartuchos utilizados en la columna se calcula utilizando la ecuación (30), y la variable correspondiente es "NCA". Finalmente, el valor del taco es el mismo que el utilizado en el arranque y se representa mediante la variable "TA", tal como se muestra en la figura siguiente.
Figura 58
Código para obtener los parámetros de los taladros de arrastre
Nota: fuente propia.
Con respecto al contorno, este se dividirá en dos partes: la corona y los hastiales, lo cual facilitará su representación gráfica en el software. En cuanto a la corona, en una voladura de precorte, es fundamental utilizar un explosivo de menor potencia, dado que la presión de taladro efectiva debe ser inferior al esfuerzo de compresión de la roca para evitar dañar la roca circundante y reducir la sobrerotura.
Para ello, se implementará un bucle "while" con una variable de indexación denominada "i", que tendrá un valor inicial de cero. Este bucle comienza solicitando al usuario los datos del explosivo a través del comando "input". Luego, se calcula la presión del taladro utilizando la ecuación (31), la cual se representa mediante la variable "Pt". De igual manera, se calcula la presión de taladro efectiva mediante la ecuación (32), representada por la variable "Pte". A continuación, se calcula la concentración de carga mínima según Holdmerg utilizando la ecuación (33), la cual se denota por la variable "qc". Finalmente, se calcula la concentración lineal del explosivo con la ecuación (34), representada por la variable "qce". Estos cuatro parámetros son cruciales, ya que la presión de taladro efectiva no debe superar el esfuerzo de compresión de la roca y la concentración de carga lineal del explosivo debe ser mayor que la concentración mínima para asegurar la formación adecuada del plano de corte.
Posteriormente la variable de indexación "i" pasa por un comando condicional que verifica estas dos condiciones. Si ambas se cumplen, se imprime un mensaje positivo y el bucle finaliza con la palabra clave "break". En caso contrario, el flujo pasa al bloque "else", donde se imprime un mensaje de error, y el bucle se repite hasta que el usuario proporcione un explosivo válido que cumpla con las condiciones requeridas, tal como se muestra en la siguiente figura.
Figura 59
Código para corroborar la buena elección del explosivo de contorno
Nota: fuente propia.
Posteriormente, se calcula el espaciamiento de los taladros en la corona utilizando la ecuación (35), representada por la variable "SC". De igual manera, se determina el burden teórico mediante la ecuación (36), que se representa con la variable "BTC". A continuación, se calcula el burden práctico utilizando la ecuación (37), el cual se representa mediante la variable "BPC". Con respecto al taco, este tendrá el mismo valor que en el arranque y estará representado por la variable "TC".
En cuanto a la altura de la columna, esta se determinará a través de la ecuación (39), representada por la variable "LCC". Para calcular el número de taladros a utilizar, primero es necesario calcular la longitud de arco con la cual se desea trabajar. Esta longitud se obtiene mediante la ecuación (40) y se denota por la variable "long_arc". Con esta información, se procede a calcular el número de taladros necesarios utilizando la ecuación (41), y el resultado se representa mediante la variable "NTC". Finalmente, se calcula el número de cartuchos por taladro mediante la ecuación (42), que se representa por la variable "NCC", tal como se demuestra en la siguiente figura
Figura 60
Código para obtener los parámetros de sección de contorno
Nota: fuente propia.
Para los hastiales, se asignarán los mismos valores obtenidos para la corona, con la excepción del número de taladros. Para determinar cuántos taladros deben colocarse en cada lado, primero es necesario conocer la longitud disponible, la cual se calcula mediante la siguiente ecuación:
(46)
Esta longitud se denota como “Long_disponible_H”. Con esta información, se procederá al cálculo del número de taladros requeridos, el cual se representa mediante la variable NTH. Todo lo resaltado se representa en la siguiente imagen.
Figura 61
Código para obtener los parámetros de los taladros de los hastiales
Nota: fuente propia.
Los taladros de tajeo no serán incluidos, ya que no están parametrizados y no cuentan con una definición clara respecto a su ubicación y cantidad, en función de las dimensiones de las labores.
A continuación, se procede a automatizar la generación de la gráfica de la malla de perforación, comenzando por dibujar la estructura de la labor, la cual tiene un diseño tipo "D".
En primer lugar, para dibujar la línea base, se utiliza “ax1.plot([0, Ancho], [0, 0], color='black', linewidth=0.5)”, lo que genera una línea horizontal que va desde el punto (0, 0) hasta el punto (Ancho, 0), con un color negro y un grosor de línea de 0.5. Luego, para crear las líneas laterales, se emplean dos comandos “plot() adicionales: ax1.plot([0, 0], [0, Altura-fl], color='black', linewidth=0.5)” y “ax1.plot([Ancho, Ancho], [0, Altura-fl], color='black', linewidth=0.5)”, que dibujan las líneas verticales en los extremos izquierdo y derecho de la figura, desde la base hasta una altura determinada por “Altura-fl”, con el mismo color negro y grosor. Finalmente, se calcula y dibuja el arco de la corona utilizando funciones trigonométricas. Primero, se calcula el centro del arco con la fórmula “centro = (Ancho/2, Altura-(((Ancho**2)+(4*fl**2))/(8*fl)))” y el radio con “radio = (((Ancho**2)+(4*fl**2))/(8*fl))”. Después, se determinan los ángulos de inicio y fin con las expresiones “theta_inicio = (np.pi/2)-np.arcsin((4*Ancho*fl)/((Ancho**2)+(4*fl**2)))” y “theta_fin = (np.pi/2)+np.arcsin((4*Ancho*fl)/((Ancho**2)+(4*fl**2)))”. Con estos parámetros, se generan 100 puntos de la curva mediante “np.linspace()” y luego se calcula la posición de cada punto del arco con las fórmulas “x = centro[0] + radio * np.cos(theta)” y “y = centro[1] + radio * np.sin(theta)”. Finalmente, se dibuja el arco en la gráfica con “ax1.plot(x, y, color='black', linewidth=0.5)”, generando una línea curva que representa la corona, tal como se presenta en la siguiente figura.
Figura 62
Código para graficar la estructura inicial de la labor
Nota: fuente propia.
Para los taladros en la corona. Primero, se genera un rango de ángulos utilizando “np.linspace()”, que va desde el ángulo inicial hasta el ángulo final. Estos ángulos se calculan usando una fórmula basada en la geometría del arco de la corona, utilizando el valor del ancho (Ancho) y la longitud de la flecha (fl). Los ángulos se obtienen mediante la función “np.arcsin()”, la cual se emplea para determinar los límites del arco en función de los parámetros geométricos. El número de taladros en la corona se define por “NTC”, y estos ángulos son distribuidos equidistantemente entre el inicio y el final del arco.
Una vez que se tienen los ángulos, se calculan las coordenadas “x” e “y” de cada taladro en la corona utilizando las ecuaciones paramétricas de un círculo, con el centro (centro) y el radio previamente calculado. El valor de “x_corona” se calcula sumando el centro en “x” y multiplicando el radio por el coseno de cada ángulo, mientras que el valor de “y_corona” se obtiene sumando el centro en “y” y multiplicando el radio por el seno de cada ángulo.
Finalmente, se utiliza la función “plt.scatter()” para trazar los puntos de los taladros sobre la gráfica. Cada taladro se representa como un círculo de color naranja con borde negro, y el tamaño de cada círculo se define con el parámetro “s=50”, tal como se muestra en la siguiente figura.
Figura 63
Código para dibujar los taladros en la corona
Nota: fuente propia.
Procediendo con los taladros de arrastre. En primer lugar, se representan los taladros ubicados en las esquinas, que están en las posiciones (0, 0) y (Ancho, 0) en el plano de la gráfica. Estos taladros se dibujan utilizando la función “plt.scatter()” y se les asigna un color de relleno rojo (facecolors='red') y borde negro (edgecolors='black') con un tamaño de “s=50”, lo que crea dos puntos representando los taladros de esquina en la base de la estructura.
Luego, se dibujan los taladros intermedios, que están distribuidos entre las esquinas de la base. Para ello, se genera un rango de posiciones “x_arrastre” mediante la función “np.linspace()”, que crea un conjunto de puntos equidistantes entre “SPA” (espaciado del taladro de arrastre) y (Ancho-SPA), y la cantidad total de puntos generados es “NTA-2”, ya que se excluyen los taladros en las esquinas. Esto da como resultado una lista de posiciones “x” para los taladros intermedios.
Luego, se define una lista vacía “y_arrastre”, en la cual se añaden las coordenadas y para cada uno de los taladros. En este caso, dado que todos los taladros de arrastre se encuentran en la base, el valor de y se establece en 0 para todos ellos. Después de calcular las coordenadas y, se convierte la lista “y_arrastre” en una tupla para asegurar su formato correcto. Finalmente, los taladros intermedios se grafican usando “plt.scatter()” al igual que los de esquina, con color rojo y borde negro, y un tamaño de “s=50”.
Figura 64
Código para graficar los taladros de arrastre
Nota: fuente propia.
Para generar los puntos correspondientes a los taladros en los hastiales (los lados de la estructura). Primero se calculan los taladros en el hastial derecho. Se crea una lista vacía “x_Hastial” y luego se calcula un conjunto de posiciones “y_Hastial” mediante la función “np.linspace()”, que distribuye de manera equidistante los taladros en el eje vertical. Este conjunto de puntos va desde el valor de “BPA” (el espaciamiento del taladro de arrastre) hasta (Altura-fl), lo que establece el rango en el que se dibujarán los taladros en el lado derecho de la estructura. El parámetro (“NTH”-1) determina el número de puntos generados, restando 1 para excluir el primer valor (ya que el primer taladro está en la base).
Luego, se itera sobre los valores de “y_Hastial” y se asigna a cada valor de “y” un valor constante de (x_values = 0), ya que los taladros en el hastial derecho se ubican en el extremo izquierdo de la estructura, es decir, en la coordenada (x = 0). Estos puntos de coordenadas (x_values, y) se añaden a la lista “x_Hastial”. Después, esta lista se convierte en una tupla para asegurar que sea un formato adecuado para su uso en la gráfica.
Los taladros del hastial derecho se dibujan en el gráfico utilizando la función “plt.scatter()”, con color de relleno anaranjado (facecolors='orange'), borde negro (edgecolors='black') y un tamaño de s=50, lo que genera los puntos en las posiciones correspondientes a los taladros del lado derecho de la estructura.
A continuación, se repite el mismo proceso para los taladros en el hastial izquierdo. Se calcula nuevamente el conjunto de posiciones “y_Hastial” mediante “np.linspace()”, de modo que los taladros estén igualmente distribuidos en el eje vertical. Sin embargo, en este caso, se asigna a cada valor de y un valor constante de (x_values = Ancho), ya que los taladros del hastial izquierdo se encuentran en el borde derecho de la estructura. Al igual que en el caso anterior, se añaden las coordenadas (x_values, y) a la lista “x_Hastial”, que luego se convierte en una tupla.
Finalmente, se dibujan los taladros en el hastial izquierdo utilizando “plt.scatter()”, con las mismas características de color y tamaño que los taladros en el hastial derecho.
Figura 65
Código para graficar los taladros de los hastiales
Nota: fuente propia.
Para los puntos correspondientes a los cuadradores de la malla de perforación. Utiliza un bucle for para iterar sobre los elementos de la lista “List_A”. Para los índices i == 0 y i == 2, calcula el valor de “h”, que es la mitad de la altura disponible ajustada por el valor “fl”, y A, que es la mitad de la diagonal de los cuadradores, calculada usando la fórmula “A = (List_A[i] * np.sqrt(2)) / 2”. A partir de estos valores, define las coordenadas de los vértices de cada cuadrador y los organiza en una lista vertices. Luego, usa “np.array(vertices)” para convertirlos en un arreglo NumPy y trazar el cuadrador en el gráfico utilizando “plt.plot()”. Además, los vértices individuales de cada cuadrador se marcan con “plt.scatter()”, utilizando un color amarillo con borde negro para destacarlos. Para los otros índices de la lista “List_A”, se calcula el valor de “A” de forma diferente, simplemente dividiendo el valor de “List_A[i]” entre 2, y se repite el proceso de cálculo de vértices y graficado de los cuadradores. Esto permite visualizar la distribución de los cuadradores en la malla con una disposición de forma dinámica en función de los valores proporcionados en “List_A”, tal como se muestra en la siguiente figura.
Figura 66
Código para dibujar los taladros de la sección de corte
Nota: fuente propia.
Respecto al dibujo de la gradiente se crea un comando condicional, dependiendo de la altura (Altura) de la malla. Si Altura es menor o igual a 3, se dibujan tres líneas: primero, una línea discontinua vertical en el centro del ancho de la malla (en Ancho/2) que se extiende desde el fondo hasta la altura total de la malla; luego, una línea horizontal discontinua en (y = 1) a lo largo de todo el ancho de la malla, que se etiqueta como "Gradiente" y tiene color magenta; y finalmente, una línea horizontal discontinua ubicada en (Altura - fl + 1) / 2, que también atraviesa todo el ancho de la malla. Si Altura es mayor a 3, se repiten las primeras dos líneas, pero con la línea horizontal en (y = 1.5) para el gradiente, y la tercera línea horizontal permanece en la misma posición (Altura - fl + 1) / 2. En ambos casos, las líneas se trazan usando ax1.plot(), con un estilo de línea discontinua (linestyle='--'), un color negro para las líneas horizontales y un color magenta para la línea del gradiente, con un grosor de línea definido por “linewidth=0.5”.
Figura 67
Código para dibujar la gradiente
Nota: fuente propia.
Finalmente se genera un punto de dispersión (scatter plot) que representa el taladro de alivio equivalente en el gráfico. El taladro se ubica en las coordenadas (Ancho/2, (Altura-fl+1)/2), es decir, en el centro horizontal de la malla (Ancho/2) y a una altura ajustada por el valor de fl (restando de Altura un valor relacionado con la longitud de la voladura). El marcador tiene un color de fondo transparente (facecolors='none'), un borde de color negro (edgecolors='black'), y un tamaño de 300 puntos (s=300), lo que lo hace visualmente destacado. Luego, se añade una leyenda con plt.legend() para identificar las diferentes características de la malla en el gráfico, y se establece el título del gráfico como 'MALLA DE PERFORACIÓN PRE-CORTE' con un tamaño de fuente de 20 puntos mediante plt.title(), tal como se representa en la siguiente imagen.
Figura 68
Código para dibujar el taladro de alivio equivalente
Nota: fuente propia.
Para agregar texto a la figura utilizando plt.text(), donde se coloca información relevante sobre los parámetros de perforación, tales como el número de taladros de alivio, el diámetro equivalente (en milímetros), el GSI y el RQD, los cuales son calculados previamente. Esta información se presenta de manera legible en la parte superior de la figura, con un tamaño de fuente de 10 puntos. Después, se utiliza “PdfPages” para generar un archivo PDF llamado 'documento.pdf'. Dentro de un bloque “with”, se guarda la figura generada (fig1) en el archivo PDF y luego se cierra la figura para liberar recursos.
Posterior a ello, se crean cuatro tablas usando “pandas.DataFrame”, cada una correspondiente a diferentes secciones del diseño de perforación: los cuadrantes, los arrastres, la corona y los hastiales. Para cada tabla, se define un diccionario con los parámetros correspondientes, sus valores y las unidades correspondientes, luego se crea un objeto “DataFrame” con esos datos. Estas tablas se dibujan en el archivo PDF mediante “ax.table()”, que coloca las tablas en la figura, y se ajusta el tamaño de la fuente para asegurar que todo el contenido sea visible. Cada tabla se guarda en el PDF después de ser generada, y se cierra para proceder con la siguiente.
Finalmente, una vez que todas las tablas y figuras han sido agregadas al archivo PDF, se abre automáticamente el archivo utilizando “os.startfile(pdf_filename)”, lo que permite que el usuario vea el documento generado en su visor de PDFs predeterminado, todo ello se representa en las siguientes imagenes.
Figura 69
Código para imprimir mensajes de interés en la grafica de la malla
Nota: fuente propia.
Figura 70
Código para crear las tablas de interés que almacenan los parámetros de las secciones calculadas
Nota: fuente propia.
Figura 71
Código para representar las tablas en el documento PDF
Nota: fuente propia.
Al ejecutar el código con los parámetros obtenidos de las diferentes áreas, se obtiene lo siguiente:
Figura 72
Representación gráfica de la malla que otorgo el software
Nota: fuente propia.
Figura 73
Representación gráfica de los parámetros de los taladros de corte
Nota: fuente propia.
Figura 74
Representación gráfica de los parámetros de los taladros de la corona
Nota: fuente propia.
Figura 75
Representación gráfica de los parámetros de los taladros del arrastre
Nota: fuente propia.
Figura 76
Representación gráfica de los parámetros de los taladros en los hastiales
Nota: fuente propia.
Debido a que la malla está incompleta por la falta de taladros en el tajo, se procederá a complementar con los datos de la malla del maestro. Como resultado, se observa de la siguiente manera en la figura a continuación.
Figura 77
Representación de grafica de la malla de perforación optimizada
Nota: fuente propia.
3.1.3.3.3	Cálculo de la nueva sobrerotura y actualización precios unitarios de perforación, voladura utilizando nueva malla de perforación precorte.
Cálculo de la nueva sobrerotura
Para el cálculo de la nueva sobrerotura, se tomaron un total de 50 datos después de aplicar la malla de perforación optimizada según el método de Holmberg.
Estos datos se almacenaron de manera similar a los de la sobrerotura anterior, con mediciones realizadas cada tres metros, tal como se muestra en la siguiente imagen.
Figura 78
Código que muestra el almacenamiento de los datos obtenidos al aplicar la malla de perforación optimizada
Nota: fuente propia.
Como resultado, se obtuvo un promedio de sobrerotura de 3.33%, lo cual es un valor inferior a la meta previamente establecida del 5%. La gráfica que muestra los resultados de esta nueva sobrerotura se presenta a continuación.
Figura 79
Representación gráfica de la evolución de la sobrerotura al aplicar la malla de perforación optimizada
Nota: fuente propia.
Actualización de precios unitario de perforación y voladura
La actualización de los precios unitarios se realizará tomando en cuenta los ajustes efectuados en la malla de perforación optimizada, la cual se muestra en la figura (77). Es importante destacar que, dado que se trata de una voladura de precorte en el contorno, se intercalará un taladro cargado y un taladro vacío. Estos ajustes se reflejan en las siguientes tablas.
Tabla 22
Parámetros de interés en la actividad unitaria de perforación aplicando la malla de perforación optimizada
Nota: fuente propia.
Tabla 23
Parámetros de interés en la actividad unitaria de voladura aplicando la malla de perforación optimizada
Nota: fuente propia.
Con base en estas variaciones, los precios unitarios se ajustarán de la siguiente manera.
Figura 80
Precio unitario de voladura aplicando la nueva malla de perforación optimizada
Nota: fuente propia.
Figura 81
Precio unitario de perforación aplicando la nueva malla de perforación optimizada
Nota: fuente propia.
Capítulo IV. Análisis e interpretación de resultados
4.1	Análisis de resultados
4.1.1	Comparación de resultados de la sobrerotura
Al observar inicialmente una sobre rotura del 34.36%, se decidió aplicar una malla de perforación optimizada basada en el modelo matemático de Holmberg para voladura de precorte. Este modelo proporcionó un resultado en el que la sobre rotura promedio fue reducida a un 3.33%. Este valor se encuentra muy por debajo del estándar permitido por la compañía minera Poderosa, que establece un límite máximo de 10%.
Figura 82
Representación gráfica de comparación de sobrerotura en las dos etapas
Nota: fuente propia. La línea roja representa a la sobrerotura aplicando la malla de perforación optimizada y la línea morada la sobrerotura en la etapa preliminar.
4.1.2	Comparación de resultados de costos operativos de interés
En la etapa preliminar, se establecieron los siguientes precios unitarios para las actividades correspondientes: la voladura tuvo un costo de 600.52 dólares por disparo, la perforación fue de 321.57 dólares por disparo y el shotcrete se fijó en 516.58 dólares por metro cúbico. Al observar una sobrerotura promedio del 34.36%, se estimó que se requerirían 3.779 m³ de shotcrete, lo que generó un costo de 1,952.54 dólares por disparo, conforme a los cálculos realizados previamente. De esta manera, el costo total por disparo, considerando las tres actividades unitarias, ascendió a 2874.63 dólares.
Después de implementar la malla de perforación optimizada, se observó una sobrerotura promedio del 3.33%, lo que resultó en una longitud real promedio de 4.57 m. Al sustituir estos valores en la ecuación (1), tal como se muestra en la siguiente expresión.
Y con un avance promedio de disparo de 2.95 m, podemos calcular la cantidad de shotcrete necesaria utilizando la ecuación (2).
Considerando que el precio unitario del shotcrete es de 516.58 dólares por metro cúbico lanzado, el costo total por disparo para esta actividad sería de 1,709.41 dólares.
Además, el precio unitario de la actividad de voladura es de 570.13 dólares por disparo, y el costo de la perforación alcanza un total de 344.89 dólares por disparo. En consecuencia, el costo total por disparo para las tres actividades unitarias sumaría 2,624.39 dólares.
4.2	Contrastación de la hipótesis
4.2.1	Sobrerotura
Para realizar la contradicción de la hipótesis en el caso de la sobrerotura, en primer lugar, se define la hipótesis nula
Hipótesis nula (H0) = Al aplicar la malla optimizada la sobrerotura es menor igual al 5%, es decir, µ ≤ 5%
Hipótesis alternativa (H1) = Al aplicar la malla optimizada la sobrerotura es mayor al 5%, es decir, µ > 5%
El nivel de significancia con el que se trabajó en este trabajo de investigación es de 5%, por lo cual α=0.05.
Como tenemos una muestra de 50 datos tal como se muestra en el anexo (5), utilizaremos una prueba t de Student para una muestra, ya que estamos trabajando con una muestra y no con una población completa.
Donde:
= media muestral
= valor hipotético de la media (en este caso, 5%)
= desviación estándar de la muestra
= tamaño de la muestra
Mediante Python obtenemos la desviación estándar y la media muestral de los 50 datos.
Entonces aplicando la formula del estadístico “t” tenemos:
A continuación, obtenemos el valor critico de t para un nivel de significación de 0.05 y 49 grados de libertad (n - 1 = 50 - 1 = 49) esto lo ubicamos de la tabla de distribución t de Student ilustrada en el anexo (7).
Para una prueba de una cola y un nivel de significación de 0.05, el valor crítico es aproximadamente 1.676.
Entonces se procede a hacer la gráfica representativa de la distribución normal tal como se muestra en la siguiente imagen.
Figura 83
Grafica de la distribución normal del t de student para comprobar hipótesis.
Nota: fuente propia.
Entonces se concluye que dado que t calculado (-23.2434) es menor que el valor crítico 1.676, no rechazamos la hipótesis nula​. Esto significa que, con un nivel de significación del 5%, no tenemos evidencia suficiente para afirmar que la sobrerotura es mayor al 5%. En otras palabras, la sobrerotura es menor o igual al 5%.
4.2.2	Costo de sostenimiento
Debido a que al inicio se tomaron 92 datos y posterior a la aplicación de la malla de perforación se tomaron un total de 50 datos, se seleccionaran de los 92 datos 50 que son los menores de tal manera de contrarrestar la hipótesis y que el resultado tenga un nivel de incertidumbre menor, estos 50 datos de cada uno se ilustran en el anexo (6).
Con la aclaración ya pasmada para realizar la contrastación de la hipótesis en el caso de la sobrerotura, en primer lugar, se define la hipótesis nula
Hipótesis nula (H₀): No hay diferencia o el costo después no es menor que el costo antes. Es decir, el costo después es igual o mayor que el costo antes.
Hipótesis alternativa (H₁): El costo después es significativamente menor que el costo antes. Es decir, la media del costo después es menor que la del costo antes.
El nivel de significancia también se consideró de 5%, por lo cual α=0.05.
Para este caso, realizaremos una prueba t de Student para muestras emparejadas. Primero, calcularemos las diferencias entre el costo después y el costo antes para cada par de datos. Con estas diferencias, calcularemos la estadística t para determinar si existe una diferencia significativa entre los costos antes y después.
Con ayuda de Python pudimos obtener los siguientes valores
Para calcular la estadística de prueba t se utiliza la siguiente formula
Donde:
es la media de las diferencias.
es la desviación estándar de las diferencias.
es el número total de observaciones.
Entonces reemplazando los valores tenemos
A continuación, obtenemos el valor crítico de t utilizando un nivel de significación de 0.05 y 49 grados de libertad (n - 1 = 50 - 1 = 49), el cual se localiza en la tabla de distribución t de Student presentada en el Anexo (7). Para una prueba unilateral con un nivel de significación de 0.05, el valor crítico es aproximadamente 1.676. Luego, se procede a graficar la distribución t correspondiente, como se muestra en la siguiente imagen.
Figura 84
Grafica de la distribución normal del t de student para comprobar hipótesis.
Nota: fuente propia.
Dado que el valor de t es significativamente mayor que el valor crítico, se rechaza la hipótesis nula. Esto implica que aceptamos la hipótesis alternativa, que sugiere que el costo de mantenimiento después es menor que el costo previo, tal como se planteó en la hipótesis inicial.
4.3	Discusión de resultados
Al analizar los resultados obtenidos, se observó una mejora significativa en diversos aspectos clave. En primer lugar, la sobre rotura se redujo del 34.36% al 3.33%, lo que representa una disminución del 31.06%. Este resultado positivo se traduce en una mayor eficiencia en la perforación y voladura, lo cual contribuye a la optimización de los procesos.
En cuanto a la actividad de voladura, en la etapa preliminar, el costo unitario por disparo era de 600.52 dólares. Sin embargo, tras la implementación de la malla de perforación optimizada, el costo se redujo a 570.13 dólares por disparo, lo que representa una disminución de 30.39 dólares por disparo, reflejando un importante ahorro en esta actividad.
En lo que respecta a la perforación, se registró un incremento en el costo unitario, pasando de 321.57 dólares por disparo en la etapa preliminar a 344.85 dólares por disparo después de la optimización. Este aumento se debe al incremento en el número de taladros necesarios, lo cual, aunque genera un costo adicional de 23.28 dólares por disparo.
Por otro lado, en el caso del sostenimiento, específicamente en la actividad de lanzado de shotcrete, el costo unitario por disparo en la etapa preliminar era de 1,952.54 dólares. Tras la implementación de la malla optimizada, el costo disminuyó a 1,709.41 dólares por disparo, lo que refleja una reducción de 243.13 dólares por disparo. Esta mejora en el costo de sostenimiento es un factor clave en la optimización de los costos totales.
Al analizar el costo total de las tres actividades unitarias, se identificó una reducción global de 250.24 dólares por disparo. Dado que el avance por disparo es de 2.95 metros y el proyecto de la cortada abarca 2 km, se estima un ahorro total de 169,654.23 dólares, lo que representa una mejora significativa en la rentabilidad del proyecto.
Conclusiones
Al implementar la malla de perforación optimizada, basada en el modelo matemático de Holmberg para voladuras de precorte, se logró una sobre rotura del 3.33%, la cual se encuentra dentro del rango aceptable estipulado por los estándares de la mina, que permiten un máximo del 10%. Además, este resultado representa una reducción del 31.06% en comparación con la sobre rotura obtenida previamente con la malla de perforación tradicional.
El costo de sostenimiento mediante el lanzamiento de shotcrete, al presentar una sobre rotura del 3.33%, experimentó una reducción de 243.13 dólares por disparo en comparación con los costos previos, lo que refleja una mejora significativa en la eficiencia económica del proceso.
El tiempo requerido para elaborar las mallas de perforación optimizadas para voladuras de precorte se redujo de manera considerable gracias a la automatización del proceso. Al ingresar los datos relacionados con la calidad de la roca y los parámetros del explosivo, el software genera la malla de forma instantánea, eliminando así posibles errores de cálculo y optimizando la eficiencia en el diseño de las voladuras.
Dado que el proyecto está planificado para una longitud total de 2 km, la implementación de la malla de perforación optimizada ha generado un ahorro significativo de 169,654.23 dólares en comparación con los precios unitarios previos, calculados con la malla utilizada anteriormente para las actividades unitarias de perforación, voladura y sostenimiento. Este ahorro resalta el impacto positivo de la optimización en los costos, lo que representa un beneficio considerable para el proyecto.
Recomendaciones
Es fundamental garantizar el paralelismo adecuado al realizar la perforación en frentes de gran dimensión, con el fin de minimizar la desviación, logrando que esta no supere el 2%. Esto es crucial para aplicar el modelo matemático de Holmberg y asegurar una eficiencia de avance del 95%, tal como lo estipula el modelo, lo que permitirá un mejor control de la sobrerotura y optimización de la voladura.
Se recomienda aplicar las mallas de perforación optimizadas para voladura de precorte solo en casos donde se presenten sobrarotura excesiva. Para labores con niveles moderados de sobrerotura, es más adecuado utilizar mallas de perforación para voladura de recorte.
Es recomendable parametrizar la ubicación y cantidad de los taladros de tajeo. Esta medida facilita la conclusión de ejecución del software desarrollado en este trabajo.
Referencias bibliográficas
Vidal, M. (2020). Voladura controlada aplicando el modelo matemático de Holmberg y la ingeniería de explosivos para mejorar la eficiencia de avance en la CIA minera poderosa s.a. [Tesis de pregrado, Universidad Nacional del Centro del Perú]. Repositorio Institucional – UNCP.
https://repositorio.uncp.edu.pe/handle/20.500.12894/5923
Baltazar, R. (2023). Análisis de las variables operacionales de shotcrete y sobrerotura en el CX 2713, NV 1565, zona centro para la reducción de costos en sostenimiento – Consorcio Minero Horizonte, 2023 [Tesis de pregrado, Universidad Continental]. Repositorio Institucional Continental.
https://repositorio.continental.edu.pe/handle/20.500.12394/13782
Jimenez, A. (2021) Automatización del modelo matemático Holmberg para el cálculo y diseño de mallas de perforación en frentes de desarrollo [Tesis de pregrado, Universidad Continental] Repositorio Institucional Continental.
https://repositorio.continental.edu.pe/handle/20.500.12394/10808
Zuñiga, G. (2019) Control de calidad topológico de los objetos espaciales a través de la automatización con Python en el proceso de validación de la información [Tesis de pregrado, Pontificia Universidad Católica del Ecuador] Repositorio PUCE
http://repositorio.puce.edu.ec/handle/22000/16178
Ticona, S (2024) Aplicación del método de Holmberg para la optimización de la malla de perforación y voladura en minería en rocas del grupo pucará 2023 [Tesis de pregrado, Universidad Nacional Jorge Basadre Grohmann] Repositorio de la UNJBG
https://repositorio.unjbg.edu.pe/items/5ef7b3bf-cf05-4e83-a8e3-0f963c2d3f1f
Carrasco, P (2015) Aplicación del método Holmberg para optimizar la malla de perforación y voladura en la unidad parcoy- cia. consorcio minero horizonte s.a [Tesis de pregrado, Universidad Nacional de San Cristóbal de Huamanga] Repositorio Institucional UNSCH.
https://repositorio.unsch.edu.pe/items/f8e0f691-5b4a-44ba-b62e-522184f99902
Mostacero, E. et al (2017) Optimización del diseño de perforación y voladura, para reducir costos en labores de avance en la mina Santa María – Poderosa S.A. [Tesis de pregrado, Universidad Nacional de Trujillo] Repositorio UNITRU
https://dspace.unitru.edu.pe/items/cb164d1e-844c-4413-a701-bfb34c65564f
Quezada, W. (2017) Optimización de perforación y voladura aplicando el modelo matemático de Holmberg en frente de 3.5m*3.5m en roca tipo II veta Papagayo, mina Poderosa, 2017 [Tesis de pregrado, Universidad Nacional de Trujillo] Repositorio UNITRU
https://dspace.unitru.edu.pe/items/143d6e84-eab3-4711-86bc-a1fe0cbc95e0
Ttica, E. (2018) Diseño de malla de perforación y voladura según Holmberg, para reducir los costos unitarios en la cortada SW nivel 2760. Contrata minera ARCA. S.A.C.- Unidad de producción Santa María – CIA. Minera Poderosa S.A., 2017 [Tesis de pregrado, Universidad Nacional Micaela Bastidas de Apurímac] Repositorio UNA
https://repositorio.unamba.edu.pe/handle/UNAMBA/604MBA
Sulcacondor, J. (2018) Optimización de operaciones unitarias de perforación y voladura mediante voladura controlada en labores horizontales en la CIA. Minera Poderosa S.A. [Tesis de pregrado, Universidad Nacional de San Cristóbal de Huamanga] Repositorio Institucional UNSCH
https://repositorio.unsch.edu.pe/items/be9b287b-c84a-450c-bbd9-14dfac27addf
Acero, A. (2021) Propuesta de una malla de perforación y voladura para labores de avance [Tesis de pregrado, Universidad Nacional de Ingeniería] Repositorio institucional Cybertesis UNI.
https://repositorio.uni.edu.pe/handle/20.500.14076/22526
Valenzuela, B. (1995) Desarrollo de software para ser aplicado a las operaciones mineras unitarias de perforación y voladura [Tesis de pregrado, Universidad Nacional de Ingeniería] Repositorio institucional Cybertesis UNI.
https://repositorio.uni.edu.pe/handle/20.500.14076/1913
Orihuela, J. (1992) Aplicación de voladuras controladas en minería subterránea y tunelaría [Tesis de pregrado, Universidad Nacional de Ingeniería] Repositorio institucional Cybertesis UNI.
https://repositorio.uni.edu.pe/handle/20.500.14076/15213
Anexos
Pág.
Anexo 1: Precio unitario de voladura compartido por compañía.	1
Anexo 2: Precio unitario de perforación compartido por compañía	2
Anexo 3: Precio unitario de sostenimiento compartido por compañía.	3
Anexo 4: Precios de explosivos y accesorios de voladura	4
Anexo 5: Datos de sobrerotura tomados después de aplicar la malla de perforaciónlllllllllll lllllllllllllllllllloptimizada	5
Anexo 6: Costo de sostenimiento por lanzado de shotcrete	6
Anexo 7: Matriz de consistencia	7
Anexo 8: Cronograma del trabajo	8
Anexo 1: Precio unitario de voladura compartido por compañía.
Anexo 2: Precio unitario de perforación compartido por compañía
Anexo 3: Precio unitario de sostenimiento compartido por compañía.
Anexo 4: Precios de explosivos y accesorios de voladura
Anexo 5: Datos de sobrerotura en (%) tomados después de aplicar la malla de perforación optimizada
Anexo 6: Costo de sostenimiento en USD/disp. por lanzado de shotcrete
Costos de sostenimiento en la etapa posterior a la aplicación de la malla de perforación optimizada.
Costos de sostenimiento en la etapa preliminar.
Anexo 7: Tabla de distribución de la t de Student
Anexo 8: Matriz de consistencia
Anexo 9: Cronograma del trabajo

### Tabla 1 de Documento:
| Citar/How to cite | Perez Guia [1] | Perez Guia [1] |
| --- | --- | --- |
| Referencia/Reference  Estilo/Style: IEEE (2020) | [1] | R. Perez Guia, “Automatización del cálculo y diseño de mallas de perforación optimizadas para reducir la sobrerotura y costo de sostenimiento en labores de avance y desarrollo” [Tesis de pregrado]. Lima (Perú): Universidad Nacional de Ingeniería, 2024. |

### Tabla 2 de Documento:
| Citar/How to cite | (Perez, 2024) |
| --- | --- |
| Referencia/Reference  Estilo/Style: APA (7ma ed.) | Perez, R. (2024). Automatización del cálculo y diseño de mallas de perforación optimizadas para reducir la sobrerotura y costo de sostenimiento en labores de avance y desarrollo. [Tesis de pregrado, Universidad Nacional de Ingeniería]. Repositorio institucional Cybertesis UNI. |

### Tabla 3 de Documento:
| Dirección de salida de los taladros | Factor de fijación “” | Relación |
| --- | --- | --- |
| Hacia arriba y horizontalmente | 1.45 | 1.25 |
| Hacia abajo | 1.20 | 1.25 |

### Tabla 4 de Documento:
| Indicadores | Valores |
| --- | --- |
| Factor de fijación “” | 1.45 |
| Relación | 1.20 |
| Concentración de la carga de columna | 0.5* |

### Tabla 5 de Documento:
| Constructor | Definición |
| --- | --- |
| str() | Convierte datos en forma de cadena. |
| int() | Convierte datos en número entero. |
| float() | Convierte datos en un número real. |
| complex() | Convierte datos en un numero complejo. |
| list() | Convierte datos en una lista. |
| set() | Convierte datos en un conjunto. |
| tuple() | Convierte datos en una tupla |
| dict() | Convierte datos en un diccionario |
| bool() | Convierte datos en un valor booleano |
| none() | Convierte los datos en un valor nulo |

### Tabla 6 de Documento:
| Tipo de operador | Algoritmos |
| --- | --- |
| Operadores aritméticos | + , - , * , / , % , ** , // |
| Operadores de asignación | = , += , -= , /= , %= , //= , **= |
| Operadores de comparación | == , != , > , < , >= , <= |
| Operadores lógicos | and, or, not |
| Operadores de identidad | is, is not |
| Operadores de membresía | in, not in |

### Tabla 7 de Documento:
| Método | Descripción |
| --- | --- |
| a.upper() | Coloca a todos los caracteres en mayúscula. |
| a.lowe() | Coloca a todos los caracteres en minúscula. |
| a.strip() | Elimina espacios en blanco de la cadena. |
| a.replace(a,b) | Reemplaza el carácter “a” por el carácter “b”. |
| a.split(“,”) | Genera una lista separando los caracteres donde se presente el “,” |

### Tabla 8 de Documento:
| Carácter | Descripción |
| --- | --- |
| \’ | Este carácter permite colocar “comillas”. |
| \\ | Coloca un slash. |
| \n | Hace que la cadena termine la línea de código y se inicie una nueva |
| \r | Inicia una nueva cadena en la siguiente línea de código. |
| \b | Quita espacios en la unión de cadenas |

### Tabla 9 de Documento:
| Método | Descripción |
| --- | --- |
| list.sort() | Ordena los elementos de la lista alfanuméricamente. |
| list.sort(reverse=true) | Ordena los elementos de la lista de forma inversa. |
| list.copy() | Copia las listas hacia otra lista diferente. |

### Tabla 10 de Documento:
| Método | Descripción |
| --- | --- |
| tuple.count() | Indica la cantidad de elementos que ostenta la tupla |
| tuple.index() | Indica el índice donde se encuentra el elemento. |

### Tabla 11 de Documento:
| Método | Descripción |
| --- | --- |
| set.union(set2) | Se genera una unión de conjuntos |
| set.update(set2) | Intercepta elemento de los conjuntos |
| set.intersection(set2) | Intercepta todo tipo de clase |
| set.intersection_update(set2) | Conserva todos sus duplicados |
| set.difference(set2) | Sirve para hacer la operación de diferencia |

### Tabla 12 de Documento:
| Método | Descripción |
| --- | --- |
| fromkeys() | Devuelve un diccionario con las claves y valores |
| get() | Devuelve el valor de una clave especifica |
| setdefault() | Devuelve el valor de la clave especifica peros i la clave  no existe esta función no emite error. |
| update() | Actualiza el diccionario con los pares clave/valores especificados |

### Tabla 13 de Documento:
| Método | Descripción |
| --- | --- |
| math.sqrt(x) | Devuelve la raíz cuadrada de x, donde x debe ser positivo. |
| math.factorial(x) | Devuelve la factorial de un número x, solo para enteros no negativos. |
| math.sin(x) | Calcula el seno de x, donde x está en radianes. |
| math.cos(x) | Calcula el coseno de x, donde x está en radianes. |
| math.log(x, base) | Devuelve el logaritmo de x con la base especificada, por defecto es base e. |
| math.pi | Proporciona el valor de pi, aproximadamente 3.141592653589793. |

### Tabla 14 de Documento:
| Método | Descripción |
| --- | --- |
| matplotlib.pyplot.plot() | Traza un gráfico de líneas, muy útil para series de datos. |
| matplotlib.pyplot.scatter() |  |
| matplotlib.pyplot.hist() |  |
| matplotlib.pyplot.show() | Muestra el gráfico generado en pantalla. Es el comando final para visualizar cualquier figura. |
| matplotlib.pyplot.bar() |  |
| matplotlib.pyplot.subplot() | Permite crear una cuadrícula de subgráficos en una sola figura. |

### Tabla 15 de Documento:
| Método | Descripción |
| --- | --- |
| numpy.array() | Crea un arreglo de numpy a partir de una lista, lista de listas, o cualquier objeto iterable. |
| numpy.mean() |  |
| numpy.median() |  |
| numpy.std() | Calcula la desviación estándar de los elementos de un arreglo. |
| numpy.dot() | Realiza el producto punto entre dos arreglos. Es útil para operaciones de álgebra lineal. |
| numpy.reshape() | Cambia la forma de un arreglo sin modificar sus datos. |

### Tabla 16 de Documento:
| Método | Descripción |
| --- | --- |
| pandas.DataFrame() | Crea un DataFrame a partir de un diccionario, lista o arreglo. |
| pandas.Series() | Crea una Serie de pandas, que es una estructura unidimensional similar a un arreglo. |
| pandas.read_csv() | Lee un archivo CSV y lo convierte en un DataFrame, ideal para importar datos. |
| pandas.head() | Devuelve las primeras 5 filas de un DataFrame, útil para obtener una vista preliminar de los datos. |
| pandas.groupby() | Agrupa un DataFrame según una o más columnas, permitiendo realizar operaciones de agregación. |
| pandas.merge() |  |

### Tabla 17 de Documento:
| Tramos | Distancia (Km) | Tiempo empleado | Medio de trasporte |
| --- | --- | --- | --- |
| Lima – Trujillo | 560 | 08:00 | Bus de Plaza Norte |
| Trujillo – Camp. Santa María 2520 | 360 | 12:00 | Bus del terminal terrestre Poderosa – Trujillo |
| Camp. Santa María 2520 – CR NW 2350 | 3 | 00:15 | Camioneta de Cía. Poderosa |
| Total | 923 | 20:15 |  |

### Tabla 18 de Documento:
| Tramos | Distancia (Km) | Tiempo empleado | Medio de trasporte |
| --- | --- | --- | --- |
| Lima – Trujillo | 560 | 00:40 | Avión |
| Trujillo – Terminal aéreo Chagual | 340 | 00:50 | Avioneta |
| Terminal aéreo Chagual - Camp. Santa María 2520 | 20 | 00:45 | Camioneta de Cía. Poderosa |
| Camp. Santa María 2520 – CR NW 2350 | 3 | 00:15 | Camioneta de Cía. Poderosa |
| Total | 923 | 02:30 |  |

### Tabla 19 de Documento:
| Parámetro | Valor |
| --- | --- |
| UP | Santa María |
| Labor | CR NW |
| Nivel | 2350 |
| Resistencia a la tracción (MPa) | 12.15 |
| Resistencia a la compresión (MPa) | 180.05 |
| Módulo de Young (GPa) | 35.78 |
| Índice de calidad de roca (Barton) | Buena (10) |
| Rock Mass Rating (RMR) | 55.5 |
| Geological Strength Index promedio (GSI) | 50 |
| Rock Quality Designation promedio (RQD) | 60 |
| Densidad de la roca promedio (Tm/m3) | 2.7 |

### Tabla 20 de Documento:
| Parámetro | Valor | Unidad |
| --- | --- | --- |
| Peso neto del cartucho | 0.265 | Kg |
| Potencia relativa en peso referida al ANFO | 112 | % |
| Diámetro del cartucho del explosivo | 31.8 | mm |
| Longitud del encartuchado | 12 | Pulg |
| Densidad del explosivo | 1.16 | g/cc |

### Tabla 21 de Documento:
| Parámetro | Valor | Unidad |
| --- | --- | --- |
| Peso de una unidad de explosivo | 0.138 | Kg |
| Densidad del explosivo | 1.1 | g/cc |
| Velocidad de detonación del explosivo | 4200 | m/seg |
| Diámetro del explosivo | 17.5 | mm |

### Tabla 22 de Documento:
| Descripción | Cantidad | Unidad |
| --- | --- | --- |
| Número de taladros de producción | 46 | [] |
| Número de taladros rimados | 3 | [] |

### Tabla 23 de Documento:
| Descripción | Cantidad | Unidad |
| --- | --- | --- |
| Cantidad de emulnor 5000 | 349 | [] |
| Cantidad de emulnor 3000 | 189 | [] |
| Cantidad de Famecorte E-20 | 30 | [] |
| Mecha rápida de ignición Z-18 | 0.3 | M |
| Fanel 2.4m | 46 | [] |
| Cordón detonante 5g | 2 | M |
| Detonador ensamblado | 3 | [] |

### Tabla 24 de Documento:
| Descripción | Cantidad | Unidad |
| --- | --- | --- |
| Número de taladros de producción | 44 | [] |
| Número de taladros de alivio | 7 | [] |
| Número de taladros rimados | 3 | [] |

### Tabla 25 de Documento:
| Descripción | Cantidad | Unidad |
| --- | --- | --- |
| Cantidad de emulnor 5000 | 335 | [] |
| Cantidad de emulnor 3000 | 153 | [] |
| Cantidad de Famecorte E-20 | 42 | [] |
| Mecha rápida de ignición Z-18 | 0.3 | m |
| Fanel 2.4m | 44 | [] |
| Cordón detonante 5g | 2 | m |
| Detonador ensamblado | 3 | [] |

### Tabla 26 de Documento:
| EXPLOSIVOS Y ACCESORIOS DE VOLADURA | EXPLOSIVOS Y ACCESORIOS DE VOLADURA |  |
| --- | --- | --- |
| Item | Descr_Material2 | Costo |
| Item | Descr_Material2 | S/./UNDAD |
| 4.00 | EXPLOSIVOS Y ACCESORIOS DE VOLADURA |  |
| 4.01 | Nitrato de amonio - anfo | 7.32 |
| 4.02 | Dinamita semi gelatina 65%  (312) 7/8" X 7" 65% | 0.81 |
| 4.03 | Dinamita sg 65 (132 pza) 1.1/4" X 8" | 1.69 |
| 4.04 | Dinamita sg 80  (128 pza) 1.1/4" X 8" | 1.82 |
| 4.05 | Emulsion emulnor 1000 (264 pza) 1" X 7"  85% | 0.96 |
| 4.06 | Emulsion emulnor 3000 (228 pza) 1" X 8" 100% | 1.14 |
| 4.07 | Emulsion emulnor 5000 (216 pza) 1" X 8"  105% | 1.24 |
| 4.08 | Emulsion emulnor 1000 (100 pza 1.1/4" X 12" | 2.35 |
| 4.09 | Emulsion emulnor 3000 (94 pza) 1.1/4" X 12" | 2.56 |
| 4.10 | Emulsion emulnor 5000 (94 pza) 1.1/4" X 12" | 2.65 |
| 4.11 | Emulsion famecorte e20  (144 p) 17.5 X 512MM 74% | 4.07 |
| 4.12 | Cordon detonante 5G | 0.98 |
| 4.13 | Mecha rapida de ignicion Z-18 | 1.47 |
| 4.14 | Detonador no electrico fanel 2.40m (lp) | 3.63 |
| 4.15 | Detonador no electrico fanel 3.00 m  lp | 4.25 |
| 4.16 | Detonador no electrico fanel 4.20 m  lp | 4.38 |
| 4.17 | Detonador ensamblado (300 pza) 2.4 MTR | 2.77 |
|  |  |  |

### Tabla 27 de Documento:
| PROBLEMA | OBJETIVO | HIPÓTESIS | VARIABLES | VARIABLES | INDICADORES | TÉCNICA E INSTRUMENTOS DE RECOLECCIÓN DE DATOS |
| --- | --- | --- | --- | --- | --- | --- |
| PROBLEMA | OBJETIVO | HIPÓTESIS | DEPENDIENTE | INDEPENDIENTE | INDICADORES | TÉCNICA E INSTRUMENTOS DE RECOLECCIÓN DE DATOS |
| GENERAL | GENERAL | GENERAL | GENERAL | GENERAL | GENERAL | GENERAL |
| ¿En qué medida un mal diseño y cálculo de la malla de perforación incrementa la sobrerotura de las labores de avance y desarrollo? | Reducir la sobrerotura a un máximo de 5% en las labores de avance y desarrollo de las minas subterráneas. | Un diseño y cálculo de las mallas de perforación optimizada permitirá reducir la sobrerotura a un máximo del 5% en las labores de avance y desarrollo. | Sobrerotura. | Diseño y cálculo de las mallas de perforación optimizada. | Porcentaje de sobrerotura Parámetros de calidad de roca Características del explosivo Características de la sección | Utilización de distanciómetro para cálculo de dimensión Recolección de datos manuales |
| ESPECIFICO | ESPECIFICO | ESPECIFICO | ESPECIFICO | ESPECIFICO | ESPECIFICO | ESPECIFICO |
| ¿En qué medida el incremento de la sobrerotura eleva los costos de sostenimiento mediante el lanzado de shotcrete en las labores de avance y desarrollo? | Reducir los costos de sostenimiento por lanzado de shotcrete en las labores de avance y desarrollo de las minas subterráneas. | La reducción de la sobrerotura permitirá disminuir los costos de sostenimiento por lanzado shotcrete en las labores de avance y desarrollo. | Costos de sostenimiento por lanzado de shotcrete. | Sobrerotura. | Rendimiento de sostenimiento, perforación y voladura. Costo de mano de obra, materiales y equipos | Recolección de datos manuales |
| ¿En qué medida la falta de un software de automatización de diseño y cálculo de mallas de perforación optimizadas aumenta el tiempo empleado para realizar esta actividad? | Reducir el tiempo empleado en la realización del diseño y cálculo de mallas de perforación optimizadas en las labores de avance y desarrollo de las minas subterráneas. | La creación de un software de automatización de diseño y cálculo de mallas de perforación optimizadas reducirá el tiempo empleado para realizar esta tarea. | Tiempo empleado para realizar mallas de perforación optimizadas. | Software de automatización de diseño y cálculo de mallas de perforación optimizadas. | Tiempo estimado en la realización | Recolección de datos manuales |

### Tabla 28 de Documento:
|  |  | AÑO 2024 | AÑO 2024 | AÑO 2024 | AÑO 2024 | AÑO 2024 | AÑO 2024 | AÑO 2024 | AÑO 2024 | AÑO 2024 | AÑO 2024 | AÑO 2024 | AÑO 2024 | AÑO 2024 | AÑO 2024 | AÑO 2024 | AÑO 2024 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | ACTIVIDADES | AGOSTO | AGOSTO | AGOSTO | AGOSTO | SETIEMBRE | SETIEMBRE | SETIEMBRE | SETIEMBRE | OCTUBRE | OCTUBRE | OCTUBRE | OCTUBRE | NOVIEMBRE | NOVIEMBRE | NOVIEMBRE | NOVIEMBRE |
|  | ACTIVIDADES | 1 | 2 | 3 | 4 | 1 | 2 | 3 | 4 | 1 | 2 | 3 | 4 | 1 | 2 | 3 | 4 |
| I. | RECOLECCIÓN DE DATOS |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1.1 | Recolección de información del Proyecto |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1.2 | Recolección de información de mediciones en campo |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1.3 | Realización de encuestas |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| II. | PROCESAMIENTO DE LA INFORMACIÓN |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 2.1 | Digitalización y procesamiento de información |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 2.2 | Aplicación de metodología de investigación |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| III. | ANÁLISIS DE LA INFORMACIÓN |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3.1 | Realización de software de automatización de diseño y cálculo de mallas de perforación optimizada |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3.2 | Validez de investigación |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3.3 | Contratación de la hipótesis |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3.4 | Conclusión y Recomendaciones |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |