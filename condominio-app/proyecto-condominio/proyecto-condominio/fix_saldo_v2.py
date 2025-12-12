file_path = r"c:\Users\dhira\.gemini\antigravity\scratch\nexia-soluciones\condominio-app\proyecto-condominio\proyecto-condominio\condominio\templates\condominio\dashboard_residente_nuevo.html"

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Lines 59-60 need to be joined (0-indexed: 58-59)
for i, line in enumerate(lines):
    if '{% elif casa.saldo < 0 %}' in line and '{{' in line and '}}' not in line:
        print(f"Found split line at {i+1}: {line[:80]}")
        # This line has the opening {{ but not the closing }}
        # Next line should have the rest
        if i+1 < len(lines) and '}}' in lines[i+1]:
            print(f"Next line: {lines[i+1][:80]}")
            # Create fixed content
            fixed_line = '                {% elif casa.saldo < 0 %}\r\n                <p class="text-4xl font-bold text-green-500">${{ casa.saldo|stringformat:".2f"|slice:"1:" }}</p>\r\n'
            lines[i] = fixed_line
            lines[i+1] = ''  # Remove the old second line
            print("FIXED!")
            break

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("File saved successfully")
