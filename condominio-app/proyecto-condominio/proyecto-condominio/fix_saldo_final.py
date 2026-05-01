file_path = r"c:\Users\dhira\.gemini\antigravity\scratch\nexia-soluciones\condominio-app\proyecto-condominio\proyecto-condominio\condominio\templates\condominio\dashboard_residente_nuevo.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the split balance template tag
old_text = '''{% elif casa.saldo < 0 %} <p class="text-4xl font-bold text-green-500">${{
                    casa.saldo|stringformat:".2f"|slice:"1:" }}</p>'''

new_text = '''{% elif casa.saldo < 0 %}
                <p class="text-4xl font-bold text-green-500">${{ casa.saldo|stringformat:".2f"|slice:"1:" }}</p>'''

if old_text in content:
    content = content.replace(old_text, new_text)
    print("✅ Fixed split balance template tag!")
else:
    print("⚠️ Pattern not found, trying alternate pattern...")
    # Try with different line endings
    old_alt = old_text.replace('\n', '\r\n')
    if old_alt in content:
        content = content.replace(old_alt, new_text.replace('\n', '\r\n'))
        print("✅ Fixed with alternate line endings!")
    else:
        print("❌ Could not find pattern")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"File saved: {file_path}")
