---
name: teorico
description: >-
  Use this skill to autonomously research, discover, formulate, and draft complete
  theoretical frameworks (Bases Teóricas and Marco Conceptual) for ANY engineering
  or scientific thesis plan, using methodological deduction (Dra. Rosario Martínez),
  Google NotebookLM Deep Research, and anti-hallucination grounded extraction.
---

# Skill: Constructor Autónomo de Marcos Teóricos (Bases Teóricas y Marco Conceptual)

Esta habilidad dota al agente de la capacidad integral para **investigar activamente, deducir la teoría a partir de las variables, ejecutar Deep Research, consultar NotebookLM y construir el Marco Teórico completo** para **cualquier plan de tesis de ingeniería**, eliminando alucinaciones y garantizando el máximo rigor académico (estándares UNI FIGMM y escuela metodológica de la Dra. Rosario Martínez).

---

## 1. Núcleo Metodológico: Cómo Deducir qué Teoría Buscar

El agente **no adivina ni busca al azar**. Utiliza los lineamientos de la Dra. Rosario Martínez para deducir la **Ruta Teórica** a partir de la formulación del problema y las variables:

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                        MOTOR DE DEDUCCIÓN TEÓRICA (DRA. ROSARIO MARTÍNEZ / UNI FIGMM)                  │
└────────────────────────────────────────────────────────────────────────────────────────────────────────┘
                                                    │
                 ┌──────────────────────────────────┼──────────────────────────────────┐
                 ▼                                  ▼                                  ▼
┌─────────────────────────────────┐┌─────────────────────────────────┐┌─────────────────────────────────┐
│     VARIABLE INDEPENDIENTE (X)  ││      VARIABLE DEPENDIENTE (Y)   ││   VARIABLES INTERVINIENTES (Z)  │
│        (Aporte / Causa)         ││       (Finalidad / Efecto)      ││     (Condiciones del Medio)     │
├─────────────────────────────────┤├─────────────────────────────────┤├─────────────────────────────────┤
│ Teorías que explican la técnica,││ Teorías que explican el fenó-   ││ Teorías geomecánicas, estructu- │
│ modelo físico, algoritmo o mé-  ││ meno a controlar, optimizar o   ││ rales o ambientales del entorno │
│ todo propuesto por el tesista.  ││ mitigar (mecanismo de rotura).  ││ que fijan condiciones límite.   │
└─────────────────────────────────┘└─────────────────────────────────┘└─────────────────────────────────┘
                                                    │
                                                    ▼
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                LEYES DE INTERACCIÓN CAUSAL (X -> Y)                                    │
│  Modelos físico-matemáticos, termodinámicos o computacionales que gobiernan cómo X modifica a Y.       │
└────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Flujo Operativo Universal: De la Búsqueda a la Redacción

### Paso 1: Análisis de Variables y Formulación de la Ruta Teórica
1. Identificar el Título, Problema General, Objetivo General e Hipótesis de la tesis.
2. Desglosar las variables:
   - **$X$ (Independiente):** ¿Qué leyes rigen el aporte tecnológico/matemático?
   - **$Y$ (Dependiente):** ¿Qué modelos describen el comportamiento del objeto de estudio?
   - **$Z$ (Intervinientes):** ¿Qué propiedades del medio condicionan la interacción?
3. Listar los modelos analíticos y deducciones matemáticas requeridas.

### Paso 2: Verificación de Sesión, Creación del Cuaderno e Ingesta con Deep Research
**REGLA DE ORO INVIOLABLE:** El agente tiene terminantemente prohibido redactar marcos teóricos o bases teóricas por su cuenta o a partir de memoria previa sin que exista un cuaderno en NotebookLM que contenga las fuentes de investigación indexadas.

Para cualquier tesis nueva o existente:
1. **Comprobar la autenticación y estado del CLI:**
   ```bash
   notebooklm doctor
   ```
   *Si las cookies expiraron (error `_LoginRedirectError`), solicitar al usuario ejecutar `notebooklm login` en su terminal.*
2. **Identificar o Crear el Cuaderno Dedicado de la Tesis:**
   Listar los cuadernos existentes:
   ```bash
   notebooklm list
   ```
   Si no existe un cuaderno específico para la tesis abordada, **crear inmediatamente el cuaderno dedicado**:
   ```bash
   notebooklm create "Tesis: <Nombre de la Tesis o Tema de Investigación>"
   ```
   Registrar el `<notebook_id>` generado como fuente de verdad primaria para toda la tesis.
3. **Alimentar el Cuaderno mediante Deep Research en Modo Deep:**
   Ejecutar búsquedas bibliográficas profundas utilizando **Google Deep Research en modo deep**, importando el 100% de las fuentes para alimentar la base de conocimiento:
   ```bash
   notebooklm source add-research "<consulta_cientifica_especifica>" --mode deep --import-all -n <notebook_id>
   ```
4. **Consultar el Cuaderno Metodológico de Posgrado:**
   Consultar el cuaderno de la Dra. Rosario Martínez (`769227ea-9b15-4fbc-a382-b14cd5e7435f`) para resolver dudas de estructura científica o consistencia de variables.

### Paso 3: Extracción Antialucinación (Grounding Estricto en el Cuaderno)
Para garantizar CERO invención de datos o fórmulas:
1. Interrogar el cuaderno dedicado con consultas analíticas directas:
   ```bash
   notebooklm ask "Deducción matemática completa, hipótesis de partida y fórmulas de: <modelo>" -n <notebook_id>
   ```
2. Si una formulación o parámetro geomecánico requiere verificación directa en el paper original, extraer su texto completo:
   ```bash
   notebooklm source fulltext <source_id> -n <notebook_id>
   ```
3. **Regla de Cero Alucinación:** Ninguna ecuación, parámetro o constante se asume si no está presente en las fuentes del cuaderno de NotebookLM. La redacción debe citar fielmente las fuentes sintetizadas por el cuaderno.

### Paso 4: Construcción de las Bases Teóricas
Redactar cada subsección teórica con la siguiente arquitectura:
- **Fundamento Físico y Fenomenológico:** Principios que rigen el fenómeno.
- **Deducción Matemática Continua:** Desarrollo analítico paso a paso en LaTeX formal sin omitir etapas algebraicas.
- **Definición de Variables:** Nomenclatura completa con unidades en el Sistema Internacional (SI).
- **Condiciones de Contorno y Compuertas de Calidad:** Límites físicos de validez de la formulación.
- **Fundamentación Epistemológica:** Argumentación científica de por qué el enfoque adoptado es el óptimo frente a enfoques alternativos.

### Paso 5: Construcción del Marco Conceptual
Generar entre 20 y 30 términos esenciales derivados directamente de las variables e indicadores:
- **Párrafo 1 (Definición Teórico-Científica):** Definición formal según autores canónicos, disciplina científica y significado conceptual.
- **Párrafo 2 (Contextualización Operativa y Causal):** Cómo se manifiesta el concepto en la unidad de estudio / yacimiento / proceso, y cómo influye en las variables del problema.

---

## 3. Guía Completa de Referencia
Para consultar el manual metodológico exhaustivo, plantillas de redacción para cualquier especialidad de ingeniería y ejemplos de prompt de Deep Research, consulte:
[Guía Metodológica del Flujo de Elaboración](./references/flujo_elaboracion_marcos.md).
