import fitz
import os

doc = fitz.open("formateador/input/proyectoCJN.pdf")
os.makedirs("formateador/output/figures_individual", exist_ok=True)

# Guardar imagenes extraidas directas
extracted = {}
for p_no in range(len(doc)):
    page = doc[p_no]
    img_list = page.get_images(full=True)
    for idx, img in enumerate(img_list):
        xref = img[0]
        base_img = doc.extract_image(xref)
        w, h = base_img["width"], base_img["height"]
        ext = base_img["ext"]
        # Ignorar logos de encabezado repetitivos
        if w == 1711 and h == 373:
            continue
        out_path = f"formateador/output/figures_individual/raw_p{p_no+1:02d}_img{idx+1}_{w}x{h}.{ext}"
        with open(out_path, "wb") as f:
            f.write(base_img["image"])
        extracted[f"p{p_no+1}_{idx+1}"] = out_path
        print(f"Guardada imagen pura: {out_path}")

print(f"[OK] Total imagenes puras guardadas: {len(extracted)}")
