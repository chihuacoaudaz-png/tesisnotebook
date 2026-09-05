import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('formateador/input/proyectoCJN.pdf')

for p_no in range(7, 13):
    page = doc[p_no]
    blocks = page.get_text('blocks')
    images = page.get_images()
    print(f'\n========================================')
    print(f'=== PAGINA {p_no+1} ===')
    print(f'========================================')
    for b in sorted(blocks, key=lambda x: x[1]):
        text = b[4].strip().replace('\n', ' ')
        print(f'   TEXT (y0={b[1]:.1f}, y1={b[3]:.1f}, x0={b[0]:.1f}, x1={b[2]:.1f}): "{text}"')
    for img_info in images:
        xref = img_info[0]
        rects = page.get_image_rects(xref)
        for rect in rects:
            print(f'   IMG xref={xref}: (y0={rect.y0:.1f}, y1={rect.y1:.1f}, x0={rect.x0:.1f}, x1={rect.x1:.1f})')
