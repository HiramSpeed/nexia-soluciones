import pandas as pd
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from condominio.models import Casa, Villa # <-- Importa Villa
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    help = 'Importa casas y crea usuarios desde un archivo Excel, asignándolos a una Villa específica.'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='La ruta del archivo Excel a importar.')
        # --- NUEVO ARGUMENTO ---
        parser.add_argument(
            '--villa_id',
            type=int,
            required=True,
            help='El ID de la Villa a la que se asignarán las casas.'
        )

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        villa_id = kwargs['villa_id']

        # --- NUEVA VALIDACIÓN ---
        try:
            villa = Villa.objects.get(id=villa_id)
            self.stdout.write(self.style.SUCCESS(f'Asignando casas a "{villa.nombre}"...'))
        except Villa.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Error: No se encontró una Villa con el ID "{villa_id}".'))
            return

        try:
            df = pd.read_excel(file_path, dtype=str)

            for index, row in df.iterrows():
                username = str(row['username']).strip()
                email = str(row['email']).strip()
                numero_casa = str(row['numero_casa']).strip()
                propietario = str(row['propietario']).strip()
                telefono = str(row['telefono']).strip()
                
                if User.objects.filter(username=username).exists():
                    self.stdout.write(self.style.WARNING(f'Usuario "{username}" ya existe. Saltando...'))
                    continue

                temp_password = get_random_string(length=10)
                user = User.objects.create_user(username=username, email=email, password=temp_password)
                
                # Checamos si la casa ya existe EN ESA VILLA
                if Casa.objects.filter(villa=villa, numero_casa=numero_casa).exists():
                    self.stdout.write(self.style.WARNING(f'Casa "{numero_casa}" en "{villa.nombre}" ya existe. Saltando...'))
                    user.delete()
                    continue

                # --- LÍNEA MODIFICADA ---
                Casa.objects.create(
                    villa=villa, # <-- Se asigna la villa
                    usuario=user,
                    numero_casa=numero_casa,
                    propietario=propietario,
                    telefono=telefono
                )

                self.stdout.write(f'Usuario "{username}" y Casa "{numero_casa}" creados con éxito. Contraseña temporal: {temp_password}')

            self.stdout.write(self.style.SUCCESS('¡Importación completada!'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'Error: El archivo "{file_path}" no fue encontrado.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ocurrió un error: {e}'))