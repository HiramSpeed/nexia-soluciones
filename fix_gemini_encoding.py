#!/usr/bin/env python3
"""
Reparar archivos con encoding incorrecto en .gemini
Convierte todo a UTF-8 puro sin BOM
"""
from pathlib import Path
import os

gemini_base = Path(r'C:\Users\dhira\.gemini\antigravity\scratch\nexia-soluciones\condominio-app\proyecto-condominio')
files_to_fix = [
    gemini_base / 'condominio\templates\condominio\dashboard_residente_nuevo.html',
    gemini_base / 'condominio\templates\condominio\reservaciones.html',
    gemini_base / 'condominio\templates\condominio\_header_villa.html',
]

for fpath in files_to_fix:
    if not fpath.exists():
        print(f"SKIP (not found): {fpath}")
        continue
    
    print(f"Processing: {fpath}")
    
    # Leer con detección automática
    try:
        # Intenta leer como UTF-8 con BOM, luego fallback a latin-1
        raw_bytes = fpath.read_bytes()
        
        # Detectar encoding
        if raw_bytes.startswith(b'\xff\xfe'):
            # UTF-16 LE
            content = raw_bytes.decode('utf-16-le')
            print(f"  Detected: UTF-16-LE")
        elif raw_bytes.startswith(b'\xfe\xff'):
            # UTF-16 BE
            content = raw_bytes.decode('utf-16-be')
            print(f"  Detected: UTF-16-BE")
        elif raw_bytes.startswith(b'\xef\xbb\xbf'):
            # UTF-8 with BOM
            content = raw_bytes.decode('utf-8-sig')
            print(f"  Detected: UTF-8-BOM")
        else:
            # Intenta UTF-8
            try:
                content = raw_bytes.decode('utf-8')
                print(f"  Detected: UTF-8 (clean)")
            except:
                # Fallback latin-1
                content = raw_bytes.decode('latin-1', errors='ignore')
                print(f"  Detected: Latin-1 (fallback)")
        
        # Reescribir como UTF-8 puro sin BOM
        fpath.write_text(content, encoding='utf-8')
        print(f"  ✓ Fixed to UTF-8")
        
    except Exception as e:
        print(f"  ✗ ERROR: {e}")

print("\nDone!")
