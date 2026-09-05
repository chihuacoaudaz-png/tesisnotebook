# PMO STATE TRACKER - AGENTE FORMATEADOR UNI

- **PROYECTO:** Sistema Autónomo de Formateo y Maquetación Oficial UNI FIGMM.
- **OBJETIVO:** Transformación y diagramación automatizada de investigaciones a formato oficial UNI (LaTeX + PDF) con auditoría visual Red Team.
- **ESTADO ACTUAL:** TRABAJO DE INVESTIGACIÓN CUAJONE 2025 FORMATEADO Y CERTIFICADO

## WORK BREAKDOWN STRUCTURE (WBS) & QUALITY GATES
- [x] WBS 1.0: Definición de Normativa y Resolución Rectoral UNI (`RESOLUCION_RECTORAL_FORMATO_UNI.md`) -> Aprobado.
- [x] WBS 2.0: Construcción de Plantillas Maestras LaTeX (`templates/uni_tesis.cls`, `preamble.tex`, `portada.tex`) -> Aprobado.
- [x] WBS 3.0: Implementación del Compilador Automatizado (`src/compiler/compile_pdf.py`) -> Aprobado.
- [x] WBS 4.0: Implementación del Motor de Auditoría Visual e Inspección de Renders (`src/auditor/visual_auditor.py`) -> Aprobado.
- [x] WBS 5.0: Ingesta y Formateo del Trabajo `formateador/input/proyectoCJN.pdf` -> Aprobado.
- [x] WBS 6.0: Compilación a PDF (28 págs físicas) y Auditoría Visual Red Team 300 DPI (`output/REPORTE_AUDITORIA_VISUAL.md`) -> Aprobado.
