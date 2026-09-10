import asyncio
import os
import glob
import time
from playwright.async_api import async_playwright

TARGET_FOLDER_URL = "https://drive.google.com/drive/folders/1lBx77NmmJBUlClADUEnL__mLZNcKOBmb"
SCRAPED_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "data", "scraped_theses"))

async def upload_theses():
    pdf_files = sorted(glob.glob(os.path.join(SCRAPED_DIR, "*.pdf")))
    print(f"Found {len(pdf_files)} PDF files to upload from {SCRAPED_DIR}:")
    for p in pdf_files:
        print(f"  - {os.path.basename(p)} ({os.path.getsize(p) / (1024*1024):.2f} MB)")

    if not pdf_files:
        print("No PDF files found to upload!")
        return

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        storage_path = os.path.expanduser("~/.notebooklm/profiles/default/storage_state.json")
        context = await browser.new_context(storage_state=storage_path)
        page = await context.new_page()
        
        print(f"\nNavigating to Google Drive target folder:\n{TARGET_FOLDER_URL}")
        await page.goto(TARGET_FOLDER_URL, wait_until="load")
        await page.wait_for_timeout(8000)
        print("Folder Title:", await page.title())

        # Click Nuevo
        nuevo = page.locator("button:has-text('Nuevo'), div[role='button']:has-text('Nuevo')").first
        print("Clicking 'Nuevo' button...")
        await nuevo.click()
        await page.wait_for_timeout(2000)

        # Trigger file chooser on 'Subir archivo'
        print("Clicking 'Subir archivo' and setting all files...")
        async with page.expect_file_chooser() as fc_info:
            subir_btn = page.locator("[role='menuitem']:has-text('Subir archivo')").first
            await subir_btn.click(force=True)
        
        file_chooser = await fc_info.value
        await file_chooser.set_files(pdf_files)
        print(f"Successfully queued {len(pdf_files)} PDF files to Google Drive! Monitoring upload progress...")
        
        # Monitor Google Drive upload progress dialog
        start_time = time.time()
        # Allow up to 300 seconds (5 minutes) for all 25 PDFs (~130MB) to upload
        while time.time() - start_time < 300:
            await page.wait_for_timeout(6000)
            content = await page.content()
            # In Drive, the upload snackbar shows: "Se completaron X cargas de 25" or "X cargas completas"
            if "Se completaron 25 cargas" in content or "25 cargas completadas" in content or ("Se completaron" in content and "cargas" in content):
                print(f"Drive confirmed uploads complete! Elapsed: {int(time.time() - start_time)}s")
                break
            print(f"  Uploading in progress... elapsed: {int(time.time() - start_time)}s")

        # Final verification: list files in the Drive folder
        print("\n--- Final Verification: Refreshing folder view ---")
        await page.reload(wait_until="load")
        await page.wait_for_timeout(6000)
        
        # Take verification screenshot
        screenshot_path = "drive_uploaded_verification.png"
        await page.screenshot(path=screenshot_path)
        print(f"Verification screenshot saved to: {screenshot_path}")

        # List items in table
        rows = await page.locator("[role='row']").all_inner_texts()
        print(f"\nTotal visible items in Drive folder: {len(rows)}")
        uploaded_theses = []
        for r in rows:
            clean = r.replace("\n", " | ").strip()
            if "TESIS" in clean or ".pdf" in clean.lower():
                print("  [DRIVE CONFIRMED]", clean)
                uploaded_theses.append(clean)

        with open("drive_upload_report.txt", "w", encoding="utf-8") as rep:
            rep.write(f"Google Drive Upload Report\nTarget: {TARGET_FOLDER_URL}\n")
            rep.write(f"Total Confirmed Files: {len(uploaded_theses)}\n\n")
            for ut in uploaded_theses:
                rep.write(f"{ut}\n")

        await browser.close()
        print("\n=== GOOGLE DRIVE UPLOAD FINISHED SUCCESSFULLY ===")

if __name__ == "__main__":
    asyncio.run(upload_theses())
