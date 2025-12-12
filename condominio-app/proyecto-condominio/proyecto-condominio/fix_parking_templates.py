import re

file_path = r"c:\Users\dhira\.gemini\antigravity\scratch\nexia-soluciones\condominio-app\proyecto-condominio\proyecto-condominio\condominio\templates\condominio\crear_reserva_parking.html"

# Read the file
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix split add_class tags - join lines that are part of Django template variables
# Pattern: finds {{ form.field|add_class:" that spans multiple lines
content = re.sub(
    r'\{\{\s*form\.(fecha_inicio|fecha_fin)\|add_class:"([^"]*?)\s+([^"]*?)\s+([^"]*?)"\s*\}\}',
    r'{{ form.\1|add_class:"\2 \3 \4" }}',
    content,
    flags=re.DOTALL
)

# More aggressive: join any line breaks within Django template variables
lines = content.split('\n')
result_lines = []
i = 0

while i < len(lines):
    line = lines[i]
    
    # Check if this line has an opening {{ but no closing }}
    if '{{' in line and '}}' not in line:
        # Join with next lines until we find the closing }}
        joined = line
        i += 1
        while i < len(lines) and '}}' not in lines[i]:
            joined += ' ' + lines[i].strip()
            i += 1
        if i < len(lines):
            joined += ' ' + lines[i].strip()
            i += 1
        # Clean up multiple spaces
        joined = re.sub(r'\s+', ' ', joined)
        result_lines.append(joined)
    else:
        result_lines.append(line)
        i += 1

content = '\n'.join(result_lines)

# Write back
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Fixed split Django template tags in: {file_path}")
