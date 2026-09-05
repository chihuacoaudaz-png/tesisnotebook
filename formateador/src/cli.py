# -*- coding: utf-8 -*-
"""
CLI PRINCIPAL DEL AGENTE FORMATEADOR UNI
Ejecuta el ciclo completo:
1. Ingesta / Formateo al estándar UNI FIGMM.
2. Compilación a PDF de alta resolución.
3. Auditoría Visual Red Team (Renderizado de páginas a 300 DPI + detección de anomalías).
4. Emisión del Dictamen Oficial QA/QC.
"""

import os
import sys
import argparse
from compiler.compile_pdf import compile_latex, convert_docx_to_pdf_word
from auditor.visual_auditor import render_pdf_to_images, audit_visual_layout, generate_audit_report

def run_pipeline(input_file, output_dir="output", dpi=300):
    print("==================================================================")
    print("  AGENTE FORMATEADOR UNI - SISTEMA DE MAQUETACION Y QA/QC VISUAL  ")
    print("==================================================================")
    
    if not os.path.exists(input_file):
        print(f"[ERROR] No se encontro el archivo de entrada: {input_file}")
        sys.exit(1)
        
    os.makedirs(output_dir, exist_ok=True)
    renders_dir = os.path.join(output_dir, "renders")
    
    pdf_target = None
    if input_file.endswith(".pdf"):
        pdf_target = input_file
    elif input_file.endswith(".docx"):
        base_name = os.path.splitext(os.path.basename(input_file))[0]
        pdf_target = os.path.join(output_dir, f"{base_name}.pdf")
        convert_docx_to_pdf_word(input_file, pdf_target)
    elif input_file.endswith(".tex"):
        pdf_target = compile_latex(input_file, output_dir=output_dir)
        
    if not pdf_target or not os.path.exists(pdf_target):
        print(f"[ERROR] No se pudo obtener el PDF compilado para auditar.")
        sys.exit(1)
        
    print(f"\n[*] PASO 2: Ejecutando Auditoria Visual Red Team sobre {pdf_target}...")
    rendered_images = render_pdf_to_images(pdf_target, output_dir=renders_dir, dpi=dpi)
    
    print(f"[*] PASO 3: Analizando metricas de maquetacion y margenes...")
    audit_results = audit_visual_layout(pdf_target, rendered_images)
    
    report_file = os.path.join(output_dir, "REPORTE_AUDITORIA_VISUAL.md")
    generate_audit_report(pdf_target, audit_results, report_path=report_file)
    
    print("\n==================================================================")
    print(f"[DICTAMEN QA/QC] Proceso finalizado con exito.")
    print(f"- Total Paginas Fisicas: {audit_results['total_pages']}")
    print(f"- Renders generados en:  {renders_dir}")
    print(f"- Informe de Auditoria:  {report_file}")
    print("==================================================================")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Agente Formateador UNI - Pipeline de Maquetacion y Auditoria")
    parser.add_argument("--input", required=False, default="../output/PLAN_DE_TESIS_OFICIAL_UNI_LINCUNA.pdf", help="Archivo de entrada (.pdf, .docx, .tex)")
    parser.add_argument("--output", required=False, default="output", help="Directorio de salida")
    parser.add_argument("--dpi", type=int, required=False, default=300, help="Resolucion de renders (DPI)")
    args = parser.parse_args()
    
    run_pipeline(args.input, output_dir=args.output, dpi=args.dpi)
