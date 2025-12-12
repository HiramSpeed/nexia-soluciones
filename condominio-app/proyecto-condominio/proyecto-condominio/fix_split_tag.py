import os

file_path = r"c:\Users\dhira\.gemini\antigravity\scratch\nexia-soluciones\condominio-app\proyecto-condominio\proyecto-condominio\condominio\templates\condominio\dashboard_residente_nuevo.html"

# Read the file
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Join lines 188-189 (index 187-188)
if len(lines) > 188:
    # Check if line 187 (index 187) contains the split pattern
    if "{% if transaccion.tipo == 'ABONO' and transaccion.estado_aprobacion == 'APROBADO'" in lines[187]:
        # Join line 187 and 188
        joined_line = lines[187].rstrip('\r\n') + ' and transaccion.recibo_pdf %}\r\n'
        # Replace lines 187-188 with the joined line
        lines[187] = joined_line
        # Remove line 188
        del lines[188]
        print("Fixed lines 188-189!")
    else:
        print("Pattern not found on expected line")
else:
    print("File doesn't have enough lines")

# Write back
with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print(f"File updated: {file_path}")
