import os

file_path = r"c:\Users\dhira\.gemini\antigravity\scratch\nexia-soluciones\condominio-app\proyecto-condominio\proyecto-condominio\condominio\templates\condominio\reservaciones.html"

# Read the file
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find and fix the {% for hora in horas_disponibles %} line that's missing {% endfor %}
# The line is split across multiple lines without proper closure

# Look for the pattern where the for loop is on one line
old_pattern = '''{% for hora in horas_disponibles %}<option value="{{ hora }}">{{ hora }}</option>{% endfor %}'''

# This should be the corrected single line version
new_pattern = '''{% for hora in horas_disponibles %}<option value="{{ hora }}">{{ hora }}</option>{% endfor %}'''

# Actually, let me check if the issue is the for loop is inline without endfor
# Based on the error, line 171 has {% endif %} but should have {% endfor %}
# This means there's a {% for %} loop that's not closed properly

# Let's search for the specific pattern
if '{% for hora in horas_disponibles %}' in content:
    print("Found the for loop")
    # Split content into lines to work with
    lines = content.split('\n')
    for i, line in enumerate(lines, 1):
        if '{% for hora in horas_disponibles %}' in line and '{% endfor %}' not in line:
            print(f"Line {i}: {line[:100]}")
            # Check if endfor is missing
            # Add endfor after the option tag closes
            if '<option value="{{ hora }}">{{ hora }}</option>' in line:
                # Replace the line to include endfor
                lines[i-1] = line.replace(
                    '<option value="{{ hora }}">{{ hora }}</option>',
                    '<option value="{{ hora }}">{{ hora }}</option>{% endfor %}'
                )
                print(f"Fixed line {i}")
                break
    
    # Write back
    content = '\n'.join(lines)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"File updated: {file_path}")
