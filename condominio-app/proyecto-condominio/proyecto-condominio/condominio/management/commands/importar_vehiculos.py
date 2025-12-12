# condominio/management/commands/importar_vehiculos.py

import pandas as pd
from django.core.management.base import BaseCommand
from condominio.models import Marca, Modelo

class Command(BaseCommand):
    help = 'Importa marcas y modelos de vehículos desde un archivo Excel.'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='La ruta del archivo Excel.')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        self.stdout.write(self.style.SUCCESS(f'Iniciando importación desde "{file_path}"...'))

        try:
            df = pd.read_excel(file_path)

            for index, row in df.iterrows():
                nombre_marca = str(row['Marca']).strip()
                nombre_modelo = str(row['Modelo']).strip()

                if not nombre_marca or not nombre_modelo:
                    continue

                # get_or_create busca el objeto, y si no existe, lo crea.
                # Esto evita duplicados.
                marca, created_marca = Marca.objects.get_or_create(nombre=nombre_marca)
                
                if created_marca:
                    self.stdout.write(f'Marca creada: {marca.nombre}')

                # Hacemos lo mismo para el modelo, asegurándonos de ligarlo a la marca correcta.
                modelo, created_modelo = Modelo.objects.get_or_create(
                    marca=marca, 
                    nombre=nombre_modelo
                )
                
                if created_modelo:
                    self.stdout.write(f'  - Modelo creado: {modelo.nombre}')

            self.stdout.write(self.style.SUCCESS('¡Importación de catálogo completada!'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'Error: El archivo "{file_path}" no fue encontrado.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ocurrió un error: {e}'))