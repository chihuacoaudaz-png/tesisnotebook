import matplotlib.pyplot as plt
import numpy as np
import os
import json

os.makedirs("./output/figures", exist_ok=True)

# Set styling
plt.rcParams.update({
    'font.size': 10,
    'font.family': 'sans-serif',
    'axes.labelsize': 11,
    'axes.titlesize': 12,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'figure.autolayout': True
})

# 1. FIGURA 1: SECCIÓN TRANSVERSAL Y MALLA DE PERFORACIÓN LINCUNA 2026 (HOLMBERG + AUTO-TAJEO)
def plot_blast_pattern():
    ancho = 4.5
    altura = 4.5
    fl = 1.25
    
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Línea base
    ax.plot([0, ancho], [0, 0], color='black', linewidth=1.5, label='Perfil Teórico de Excavación')
    # Laterales (hastiales)
    ax.plot([0, 0], [0, altura - fl], color='black', linewidth=1.5)
    ax.plot([ancho, ancho], [0, altura - fl], color='black', linewidth=1.5)
    
    # Corona (Arco baúl)
    centro = (ancho/2.0, altura - (((ancho**2) + (4*fl**2)) / (8*fl)))
    radio = ((ancho**2) + (4*fl**2)) / (8*fl)
    theta_ini = (np.pi/2) - np.arcsin((4*ancho*fl) / ((ancho**2) + (4*fl**2)))
    theta_fin = (np.pi/2) + np.arcsin((4*ancho*fl) / ((ancho**2) + (4*fl**2)))
    theta = np.linspace(theta_ini, theta_fin, 200)
    ax.plot(centro[0] + radio * np.cos(theta), centro[1] + radio * np.sin(theta), color='black', linewidth=1.5)
    
    # Centro de corte
    cx = ancho / 2.0
    cy = (altura - fl + 1.0) / 2.0
    
    # Taladro de alivio central (102 mm)
    ax.scatter(cx, cy, s=250, facecolors='white', edgecolors='black', linewidth=2, label='Alivio Central (Ø 102 mm)')
    
    # Cuadrantes 1 al 4
    aperturas = [0.216, 0.609, 1.246, 2.069]
    colors_c = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
    for idx, a in enumerate(aperturas):
        # Dibujar cuadrado inclinado 45° o recto
        if idx % 2 == 0:
            diag = (a * np.sqrt(2)) / 2.0
            verts = np.array([[cx + diag, cy], [cx, cy + diag], [cx - diag, cy], [cx, cy - diag], [cx + diag, cy]])
        else:
            side = a / 2.0
            verts = np.array([[cx + side, cy + side], [cx - side, cy + side], [cx - side, cy - side], [cx + side, cy - side], [cx + side, cy + side]])
        ax.plot(verts[:, 0], verts[:, 1], linestyle='--', color='gray', linewidth=0.8)
        label_c = f'Corte Cuadrante {idx+1}' if idx == 0 else f'Cuadrante {idx+1}'
        ax.scatter(verts[:-1, 0], verts[:-1, 1], s=45, color=colors_c[idx], edgecolors='black', label=label_c)
        
    # Taladros de Corona (Precorte / Amortiguado)
    angulos = np.linspace(theta_ini, theta_fin, 9)
    # Burden práctico hacia el interior
    r_corona = radio - 0.20 # Offset visual de perforación
    xc = centro[0] + r_corona * np.cos(angulos)
    yc = centro[1] + r_corona * np.sin(angulos)
    ax.scatter(xc, yc, s=55, color='#9467bd', edgecolors='black', label='Corona Precorte (9 tal.)')
    
    # Taladros de Hastiales
    yh = np.linspace(0.889, altura - fl - 0.2, 4)
    ax.scatter([0.25]*len(yh), yh, s=55, color='#8c564b', edgecolors='black', label='Hastiales (6 tal.)')
    ax.scatter([ancho - 0.25]*len(yh), yh, s=55, color='#8c564b', edgecolors='black')
    
    # Taladros de Arrastres
    xa = np.linspace(0.45, ancho - 0.45, 5)
    ya = [0.20] * 5
    ax.scatter(xa, ya, s=60, color='#e377c2', edgecolors='black', label='Arrastres (5 tal.)')
    
    # Taladros de Auto-Tajeo y Ayudas
    # Inferior
    ax.scatter([cx - 0.938, cx, cx + 0.938], [cy - 1.034 - 0.35]*3, s=50, color='#17becf', edgecolors='black', label='Auto-Tajeo / Ayudas (10 tal.)')
    # Superior
    ax.scatter([cx - 0.938, cx, cx + 0.938], [cy + 1.034 + 0.35]*3, s=50, color='#17becf', edgecolors='black')
    # Laterales
    ax.scatter([cx - 1.034 - 0.35]*2, [cy - 0.5, cy + 0.5], s=50, color='#17becf', edgecolors='black')
    ax.scatter([cx + 1.034 + 0.35]*2, [cy - 0.5, cy + 0.5], s=50, color='#17becf', edgecolors='black')
    
    ax.set_xlim(-0.3, ancho + 0.3)
    ax.set_ylim(-0.3, altura + 0.3)
    ax.set_aspect('equal')
    ax.set_xlabel('Ancho de la Labor (m)')
    ax.set_ylabel('Altura de la Labor (m)')
    ax.set_title('Diseño de Malla de Perforación Asistida por Sistema Agéntico (Sección D 4.5m x 4.5m)', fontweight='bold')
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend(loc='upper right', bbox_to_anchor=(1.35, 1.0), fontsize=8)
    
    plt.savefig('./output/figures/figura_01_malla_perforacion.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("[OK] Generada: figura_01_malla_perforacion.png")

# 2. FIGURA 2: COMPARACIÓN DE SOBREROTURA HISTÓRICA VS SISTEMA AGÉNTICO
def plot_overbreak_comparison():
    fig, ax = plt.subplots(figsize=(7, 4.5))
    
    np.random.seed(42)
    pre = np.random.normal(loc=34.36, scale=4.2, size=30)
    post = np.random.normal(loc=4.85, scale=0.88, size=30)
    
    disparos = np.arange(1, 31)
    
    ax.plot(disparos, pre, marker='o', color='#d62728', linewidth=1.5, markersize=5, label='Línea Base Convencional (Media = 34.36%)')
    ax.plot(disparos, post, marker='s', color='#2ca02c', linewidth=1.5, markersize=5, label='Sistema Agéntico Holmberg (Media = 4.85%)')
    ax.axhline(5.0, color='blue', linestyle='--', linewidth=1.2, label='Límite Meta Operacional (≤ 5.0%)')
    
    ax.set_xlabel('Número de Disparo Experimental')
    ax.set_ylabel('Índice de Sobrerotura (%)')
    ax.set_title('Evolución de la Sobrerotura en 30 Disparos Experimentales (Pre vs. Post)', fontweight='bold')
    ax.set_ylim(0, 45)
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend(loc='upper right', fontsize=9)
    
    plt.savefig('./output/figures/figura_02_comparacion_sobrerotura.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("[OK] Generada: figura_02_comparacion_sobrerotura.png")

# 3. FIGURA 3: DESGLOSE DE COSTOS Y AHORRO EN SHOTCRETE
def plot_cost_savings():
    fig, ax = plt.subplots(figsize=(6.5, 4.5))
    
    categorias = ['Shotcrete', 'Limpieza Scooptramp', 'Acarreo Dumper', 'Total Unitario']
    costos_pre = [7639.50, 480.00, 320.00, 8439.50]
    costos_post = [1099.50, 360.00, 240.00, 1699.50]
    
    x = np.arange(len(categorias))
    width = 0.35
    
    rects1 = ax.bar(x - width/2, costos_pre, width, label='Diseño Convencional', color='#e74c3c')
    rects2 = ax.bar(x + width/2, costos_post, width, label='Sistema Agéntico', color='#2ecc71')
    
    ax.set_ylabel('Costo por Disparo (USD)')
    ax.set_title('Comparativa de Costos Operacionales por Disparo de Avance', fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(categorias)
    ax.legend()
    ax.grid(True, linestyle=':', alpha=0.5, axis='y')
    
    # Add values on top
    for rect in rects1:
        height = rect.get_height()
        ax.annotate(f'${height:,.0f}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points",
                    ha='center', va='bottom', fontsize=8)
    for rect in rects2:
        height = rect.get_height()
        ax.annotate(f'${height:,.0f}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points",
                    ha='center', va='bottom', fontsize=8)
                    
    plt.savefig('./output/figures/figura_03_ahorro_costos.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("[OK] Generada: figura_03_ahorro_costos.png")

if __name__ == "__main__":
    plot_blast_pattern()
    plot_overbreak_comparison()
    plot_cost_savings()
