---
name: drive-notebooklm-pipeline
description: End-to-end pipeline to synchronize local research papers with Google Drive using Playwright session state, ingest sources into NotebookLM, execute grounded queries, and persist web-visible Studio notes.
---

# Pipeline Integral: Google Drive + NotebookLM + Deep Research

Esta habilidad define el flujo de trabajo estándar para la adquisición, almacenamiento en la nube (Google Drive), ingesta documental en Google NotebookLM, consultas de verdad absoluta (grounding) y persistencia de notas para el proyecto de tesis UNI FIGMM.

---

## 1. Arquitectura de Autenticación Unificada

### El Problema de OAuth 403 `restricted_client`
Las aplicaciones externas que solicitan el alcance `https://www.googleapis.com/auth/drive` sufren rechazo `403: restricted_client` si el Client ID no ha superado la verificación de seguridad de Google Cloud.

### La Solución: Sesión Reutilizable de Playwright
El comando `notebooklm login` autentica la cuenta del usuario (`chihuacoaudaz@gmail.com`) en Chromium y almacena las cookies de sesión y tokens en:
`~/.notebooklm/profiles/default/storage_state.json` (en Windows: `C:\Users\<usuario>\.notebooklm\profiles\default\storage_state.json`).

Dado que esta sesión pertenece al navegador de Google, tiene **permisos completos y legítimos para operar tanto en Google Drive como en NotebookLM**.

---

## 2. Flujo Automatizado de Carga a Google Drive

### Script de Referencia: `src/tools/upload_theses_to_drive.py`
Para subir archivos en lote a Google Drive sin depender de APIs restringidas:

```python
import asyncio, os, glob, time
from playwright.async_api import async_playwright

TARGET_FOLDER_URL = "https://drive.google.com/drive/folders/1lBx77NmmJBUlClADUEnL__mLZNcKOBmb"
STORAGE_STATE = os.path.expanduser("~/.notebooklm/profiles/default/storage_state.json")

async def upload_batch(files_to_upload):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(storage_state=STORAGE_STATE)
        page = await context.new_page()
        
        # 1. Navegar a la carpeta objetivo
        await page.goto(TARGET_FOLDER_URL, wait_until="load")
        await page.wait_for_timeout(6000)
        
        # 2. Desplegar menú 'Nuevo'
        nuevo_btn = page.locator("button:has-text('Nuevo'), div[role='button']:has-text('Nuevo')").first
        await nuevo_btn.click()
        await page.wait_for_timeout(2000)
        
        # 3. Interceptar selector de archivos con force=True
        async with page.expect_file_chooser() as fc_info:
            subir_btn = page.locator("[role='menuitem']:has-text('Subir archivo')").first
            await subir_btn.click(force=True)
        
        file_chooser = await fc_info.value
        await file_chooser.set_files(files_to_upload)
        
        # 4. Monitorear progreso de subida en snackbar
        start_time = time.time()
        while time.time() - start_time < 300:
            await page.wait_for_timeout(6000)
            content = await page.content()
            if "cargas completadas" in content or "Se completaron" in content:
                break
                
        # 5. Captura y verificación en el DOM
        await page.reload(wait_until="load")
        await page.wait_for_timeout(5000)
        await page.screenshot(path="drive_uploaded_verification.png")
        await browser.close()
```

### Reglas Críticas de Interacción con Drive:
1. **Selector de Subida:** Debe usarse `page.locator("[role='menuitem']:has-text('Subir archivo')").first.click(force=True)`. El parámetro `force=True` es indispensable porque las superposiciones transparentes del menú contextual pueden interceptar el click.
2. **Carpeta Exclusiva:** Solo escribir en `AGENTE TESIS/TESIS PARA SCRAPEAR INDICE` (`1lBx77NmmJBUlClADUEnL__mLZNcKOBmb`). Nunca tocar las carpetas adyacentes de borradores o tesis finales.

---

## 3. Ingesta y Grounding en NotebookLM

### Cuadernos de Referencia
* **Marco Metodológico de Posgrado:** `769227ea-9b15-4fbc-a382-b14cd5e7435f`
* **Tesis Núcleo Lincuna 2026:** `780ac1ad-e15b-4801-be5e-44131370dfbc`

### Ingesta de Fuentes
1. **Vía MCP:**
   - `source_add`: Permite añadir textos en formato markdown o URLs.
   - `source_add_drive_file`: Permite incorporar archivos directamente desde Google Drive pasando el `drive_document_id`.
2. **Vía Deep Research (Modo Deep Obligatorio):**
   ```bash
   notebooklm source add-research "<tema_o_pregunta>" --mode deep --import-all -n <notebook_id>
   ```

### Consultas de Verdad Absoluta (`chat_ask`)
- Siempre invocar `chat_ask` con `notebook="<notebook_id>"` y `references="lite"` o `"full"`.
- Analizar las citas numéricas devueltas (`[1]`, `[2]`, etc.) para contrastar con las fuentes originales.
- Si una afirmación no cuenta con un pasaje citado que la respalde, **se descarta por considerarse alucinación**.

### Persistencia de Notas en el Panel Web (`note_save`)
Para que el usuario vea el avance en la interfaz web de NotebookLM:
- Usar `note_save` omitiendo el argumento `note` (modo creación).
- Suministrar `notebook`, `title` y `content`.
- Esto genera un nodo permanente en la sección Studio accesible desde cualquier navegador.

---

## 4. Auditoría Quíntuple de Conformidad
Antes de dar por concluido cualquier lote de trabajo, ejecutar la verificación en 5 fases:
1. **Fase 1 (Drive):** Verificación de conteo y presencia de archivos mediante scraping de filas DOM (`[role='row']`).
2. **Fase 2 (NotebookLM):** Verificación de fuentes (`source_list`) y existencia de notas en Studio (`studio_list`).
3. **Fase 3 (Metodología):** Verificación de formulación formal del título, problema, objetivos e hipótesis según Dra. Rosario Martínez.
4. **Fase 4 (Formateador):** Verificación de validez del esquema JSON contra `thesis_input_schema.json`.
5. **Fase 5 (VCS):** Verificación de limpieza del árbol git (`git status`) y sincronización con GitHub (`git push origin master`).
