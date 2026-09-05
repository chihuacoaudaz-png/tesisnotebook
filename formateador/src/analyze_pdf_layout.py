import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('formateador/input/proyectoCJN.pdf')

for p_no in range(len(doc)):
    page = doc[p_no]
    blocks = page.get_text('blocks')
    images = page.get_images()
    print(f'=== PAGINA {p_no+1} === (W={page.rect.width}, H={page.rect.height})')
    print(f'   Imagenes rasterizadas encontradas: {len(images)}')
    for img_info in images:
        xref = img_info[0]
        rects = page.get_image_rects(xref)
        for rect in rects:
            print(f'      IMG xref={xref}: bbox=({rect.x0:.1f}, {rect.y0:.1f}, {rect.x1:.1f}, {rect.y1:.1f}) -> W={rect.width:.1f}, H={rect.height:.1f}')
    
    print('   Bloques de texto:')
    for b in blocks:
        text = b[4].strip().replace('\n', ' ')
        if len(text) > 80:
            text = text[:80] + '...'
        print(f'      TEXT: ({b[0]:.1f}, {b[1]:.1f}, {b[2]:.1f}, {b[3]:.1f}) -> "{text}"')
