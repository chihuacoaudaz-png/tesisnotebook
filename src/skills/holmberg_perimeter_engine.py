import math as mt
import numpy as np
import json
import os

def solve_holmberg(
    ancho=4.5,
    altura=4.5,
    fl=1.25,
    hp_ft=12.0,
    d_prod_mm=45.0,
    d_alivio_mm=102.0,
    n_alivio=1,
    ucs_mpa=180.05,
    traccion_mpa=12.15,
    densidad_roca=2.7,
    gsi=50.0,
    rqd=60.0,
    desv_pct=1.0,
    peso_cartucho_kg=0.18,
    s_anfo=1.05,
    dc_mm=32.0,
    long_cartucho_pulg=8.0,
    densidad_explo=1.15,
    vod_corona=4000.0,
    dc_corona_mm=22.0,
    densidad_explo_corona=1.0,
    peso_explo_corona=0.12
):
    """
    Motor Físico Determinístico de Holmberg-Persson (SKILL-02)
    Calcula las 5 secciones de la malla de perforación en labores subterráneas.
    """
    hp = hp_ft * 0.3048 # metros
    d1 = d_prod_mm / 1000.0 # diámetro taladro producción en m
    long_cartucho = long_cartucho_pulg * 0.0254 # m
    
    # 1. Alivio y avance
    if d_alivio_mm > 0:
        d2 = d_alivio_mm / 1000.0
        dv = d2 * mt.sqrt(n_alivio)
    else:
        dv = d1 * mt.sqrt(n_alivio)
        
    avance_esperado = 0.15 + 34.1 * dv - 39.4 * (dv ** 2)
    if avance_esperado > hp * 0.95:
        avance_esperado = hp * 0.95

    # 2. Constante de roca sueca C (Ashby modificado)
    ce = (0.56 * densidad_roca * mt.tan(mt.radians((gsi + 15.0) / 2.0))) / (((115.0 - rqd) / 3.3) ** (1.0 / 3.0))
    c_roca = 0.878 * ce + 0.0052

    # Error de perforación F
    alfa = 0.010 # 10 mm/m
    beta = 0.020 # 20 mm emboquillado
    f_err = alfa * hp + beta

    # Primer Cuadrante
    bt1_o = 1.5 * dv if desv_pct < 1.0 else 1.7 * dv
    q1 = (densidad_explo * mt.pi * ((dc_mm / 1000.0) ** 2) * 1000.0) / 4.0 # kg/m
    
    # Resolver ecuación polinómica para BT1
    coef = [1.0, -dv, (dv**2)/4.0, 0.0, 0.0, -(((q1 * s_anfo * 0.4 * (dv**1.5)) / (55.0 * d1 * c_roca)) ** 2)]
    roots = np.roots(coef)
    pos_roots = [r.real for r in roots if np.isreal(r) and r.real > 0]
    bt1 = min(pos_roots, key=lambda x: abs(x - bt1_o)) if pos_roots else bt1_o
    bp1 = bt1 - f_err
    a1 = bp1 * mt.sqrt(2.0)
    t1 = 10.0 * d1
    lc1 = hp - t1
    n1 = int(q1 * lc1 / peso_cartucho_kg)

    cuadrantes = [{
        "cuadrante": 1,
        "burden_teorico_m": round(bt1, 3),
        "burden_practico_m": round(bp1, 3),
        "apertura_m": round(a1, 3),
        "taco_m": round(t1, 3),
        "long_carga_m": round(lc1, 3),
        "q_kg_m": round(q1, 3),
        "cartuchos_por_taladro": n1,
        "num_taladros": 4
    }]

    # Cuadrantes 2 al 4
    bp_prev = bp1
    ah_prev = a1
    for i in range(1, 4):
        ak = (bp_prev + ah_prev / 2.0 - f_err) * mt.sqrt(2.0)
        bt = 8.8e-2 * mt.sqrt((ak * q1 * s_anfo) / (d1 * c_roca))
        bp = bt - f_err
        ah = mt.sqrt(2.0) * (bp + ah_prev / 2.0)
        t_cuad = 10.0 * d1
        lc_cuad = hp - t_cuad
        n_cuad = int(q1 * lc_cuad / peso_cartucho_kg)
        cuadrantes.append({
            "cuadrante": i + 1,
            "burden_teorico_m": round(bt, 3),
            "burden_practico_m": round(bp, 3),
            "apertura_m": round(ah, 3),
            "taco_m": round(t_cuad, 3),
            "long_carga_m": round(lc_cuad, 3),
            "q_kg_m": round(q1, 3),
            "cartuchos_por_taladro": n_cuad,
            "num_taladros": 4
        })
        bp_prev = bp
        ah_prev = ah

    # 3. Arrastres (Gustafsson)
    f_fix = 1.45
    c_arrastre = c_roca + 0.05 if bp_prev >= 1.4 else c_roca + (0.07 / bp_prev)
    bta = 0.9 * mt.sqrt((q1 * s_anfo) / (c_arrastre * f_fix * 1.0))
    if bta > 0.6 * hp:
        bta = 0.6 * hp
    phi_deg = 3.0
    phi_rad = mt.radians(phi_deg)
    nta = int((ancho + 2.0 * hp * mt.sin(phi_rad)) / bta + 1)
    sta = (ancho + 2.0 * hp * mt.sin(phi_rad)) / (nta - 1)
    spa = sta - hp * mt.sin(phi_rad)
    bpa = bta - hp * mt.sin(phi_rad) - f_err
    hfa = 1.25 * bpa
    qfa = q1
    nfa = int(hfa / long_cartucho)
    hca = hp - hfa - 10.0 * d1
    qca = qfa * 0.7
    nca = int(hca / long_cartucho)

    arrastres = {
        "num_taladros": nta,
        "burden_teorico_m": round(bta, 3),
        "burden_practico_m": round(bpa, 3),
        "espaciamiento_practico_m": round(spa, 3),
        "taco_m": round(10.0 * d1, 3),
        "long_carga_fondo_m": round(hfa, 3),
        "cartuchos_fondo": nfa,
        "long_carga_columna_m": round(hca, 3),
        "cartuchos_columna": nca,
        "q_fondo_kg_m": round(qfa, 3),
        "q_columna_kg_m": round(qca, 3)
    }

    # 4. Corona (Precorte / Amortiguada)
    # Presión de detonación de Chapman-Jouguet
    pt = 228e-6 * densidad_explo_corona * ((vod_corona ** 2) / (1.0 + 0.8 * densidad_explo_corona)) # MPa
    # Presión efectiva desacoplada
    pte = pt * (((dc_corona_mm) ** 0.42) / (d1 * 1000.0))
    
    # Comprobación de seguridad geomecánica
    pte_ok = (pte <= ucs_mpa)
    qc_min = 90.0 * (d1 ** 2)
    qce = densidad_explo_corona * 1000.0 * mt.pi * ((dc_corona_mm / 1000.0) ** 2) / 4.0
    
    sc = d1 * (pte + traccion_mpa) / traccion_mpa
    btc = sc / 0.8
    bpc = btc - hp * mt.sin(phi_rad) - f_err
    
    # Longitud arco corona baúl
    long_arc_corona = (((ancho**2) + 4.0 * (fl**2)) / (4.0 * fl)) * np.arcsin((4.0 * ancho * fl) / ((ancho**2) + 4.0 * (fl**2)))
    ntc = int((long_arc_corona / sc) + 1)
    ncc = int((hp - 10.0 * d1) * qce / peso_explo_corona + 0.5)

    corona = {
        "num_taladros": ntc,
        "presion_detonacion_pt_mpa": round(pt, 2),
        "presion_efectiva_pte_mpa": round(pte, 2),
        "condicion_pte_le_ucs": pte_ok,
        "ucs_roca_mpa": ucs_mpa,
        "espaciamiento_sc_m": round(sc, 3),
        "burden_teorico_btc_m": round(btc, 3),
        "burden_practico_bpc_m": round(bpc, 3),
        "taco_m": round(10.0 * d1, 3),
        "long_carga_m": round(hp - 10.0 * d1, 3),
        "cartuchos_por_taladro": ncc,
        "qce_kg_m": round(qce, 3)
    }

    # 5. Hastiales
    long_disp_h = altura - bpa - fl
    nth = int((long_disp_h / sc) + 1)
    total_hastiales = 2 * (nth - 1)
    nch = int((hp - 10.0 * d1) * qce / peso_explo_corona + 0.5)

    hastiales = {
        "num_taladros": total_hastiales,
        "espaciamiento_sh_m": round(sc, 3),
        "burden_practico_bph_m": round(bpc, 3),
        "taco_m": round(10.0 * d1, 3),
        "long_carga_m": round(hp - 10.0 * d1, 3),
        "cartuchos_por_taladro": nch,
        "q_kg_m": round(qce, 3)
    }

    result = {
        "labor": {
            "seccion": "D (Baul)",
            "ancho_m": ancho,
            "altura_m": altura,
            "flecha_arco_m": fl,
            "long_perforacion_m": round(hp, 2),
            "avance_esperado_m": round(avance_esperado, 2)
        },
        "alivio": {
            "num_taladros": n_alivio,
            "diametro_mm": d_alivio_mm,
            "diametro_eq_mm": round(dv * 1000.0, 1)
        },
        "corte_cuadrantes": cuadrantes,
        "arrastres": arrastres,
        "corona_precorte": corona,
        "hastiales": hastiales
    }
    return result

if __name__ == "__main__":
    res = solve_holmberg()
    print("=== MOTOR DE HOLMBERG RESUELTO CON ÉXITO ===")
    print(json.dumps(res, indent=2))
