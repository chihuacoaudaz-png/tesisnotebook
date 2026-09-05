import os
import shutil

src_dir = "formateador/output/figuras_numeradas"
backup_dir = "formateador/backup_figuras_usuario"
target_dir = "formateador/figuras"

os.makedirs(backup_dir, exist_ok=True)
os.makedirs(target_dir, exist_ok=True)

# 1. Realizar BACKUP COMPLETO de todas las modificaciones del usuario
print("=== PASO 1: Creando BACKUP de figuras del usuario ===")
user_files = os.listdir(src_dir)
for f in user_files:
    src_f = os.path.join(src_dir, f)
    dst_f = os.path.join(backup_dir, f)
    shutil.copy2(src_f, dst_f)
print(f"[OK] Backup completado: {len(user_files)} archivos guardados en {backup_dir}")

# 2. Sincronizar y estandarizar a target_dir (formateador/figuras/)
print("\n=== PASO 2: Estandarizando y sincronizando a formateador/figuras/ ===")

# Copiar todas las figuras figura_XX.png, tabla_01.png, figura_09a.png, etc.
for f in user_files:
    src_f = os.path.join(src_dir, f)
    if f.startswith("figura_") or f.startswith("tabla_"):
        dst_f = os.path.join(target_dir, f)
        shutil.copy2(src_f, dst_f)
        print(f"  Copiado: {f}")

# Reemplazar las figuras 35 a 48 que el usuario nombró como '35.png' a '48.png'
for num in range(35, 49):
    raw_name = f"{num}.png"
    std_name = f"figura_{num:02d}.png"
    src_f = os.path.join(src_dir, raw_name)
    if os.path.exists(src_f):
        dst_f = os.path.join(target_dir, std_name)
        shutil.copy2(src_f, dst_f)
        print(f"  Reemplazado: {raw_name} -> {std_name}")
    else:
        print(f"  [AVISO] No se encontró {raw_name}")

print("\n=== Total de figuras en formateador/figuras/ ===")
final_files = sorted(os.listdir(target_dir))
for f in final_files:
    sz = os.path.getsize(os.path.join(target_dir, f))
    print(f"  {f:25s} ({sz/1024:.1f} KB)")

print(f"\n[EXITO TOTAL] {len(final_files)} figuras sincronizadas y respaldadas.")
