# Reglas de Operación y Fuentes de Investigación (NotebookLM + Deep Research)

## 1. Uso Obligatorio de NotebookLM como Fuente Primaria
- **Fundamentación basada en Cuadernos:** Para cualquier consulta, análisis, redacción de tesis, marco teórico o soporte técnico, el agente debe utilizar siempre como fuente de verdad y contexto principal un cuaderno de **Google NotebookLM**.
- **Consulta Activa:** Se deben consultar las fuentes y notas del cuaderno seleccionado mediante las herramientas de NotebookLM (`notebooklm ask`, consultas vía MCP o scripts auxiliares) para garantizar respuestas citadas y fundamentadas en la literatura disponible.
- **Cuadernos Oficiales del Proyecto:**
  - *Cuaderno 1 (Marco Metodológico de Posgrado):* `Marco Metodologico de Posgrado UNI FIGMM - Dra. Rosario Martinez` (`769227ea-9b15-4fbc-a382-b14cd5e7435f`).
  - *Cuaderno 2 (Tesis de Posgrado - Núcleo Técnico y Agéntico):* `Tesis: Sistema Agentico de P&V y Control de Sobrerotura - Minera Lincuna 2026` (`780ac1ad-e15b-4801-be5e-44131370dfbc`).
  - *Cuadernos Secundarios / Históricos:* `Modernizing Blast Fragmentation: From Kuz-Ram to Machine Learning` (`335db12c-d698-4332-8608-152fa04dc79d`) y `Rock Fragmentation Prediction using the Kuz-Ram Model` (`ae93a924-19a7-44ce-838a-20c5d133610b`).

## 2. Ingesta Obligatoria de Deep Research en el Modo Más Profundo
- **Modo Deep Obligatorio:** Toda búsqueda o investigación de nuevos artículos científicos, normativas o documentación técnica debe ejecutarse utilizando **Google Deep Research en NotebookLM** en el modo más profundo disponible:
  ```bash
  notebooklm source add-research "<tema_o_pregunta>" --mode deep --import-all -n <notebook_id>
  ```
- **Alimentación Continua del Cuaderno:** Todas las fuentes resultantes del Deep Research deben ser importadas íntegramente al cuaderno objetivo (`--import-all`), asegurando que la base de conocimiento crezca de forma estructurada con cada investigación.

## 3. Máximo Nivel de Modelo y Rigor Académico
- **Modelo más Avanzado:** Cuando se requiera invocar subagentes o procesos de razonamiento avanzado para el análisis o redacción de la tesis, se debe seleccionar siempre el modelo más avanzado disponible (`pro`).
- **Trazabilidad y Citas:** Todas las afirmaciones técnicas, fórmulas (ej. Kuz-Ram, Swebrec, KCO), métricas de ML ($R^2$, RMSE, MAE, SHAP values) y análisis geomecánicos deben estar estrictamente respaldados y contrastados con las fuentes del cuaderno.
