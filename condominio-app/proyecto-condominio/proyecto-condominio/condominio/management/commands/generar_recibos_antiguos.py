# /condominio/management/commands/generar_recibos_antiguos.py

from django.core.management.base import BaseCommand
from condominio.models import Transaccion
# ¡Importante! Importamos la función que ya creamos para generar el PDF
from condominio.views import generar_y_guardar_recibo_transaccion

class Command(BaseCommand):
    help = 'Genera los recibos PDF para todas las transacciones de abono aprobadas que no lo tengan.'

    def handle(self, *args, **kwargs):
        # 1. Buscamos todas las transacciones que cumplen las condiciones:
        #    - Son de tipo 'ABONO'.
        #    - Ya están 'APROBADAS'.
        #    - Su campo de recibo está vacío.
        transacciones_sin_recibo = Transaccion.objects.filter(
            tipo='ABONO',
            estado_aprobacion='APROBADO',
            recibo_pdf__in=['', None]
        )

        if not transacciones_sin_recibo.exists():
            self.stdout.write(self.style.SUCCESS('¡Excelente! No hay transacciones antiguas que necesiten un recibo.'))
            return

        self.stdout.write(f'Se encontraron {transacciones_sin_recibo.count()} transacciones sin recibo. Iniciando proceso...')

        # 2. Recorremos cada una y generamos su recibo
        for transaccion in transacciones_sin_recibo:
            try:
                generar_y_guardar_recibo_transaccion(transaccion)
                self.stdout.write(self.style.SUCCESS(f' -> Recibo generado exitosamente para la transacción ID: {transaccion.id}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f' -> Error al generar recibo para la transacción ID: {transaccion.id}. Error: {e}'))

        self.stdout.write(self.style.SUCCESS('¡Proceso completado!'))