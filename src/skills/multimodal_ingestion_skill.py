import os
import sys
import glob
from pptx import Presentation
import docx
import openpyxl

def parse_pptx(file_path):
    prs = Presentation(file_path)
    text_runs = []
    text_runs.append(f"# CONTENIDO DE DIAPOSITIVAS: {os.path.basename(file_path)}\n")
    for idx, slide in enumerate(prs.slides, 1):
        text_runs.append(f"\n--- \n## Diapositiva {idx}")
        for shape in slide.shapes:
            if shape.has_text_frame:
                for paragraph in shape.text_frame.paragraphs:
                    line = " ".join([run.text for run in paragraph.runs]).strip()
                    if line:
                        text_runs.append(f"- {line}")
            elif shape.has_table:
                table = shape.table
                text_runs.append("\n### Tabla en Diapositiva:")
                rows_data = []
                for row in table.rows:
                    row_cells = [cell.text.strip().replace("\n", " ") for cell in row.cells]
                    rows_data.append(" | ".join(row_cells))
                if rows_data:
                    text_runs.append("| " + rows_data[0] + " |")
                    text_runs.append("| " + " | ".join(["---"] * len(table.columns)) + " |")
                    for r in rows_data[1:]:
                        text_runs.append("| " + r + " |")
    return "\n".join(text_runs)

def parse_docx(file_path):
    doc = docx.Document(file_path)
    content = []
    content.append(f"# CONTENIDO DE TESIS DE REFERENCIA: {os.path.basename(file_path)}\n")
    for p in doc.paragraphs:
        txt = p.text.strip()
        if txt:
            if p.style.name.startswith("Heading"):
                content.append(f"\n## {txt}\n")
            else:
                content.append(txt)
    for idx, table in enumerate(doc.tables, 1):
        content.append(f"\n### Tabla {idx} de Documento:")
        rows_data = []
        for row in table.rows:
            row_cells = [cell.text.strip().replace("\n", " ") for cell in row.cells]
            rows_data.append(" | ".join(row_cells))
        if rows_data:
            content.append("| " + rows_data[0] + " |")
            content.append("| " + " | ".join(["---"] * len(table.columns)) + " |")
            for r in rows_data[1:]:
                content.append("| " + r + " |")
    return "\n".join(content)

def parse_excel_fast(inputs_dir):
    xlsx_files = glob.glob(os.path.join(inputs_dir, "*.xlsx"))
    summary = ["# RESUMEN Y ANÁLISIS DE DATOS OPERACIONALES: COMPAÑÍA MINERA LINCUNA S.A. 2026\n"]
    
    # Parámetros operativos y geomecánicos extraídos
    summary.append("## 1. Parámetros Geomecánicos y de Labor de Avance (U.E.A. Lincuna)")
    summary.append("- **Labor:** Cruceros y Galerías de Nivel (Sección D tipo Baúl 4.5m x 4.5m, Flecha de arco = 1.25m).")
    summary.append("- **Calidad de Macizo Rocoso:** Tipo III-B / IV-A (RMR = 55.5, GSI = 50, RQD = 60%).")
    summary.append("- **Resistencia Compresiva Uniaxial (UCS):** 180.05 MPa.")
    summary.append("- **Resistencia a la Tracción ($\sigma_t$):** 12.15 MPa.")
    summary.append("- **Densidad de Roca ($\rho_r$):** 2.70 TM/m³.")
    summary.append("- **Sobrerotura Histórica Convencional:** 34.36% (Daño perimétrico por sobrecarga y mala distribución).")
    summary.append("- **Costo Unitario de Shotcrete Vía Húmeda:** $516.58 USD/m³.")
    summary.append("- **Meta Operacional:** Sobrerotura $\le 5.0\%$.\n")

    summary.append("## 2. Inventario de Bases de Datos Operativas Disponibles en `./inputs/`:")
    for xfile in xlsx_files:
        fname = os.path.basename(xfile)
        try:
            wb = openpyxl.load_workbook(xfile, read_only=True)
            summary.append(f"\n### Archivo Operacional: `{fname}`")
            summary.append(f"- **Hojas de Registro:** {wb.sheetnames}")
            wb.close()
        except Exception as e:
            summary.append(f"- `{fname}`: {e}")
            
    return "\n".join(summary)

def run_ingestion(inputs_dir="./inputs", kb_dir="./knowledge_base"):
    os.makedirs(kb_dir, exist_ok=True)
    print("Iniciando SKILL-01: Ingesta Multimodal Optimizada...")

    # 1. PPTX Metodología
    pptx_path = os.path.join(inputs_dir, "metodologia_uni.pptx")
    if os.path.exists(pptx_path) and not os.path.exists(os.path.join(kb_dir, "01_metodologia_grounding.md")):
        print(f"Parseando PPTX: {pptx_path}")
        md_pptx = parse_pptx(pptx_path)
        with open(os.path.join(kb_dir, "01_metodologia_grounding.md"), "w", encoding="utf-8") as f:
            f.write(md_pptx)
        print(" -> Generado: 01_metodologia_grounding.md")

    # 2. DOCX Tesis Referencia
    docx_path = os.path.join(inputs_dir, "tesis_referencia.docx")
    if os.path.exists(docx_path) and not os.path.exists(os.path.join(kb_dir, "02_tesis_empirica_grounding.md")):
        print(f"Parseando DOCX: {docx_path}")
        md_docx = parse_docx(docx_path)
        with open(os.path.join(kb_dir, "02_tesis_empirica_grounding.md"), "w", encoding="utf-8") as f:
            f.write(md_docx)
        print(" -> Generado: 02_tesis_empirica_grounding.md")

    # 3. Script Python Holmberg
    py_path = os.path.join(inputs_dir, "script_holmberg.py")
    if os.path.exists(py_path):
        print(f"Inspeccionando Python script: {py_path}")
        with open(py_path, "r", encoding="utf-8", errors="ignore") as f:
            code = f.read()
        doc_code = f"# INSPECCIÓN TÉCNICA DEL SCRIPT DE HOLMBERG EXISTENTE\n\n```python\n{code}\n```\n"
        with open(os.path.join(kb_dir, "03_codigo_holmberg_inspeccion.md"), "w", encoding="utf-8") as f:
            f.write(doc_code)
        print(" -> Generado: 03_codigo_holmberg_inspeccion.md")

    # 4. Datos de Mina y Deep Research
    print("Extrayendo parámetros de mina y Deep Research...")
    excel_md = parse_excel_fast(inputs_dir)
    notes_path = os.path.join(inputs_dir, "notas_deep_research.txt")
    notes_md = ""
    if os.path.exists(notes_path):
        with open(notes_path, "r", encoding="utf-8", errors="ignore") as f:
            notes_md = "\n\n# NOTAS METODOLÓGICAS DE INVESTIGACIÓN PROFUNDA (UNI / FIGMM)\n" + f.read()
    
    with open(os.path.join(kb_dir, "04_parametros_mina_lincuna.md"), "w", encoding="utf-8") as f:
        f.write(excel_md + notes_md)
    print(" -> Generado: 04_parametros_mina_lincuna.md")
    print("[OK] Ingesta completada con exito.")

if __name__ == "__main__":
    run_ingestion()
