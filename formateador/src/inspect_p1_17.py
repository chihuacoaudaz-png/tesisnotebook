import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('formateador/input/proyectoCJN.pdf')

for p_no in range(0, 17):
    page = doc[p_no]
    blocks = page.get_text('blocks')
    images = page.get_images()
    print(f'=== PAGINA {p_no+1} ===')
    for b in blocks:
        text = b[4].strip().replace('\n', ' ')
        if len(text) > 90:
            text = text[:90] + '...'
        print(f'   TEXT ({b[0]:.1f}, {b[1]:.1f}, {b[2]:.1f}, {b[3]:.1f}): "{text}"')
    for img_info in images:
        xref = img_info[0]
        rects = page.get_image_rects(xref)
        for rect in rects:
            print(f'   IMG xref={xref}: ({rect.x0:.1f}, {rect.y0:.1f}, {rect.x1:.1f}, {rect.y1:.1f})')
