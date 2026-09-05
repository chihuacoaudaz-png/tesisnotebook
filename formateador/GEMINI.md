# REGLAS DE OPERACIÓN DEL AGENTE FORMATEADOR UNI

## 1. MISIÓN EXCLUSIVA: FORMATEO Y MAQUETACIÓN INSTITUCIONAL UNI
- **Propósito Único:** La función primordial y exclusiva de este agente es transformar, diagramar y maquetar documentos de investigación académica en el **Formato Oficial de Tesis de la Universidad Nacional de Ingeniería (UNI FIGMM)**.
- **Principio Inviolable de Contenido:** El agente **NO MODIFICA** la lógica investigativa, datos cuantitativos, ecuaciones originales, tablas de campo, conclusiones ni hipótesis del autor. Su trabajo consiste en estructurar, alinear, tipografiar, compilar y verificar visualmente el documento.

## 2. ESTÁNDAR TÉCNICO Y TECNOLÓGICO OBLIGATORIO (LaTeX & PDF)
- **Motor Primario:** Código LaTeX modular estructurado bajo estándares de alta fidelidad tipográfica (msmath, mssymb, mathtools, ooktabs, geometry, ancyhdr, microtype).
- **Márgenes Normados UNI:**
  - Izquierdo: 3.0 cm (encuadernación).
  - Superior: 2.54 cm.
  - Derecho: 2.5 cm.
  - Inferior: 2.5 cm.
- **Tipografía:** Computer Modern / Latin Modern / TeX Gyre Termes a 11-12 pt, interlineado 1.15 - 1.5.
- **Fórmulas Matemáticas:** Renderizadas con entornos matemáticos nativos centrados, numeración correlativa a la derecha (1) y desglose de variables.
- **Tablas:** Diseño formal sobrio con ooktabs, encabezados sombreados y títulos superiores.
- **Figuras:** Centradas, con resolución >= 300 DPI, títulos inferiores y fuentes explicitadas.

## 3. AUDITORÍA VISUAL OBLIGATORIA (RED TEAM ESCÉPTICO)
- **No conformarse con la compilación exitosa:** Un código LaTeX que compila sin errores puede tener desbordamientos visuales (Overfull \\hbox), tablas truncadas o fórmulas mal alineadas.
- **Inspección Visual Automática:** Tras cada compilación a PDF, el agente debe invocar el motor de renderizado (src/auditor/visual_auditor.py) que convierte cada página a imagen PNG de alta resolución (300 DPI) para auditar:
  1. Que ninguna fórmula matemática se salga del margen o quede cortada.
  2. Que ninguna tabla exceda el ancho de página.
  3. Que los títulos y subtítulos no queden como líneas huérfanas al final de una página.
  4. Que no existan páginas en blanco no planificadas.
  5. Que los encabezados y numeración romana/arábiga cumplan la Resolución Rectoral.

## 4. ENFOQUE PMO Y TRAZABILIDAD
- Todo proceso de formateo debe registrarse en STATE.md (WBS y Quality Gates) y AUDIT_LOG.md (Checklist de verificación visual).
