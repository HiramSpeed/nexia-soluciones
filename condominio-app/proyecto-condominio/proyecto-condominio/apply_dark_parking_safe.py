import re

file_path = r"c:\Users\dhira\.gemini\antigravity\scratch\nexia-soluciones\condominio-app\proyecto-condominio\proyecto-condominio\condominio\templates\condominio\crear_reserva_parking.html"

# Read the file  
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Simple CSS class replacements that don't affect Django templates
replacements = [
    # Headers and links
    ('text-slate-800', 'text-gray-100'),
    ('text-slate-500', 'text-blue-400'),
    ('hover:text-blue-600', 'hover:text-blue-300'),
    
    # Main card
    ('bg-white rounded-xl shadow-lg border border-slate-100', 'bg-gray-800 rounded-xl shadow-lg border border-gray-700'),
    
    # Modal header
    ('bg-slate-50 px-6 py-5 border-b border-slate-200', 'bg-gray-750 px-6 py-5 border-b border-gray-700'),
    ('bg-blue-100 rounded-lg text-blue-600', 'bg-blue-900/30 rounded-lg text-blue-400'),
    
    # Titles and text in header
    ('text-lg font-bold text-slate-800', 'text-lg font-bold text-gray-100'),
    ('text-sm text-slate-500', 'text-sm text-gray-400'),
    
    # Info box
    ('bg-blue-50 border-l-4 border-blue-500', 'bg-blue-900/20 border-l-4 border-blue-500'),
    ('text-blue-800', 'text-blue-300'),
    ('text-blue-700', 'text-blue-200'),
    
    # Labels
    ('text-slate-700 mb-2', 'text-gray-300 mb-2'),
    
    # Inputs - be careful with multi line templates
    ('bg-gray-50 text-gray-900', 'bg-gray-700 text-gray-200'),
    ('border border-gray-300', 'border border-gray-600'),
    
    # Cancel button
    ('bg-white text-slate-700 font-bold py-3 px-4 rounded-lg border border-slate-300 hover:bg-slate-50', 
     'bg-gray-700 text-gray-200 font-bold py-3 px-4 rounded-lg border border-gray-600 hover:bg-gray-600'),
]

for old, new in replacements:
    content = content.replace(old, new)

# Write back
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Dark mode applied successfully to: {file_path}")
