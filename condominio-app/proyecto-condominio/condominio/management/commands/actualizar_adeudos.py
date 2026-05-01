# condominio/management/commands/actualizar_adeudos.py

from django.core.management.base import BaseCommand
from condominio.models import Pago, Casa
from datetime import date

class Command(BaseCommand):
    help = 'Revisa los pagos pendientes y los marca como "Atrasado" si la fecha de vencimiento ya pasó.'

    def handle(self, *args, **kwargs):
        hoy = date.today()
        # Buscamos pagos que están 'Pendientes' y cuya fecha de vencimiento es anterior a hoy
        pagos_vencidos = Pago.objects.filter(
            estado='Pendiente',
            fecha_vencimiento__lt=hoy
        )
        
        casas_afectadas = set()
        for pago in pagos_vencidos:
            casas_afectadas.add(pago.casa)

        # Actualizamos todos los pagos vencidos encontrados a 'Atrasado'
        num_actualizados = pagos_vencidos.update(estado='Atrasado')

        if num_actualizados > 0:
            self.stdout.write(self.style.SUCCESS(f'Se actualizaron {num_actualizados} pagos a "Atrasado".'))
            # Ahora, recalculamos el estatus de las casas afectadas
            for casa in casas_afectadas:
                casa.actualizar_estatus_automatico()
            self.stdout.write(f'Se revisó el estatus de {len(casas_afectadas)} casas.')
        else:
            self.stdout.write('No se encontraron nuevos pagos vencidos.')