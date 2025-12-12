import os
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto-condominio.settings') # <--- CAMBIA ESTO por el nombre de tu carpeta de settings (ej: 'proyecto_condominio')
django.setup()

from condominio.models import CategoriaIncidencia

# Lista de faltas basadas en el Reglamento de Villa Catania
categorias = [
    {
        "nombre": "Ruido Excesivo / Fiestas",
        "monto": 500.00,
        "desc": "Violación al Art. 97: Ruido que perturba la paz vecinal (música alta, gritos)."
    },
    {
        "nombre": "Estacionamiento Prohibido",
        "monto": 300.00,
        "desc": "Violación al Art. 22: Estacionarse en vialidades comunes, banquetas o bloquear cocheras."
    },
    {
        "nombre": "Mascotas (Heces / Sin Correa)",
        "monto": 250.00,
        "desc": "Violación al Art. 38: No recoger heces fecales o pasear mascotas sin correa."
    },
    {
        "nombre": "Basura en Área Común",
        "monto": 200.00,
        "desc": "Violación al Art. 36: Depositar basura o escombros fuera de los contenedores designados."
    },
    {
        "nombre": "Faltas a la Moral / Higiene",
        "monto": 800.00,
        "desc": "Violación al Art. 19: Actos contra la moral (ej. necesidades fisiológicas en áreas comunes, exhibicionismo)."
    },
    {
        "nombre": "Fachada no Autorizada",
        "monto": 1000.00,
        "desc": "Violación al Art. 72: Alteración de fachada, pintura no autorizada o ampliaciones sin permiso."
    },
    {
        "nombre": "Uso Indebido de Alberca/Terraza",
        "monto": 400.00,
        "desc": "Violación al Art. 34: Daños o mal uso de las instalaciones recreativas."
    }
]

print("--- Iniciando carga de categorías ---")

for cat in categorias:
    obj, created = CategoriaIncidencia.objects.get_or_create(
        nombre=cat["nombre"],
        defaults={
            'monto_base': cat["monto"]
            # Si agregaste el campo 'descripcion' al modelo CategoriaIncidencia, descomenta esto:
            # 'descripcion': cat["desc"]
        }
    )
    if created:
        print(f"✅ Creada: {cat['nombre']}")
    else:
        print(f"ℹ️ Ya existía: {cat['nombre']}")

print("--- ¡Listo! Ya aparecerán en el formulario ---")