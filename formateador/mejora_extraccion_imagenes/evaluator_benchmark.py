# -*- coding: utf-8 -*-
"""
EVALUADOR DE BENCHMARK Y APRENDIZAJE DE EXTRACCIÓN DE IMÁGENES
Compara métricamente las imágenes generadas por el algoritmo inicial
frente a las imágenes de validación manual (Ground Truth).
"""

import os
from PIL import Image

def analyze_figure_catalog():
    figuras_dir = "formateador/figuras"
    backup_dir = "formateador/backup_figuras_usuario"
    
    if not os.path.exists(figuras_dir):
        print(f"[ERROR] No existe {figuras_dir}")
        return
        
    print("==================================================================")
    print("  BENCHMARK Y MÉTRICAS DE CALIBRACIÓN DE IMÁGENES (GROUND TRUTH)  ")
    print("==================================================================")
    
    files = sorted(os.listdir(figuras_dir))
    paired_count = 0
    single_count = 0
    
    print(f"\nTotal de figuras analizadas: {len(files)}")
    print(f"{'Nombre':20s} {'Dimensiones (px)':20s} {'Aspect Ratio':15s} {'Tipo Layout'}")
    print("-" * 70)
    
    for f in files:
        if not f.endswith(".png"):
            continue
        fp = os.path.join(figuras_dir, f)
        with Image.open(fp) as img:
            w, h = img.size
            ar = w / h if h > 0 else 0
            
            # Clasificar si corresponde a par o individual
            # Figuras 33 a 48 y 50 a 53 son pareadas
            is_paired = False
            for num in range(33, 49):
                if f"figura_{num:02d}" in f:
                    is_paired = True
                    break
            if "figura_50" in f or "figura_51" in f or "figura_52" in f or "figura_53" in f:
                is_paired = True
                
            layout = "Pareado (2-col)" if is_paired else "Unitario (1-col)"
            if is_paired:
                paired_count += 1
            else:
                single_count += 1
                
            print(f"{f:20s} {f'{w} x {h}':20s} {f'{ar:.2f}':15s} {layout}")
            
    print("-" * 70)
    print(f"Resumen de Maquetación:")
    print(f"  - Figuras en Parejas (Side-by-Side): {paired_count} ({paired_count//2} filas dobles)")
    print(f"  - Figuras Unitarias (Ancho completo): {single_count}")
    print("==================================================================")

if __name__ == "__main__":
    analyze_figure_catalog()
