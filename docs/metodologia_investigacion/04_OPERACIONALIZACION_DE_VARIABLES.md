---
title: Operacionalización de Variables
description: Guía canónica para la definición conceptual, operacional, desglose en dimensiones, indicadores y escalas de medición.
tags:
  - variables
  - operacionalizacion
  - indicadores
  - escalas-medicion
  - instrumentos
---

# 📊 Operacionalización de Variables (Estándar UNI FIGMM)

La operacionalización de variables es el proceso deductivo mediante el cual un concepto teórico abstracto se transforma en magnitudes medibles y verificables en el campo de trabajo de la mina.

---

## 1. Anatomía de la Matriz de Operacionalización

Toda matriz de operacionalización en la FIGMM - UNI debe contener rigurosamente las siguientes 8 columnas:

```mermaid
graph LR
    V["1. Variable (Tipo)"] --> DC["2. Definición Conceptual"]
    DC --> DO["3. Definición Operacional"]
    DO --> DIM["4. Dimensiones"]
    DIM --> IND["5. Indicadores"]
    IND --> ESC["6. Escala de Medición"]
    ESC --> UNI["7. Unidad de Medida"]
    UNI --> INS["8. Instrumento / Fuente"]
```

### Definiciones Metodológicas Clave:
1. **Definición Conceptual:** Explica qué significa la variable según los autores canónicos y la literatura científica (citas formales).
2. **Definición Operacional:** Describe *cómo se mide o manipula físicamente* la variable en el contexto específico de la mina.
3. **Dimensión:** Sub-área o componente fundamental de la variable.
4. **Indicador:** Parámetro numérico observable y cuantificable que refleja el estado de la dimensión.
5. **Escala de Medición:** Tipo de variable estadística (Razón, Intervalo, Ordinal o Nominal). En ingeniería predomina la **Escala de Razón** (cero absoluto físico).
6. **Instrumento / Fuente:** Equipo técnico, ensayo de laboratorio o software empleado para la recolección de los datos.

---

## 2. Matriz Canónica de Operacionalización (Caso de Estudio)

A continuación se presenta la matriz completa y verificada para la tesis de sostenimiento dinámico:

| Variable | Tipo | Definición Conceptual | Definición Operacional | Dimensiones | Indicadores | Escala / Unidad | Instrumento / Fuente |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Sistema Q de Barton y Monitoreo de Vibraciones** | **Independiente ($X$)** | Modelo empírico-analítico de calidad del macizo rocoso acoplado a la física de propagación de ondas dinámicas transitorias inducidas por detonación. | Cuantificación en campo del índice Q (Barton et al., 1974) y registro instrumental de ondas elásticas triaxiales en hastiales y techo. | **1. Calidad Geomecánica Intrínseca**<br><br>**2. Dinámica de Vibraciones** | - RQD (%)<br>- Cociente $J_r / J_a$<br>- Factor $SRF$<br>- Índice $Q$<br><br>- Vector Suma Pico ($PPV$)<br>- Frecuencia ($f_d$)<br>- Esfuerzo dinámico ($\sigma_d$) | - Razón (%)<br>- Razón (adim.)<br>- Razón (adim.)<br>- Razón (log)<br><br>- Razón ($mm/s$)<br>- Razón ($Hz$)<br>- Razón ($MPa$) | - Mapeo geomecánico de frentes (ISRM).<br>- Testigos diamantinos.<br><br>- Sismógrafo triaxial Instantel / Micromate.<br>- Geófonos de campo cercano.<br>- Software de análisis FFT. |
| **Selección del Sostenimiento Dinámico** | **Dependiente ($Y$)** | Determinación de la arquitectura de soporte perimetral compatible capaz de disipar energía cinética y deformación inelástica severa sin colapso estructural. | Evaluación cuantitativa de la demanda de energía cinética versus la capacidad de absorción plástica del sistema compuesto perno-malla-shotcrete. | **1. Demanda Dinámica**<br><br>**2. Capacidad de Absorción**<br><br>**3. Confiabilidad Estructural** | - Energía de eyección ($E_k$)<br>- Desplazamiento ($d$)<br><br>- Capacidad perno ($E_{\text{perno}}$)<br>- Resistencia malla ($E_{\text{malla}}$)<br>- Tenacidad FRS ($J$)<br><br>- Factor de Seguridad ($FS_{\text{dinámico}}$) | - Razón ($kJ/m^2$)<br>- Razón ($mm$)<br><br>- Razón ($kJ$)<br>- Razón ($kJ/m^2$)<br>- Razón (Joules)<br><br>- Razón (adim.) | - Ecuación de balance cinético (Kaiser).<br>- Extensómetros multipunto.<br><br>- Curvas carga-desplazamiento D-Bolt.<br>- Ensayo de impacto Geobrugg.<br>- Ensayo panel redondo ASTM C1550.<br><br>- Relación de balance $E_{\text{cap}} / E_{\text{dem}}$. |
| **Macizo Rocoso y Estado Tensional** | **Interviniente ($Z$)** | Entorno litológico, estructural y tensional preexistente en la excavación profunda. | Ensayos geomecánicos de laboratorio y modelamiento numérico del campo tensional inducido alrededor de la labor. | **1. Competencia de Roca Intacta**<br><br>**2. Campo Tensional Inducido** | - Compresión uniaxial ($\sigma_c$)<br>- Módulo elástico ($E_d$)<br>- Densidad ($\rho_r$)<br><br>- Esfuerzo principal ($\sigma_1$)<br>- Razón de esfuerzo ($\sigma_c / \sigma_1$) | - Razón ($MPa$)<br>- Razón ($GPa$)<br>- Razón ($kg/m^3$)<br><br>- Razón ($MPa$)<br>- Razón (adim.) | - Prensa servo-controlada (ASTM D7012).<br>- Ensayos ultrasónicos de onda.<br>- Balanza hidrostática.<br><br>- Modelamiento numérico 2D/3D (RS2/FLAC).<br>- Celdas de sobreperforación (CSIR). |

---

## 3. Reglas de Validación de Indicadores para Agentes de IA

1. **Evitar indicadores ambiguos:** Expresiones como *"calidad del soporte"* o *"seguridad del túnel"* son conceptos, no indicadores. Un indicador debe ser **estrictamente numérico y medible** (ej. $kJ/m^2$, $mm/s$, $FS$).
2. **Coherencia con las Fuentes de Datos:** Cada indicador debe tener un instrumento de recolección comercialmente disponible o una norma técnica estandarizada (ASTM, ISRM, UNE, EN).
3. **Alimentación al Modelo Matemático:** Los indicadores de la Variable Independiente deben alimentar directamente las ecuaciones que determinan el estado de la Variable Dependiente.
