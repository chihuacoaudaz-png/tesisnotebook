# Guía Maestra de Portabilidad y Despliegue en Cualquier Entorno (PC de Trabajo)

Esta guía permite clonar y ejecutar de forma 100% portable el entorno completo del **Sistema Agéntico de Tesis y Formateador Científico (UNI FIGMM)** en tu PC de trabajo o en cualquier nueva máquina, manteniendo intactas todas las herramientas, subagentes, habilidades, configuraciones MCP y conexiones a Google Drive y NotebookLM.

---

## 1. Arquitectura de Portabilidad

El repositorio ha sido estructurado para ser completamente autocontenido. Toda la configuración requerida por **Google Antigravity** y **Gemini CLI** reside dentro del mismo repositorio:

```text
c:\tesisnotebook\ (o ruta de clonación)
├── .agents/                        # Descubrimiento nativo de Antigravity (VCS compartible)
│   ├── agents/                     # Subagentes especializados (auditor, drive_notebooklm, teorico...)
│   ├── rules/                      # Reglas de operación obligatorias
│   ├── skills/                     # Habilidades procedimentales (drive_notebooklm_pipeline...)
│   └── mcp_config.json             # Configuración de servidores MCP a nivel de espacio de trabajo
├── .gemini/                        # Espejo compatible con Gemini CLI estándar
│   ├── agents/                     # Espejo de subagentes
│   ├── skills/                     # Espejo de habilidades
│   └── mcp_config.json             # Espejo de configuración MCP
├── config/                         # Configuraciones maestras del proyecto
│   ├── mcp/notebooklm/             # 34 esquemas JSON oficiales y manual de herramientas MCP
│   └── mcp_config.json             # Manifiesto JSON de servidores MCP
├── data/scraped_theses/            # 25 tesis descargadas en PDF con metadatos Dublin Core
├── docs/                           # Documentación canónica y reportes de auditoría
│   ├── formateador_indices/        # Modelos canónicos de índices y esquema JSON
│   ├── metodologia_investigacion/  # Guía metodológica oficial UNI FIGMM (Dra. Rosario Martínez)
│   ├── AUDITORIA_PROMPT_CONFORMIDAD.md # Certificación quíntuple formal
│   └── GUIA_PORTABILIDAD_Y_DESPLIEGUE.md # Este manual
├── src/tools/                      # Herramientas de automatización en Python
│   ├── drive_uploader.py           # Uploader modular a Google Drive vía Playwright
│   ├── upload_theses_to_drive.py   # Uploader batch de las 25 tesis oficiales
│   └── inspect_notebooks.py        # Diagnóstico e inspección de cuadernos
├── AGENTS.md / GEMINI.md           # Reglas de operación obligatorias inyectadas en el prompt
└── requirements.txt                # Dependencias exactas de Python
```

---

## 2. Requisitos Previos en la PC de Trabajo

1. **Python 3.11 o superior:** Con `pip` configurado en las variables de entorno.
2. **Git:** Instalado y configurado.
3. **Google Chrome o Chromium:** Requerido por Playwright.
4. **Antigravity CLI / Gemini CLI:** Instalado globalmente.

---

## 3. Despliegue Rápido Paso a Paso (Quickstart)

### Paso 1: Clonar el Repositorio desde GitHub
Abre la terminal (PowerShell o Bash) en tu PC de trabajo y ejecuta:
```bash
git clone https://github.com/chihuacoaudaz-png/tesisnotebook.git
cd tesisnotebook
```

### Paso 2: Instalar Dependencias de Python
Instala todas las librerías necesarias (incluyendo `notebooklm-py`, `playwright`, `jsonschema`, etc.):
```bash
pip install -r requirements.txt
```

### Paso 3: Instalar Navegadores de Playwright
Playwright requiere descargar los binarios de Chromium para la automatización web:
```bash
playwright install chromium
```

### Paso 4: Autenticar Sesión Google (NotebookLM + Drive)
Para vincular tu cuenta (`chihuacoaudaz@gmail.com`) y crear el archivo de sesión:
```bash
notebooklm login
```
*Se abrirá una ventana de Chromium. Inicia sesión con tus credenciales de Google.*  
Una vez completado el inicio de sesión, las credenciales quedarán almacenadas en:
`~/.notebooklm/profiles/default/storage_state.json`

Verifica que el estado de salud sea óptimo:
```bash
notebooklm doctor
```

---

## 4. Conexión a Google Drive sin Errores OAuth 403

### Por qué funciona:
Google restringe el alcance `drive` para clientes OAuth externos no verificados (`403: restricted_client`). Nuestro pipeline resuelve esto reutilizando la sesión del navegador (`storage_state.json`), operando con la identidad legítima de tu cuenta en la web.

### Cómo subir nuevos archivos a Drive:
Para subir un lote de archivos a la carpeta oficial de Drive (`AGENTE TESIS/TESIS PARA SCRAPEAR INDICE`):
```bash
# Opción A: Subir los 25 PDFs oficiales del repositorio
python src/tools/upload_theses_to_drive.py

# Opción B: Subir archivos arbitrarios con el módulo genérico
python src/tools/drive_uploader.py --dir "ruta/a/mis/pdfs" --pattern "*.pdf"
```

---

## 5. Conexión y Uso de NotebookLM como Fuente de Verdad

### Cuadernos Oficiales en tu Cuenta:
- **Marco Metodológico UNI FIGMM (Dra. Rosario Martínez):** `769227ea-9b15-4fbc-a382-b14cd5e7435f`
- **Tesis Central Lincuna 2026 (P&V y Sobrerotura):** `780ac1ad-e15b-4801-be5e-44131370dfbc`

### Consultas Libres de Alucinación (CLI / MCP):
```bash
# Consultar el marco metodológico
notebooklm ask "¿Cuáles son los 8 ítems del Formato 1?" -n 769227ea-9b15-4fbc-a382-b14cd5e7435f

# Ejecutar investigación profunda (Deep Research) e importar fuentes automáticamente
notebooklm source add-research "Control de sobrerotura en taladros largos y precorte en minería subterránea" --mode deep --import-all -n 780ac1ad-e15b-4801-be5e-44131370dfbc
```

---

## 6. Ejecución del Agente en tu PC de Trabajo

Al iniciar **Antigravity CLI** o **Gemini CLI** dentro de la carpeta `tesisnotebook`:
1. El agente detecta automáticamente `.agents/` y `.gemini/`.
2. Se cargan las reglas obligatorias de `AGENTS.md` y `GEMINI.md`.
3. Se registran los subagentes especializados:
   - `auditor_cumplimiento`: Auditor riguroso de prompts y directivas.
   - `agente_drive_notebooklm`: Gestor de subida a Drive e ingesta a NotebookLM.
   - `Teorico` / `InvestigadorTeorico`: Redactor y deducidor de bases teóricas.
4. Se registra el servidor MCP `notebooklm-mcp` configurado en `config/mcp_config.json`.
5. Se activan las habilidades `drive-notebooklm-pipeline` y `teorico`.
