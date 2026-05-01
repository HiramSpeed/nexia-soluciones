import calendar
from datetime import date
from django.core.management.base import BaseCommand
from django.db import transaction
from condominio.models import Casa, Transaccion, Villa
from decimal import Decimal

class Command(BaseCommand):
    help = 'Crea una Transaccion de CARGO por mantenimiento para todas las casas de una Villa específica.'

    def add_arguments(self, parser):
        parser.add_argument(
            'villa_id',
            type=int,
            help='El ID de la Villa para la cual generar los cargos.'
        )

    def handle(self, *args, **kwargs):
        villa_id = kwargs['villa_id']

        try:
            villa = Villa.objects.get(id=villa_id)
        except Villa.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Error: No se encontró una Villa con el ID "{villa_id}".'))
            return

        hoy = date.today()
        mes_a_cargar = hoy.month
        ano_a_cargar = hoy.year

        nombres_meses = {1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"}
        nombre_mes = nombres_meses.get(mes_a_cargar, "")
        concepto = f"Mantenimiento {nombre_mes} {ano_a_cargar}"
        monto_cargo = Decimal('750.00')

        casas = Casa.objects.filter(villa=villa)
        casas_cargadas = 0

        self.stdout.write(f"Iniciando creación de cargos para {nombre_mes} {ano_a_cargar} en '{villa.nombre}'...")

        for casa in casas:
            # Revisamos si ya existe una TRANSACCIÓN de cargo para este mes
            cargo_existente = Transaccion.objects.filter(
                casa=casa,
                tipo='CARGO',
                concepto=concepto
            ).exists()

            if not cargo_existente:
                # Usamos una transacción de base de datos para asegurar que todo se guarde correctamente
                with transaction.atomic():
                    # 1. Creamos la Transacción del cargo
                    Transaccion.objects.create(
                        casa=casa,
                        tipo='CARGO',
                        monto=monto_cargo,
                        concepto=concepto,
                        estado_aprobacion='APROBADO' # Los cargos se aprueban automáticamente
                    )

                    # 2. Actualizamos el saldo de la casa
                    casa.saldo += monto_cargo
                    casa.save()

                    casas_cargadas += 1
            else:
                self.stdout.write(self.style.WARNING(f"Cargo para Casa {casa.numero_casa} ya existe. Saltando..."))

        self.stdout.write(self.style.SUCCESS(f"¡Proceso completado! Se crearon y aplicaron nuevos cargos para {casas_cargadas} casas."))