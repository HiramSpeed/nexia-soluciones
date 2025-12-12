# condominio/management/commands/limpiar_datos.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from condominio.models import Casa

class Command(BaseCommand):
    help = 'Elimina TODAS las casas y usuarios que no sean administradores (superusers). ¡USAR CON CUIDADO!'

    def handle(self, *args, **kwargs):
        # Preguntamos al usuario para confirmar, como medida de seguridad.
        self.stdout.write(self.style.WARNING(
            'ADVERTENCIA: Estás a punto de borrar TODAS las casas y sus usuarios asociados.'
        ))
        respuesta = input('¿Estás seguro de que quieres continuar? Escribe "si" para confirmar: ')

        # Si la respuesta es afirmativa, procedemos.
        if respuesta.lower() == 'si':
            # Buscamos todos los usuarios que NO son superusuarios.
            # Esto evita que borres tu propia cuenta de administrador.
            usuarios_a_borrar = User.objects.filter(is_superuser=False)
            
            # Contamos cuántos vamos a borrar para informar al usuario.
            conteo_usuarios = usuarios_a_borrar.count()
            
            if conteo_usuarios > 0:
                # Borramos los usuarios. Las casas se borrarán en cascada.
                usuarios_a_borrar.delete()
                self.stdout.write(self.style.SUCCESS(
                    f'Se han eliminado {conteo_usuarios} usuarios y sus casas asociadas.'
                ))
            else:
                self.stdout.write(self.style.SUCCESS(
                    'No se encontraron usuarios (no administradores) para eliminar.'
                ))
        else:
            self.stdout.write(self.style.ERROR('Operación cancelada.'))