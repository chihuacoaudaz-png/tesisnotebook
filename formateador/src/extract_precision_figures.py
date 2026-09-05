import fitz
import os

doc = fitz.open('formateador/input/proyectoCJN.pdf')
os.makedirs('formateador/output/figures_precision', exist_ok=True)

# Coordenadas exactas verificadas para cada una de las figuras
figures_map = {
    # PAGINA 3: Resumen / Nivelacion
    'fig01_nivelacion_cat24m': (3, fitz.Rect(55.0, 160.0, 595.0, 465.0)),
    'fig02_compactacion_bomag': (3, fitz.Rect(55.0, 475.0, 595.0, 770.0)),
    
    # PAGINA 4: Ubicacion MineOperate y Tabla Personal
    'fig03_ubicacion_mineoperate': (4, fitz.Rect(55.0, 140.0, 595.0, 520.0)),
    'tabla01_funciones_personal': (4, fitz.Rect(55.0, 570.0, 595.0, 750.0)),
    
    # PAGINA 5: Vista en planta de pads
    'fig04_planta_pads': (5, fitz.Rect(55.0, 140.0, 595.0, 490.0)),
    
    # PAGINA 6: Procedimiento de pesaje
    'fig05_pesaje_vacio': (6, fitz.Rect(55.0, 310.0, 595.0, 525.0)),
    'fig06_pesaje_cargado': (6, fitz.Rect(55.0, 545.0, 595.0, 765.0)),
    
    # PAGINA 7: Capacidad tanque combustible
    'fig07_combustible': (7, fitz.Rect(55.0, 345.0, 595.0, 760.0)),
    
    # PAGINA 8: CAT 797F (Pesaje a la izq, Tolvas a la der)
    'fig08_pesaje_797f': (8, fitz.Rect(55.0, 150.0, 335.0, 385.0)),
    'fig09_tolvas_797f': (8, fitz.Rect(340.0, 150.0, 605.0, 385.0)),
    
    # PAGINA 9: CAT 798AC (arriba) y CAT 793D (abajo)
    'fig10_pesaje_798ac': (9, fitz.Rect(55.0, 148.0, 335.0, 375.0)),
    'fig11_tolvas_798ac': (9, fitz.Rect(340.0, 148.0, 605.0, 375.0)),
    'fig12_pesaje_793d': (9, fitz.Rect(55.0, 495.0, 335.0, 745.0)),
    'fig13_tolvas_793d': (9, fitz.Rect(340.0, 495.0, 605.0, 745.0)),
    
    # PAGINA 10: Komatsu 930E (arriba) y Komatsu 930E-4 (abajo)
    'fig14_pesaje_930e': (10, fitz.Rect(55.0, 148.0, 335.0, 375.0)),
    'fig15_tolvas_930e': (10, fitz.Rect(340.0, 148.0, 605.0, 375.0)),
    'fig16_pesaje_930e4': (10, fitz.Rect(55.0, 495.0, 335.0, 745.0)),
    'fig17_tolvas_930e4': (10, fitz.Rect(340.0, 495.0, 605.0, 745.0)),
    
    # PAGINA 11: Komatsu 930E-4SE (arriba) y Komatsu 980E-4 (abajo)
    'fig18_pesaje_930e4se': (11, fitz.Rect(55.0, 150.0, 335.0, 385.0)),
    'fig19_dados_930e4se': (11, fitz.Rect(340.0, 150.0, 605.0, 385.0)),
    'fig20_pesaje_980e4': (11, fitz.Rect(55.0, 495.0, 605.0, 735.0)),
    
    # PAGINA 12: Komatsu 980E-5 (arriba) y Distribucion Pos 1&2 Vacio (abajo)
    'fig21_pesaje_980e5': (12, fitz.Rect(55.0, 148.0, 330.0, 370.0)),
    'fig22_tolva_980e5': (12, fitz.Rect(335.0, 148.0, 605.0, 370.0)),
    'fig23_distrib_pos12_vacio': (12, fitz.Rect(55.0, 535.0, 605.0, 755.0)),
    
    # PAGINA 13: Distribucion Pos 1&2 Cargado (arriba) y Vacio Menor (abajo)
    'fig24_distrib_pos12_cargado': (13, fitz.Rect(55.0, 155.0, 605.0, 375.0)),
    'fig25_distrib_pos12_vacio_menor': (13, fitz.Rect(55.0, 495.0, 605.0, 720.0)),
    
    # PAGINA 14: Eje Posterior Cargado (arriba) y Vacio (abajo)
    'fig26_distrib_post_cargado': (14, fitz.Rect(55.0, 150.0, 605.0, 370.0)),
    'fig27_distrib_post_vacio': (14, fitz.Rect(55.0, 485.0, 605.0, 715.0)),
    
    # PAGINA 15: Eje Posterior Cargado Menor (arriba) y Vacio Menor (abajo)
    'fig28_distrib_post_cargado_menor': (15, fitz.Rect(55.0, 145.0, 605.0, 370.0)),
    'fig29_distrib_post_vacio_menor': (15, fitz.Rect(55.0, 485.0, 605.0, 715.0)),
    
    # PAGINA 16: Distribucion por Eje Vacio Flota Mayor (arriba) y Menor (abajo)
    'fig30_distrib_eje_vacio_flota': (16, fitz.Rect(55.0, 135.0, 605.0, 355.0)),
    'fig31_distrib_eje_vacio_flota2': (16, fitz.Rect(55.0, 490.0, 605.0, 720.0)),
    
    # PAGINA 17: Distribucion por Eje Cargado (arriba) y CAT 797F Vacio (abajo)
    'fig32_distrib_eje_cargado_flota': (17, fitz.Rect(55.0, 150.0, 605.0, 335.0)),
    'fig33_distrib_797f_vacio': (17, fitz.Rect(55.0, 505.0, 605.0, 710.0)),
    
    # PAGINA 18: CAT 797F Cargado (arriba) y CAT 797F Desbalance (abajo)
    'fig34_distrib_797f_cargado': (18, fitz.Rect(55.0, 140.0, 605.0, 355.0)),
    'fig34b_distrib_797f_cargado_det': (18, fitz.Rect(55.0, 495.0, 605.0, 700.0)),
    
    # PAGINA 19: CAT 798AC Vacio (arriba) y Komatsu 930E Cargado (abajo)
    'fig35_distrib_798ac_vacio': (19, fitz.Rect(40.0, 145.0, 605.0, 345.0)),
    'fig36_distrib_930e_cargado': (19, fitz.Rect(40.0, 495.0, 605.0, 700.0)),
    
    # PAGINA 20: Komatsu 930E-4 Vacio (arriba) y Komatsu 980E-4 Vacio (abajo)
    'fig39_distrib_930e4_vacio': (20, fitz.Rect(40.0, 155.0, 605.0, 360.0)),
    'fig43_distrib_980e4_vacio': (20, fitz.Rect(40.0, 485.0, 605.0, 690.0)),
    
    # PAGINA 21: CAT 793D Vacio (arriba) y CAT 793D Cargado (abajo)
    'fig47_distrib_793d_vacio': (21, fitz.Rect(40.0, 160.0, 605.0, 365.0)),
    'fig48_distrib_793d_cargado': (21, fitz.Rect(40.0, 485.0, 605.0, 690.0)),
    
    # PAGINA 22: Ranking Paleros (arriba) y VIMS 798AC/793D (abajo)
    'fig49_ranking_paleros': (22, fitz.Rect(55.0, 155.0, 605.0, 455.0)),
    'fig50_vims_798ac': (22, fitz.Rect(55.0, 560.0, 330.0, 750.0)),
    'fig51_vims_793d': (22, fitz.Rect(335.0, 560.0, 605.0, 750.0)),
    
    # PAGINA 23: VIMS 797F (arriba) y VIMS 930E (abajo)
    'fig52_vims_797f': (23, fitz.Rect(55.0, 95.0, 605.0, 315.0)),
    'fig53_vims_930e': (23, fitz.Rect(55.0, 435.0, 605.0, 745.0)),
    
    # PAGINA 24: VIMS 980E
    'fig54_vims_980e': (24, fitz.Rect(55.0, 125.0, 605.0, 335.0))
}

mat = fitz.Matrix(3.0, 3.0) # 216 DPI de maxima resolucion

for name, (p_no, rect) in figures_map.items():
    page = doc[p_no - 1]
    pix = page.get_pixmap(matrix=mat, clip=rect)
    out_path = f'formateador/output/figures_precision/{name}.png'
    pix.save(out_path)
    print(f'[OK] Extraida: {name} | Pagina {p_no} | Bbox: ({rect.x0}, {rect.y0}, {rect.x1}, {rect.y1}) -> Res: {pix.width}x{pix.height}')

print(f'\n[EXITO TOTAL] Se extrajeron {len(figures_map)} figuras de precision.')
