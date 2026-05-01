import os

file_path = r"c:\Users\dhira\.gemini\antigravity\scratch\nexia-soluciones\condominio-app\proyecto-condominio\proyecto-condominio\condominio\templates\condominio\dashboard_residente_nuevo.html"

# Read the file
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Fix line 59 (index 58) - join the split balance template tag
if len(lines) > 59:
    # Check if line 58 contains the split pattern
    if "{% elif casa.saldo < 0 %}" in lines[58] and "casa.saldo|stringformat" in lines[59]:
        # Join line 58 and 59 properly
        joined_line = '                {% elif casa.saldo < 0 %} <p class="text-4xl font-bold text-green-500">${{ casa.saldo|stringformat:".2f"|slice:"1:" }}</p>\r\n'
        # Replace lines 58-59 with the joined line
        lines[58] = joined_line
        # Remove line 59
        del lines[59]
        print("Fixed balance display lines 59-60!")
    else:
        print("Pattern not found on expected line")
        print(f"Line 59: {lines[58][:100]}")
        print(f"Line 60: {lines[59][:100]}")
else:
    print("File doesn't have enough lines")

# Write back
with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print(f"File updated: {file_path}")
