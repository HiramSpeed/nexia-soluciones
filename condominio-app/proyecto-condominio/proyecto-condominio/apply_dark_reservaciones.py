import os

file_path = r"c:\Users\dhira\.gemini\antigravity\scratch\nexia-soluciones\condominio-app\proyecto-condominio\proyecto-condominio\condominio\templates\condominio\reservaciones.html"

# Read original file
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace styles section with dark mode + list view styling
old_style = '''    <style>
        body { font-family: 'Inter', sans-serif; }
        .fc .fc-button-primary { background-color: #3b82f6; border-color: #3b82f6; }
        .fc .fc-button-primary:hover { background-color: #2563eb; }
        .fc .fc-toolbar-title { font-size: 1.25rem; }
    </style>'''

new_style = '''    <link href="https://fonts.googleapis.com/css2?family=Jura:wght@300;400;500;600;700&family=Lato:wght@300;400;700&display=swap" rel="stylesheet">
    <style>
        body {  font-family: 'Lato', sans-serif; background-color: #1a202c; }
        h1, h2, h3 { font-family: 'Jura', sans-serif; }
        
        /* Dark mode calendar styling */
        .fc { background-color: #2d3748; color: #e2e8f0; }
        .fc .fc-button-primary { background-color: #4299e1; border-color: #4299e1; }
        .fc .fc-button-primary:hover { background-color: #3182ce; }
        .fc .fc-toolbar-title { font-size: 1.25rem; color: #e2e8f0; }
        .fc-theme-standard td, .fc-theme-standard th { border-color: #4a5568; }
        .fc-daygrid-day-number { color: #cbd5e0; }
        .fc-col-header-cell-cushion { color: #a0aec0; }
        .fc-daygrid-day.fc-day-today { background-color: rgba(66, 153, 225, 0.1) !important; }
        
        /* List view date headers - make bold and visible */
        .fc-list-day-cushion { font-weight: 700 !important; color: #e2e8f0 !important; font-size: 1.1rem !important; }
        .fc-list-event-time { color: #cbd5e0; }
        .fc-list-event-title { color: #e2e8f0; }
    </style>'''

content = content.replace(old_style, new_style)

# Apply dark mode classes
content = content.replace('class="bg-gray-100"', 'class="bg-gray-900"')
content = content.replace('class="bg-white p-4 sm:p-6 md:p-8 rounded-xl shadow-lg mt-8"', 
                         'class="bg-gray-800 p-4 sm:p-6 md:p-8 rounded-xl shadow-lg mt-8 border border-gray-700"')
content = content.replace('class="inline-block mb-6 font-semibold text-blue-600 hover:text-blue-800"',
                         'class="inline-block mb-6 font-semibold text-blue-400 hover:text-blue-300"')
content = content.replace('class="text-3xl font-bold text-gray-800 mb-2"',
                         'class="text-3xl font-bold text-gray-100 mb-2"')
content = content.replace('class="text-gray-600 mb-8"', 'class="text-gray-300 mb-8"')

# Fix message boxes
content = content.replace(
    'class="p-4 mb-2 rounded-lg text-sm font-medium {% if message.tags == \'success\' %}bg-green-100 text-green-800{% else %}bg-red-100 text-red-800{% endif %}"',
    'class="p-4 mb-2 rounded-lg text-sm font-medium {% if message.tags == \'success\' %}bg-green-900/50 text-green-200 border border-green-700{% else %}bg-red-900/50 text-red-200 border border-red-700{% endif %}"'
)

# Fix modal
content = content.replace('class="hidden fixed inset-0 bg-gray-900 bg-opacity-75',
                         'class="hidden fixed inset-0 bg-gray-900 bg-opacity-90')
content = content.replace('class="bg-white rounded-xl shadow-2xl p-6 w-full max-w-md relative"',
                         'class="bg-gray-800 rounded-xl shadow-2xl p-6 w-full max-w-md relative border border-gray-700"')
content = content.replace('class="text-gray-400 hover:text-gray-600"', 'class="text-gray-400 hover:text-gray-200"')
content = content.replace('class="text-2xl font-bold text-gray-800 mb-6"', 'class="text-2xl font-bold text-gray-100 mb-6"')

# Fix form labels and inputs
content = content.replace('class="block text-sm font-medium text-gray-700 mb-1"',
                         'class="block text-sm font-medium text-gray-300 mb-1"')
content = content.replace('bg-white border border-gray-300',
                         'bg-gray-700 border border-gray-600 text-gray-200')

# Fix pool rules section
content = content.replace('class="hidden space-y-3 p-4 bg-blue-50 rounded-lg"',
                         'class="hidden space-y-3 p-4 bg-blue-900/30 rounded-lg border border-blue-700"')
content = content.replace('class="font-bold text-gray-800"', 'class="font-bold text-gray-100"')
content = content.replace('class="list-disc list-inside text-sm text-gray-700 space-y-1"',
                         'class="list-disc list-inside text-sm text-gray-300 space-y-1"')
content = content.replace('class="h-4 w-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"',
                         'class="h-4 w-4 text-blue-500 bg-gray-700 border-gray-600 rounded focus:ring-blue-500"')
content = content.replace('class="ml-2 block text-sm text-gray-900"', 'class="ml-2 block text-sm text-gray-200"')

# Fix submit button
content = content.replace('class="w-full py-3 px-4 rounded-xl bg-blue-600 text-white font-semibold hover:bg-blue-700 transition-colors"',
                         'class="w-full py-3 px-4 rounded-xl bg-blue-600 text-white font-semibold hover:bg-blue-700 transition-colors shadow-lg"')

# Fix the split endfor tag
content = content.replace(
    '{% for hora in horas_disponibles %}<option value="{{ hora }}">{{ hora }}</option>{% endfor\n                            %}',
    '{% for hora in horas_disponibles %}<option value="{{ hora }}">{{ hora }}</option>{% endfor %}'
)

# Write back
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Dark mode + list styling applied to: {file_path}")
