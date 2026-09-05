import math as mt
import numpy as np
import json
import os

def calculate_auto_tajeo(holmberg_data=None):
    """
    Algoritmo Heurístico de Auto-Tajeo y Ayudas (SKILL-03)
    Resuelve la distribución geométrica de taladros de tajeo y ayudas
    en el área remanente entre el 4to cuadrante del corte y los contornos.
    """
    if holmberg_data is None:
        from holmberg_perimeter_engine import solve_holmberg
        holmberg_data = solve_holmberg()
        
    ancho = holmberg_data["labor"]["ancho_m"]
    altura = holmberg_data["labor"]["altura_m"]
    fl = holmberg_data["labor"]["flecha_arco_m"]
    hp = holmberg_data["labor"]["long_perforacion_m"]
    
    # 4to cuadrante
    c4 = holmberg_data["corte_cuadrantes"][3]
    a4 = c4["apertura_m"] # 2.069 m
    q1 = c4["q_kg_m"] # 0.925 kg/m
    
    # Parámetros de tajeo
    f_tajeo = 1.45
    s_over_b = 1.25
    c_roca = 0.45
    
    bt_tajeo = 0.9 * mt.sqrt((q1 * 1.05) / (c_roca * f_tajeo * s_over_b))
    if bt_tajeo > 0.8:
        bt_tajeo = 0.8
    bp_tajeo = round(bt_tajeo - 0.05, 3) # 0.75 m
    esp_tajeo = round(bp_tajeo * s_over_b, 3) # 0.938 m
    
    cx = ancho / 2.0
    cy = (altura - fl + 1.0) / 2.0
    
    taladros_tajeo = []
    
    # 1. Fila de Ayudas/Tajeo Inferior (Entre corte y arrastres)
    y_inf = cy - (a4 / 2.0) - (bp_tajeo * 0.75)
    xs_inf = [cx - esp_tajeo, cx, cx + esp_tajeo]
    for x in xs_inf:
        taladros_tajeo.append({
            "tipo": "Tajeo_Inferior",
            "x_m": round(float(x), 3),
            "y_m": round(float(y_inf), 3),
            "burden_m": bp_tajeo,
            "espaciamiento_m": esp_tajeo,
            "q_kg_m": q1
        })
        
    # 2. Fila de Ayudas/Tajeo Superior (Entre corte y corona)
    y_sup = cy + (a4 / 2.0) + (bp_tajeo * 0.75)
    xs_sup = [cx - esp_tajeo, cx, cx + esp_tajeo]
    for x in xs_sup:
        taladros_tajeo.append({
            "tipo": "Tajeo_Superior",
            "x_m": round(float(x), 3),
            "y_m": round(float(y_sup), 3),
            "burden_m": bp_tajeo,
            "espaciamiento_m": esp_tajeo,
            "q_kg_m": q1
        })
        
    # 3. Ayudas/Tajeo Laterales (Izquierda y Derecha)
    x_lat_izq = cx - (a4 / 2.0) - (bp_tajeo * 0.75)
    x_lat_der = cx + (a4 / 2.0) + (bp_tajeo * 0.75)
    ys_lat = [cy - (a4 / 4.0), cy + (a4 / 4.0)]
    
    for y in ys_lat:
        taladros_tajeo.append({
            "tipo": "Tajeo_Lateral_Izq",
            "x_m": round(float(x_lat_izq), 3),
            "y_m": round(float(y), 3),
            "burden_m": bp_tajeo,
            "espaciamiento_m": esp_tajeo,
            "q_kg_m": q1
        })
        taladros_tajeo.append({
            "tipo": "Tajeo_Lateral_Der",
            "x_m": round(float(x_lat_der), 3),
            "y_m": round(float(y), 3),
            "burden_m": bp_tajeo,
            "espaciamiento_m": esp_tajeo,
            "q_kg_m": q1
        })

    # Consolidado Total de la Malla
    num_alivio = holmberg_data["alivio"]["num_taladros"]
    num_corte = sum([c["num_taladros"] for c in holmberg_data["corte_cuadrantes"]]) # 16
    num_arrastres = holmberg_data["arrastres"]["num_taladros"]
    num_corona = holmberg_data["corona_precorte"]["num_taladros"]
    num_hastiales = holmberg_data["hastiales"]["num_taladros"]
    num_tajeo = len(taladros_tajeo) # 10
    
    total_taladros_disparo = num_corte + num_arrastres + num_corona + num_hastiales + num_tajeo
    total_taladros_perforados = total_taladros_disparo + num_alivio

    area_seccion_m2 = ancho * (altura - fl) + (mt.pi * (ancho/2.0) * fl) / 2.0
    volumen_roca_m3 = area_seccion_m2 * hp * 0.95
    toneladas_roca = volumen_roca_m3 * 2.7
    
    kg_corte = num_corte * (hp - 0.45) * q1
    kg_arrastres = num_arrastres * (holmberg_data["arrastres"]["long_carga_fondo_m"] * holmberg_data["arrastres"]["q_fondo_kg_m"] + holmberg_data["arrastres"]["long_carga_columna_m"] * holmberg_data["arrastres"]["q_columna_kg_m"])
    kg_corona = num_corona * holmberg_data["corona_precorte"]["long_carga_m"] * holmberg_data["corona_precorte"]["qce_kg_m"]
    kg_hastiales = num_hastiales * holmberg_data["hastiales"]["long_carga_m"] * holmberg_data["hastiales"]["q_kg_m"]
    kg_tajeo = num_tajeo * (hp - 0.45) * q1
    
    total_explosivo_kg = kg_corte + kg_arrastres + kg_corona + kg_hastiales + kg_tajeo
    factor_potencia_kg_m3 = total_explosivo_kg / volumen_roca_m3
    factor_potencia_kg_t = total_explosivo_kg / toneladas_roca

    malla_completa = {
        "holmberg_base": holmberg_data,
        "auto_tajeo": {
            "num_taladros_tajeo": num_tajeo,
            "burden_practico_m": bp_tajeo,
            "espaciamiento_practico_m": esp_tajeo,
            "relacion_s_b": s_over_b,
            "taladros": taladros_tajeo
        },
        "resumen_malla_total": {
            "seccion_labor": "4.5 m x 4.5 m (Baul, fl=1.25m)",
            "area_labor_m2": round(area_seccion_m2, 2),
            "longitud_perforacion_m": round(hp, 2),
            "volumen_roca_rotura_m3": round(volumen_roca_m3, 2),
            "tonelaje_roca_t": round(toneladas_roca, 2),
            "taladros_alivio": num_alivio,
            "taladros_corte_4_cuadrantes": num_corte,
            "taladros_arrastre": num_arrastres,
            "taladros_corona_precorte": num_corona,
            "taladros_hastiales": num_hastiales,
            "taladros_tajeo_ayudas": num_tajeo,
            "total_taladros_cargados": total_taladros_disparo,
            "total_taladros_perforados": total_taladros_perforados,
            "total_explosivo_disparo_kg": round(total_explosivo_kg, 2),
            "factor_potencia_kg_m3": round(factor_potencia_kg_m3, 3),
            "factor_potencia_kg_t": round(factor_potencia_kg_t, 3)
        }
    }
    return malla_completa

if __name__ == "__main__":
    res = calculate_auto_tajeo()
    os.makedirs("./output", exist_ok=True)
    with open("./output/malla_lincuna_dimensionada.json", "w", encoding="utf-8") as f:
        json.dump(res, f, indent=2)
    print("=== MALLA COMPLETA CON AUTO-TAJEO GUARDADA EN ./output/malla_lincuna_dimensionada.json ===")
    print(f"Total Taladros: {res['resumen_malla_total']['total_taladros_perforados']}")
    print(f"Factor de Potencia: {res['resumen_malla_total']['factor_potencia_kg_m3']} kg/m3 ({res['resumen_malla_total']['factor_potencia_kg_t']} kg/t)")
