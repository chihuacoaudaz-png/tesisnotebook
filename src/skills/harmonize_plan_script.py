# -*- coding: utf-8 -*-
with open('src/skills/generate_full_official_plan_50p.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('output/PLAN_DE_TESIS_OFICIAL_UNI_LINCUNA.docx', 'output/PLAN_DE_TESIS_OFICIAL_LINCUNA_2026.docx')
text = text.replace('output/PLAN_DE_TESIS_OFICIAL_UNI_LINCUNA.pdf', 'output/PLAN_DE_TESIS_OFICIAL_LINCUNA_2026.pdf')

text = text.replace('add_h1("6. MARCO TEÓRICO: BASES TEÓRICAS Y CIENTÍFICAS")', 'add_h1("6. MARCO TEÓRICO")\n    add_h2("6.1. Bases Teóricas")')
text = text.replace('add_h1("7. MARCO TEÓRICO: MARCO CONCEPTUAL")', 'add_h2("6.2. Marco Conceptual")')
text = text.replace('add_h1("8. METODOLOGÍA DE LA INVESTIGACIÓN")', 'add_h1("7. METODOLOGÍA")')
text = text.replace('add_h1("9. MATRIZ DE CONSISTENCIA LÓGICA (1:1)")', 'add_h2("7.6. Matriz de Consistencia Lógica (1:1)")')
text = text.replace('add_h1("10. CRONOGRAMA DE TRABAJO (16 SEMANAS)")', 'add_h1("8. CRONOGRAMA DEL TRABAJO")')
text = text.replace('add_h1("11. PRESUPUESTO Y FINANCIAMIENTO")', 'add_h1("9. PRESUPUESTO ANALÍTICO ESTIMADO")')
text = text.replace('add_h1("12. BIBLIOGRAFIA")', 'add_h1("10. BIBLIOGRAFÍA")')
text = text.replace('add_h1("13. ANEXOS Y ENTREGABLES TÉCNICOS")', 'add_h1("11. ANEXOS Y ENTREGABLES TÉCNICOS")')

with open('src/skills/build_plan_tesis_lincuna_50p.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated script written to src/skills/build_plan_tesis_lincuna_50p.py")
