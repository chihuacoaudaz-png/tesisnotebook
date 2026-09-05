import fitz
import os

doc = fitz.open("formateador/input/proyectoCJN.pdf")
os.makedirs("formateador/output/figures_individual/charts_v2", exist_ok=True)

# Coordenadas exactas y limpias de cada gráfico estadístico de barras
# Con marco inferior completo holgado (sin cortar bordes de abajo ni etiquetas de eje)
charts_def = [
    # Pag 7: Capacidad combustible
    (7, "fig07_combustible", fitz.Rect(55, 345, 595, 765)),
    
    # Pag 8: Flota 797F Pesaje
    (8, "fig08_pesaje_797f", fitz.Rect(55, 145, 335, 390)),
    
    # Pag 9: Flota 798AC y 793D Pesajes
    (9, "fig10_pesaje_798ac", fitz.Rect(55, 145, 335, 375)),
    (9, "fig12_pesaje_793d", fitz.Rect(55, 490, 335, 745)),
    
    # Pag 10: Komatsu 930E y 930E-4 Pesajes
    (10, "fig14_pesaje_930e", fitz.Rect(55, 145, 335, 375)),
    (10, "fig16_pesaje_930e4", fitz.Rect(55, 490, 335, 745)),
    
    # Pag 11: Komatsu 930E-4SE y 980E-4 Pesajes
    (11, "fig18_pesaje_930e4se", fitz.Rect(55, 145, 335, 390)),
    (11, "fig20_pesaje_980e4", fitz.Rect(55, 490, 600, 740)),
    
    # Pag 12: Komatsu 980E-5 Pesaje y Distribución Pos 1&2 Vacío
    (12, "fig21_pesaje_980e5", fitz.Rect(55, 145, 330, 375)),
    (12, "fig23_distrib_pos12_vacio", fitz.Rect(55, 530, 600, 760)),
    
    # Pag 13: Distribución Pos 1&2 Cargado (Flota Mayor) y Vacío (Flota Menor)
    (13, "fig24_distrib_pos12_cargado", fitz.Rect(55, 150, 600, 380)),
    (13, "fig25_distrib_pos12_vacio_menor", fitz.Rect(55, 490, 600, 725)),
    
    # Pag 14: Eje Posterior Flota Mayor (Cargado y Vacío)
    (14, "fig26_distrib_post_cargado", fitz.Rect(55, 145, 600, 375)),
    (14, "fig27_distrib_post_vacio", fitz.Rect(55, 480, 600, 720)),
    
    # Pag 15: Eje Posterior Flota Menor (Cargado y Vacío)
    (15, "fig28_distrib_post_cargado_menor", fitz.Rect(55, 140, 600, 375)),
    (15, "fig29_distrib_post_vacio_menor", fitz.Rect(55, 480, 600, 720)),
    
    # Pag 16: Distribución por Eje Vacío
    (16, "fig30_distrib_eje_vacio_flota", fitz.Rect(55, 130, 600, 360)),
    (16, "fig31_distrib_eje_vacio_flota2", fitz.Rect(55, 485, 600, 725)),
    
    # Pag 17: Distribución por Eje Cargado
    (17, "fig32_distrib_eje_cargado_flota", fitz.Rect(55, 145, 600, 340)),
    (17, "fig33_distrib_797f_vacio", fitz.Rect(55, 500, 600, 715)),
    
    # Pag 18: Volquetes 797F (Vacío y Cargado)
    (18, "fig34_distrib_797f_cargado", fitz.Rect(55, 135, 600, 360)),
    
    # Pag 19: 798AC y 930E
    (19, "fig35_distrib_798ac_vacio", fitz.Rect(40, 140, 605, 350)),
    (19, "fig36_distrib_930e_cargado", fitz.Rect(40, 490, 605, 705)),
    
    # Pag 20: 930E-4 y 980E-4
    (20, "fig39_distrib_930e4_vacio", fitz.Rect(40, 150, 605, 365)),
    (20, "fig43_distrib_980e4_vacio", fitz.Rect(40, 480, 605, 695)),
    
    # Pag 21: 793D (Vacío y Cargado)
    (21, "fig47_distrib_793d_vacio", fitz.Rect(40, 155, 605, 370)),
    (21, "fig48_distrib_793d_cargado", fitz.Rect(40, 480, 605, 695)),
    
    # Pag 22: Ranking Paleros y VIMS 798AC / 793D
    (22, "fig49_ranking_paleros", fitz.Rect(55, 150, 605, 460)),
    (22, "fig50_vims_798ac", fitz.Rect(55, 555, 330, 755)),
    (22, "fig51_vims_793d", fitz.Rect(335, 555, 605, 755)),
    
    # Pag 23: VIMS 797F y 930E
    (23, "fig52_vims_797f", fitz.Rect(55, 90, 605, 320)),
    (23, "fig53_vims_930e", fitz.Rect(55, 430, 605, 750)),
    
    # Pag 24: VIMS 980E
    (24, "fig54_vims_980e", fitz.Rect(55, 120, 605, 340))
]

zoom = 3.0  # 216 DPI de alta definición
mat = fitz.Matrix(zoom, zoom)

for p_no, name, rect in charts_def:
    page = doc[p_no - 1]
    pix = page.get_pixmap(matrix=mat, clip=rect)
    out_file = f"formateador/output/figures_individual/charts_v2/{name}.png"
    pix.save(out_file)
    print(f"Chart v2 extraído limpiamente: {out_file}")

print(f"[OK] Se extrajeron {len(charts_def)} gráficos limpios con coordenadas v2.")
