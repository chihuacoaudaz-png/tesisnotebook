import re
import json

def audit_consistency_matrix(matrix_markdown):
    """
    Auditor de Matriz de Consistencia Científica (SKILL-05)
    Verifica matemáticamente la correspondencia horizontal y vertical 1:1 entre
    Problemas, Objetivos, Hipótesis, Variables e Indicadores.
    """
    issues = []
    
    # 1. Verificar presencia de componentes clave
    required_sections = ["Problemas", "Objetivos", "Hipótesis", "Variables", "Metodología"]
    for sec in required_sections:
        if sec.lower() not in matrix_markdown.lower():
            issues.append(f"Falta columna o sección obligatoria: '{sec}'")

    # 2. Conteo de Problemas Específicos vs Objetivos Específicos vs Hipótesis Específicas
    pe_matches = re.findall(r"PE\d+|Problema Específico \d+", matrix_markdown, re.IGNORECASE)
    oe_matches = re.findall(r"OE\d+|Objetivo Específico \d+", matrix_markdown, re.IGNORECASE)
    he_matches = re.findall(r"HE\d+|Hipótesis Específica \d+", matrix_markdown, re.IGNORECASE)
    
    num_pe = len(set(pe_matches))
    num_oe = len(set(oe_matches))
    num_he = len(set(he_matches))
    
    if not (num_pe == num_oe == num_he and num_pe >= 3):
        issues.append(f"Discrepancia en cantidad de componentes específicos: {num_pe} Problemas, {num_oe} Objetivos, {num_he} Hipótesis (Deben ser iguales y mínimo 3).")

    # 3. Verificación de verbos de logro en Objetivos
    verbos_invalidos = ["estudiar", "conocer", "revisar", "leer", "pensar"]
    for v in verbos_invalidos:
        if re.search(rf"\b{v}\b", matrix_markdown, re.IGNORECASE):
            issues.append(f"Se detectó verbo de actividad simple no admisible en objetivos de posgrado: '{v}'. Use verbos de logro (Determinar, Optimizar, Evaluar, Modelar).")

    # 4. Verificación de preguntas abiertas (no dicotómicas)
    preguntas_dicotomicas = ["¿Es posible", "¿Se puede", "¿Influye ", "¿Existe "]
    for p in preguntas_dicotomicas:
        if p.lower() in matrix_markdown.lower():
            issues.append(f"Pregunta formulada de manera dicotómica (Sí/No): '{p}'. Use interrogantes abiertas ('¿De qué manera...?', '¿En qué medida...?', '¿Cómo...?').")

    status = "APROBADO" if len(issues) == 0 else "OBSERVADO"
    return {
        "status": status,
        "total_problemas_especificos": num_pe,
        "total_objetivos_especificos": num_oe,
        "total_hipotesis_especificas": num_he,
        "correspondencia_1_a_1": (num_pe == num_oe == num_he and num_pe >= 3),
        "observaciones_detectadas": issues
    }

if __name__ == "__main__":
    sample_text = """
    | Problemas | Objetivos | Hipótesis | Variables | Metodología |
    | PG: ¿De qué manera el sistema agéntico optimiza la sobrerotura? | OG: Determinar la optimización... | HG: El sistema optimiza significativamente... | X: Sistema agéntico, Y: Sobrerotura | Aplicada |
    | PE1: ¿Cómo influyen los parámetros geomecánicos? | OE1: Caracterizar los parámetros... | HE1: Los parámetros geomecánicos condicionan... | X1: Geomecánica | Muestreo |
    | PE2: ¿Cuál es el desempeño del modelo de Holmberg? | OE2: Modelar y evaluar la malla... | HE2: El modelo de Holmberg reduce la sobreexcavación... | X2: Holmberg | Simulación |
    | PE3: ¿Cuál es el impacto económico en shotcrete? | OE3: Evaluar la reducción de costos de shotcrete... | HE3: La reducción de sobrerotura ahorra... | Y3: Costos | t-Student |
    """
    res = audit_consistency_matrix(sample_text)
    print("=== AUDITORÍA DE MATRIZ DE CONSISTENCIA ===")
    print(json.dumps(res, indent=2))
