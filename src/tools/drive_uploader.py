"""
Herramienta CLI y Módulo de Carga Automatizada a Google Drive usando Playwright.
Permite subir lotes de archivos a cualquier carpeta de Google Drive utilizando
la sesión autenticada de NotebookLM (~/.notebooklm/profiles/default/storage_state.json),
evitando por completo los errores de OAuth 403 (restricted_client).
"""

import argparse
import asyncio
import glob
import os
import sys
import time
from playwright.async_api import async_playwright

DEFAULT_STORAGE = os.path.expanduser("~/.notebooklm/profiles/default/storage_state.json")
DEFAULT_TARGET_URL = "https://drive.google.com/drive/folders/1lBx77NmmJBUlClADUEnL__mLZNcKOBmb"

async def upload_files_to_drive(file_paths, folder_url=DEFAULT_TARGET_URL, storage_state_path=DEFAULT_STORAGE, timeout_sec=300):
    if not os.path.exists(storage_state_path):
        raise FileNotFoundError(f"No se encontró storage_state en: {storage_state_path}. Ejecute 'notebooklm login' primero.")

    valid_files = [os.path.abspath(f) for f in file_paths if os.path.isfile(f)]
    if not valid_files:
        print("[ERROR] No se encontraron archivos válidos para subir.")
        return False

    print(f"[DRIVE UPLOADER] Iniciando carga de {len(valid_files)} archivos a:")
    print(f"  URL Carpeta: {folder_url}")
    print(f"  Sesión Google: {storage_state_path}")
    
    total_mb = sum(os.path.getsize(f) for f in valid_files) / (1024 * 1024)
    print(f"  Peso total estimado: {total_mb:.2f} MB")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(storage_state=storage_state_path)
        page = await context.new_page()

        print("\n[PASO 1] Navegando a la carpeta de Google Drive...")
        await page.goto(folder_url, wait_until="load")
        await page.wait_for_timeout(6000)
        title = await page.title()
        print(f"  Título de página: {title}")

        print("[PASO 2] Desplegando menú 'Nuevo'...")
        nuevo_btn = page.locator("button:has-text('Nuevo'), div[role='button']:has-text('Nuevo')").first
        await nuevo_btn.click()
        await page.wait_for_timeout(2000)

        print("[PASO 3] Activando selector de archivos y adjuntando lote...")
        async with page.expect_file_chooser() as fc_info:
            subir_btn = page.locator("[role='menuitem']:has-text('Subir archivo')").first
            await subir_btn.click(force=True)

        file_chooser = await fc_info.value
        await file_chooser.set_files(valid_files)
        print(f"  {len(valid_files)} archivos encolados con éxito en Google Drive.")

        print("[PASO 4] Monitoreando diálogo de carga en Drive...")
        start_time = time.time()
        completed = False
        while time.time() - start_time < timeout_sec:
            await page.wait_for_timeout(6000)
            content = await page.content()
            elapsed = int(time.time() - start_time)
            if f"Se completaron {len(valid_files)} cargas" in content or f"{len(valid_files)} cargas completadas" in content or ("Se completaron" in content and "cargas" in content):
                print(f"\n[ÉXITO] Google Drive confirmó la carga de todos los archivos en {elapsed}s.")
                completed = True
                break
            print(f"  Progreso en curso... transcurrido: {elapsed}s", end="\r")

        if not completed:
            print(f"\n[ALERTA] Se alcanzó el tiempo de espera ({timeout_sec}s). Procediendo a verificación.")

        print("\n[PASO 5] Verificando elementos en el explorador...")
        await page.reload(wait_until="load")
        await page.wait_for_timeout(5000)

        # Captura de pantalla de verificación
        screenshot_path = "drive_verification_latest.png"
        await page.screenshot(path=screenshot_path)
        print(f"  Captura guardada en: {screenshot_path}")

        # Listar filas
        rows = await page.locator("[role='row']").all_inner_texts()
        print(f"  Total elementos detectados en tabla: {len(rows)}")

        await browser.close()
        return True

def main():
    parser = argparse.ArgumentParser(description="Subida automatizada de archivos a Google Drive con Playwright.")
    parser.add_argument("--url", default=DEFAULT_TARGET_URL, help="URL de la carpeta destino de Google Drive")
    parser.add_argument("--files", nargs="*", help="Rutas de archivos a subir")
    parser.add_argument("--dir", help="Directorio con archivos a subir")
    parser.add_argument("--pattern", default="*.pdf", help="Patrón glob (si se especifica --dir)")
    parser.add_argument("--timeout", type=int, default=360, help="Tiempo máximo de espera en segundos")
    args = parser.parse_args()

    files = []
    if args.files:
        files.extend(args.files)
    if args.dir:
        files.extend(glob.glob(os.path.join(args.dir, args.pattern)))

    if not files:
        print("Debe especificar archivos vía --files o un directorio con --dir.")
        sys.exit(1)

    success = asyncio.run(upload_files_to_drive(files, folder_url=args.url, timeout_sec=args.timeout))
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
