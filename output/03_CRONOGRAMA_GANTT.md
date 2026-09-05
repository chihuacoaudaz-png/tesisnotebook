# CRONOGRAMA DE ACTIVIDADES (DIAGRAMA DE GANTT) - 4 MESES

**PROYECTO:** Sistema agéntico basado en inteligencia artificial para el diseño asistido de perforación y voladura orientado al control de la sobrerotura en labores subterráneas de la U.E.A. Lincuna, 2026.  
**DURACIÓN TOTAL:** 16 Semanas (4 Meses).

---

## 1. Estructura de Desglose del Trabajo (WBS) y Cronograma Semanal

| Código WBS | Fase / Actividad de Investigación | Mes 1 (Sem. 1 - 4) | Mes 2 (Sem. 5 - 8) | Mes 3 (Sem. 9 - 12) | Mes 4 (Sem. 13 - 16) | Responsable |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **1.0** | **FASE 1: PLANIFICACIÓN Y RECOLECCIÓN DE DATOS** | | | | | |
| 1.1 | Aprobación del Plan de Tesis en la Escuela de Posgrado / FIGMM UNI | [ X ] [   ] [   ] [   ] | [   ] [   ] [   ] [   ] | [   ] [   ] [   ] [   ] | [   ] [   ] [   ] [   ] | Tesista / Asesor |
| 1.2 | Mapeo geomecánico in situ en cruceros de la U.E.A. Lincuna (RMR, GSI, UCS) | [   ] [ X ] [ X ] [   ] | [   ] [   ] [   ] [   ] | [   ] [   ] [   ] [   ] | [   ] [   ] [   ] [   ] | Geomecánico / Tesista |
| 1.3 | Recopilación de línea base histórica de sobrerotura y costos de shotcrete | [   ] [   ] [ X ] [ X ] | [   ] [   ] [   ] [   ] | [   ] [   ] [   ] [   ] | Mina / Topografía |
| **2.0** | **FASE 2: DESARROLLO DEL SISTEMA AGÉNTICO Y MOTOR FÍSICO** | | | | | |
| 2.1 | Programación del Motor Determinístico de Holmberg en Python (`SKILL-02`) | [   ] [   ] [   ] [   ] | [ X ] [ X ] [   ] [   ] | [   ] [   ] [   ] [   ] | Desarrollador / Tesista |
| 2.2 | Desarrollo del algoritmo heurístico de Auto-Tajeo y Ayudas (`SKILL-03`) | [   ] [   ] [   ] [   ] | [   ] [ X ] [ X ] [   ] | [   ] [   ] [   ] [   ] | Desarrollador / Tesista |
| 2.3 | Integración de agentes auditores y escépticos en bucle de autocorrección | [   ] [   ] [   ] [   ] | [   ] [   ] [ X ] [ X ] | [   ] [   ] [   ] [   ] | PMO / Red Team |
| **3.0** | **FASE 3: PRUEBAS EXPERIMENTALES DE CAMPO Y MONITOREO 3D** | | | | | |
| 3.1 | Implementación de las mallas generadas en 30 disparos de prueba en Lincuna | [   ] [   ] [   ] [   ] | [   ] [   ] [   ] [   ] | [ X ] [ X ] [ X ] [   ] | Operaciones / Tesista |
| 3.2 | Levantamiento topográfico post-voladura con Escáner Láser 3D (LIDAR) | [   ] [   ] [   ] [   ] | [   ] [   ] [   ] [   ] | [ X ] [ X ] [ X ] [ X ] | Topografía / Tesista |
| 3.3 | Balance de consumo de shotcrete, horas scooptramp y fragmentación | [   ] [   ] [   ] [   ] | [   ] [   ] [   ] [   ] | [   ] [   ] [ X ] [ X ] | Costos / Geomecánica |
| **4.0** | **FASE 4: ANÁLISIS ESTADÍSTICO, REDACCIÓN Y SUSTENTACIÓN** | | | | | |
| 4.1 | Ejecución de pruebas estadísticas inferenciales $t$-Student (`SKILL-04`) | [   ] [   ] [   ] [   ] | [   ] [   ] [   ] [   ] | [   ] [   ] [   ] [   ] | [ X ] [   ] [   ] [   ] | Estadístico / Tesista |
| 4.2 | Redacción del informe final de tesis (Capítulos I al V y Anexos) | [   ] [   ] [   ] [   ] | [   ] [   ] [   ] [   ] | [   ] [   ] [   ] [   ] | [ X ] [ X ] [   ] [   ] | Tesista / Redactor |
| 4.3 | Revisión por jurado de tesis y levantamiento de observaciones | [   ] [   ] [   ] [   ] | [   ] [   ] [   ] [   ] | [   ] [   ] [   ] [   ] | [   ] [   ] [ X ] [   ] | Jurados UNI FIGMM |
| 4.4 | Sustentación pública y defensa de la Tesis Profesional | [   ] [   ] [   ] [   ] | [   ] [   ] [   ] [   ] | [   ] [   ] [   ] [   ] | [   ] [   ] [   ] [ X ] | Tesista |

---

## 2. Hitos Críticos de Control (Quality Gates)
* **Hito 1 (Semana 4):** Base de datos geomecánica y línea base operacional 100% consolidada.
* **Hito 2 (Semana 8):** Motor físico y algoritmo de auto-tajeo validados computacionalmente ($P_{te} \le \sigma_c$).
* **Hito 3 (Semana 12):** Culminación de las 30 voladuras experimentales y escaneo 3D en U.E.A. Lincuna.
* **Hito 4 (Semana 16):** Informe final aprobado y sustentación de tesis completada.
