# SISTEMA AGÉNTICO FORMATEADOR OFICIAL UNI FIGMM

Sistema autónomo especializado en dar el **Formato Oficial de Tesis y Planes de Tesis de la Universidad Nacional de Ingeniería (UNI FIGMM)** a cualquier investigación académica, integrando compilación de alta fidelidad y auditoría visual Red Team.

---

## 1. ESTRUCTURA DEL PROYECTO

```
formateador/
├── RESOLUCION_RECTORAL_FORMATO_UNI.md  # Normativa oficial UNI de formato y márgenes
├── AGENTS.md                           # Reglas de operación del agente formateador
├── GEMINI.md                           # Reglas de operación sincronizadas
├── STATE.md                            # Tracker de estado y WBS del PMO
├── AUDIT_LOG.md                        # Registro de auditorías y control QA/QC
├── README.md                           # Guía general de uso
├── templates/                          # Plantillas maestras oficiales en LaTeX
│   ├── preamble.tex                    # Paquetes matemáticos, márgenes y tipografía
│   ├── portada_uni.tex                 # Portada institucional reglamentaria
│   └── main_template.tex               # Estructura base completa
├── src/                                # Código fuente del motor de formateo
│   ├── cli.py                          # Interfaz de línea de comandos unificada
│   ├── compiler/
│   │   └── compile_pdf.py              # Compilador a PDF (LaTeX / Word COM)
│   ├── auditor/
│   │   └── visual_auditor.py           # Renderizado 300 DPI y auditoría visual
│   └── engine/
│       └── formatter_engine.py         # Motor de maquetación y ensamblado
├── subagents/                          # Definición de roles agénticos especializados
│   ├── maquetador_latex_uni.md         # Subagente Maquetador LaTeX
│   └── auditor_visual_esceptico.md     # Subagente Red Team Escéptico
└── output/                             # Directorio de entregables formateados
    ├── renders/                        # Imágenes PNG (300 DPI) de cada página
    └── REPORTE_AUDITORIA_VISUAL.md     # Dictamen oficial de auditoría visual
```

---

## 2. REGLA DE ORO DEL FORMATEADOR
El agente **NO MODIFICA** la investigación original, datos numéricos, ecuaciones ni conclusiones del autor. Su función es estrictamente de:
1. Diagramación y maquetación visual.
2. Estructuración tipográfica bajo la **Resolución Rectoral UNI**.
3. Compilación a PDF de alta resolución.
4. Auditoría visual Red Team página por página.

---

## 3. CÓMO EJECUTAR EL FORMATEADOR Y AUDITOR VISUAL

```powershell
# 1. Ejecutar el pipeline completo sobre un PDF o DOCX existente:
cd c:\tesisnotebook\formateador
python src/cli.py --input "../output/PLAN_DE_TESIS_OFICIAL_UNI_LINCUNA.pdf" --dpi 300

# 2. El sistema generará automáticamente:
#    - Renders PNG de 300 DPI de cada página en: output/renders/page_001.png, page_002.png...
#    - Reporte de Auditoría Visual en: output/REPORTE_AUDITORIA_VISUAL.md
```
