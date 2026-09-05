import fitz
import os

doc = fitz.open("formateador/input/proyectoCJN.pdf")
os.makedirs("formateador/output/figures_individual/charts", exist_ok=True)

# Coordenadas exactas por página para recortar los gráficos limpios sin títulos repetitivos
chart_configs = {
    7: [("fig07_combustible", fitz.Rect(65, 360, 580, 770))],
    8: [("fig08_pesaje_797f", fitz.Rect(65, 140, 310, 400))],
    9: [("fig10_pesaje_798ac", fitz.Rect(65, 140, 320, 380)), ("fig12_pesaje_793d", fitz.Rect(65, 480, 320, 730))],
    10: [("fig14_pesaje_930e", fitz.Rect(65, 145, 320, 385)), ("fig16_pesaje_930e4", fitz.Rect(65, 490, 320, 730))],
    11: [("fig18_pesaje_930e4se", fitz.Rect(65, 150, 320, 400)), ("fig20_pesaje_980e4", fitz.Rect(130, 490, 520, 750))],
    12: [("fig21_pesaje_980e5", fitz.Rect(65, 145, 320, 390)), ("fig23_distrib_pos12_vacio", fitz.Rect(65, 530, 580, 770))],
    13: [("fig24_distrib_pos12_cargado", fitz.Rect(65, 140, 580, 430)), ("fig25_distrib_pos12_vacio_menor", fitz.Rect(65, 490, 580, 770))],
    14: [("fig26_distrib_post_cargado", fitz.Rect(65, 140, 580, 440)), ("fig27_distrib_post_vacio", fitz.Rect(65, 490, 580, 770))],
    15: [("fig28_distrib_post_cargado_menor", fitz.Rect(65, 140, 580, 440)), ("fig29_distrib_post_vacio_menor", fitz.Rect(65, 490, 580, 770))],
    16: [("fig30_distrib_eje_vacio_flota", fitz.Rect(65, 130, 580, 430)), ("fig31_distrib_eje_vacio_flota2", fitz.Rect(65, 480, 580, 770))],
    17: [("fig32_distrib_eje_cargado_flota", fitz.Rect(65, 130, 580, 770))],
    18: [("fig33_distrib_797f_vacio", fitz.Rect(65, 130, 580, 430)), ("fig34_distrib_797f_cargado", fitz.Rect(65, 480, 580, 770))],
    19: [("fig35_distrib_798ac_vacio", fitz.Rect(65, 130, 580, 430)), ("fig36_distrib_930e_cargado", fitz.Rect(65, 480, 580, 770))],
    20: [("fig39_distrib_930e4_vacio", fitz.Rect(65, 130, 580, 430)), ("fig43_distrib_980e4_vacio", fitz.Rect(65, 480, 580, 770))],
    21: [("fig47_distrib_793d_vacio", fitz.Rect(65, 130, 580, 430)), ("fig48_distrib_793d_cargado", fitz.Rect(65, 480, 580, 770))],
    22: [("fig49_ranking_paleros", fitz.Rect(65, 120, 580, 360)), ("fig50_vims_798ac", fitz.Rect(65, 480, 320, 730)), ("fig51_vims_793d", fitz.Rect(330, 480, 580, 730))],
    23: [("fig52_vims_797f", fitz.Rect(65, 130, 320, 440)), ("fig53_vims_930e", fitz.Rect(330, 130, 580, 440))],
    24: [("fig54_vims_980e", fitz.Rect(65, 130, 580, 730))],
    25: [("fig55_memoria_parachoque", fitz.Rect(65, 130, 580, 430))]
}

zoom = 3.0  # 216 DPI alta fidelidad
mat = fitz.Matrix(zoom, zoom)

for p_no, clips in chart_configs.items():
    page = doc[p_no - 1]
    for name, rect in clips:
        pix = page.get_pixmap(matrix=mat, clip=rect)
        out_file = f"formateador/output/figures_individual/charts/{name}.png"
        pix.save(out_file)
        print(f"Grafico limpio generado: {out_file}")

print("[OK] Todos los graficos limpios fueron extraidos y recortados con exito.")
