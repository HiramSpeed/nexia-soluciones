import os

file_path = r"c:\Users\dhira\.gemini\antigravity\scratch\nexia-soluciones\condominio-app\proyecto-condominio\proyecto-condominio\condominio\templates\condominio\reservaciones.html"

# Read the file
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Fix line 130 (index 129) - join the split {% endfor %}
if len(lines) > 130:
    # Check if line 129 contains the split pattern
    if '{% endfor' in lines[129] and '%}' in lines[130]:
        print(f"Line 130: {lines[129][:100]}")
        print(f"Line 131: {lines[130][:100]}")
        
        # Join line 129 and 130
        joined_line = lines[129].rstrip('\r\n') + lines[130].lstrip()
        # Remove the extra space and format correctly
        joined_line = joined_line.replace('{% endfor\n                            %}', '{% endfor %}')
        
        # Replace lines 129 with the joined line
        lines[129] = joined_line
        # Remove line 130
        del lines[130]
        print("Fixed split endfor tag!")
    else:
        print("Pattern not found on expected lines")
        print(f"Line 130: {lines[129][:150]}")
        if len(lines) > 130:
            print(f"Line 131: {lines[130][:150]}")
else:
    print("File doesn't have enough lines")

# Write back
with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print(f"File updated: {file_path}")
