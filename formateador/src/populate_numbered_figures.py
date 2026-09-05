import os
import shutil
import fitz

# Crear la carpeta figuras
os.makedirs("formateador/figuras", exist_ok=True)
os.makedirs("formateador/output/figuras_numeradas", exist_ok=True)

# Mapeo de fotos puras individuales existentes
pure_images = {
    "figura_01.png": "formateador/output/figures_individual/raw_p03_img2_1273x651.png",
    "figura_02.png": "formateador/output/figures_individual/raw_p03_img3_1266x631.png",
    "figura_03.png": "formateador/output/figures_individual/raw_p04_img2_710x533.png",
    "tabla_01.png": "formateador/output/figures_individual/raw_p04_img3_672x236.png",
    "figura_04.png": "formateador/output/figures_individual/raw_p05_img2_672x430.png",
    "figura_05.png": "formateador/output/figures_individual/raw_p06_img3_601x240.png",
    "figura_06.png": "formateador/output/figures_individual/raw_p06_img2_596x242.png",
    "figura_09a.png": "formateador/output/figures_individual/raw_p08_img2_502x296.png",
    "figura_09b.png": "formateador/output/figures_individual/raw_p08_img3_558x332.png",
    "figura_11a.png": "formateador/output/figures_individual/raw_p09_img2_374x264.png",
    "figura_11b.png": "formateador/output/figures_individual/raw_p09_img3_372x254.png",
    "figura_13a.png": "formateador/output/figures_individual/raw_p09_img4_666x319.png",
    "figura_13b.png": "formateador/output/figures_individual/raw_p09_img5_653x314.png",
    "figura_15a.png": "formateador/output/figures_individual/raw_p10_img2_343x236.png",
    "figura_15b.png": "formateador/output/figures_individual/raw_p10_img3_722x485.png",
    "figura_17a.png": "formateador/output/figures_individual/raw_p10_img4_477x329.png",
    "figura_17b.png": "formateador/output/figures_individual/raw_p10_img5_420x291.png",
    "figura_19a.png": "formateador/output/figures_individual/raw_p11_img2_590x413.png",
    "figura_19b.png": "formateador/output/figures_individual/raw_p11_img3_757x520.png",
    "figura_22.png": "formateador/output/figures_individual/raw_p12_img3_683x482.png"
}

# Mapeo de gráficos de barras
chart_images = {
    "figura_07.png": "formateador/output/figures_individual/charts_v2/fig07_combustible.png",
    "figura_08.png": "formateador/output/figures_individual/charts_v2/fig08_pesaje_797f.png",
    "figura_10.png": "formateador/output/figures_individual/charts_v2/fig10_pesaje_798ac.png",
    "figura_12.png": "formateador/output/figures_individual/charts_v2/fig12_pesaje_793d.png",
    "figura_14.png": "formateador/output/figures_individual/charts_v2/fig14_pesaje_930e.png",
    "figura_16.png": "formateador/output/figures_individual/charts_v2/fig16_pesaje_930e4.png",
    "figura_18.png": "formateador/output/figures_individual/charts_v2/fig18_pesaje_930e4se.png",
    "figura_20.png": "formateador/output/figures_individual/charts_v2/fig20_pesaje_980e4.png",
    "figura_21.png": "formateador/output/figures_individual/charts_v2/fig21_pesaje_980e5.png",
    "figura_23.png": "formateador/output/figures_individual/charts_v2/fig23_distrib_pos12_vacio.png",
    "figura_24.png": "formateador/output/figures_individual/charts_v2/fig24_distrib_pos12_cargado.png",
    "figura_25.png": "formateador/output/figures_individual/charts_v2/fig25_distrib_pos12_vacio_menor.png",
    "figura_26.png": "formateador/output/figures_individual/charts_v2/fig26_distrib_post_cargado.png",
    "figura_27.png": "formateador/output/figures_individual/charts_v2/fig27_distrib_post_vacio.png",
    "figura_28.png": "formateador/output/figures_individual/charts_v2/fig28_distrib_post_cargado_menor.png",
    "figura_29.png": "formateador/output/figures_individual/charts_v2/fig29_distrib_post_vacio_menor.png",
    "figura_30.png": "formateador/output/figures_individual/charts_v2/fig30_distrib_eje_vacio_flota.png",
    "figura_31.png": "formateador/output/figures_individual/charts_v2/fig31_distrib_eje_vacio_flota2.png",
    "figura_32.png": "formateador/output/figures_individual/charts_v2/fig32_distrib_eje_cargado_flota.png",
    "figura_33.png": "formateador/output/figures_individual/charts_v2/fig33_distrib_797f_vacio.png",
    "figura_34.png": "formateador/output/figures_individual/charts_v2/fig34_distrib_797f_cargado.png",
    "figura_35.png": "formateador/output/figures_individual/charts_v2/fig35_distrib_798ac_vacio.png",
    "figura_36.png": "formateador/output/figures_individual/charts_v2/fig36_distrib_930e_cargado.png",
    "figura_39.png": "formateador/output/figures_individual/charts_v2/fig39_distrib_930e4_vacio.png",
    "figura_43.png": "formateador/output/figures_individual/charts_v2/fig43_distrib_980e4_vacio.png",
    "figura_47.png": "formateador/output/figures_individual/charts_v2/fig47_distrib_793d_vacio.png",
    "figura_48.png": "formateador/output/figures_individual/charts_v2/fig48_distrib_793d_cargado.png",
    "figura_49.png": "formateador/output/figures_individual/charts_v2/fig49_ranking_paleros.png",
    "figura_50.png": "formateador/output/figures_individual/charts_v2/fig50_vims_798ac.png",
    "figura_51.png": "formateador/output/figures_individual/charts_v2/fig51_vims_793d.png",
    "figura_52.png": "formateador/output/figures_individual/charts_v2/fig52_vims_797f.png",
    "figura_53.png": "formateador/output/figures_individual/charts_v2/fig53_vims_930e.png",
    "figura_54.png": "formateador/output/figures_individual/charts_v2/fig54_vims_980e.png"
}

all_figures = {**pure_images, **chart_images}

print(f"Copiando {len(all_figures)} figuras numeradas a formateador/figuras/...")

for dest_name, src_path in all_figures.items():
    dest_path1 = os.path.join("formateador/figuras", dest_name)
    dest_path2 = os.path.join("formateador/output/figuras_numeradas", dest_name)
    if os.path.exists(src_path):
        shutil.copyfile(src_path, dest_path1)
        shutil.copyfile(src_path, dest_path2)
        print(f"[OK] {dest_name} <- {src_path}")
    else:
        print(f"[ALERTA] No existe: {src_path}")

print("\n[EXITO TOTAL] Todas las figuras han sido guardadas y numeradas en formateador/figuras/.")
