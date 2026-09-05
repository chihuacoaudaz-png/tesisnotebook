# -*- coding: utf-8 -*-
"""
GENERADOR LATEX DEL TRABAJO DE INVESTIGACIÓN CUAJONE (FORMATO UNI RR 1439-2023)
"""

latex_content = r'''\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[spanish,es-tabla]{babel}
\usepackage{amsmath,amssymb,amsfonts,mathtools,bm}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{array}
\usepackage{xcolor}
\usepackage{geometry}
\usepackage{fancyhdr}
\usepackage{setspace}
\usepackage{titlesec}
\usepackage{caption}
\usepackage{hyperref}

% Márgenes Oficiales UNI (RR 1439-2023)
\geometry{
    a4paper,
    left=3.0cm,
    top=2.54cm,
    right=2.5cm,
    bottom=2.5cm,
    headheight=15pt,
    footskip=1.25cm
}

\setstretch{1.15}

\definecolor{UniBlue}{RGB}{13, 35, 58}
\definecolor{UniSecondary}{RGB}{46, 134, 193}

\hypersetup{
    colorlinks=true,
    linkcolor=UniBlue,
    citecolor=UniSecondary,
    urlcolor=UniSecondary
}

\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0.4pt}
\fancyhead[L]{\small\scshape UNIVERSIDAD NACIONAL DE INGENIERÍA | FIGMM}
\fancyhead[R]{\small\thepage}
\fancyfoot[C]{\small Trabajo de Investigación Técnica -- Gerencia Mina Cuajone 2025}

\titleformat{\section}{\normalfont\Large\bfseries\color{UniBlue}}{\thesection.}{0.8em}{}
\titleformat{\subsection}{\normalfont\large\bfseries\color{UniSecondary}}{\thesubsection.}{0.6em}{}

\begin{document}

% PORTADA INSTITUCIONAL UNI
\begin{titlepage}
    \centering
    {\bfseries\LARGE UNIVERSIDAD NACIONAL DE INGENIERÍA\par}
    \vspace{0.3cm}
    {\bfseries\large FACULTAD DE INGENIERÍA GEOLÓGICA, MINERA Y METALÚRGICA\par}
    \vspace{0.2cm}
    {\bfseries\large ESCUELA PROFESIONAL DE INGENIERÍA DE MINAS\par}
    \vspace{1.0cm}
    \hrule height 1.5pt
    \vspace{1.2cm}
    
    {\bfseries\Large INFORME DE INVESTIGACIÓN TÉCNICA OPERACIONAL\par}
    \vspace{1.2cm}
    
    {\bfseries\LARGE ``PESAJE DE VOLQUETES GERENCIA MINA CUAJONE 2025''\par}
    \vspace{1.8cm}
    
    \begin{flushleft}
    \hspace{2.5cm}\textbf{\large ÁREA:}\\
    \hspace{2.5cm}{\normalsize Entrenamiento Mina / Operaciones Mina}\par
    \hspace{2.5cm}{\normalsize Superintendencia de Operaciones Mina Cuajone}\par
    \vspace{0.8cm}
    
    \hspace{2.5cm}\textbf{\large DIRIGIDO A:}\\
    \hspace{2.5cm}{\normalsize Superintendente de Operaciones Mina}\par
    \vspace{0.8cm}
    
    \hspace{2.5cm}\textbf{\large ELABORADO POR:}\\
    \hspace{2.5cm}{\normalsize Becario de Operaciones Mina}\par
    \vspace{0.8cm}
    
    \hspace{2.5cm}\textbf{\large FECHA DE ELABORACIÓN:}\\
    \hspace{2.5cm}{\normalsize 24 de Octubre del 2025}\par
    \end{flushleft}
    
    \vfill
    {\bfseries\large MOQUEGUA -- PERÚ\par}
    {\large 2025\par}
\end{titlepage}

\tableofcontents
\newpage

\section{RESUMEN}
\subsection{Alcances}
El 12 de octubre de 2025 se llevaron a cabo los trabajos finales de preparación en la zona de pesaje, los cuales comprendieron labores de relleno, nivelación y compactación del terreno. Para la ejecución de estas actividades se emplearon los equipos Cargador Frontal WA470 (F972), Motoniveladora CAT 24M (M244) y Rodillo Bomag WB 226 DH-5 (RCC-1). Asimismo, con el propósito de garantizar una mayor precisión en la nivelación del terreno, se contó con el apoyo técnico de la empresa contratista Mincoser. En las Figuras 1 y 2 se presentan los trabajos realizados durante esta etapa.

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.90\textwidth]{figures/page_03.png}
    \caption{Trabajos de nivelación con Motoniveladora CAT 24M y compactación con apoyo de MINCOSER.}
\end{figure}

\subsection{Ubicación}
El área de pesaje estuvo delimitada por el parqueo Cocotea Bajo (Sur Oeste), Grifo Cocotea Bajo (Sur Este) y la Tranquera 4 (Norte). En la Figura 3 se muestra la ubicación del área del pesaje en el software MineOperate.

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.90\textwidth]{figures/page_04.png}
    \caption{Ubicación de la zona de pesaje en software MineOperate y personal a cargo.}
\end{figure}

\subsection{Personal a Cargo}
Durante la realización del pesaje participaron diversas áreas y empresas contratistas. El trabajo tuvo una duración total de nueve (9) días, iniciando el 12 de octubre de 2025 y culminando el 20 de octubre de 2025. Durante la jornada final, y a solicitud de la empresa Ferreyros CAT, se realizaron repesajes de los volquetes V132, V144, V163 y V164, efectuándose dos mediciones por cada unidad en condición de carga.

\section{OBJETIVOS}
\begin{enumerate}[label=\alph*.]
    \item Determinar el peso vacío (EMW) y carga útil (Payload) de los 46 volquetes de Operaciones Mina Cuajone.
    \item Mostrar la distribución de peso (ton) en cada posición de los neumáticos.
    \item Cuantificar en toneladas, el impacto de los accesorios adicionales en la distribución del peso del volquete.
    \item Calcular la diferencia entre el tonelaje real (balanza) y el tonelaje de la pantalla de ADVISOR (Caterpillar) y Payload meter (Komatsu).
    \item Determinar los operadores de pala con mayor eficiencia en el centrado de carga.
\end{enumerate}

\section{PROCEDIMIENTO DEL PESAJE}
El área de pesaje, de 15 m de ancho por 30 m de largo, se ubicó en la ruta de descarga hacia el depósito de desmonte Cocotea Bajo. En la Figura 4 se muestra la ubicación de los PADs y el acceso a la balanza. Los volquetes ingresaron a los PADs a una velocidad máxima de 5 km/h para garantizar la estabilidad de la balanza durante la medición.

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.90\textwidth]{figures/page_05.png}
    \caption{Vista en planta de la zona de pesaje y acceso a PADs.}
\end{figure}

El pesaje de cada volquete se realizó tres (3) veces vacío y cuatro (4) veces cargado con desmonte. El requerimiento del fabricante indica que el cálculo del peso del volquete vacío (EMW), debe realizarse con los fluidos al 100\%, debido a ello cada volquete contó con al menos 90\% de combustible. En el pesaje cargado se mantuvo un mínimo de 50\% de combustible.

\subsection{Procedimiento de Pesaje Operacional}
\begin{enumerate}[label=\alph*.]
    \item Previa coordinación entre Control Mina y el becario de Operaciones Mina vía radial (frecuencia C2) para autorizar el ingreso de los volquetes.
    \item En la frecuencia 13 (local), y con apoyo del vigía, se brindan las indicaciones al operador del volquete para posicionar el eje delantero sobre ambos PADs.
    \item Una vez que los neumáticos del eje delantero se encuentran centrados y la lectura del pesómetro se estabiliza, se registran los datos en el formato establecido.
    \item Posteriormente, bajo las indicaciones del becario de Operaciones Mina, se posiciona el eje trasero sobre ambos PADs y se realiza el registro correspondiente.
    \item Finalmente, se indica al operador del volquete su salida de la zona de pesaje si se encuentra cargado; en caso de estar vacío, debe retornar inmediatamente a la zona de ingreso hasta completar sus 3 pasadas.
\end{enumerate}

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.90\textwidth]{figures/page_06.png}
    \caption{Procedimiento secuencial de pesaje de volquetes vacíos y cargados sobre PADs.}
\end{figure}

\section{DATOS RECOPILADOS}
\subsection{Datos Procesados}
Los datos registrados en campo correspondieron a: fecha y hora del pesaje, tipo de material transportado, asignación de pala y pases de carguío, condición cargado/vacío, lecturas de PADs en eje delantero y posterior (derecho e izquierdo), payload, tonelaje VIMS/Display, porcentaje de combustible y horómetro.

\subsection{Cálculo del Volquete Vacío y Cargado}
El cálculo del peso del volquete cargado y vacío se realizó mediante:
\begin{equation}
\text{Peso del equipo}_{\text{vacío/cargado}} = \text{ED}(\text{TI} + \text{TD}) + \text{EP}(\text{TI} + \text{TD})
\end{equation}
\noindent donde $\text{ED}$ es el eje delantero, $\text{EP}$ es el eje posterior, $\text{TI}$ es el tonelaje del PAD izquierdo y $\text{TD}$ es el tonelaje del PAD derecho.

El tonelaje de combustible se calculó mediante:
\begin{equation}
\text{Toneladas de Combustible} = (\text{Capacidad volumétrica}) \cdot (\text{Densidad}) \cdot (\%\text{Combustible})
\end{equation}
\noindent con densidad del combustible diésel igual a $0.00322\text{ tn/gl}$.

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.90\textwidth]{figures/page_07.png}
    \caption{Capacidad volumétrica del tanque de combustible por modelo de volquete (Galones).}
\end{figure}

\section{ANÁLISIS DE PESO VACIO, CARGADO Y PAYLOAD}
\subsection{Flota Caterpillar 797F}
En la Figura 5 se presenta el análisis de peso vacío/cargado y carga útil de la flota CAT 797F, contrastando tolvas Austin JEC vs Austin WESTECH.
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.90\textwidth]{figures/page_08.png}
    \caption{Pesaje y comparación de tolvas Austin JEC vs Austin WESTECH en flota CAT 797F.}
\end{figure}

\subsection{Flota Caterpillar 798AC y 793D}
En carga útil, el volquete V10 de tolva MP supera en 3 toneladas al volquete V11 de tolva HE en la flota CAT 798AC. En la flota CAT 793D, el volquete V120 supera en 5 toneladas al volquete V121 y cargó en promedio 9 toneladas más.
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.90\textwidth]{figures/page_09.png}
    \caption{Resultados de pesaje y tipos de tolva en flotas CAT 798AC y CAT 793D.}
\end{figure}

\subsection{Flota Komatsu 930E y 930E-4}
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.90\textwidth]{figures/page_10.png}
    \caption{Pesajes y modelos de tolva en flotas Komatsu 930E y 930E-4.}
\end{figure}

\subsection{Flota Komatsu 930E-4SE y 980E-4}
En la flota 930E-4SE, el volquete V116 supera en 6 toneladas al V115 en el eje trasero debido a dados instalados en su tolva DT Hiload Phase X.
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.90\textwidth]{figures/page_11.png}
    \caption{Pesaje de flota Komatsu 930E-4SE y dados instalados en volquete V116.}
\end{figure}

\subsection{Flota Komatsu 980E-5}
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.90\textwidth]{figures/page_12.png}
    \caption{Pesaje y análisis de distribución en posición 1 y 2 en flota Komatsu 980E-5.}
\end{figure}

\section{DISTRIBUCIÓN DE CARGA EN EL EJE DELANTERO}
\subsection{Flota de Mayor Capacidad de Tonelaje}
En la flota CAT 797F la posición 1 y 2 cargan en promedio 115 toneladas, con picos de hasta 134 toneladas, superando el target de Michelin (109 t) en tamaño 59/80R63 y al target de Bridgestone VREV (123.5 t). Esto se agrava en la rampa negativa hacia Cuajone Este.

\subsection{Flota de Menor Capacidad de Tonelaje}
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.90\textwidth]{figures/page_13.png}
    \caption{Análisis de distribución de peso en posición 1 y 2 (vacío y cargado).}
\end{figure}

\section{DISTRIBUCIÓN DE CARGA EN EL EJE POSTERIOR}
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.90\textwidth]{figures/page_14.png}
    \caption{Distribución de peso en posición 3\&4 vs 5\&6 (eje posterior cargado).}
\end{figure}

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.90\textwidth]{figures/page_15.png}
    \caption{Distribución de peso en posición 3\&4 vs 5\&6 (eje posterior vacío).}
\end{figure}

\section{DISTRIBUCIÓN DE CARGA POR EJE}
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.90\textwidth]{figures/page_16.png}
    \caption{Distribución de cargas por eje en vacío por modelo de volquete.}
\end{figure}

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.90\textwidth]{figures/page_17.png}
    \caption{Distribución de cargas por eje en condición de carga.}
\end{figure}

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.90\textwidth]{figures/page_18.png}
    \caption{Distribución de peso por eje individual (CAT 797F).}
\end{figure}

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.90\textwidth]{figures/page_19.png}
    \caption{Distribución de peso por eje (CAT 798AC y Komatsu 930E).}
\end{figure}

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.90\textwidth]{figures/page_20.png}
    \caption{Distribución de peso por eje (Komatsu 930E-4 y 980E-4).}
\end{figure}

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.90\textwidth]{figures/page_21.png}
    \caption{Distribución de peso por eje (Komatsu 980E-5 y CAT 793D).}
\end{figure}

\section{PALEROS CON MAYOR EFICIENCIA EN EL CENTRADO DE CARGA}
Los operadores Oscar Pinedo, Efraín Huaypuna y Edil Valdivia destacan con la mayor eficiencia en la distribución de carga.
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.90\textwidth]{figures/page_22.png}
    \caption{Ranking de operadores de pala con mejor eficiencia en el centrado de carga.}
\end{figure}

\section{PAYLOAD VS TONELAJE VIMS / PLM}
El tonelaje de la pantalla VIMS en el volquete V11 es mayor en 1.6\% que la carga real. En la flota CAT 793D, en el volquete V121 el sistema VIMS marca un 4.4\% menos respecto a la carga útil real. En la flota Komatsu 980 la variación entre el tonelaje Payload Meter y el payload real varía en más de 5\% en los volquetes V163, V164 y V165.

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.90\textwidth]{figures/page_23.png}
    \caption{Comparativa Tonelaje VIMS / PLM vs Payload real en flotas CAT y Komatsu.}
\end{figure}

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.90\textwidth]{figures/page_24.png}
    \caption{Comparativa Tonelaje PLM vs Payload en flota Komatsu 980E.}
\end{figure}

\section{CÁLCULO DEL PESO DEL PARACHOQUE}
El volquete V131 fue pesado 6 veces vacío: 3 veces sin parachoques y 3 veces con parachoques instalado el 15 de octubre del 2025. El primer pesaje fue con $92.61\%$ de combustible y el segundo con $94.00\%$.

\begin{equation}
\text{Peso Total}_1 = \text{Peso Vacío} + \text{Combustible}_1
\end{equation}
\begin{equation}
\text{Peso Total}_2 = \text{Peso Vacío} + \text{Combustible}_2 + \text{Parachoques}
\end{equation}
\begin{equation}
\text{Parachoque (t)} = \text{Peso Total}_2 - \text{Peso Total}_1 - \text{Combustible}_2 + \text{Combustible}_1
\end{equation}
\begin{equation}
\text{Parachoque (t)} = 299.30\text{ t} - 296.93\text{ t} - 94.00\%(T) + 92.61\%(T) = 2.37\text{ t} - 1.39\%(T)
\end{equation}
\begin{equation}
\text{Parachoque (t)} = 2.37\text{ t} - (1.39\% \times 2,000\text{ gl} \times 3.22\text{ kg/gl}) = 2.30\text{ t}
\end{equation}

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.90\textwidth]{figures/page_25.png}
    \caption{Memoria de cálculo del peso del parachoques y pesaje en báscula.}
\end{figure}

\section{CONCLUSIONES}
\begin{enumerate}
    \item El tonelaje añadido por la instalación del parachoques en los volquetes CATERPILLAR 797F le añade 2.3 toneladas al eje delantero.
    \item El tonelaje añadido al eje posterior por la instalación del liner en la flota KOMATSU 980E-4 significa un adicional de 15 toneladas.
    \item Los operadores de pala con mejor centrado de carga son Oscar Pinedo, Efraín Huaypuna y Edil Valdivia.
    \item En la flota CATERPILLAR 798 AC, el volquete V10 de tolva MP presenta 3 toneladas más de carga útil que el volquete V11 de tolva HE.
    \item En condición vacía, en las flotas CAT 797F y CAT 798AC existe un desbalance de más de 7 toneladas entre los neumáticos del eje delantero, debido a la ubicación del tanque de combustible.
    \item En condición de carga, los neumáticos de posición 1 de la flota CAT 797F soportan más de 115 toneladas, excediendo el target de Michelin en el tamaño 59/80R63 (109 t).
    \item Se debe inspeccionar las suspensiones y/o las unidades de tonelajes del sistema Payload Meter en los volquetes V108, V115, V112, V165, V163, V164 y V165.
\end{enumerate}

\end{document}
'''

with open("formateador/output/INFORME_PESAJE_VOLQUETES_CUAJONE_UNI.tex", "w", encoding="utf-8") as f:
    f.write(latex_content)

print("[OK] Archivo LaTeX oficial generado en: formateador/output/INFORME_PESAJE_VOLQUETES_CUAJONE_UNI.tex")
