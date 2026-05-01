from pathlib import Path
files=[
    'condominio-app/proyecto-condominio/condominio/templates/condominio/reservaciones.html',
    'condominio-app/proyecto-condominio/condominio/templates/condominio/_header_villa.html',
    'condominio-app/proyecto-condominio/proyecto-condominio/condominio/templates/condominio/_header_villa.html'
]
for f in files:
    p=Path(f)
    print('FILE:', f)
    if not p.exists():
        print('  MISSING')
        continue
    b=p.read_bytes()
    print('  bytes:', len(b))
    print('  first10:', ' '.join(hex(x) for x in b[:10]))
    # try decode utf-8
    try:
        s=b.decode('utf-8')
        print('  decodes as utf-8 OK')
    except Exception as e:
        print('  utf-8 decode ERROR:', repr(e))
    # try decode utf-16
    try:
        s=b.decode('utf-16')
        print('  decodes as utf-16 OK')
    except Exception as e:
        print('  utf-16 decode ERROR:', repr(e))
    print()
