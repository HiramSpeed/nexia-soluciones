# condominio/admin.py

from django.contrib import admin, messages
from django.urls import path, reverse
from django.http import HttpResponseRedirect
from django.utils.html import format_html
from django.db import transaction
from django.template.loader import render_to_string
from django.core.files.base import ContentFile
from django.shortcuts import get_object_or_404, redirect
# from weasyprint import HTML # Lazy loaded in function
from num2words import num2words
from .models import CasaConAdeudo
import datetime
from django.db import models
from .models import (
    Casa, Pago, AreaComun, Reservacion, Visitante, Vehiculo,
    Marca, Modelo, ContadorFolio, Villa, Propuesta, Voto, Paquete, Transaccion, LugarEstacionamiento, ReservaEstacionamiento
)



def aprobar_abonos_seleccionados(modeladmin, request, queryset):
    abonos_a_procesar = queryset.filter(tipo='ABONO', estado_aprobacion='PENDIENTE')
    contador_exito = 0
    for transaccion in abonos_a_procesar:
        with transaction.atomic():
            casa = transaccion.casa
            casa.saldo -= transaccion.monto
            casa.save()

            contador_folio, _ = ContadorFolio.objects.get_or_create(id=1)
            nuevo_folio = contador_folio.ultimo_folio + 1

            # ===============================================================
            # INICIO: CONTEXTO DE RECIBO MEJORADO
            # ===============================================================
            contexto_recibo = {
                'folio': nuevo_folio,
                'fecha': datetime.date.today(),
                'nombre': transaccion.casa.propietario,
                'domicilio_numero': transaccion.casa.numero_casa,
                'concepto': f"Abono registrado por residente - {transaccion.fecha.strftime('%d/%m/%Y')}",
                'cantidad_numero': transaccion.monto, # <--- Pasamos el monto explícitamente
                'cantidad_letra': num2words(transaccion.monto, lang='es').capitalize() + " pesos 00/100 M.N.",
            }
            # ===============================================================
            # FIN: CONTEXTO DE RECIBO MEJORADO
            # ===============================================================

            html_string = render_to_string('condominio/recibo_template.html', contexto_recibo)
            from weasyprint import HTML # Lazy load
            pdf_file = HTML(string=html_string).write_pdf()

            if hasattr(transaccion, 'recibo_pdf'):
                transaccion.recibo_pdf.save(f'recibo_folio_{nuevo_folio}.pdf', ContentFile(pdf_file), save=False)

            contador_folio.ultimo_folio = nuevo_folio
            contador_folio.save()

            transaccion.estado_aprobacion = 'APROBADO'
            transaccion.concepto = f"Abono Aprobado (Folio {nuevo_folio})"
            transaccion.save()
            contador_exito += 1

    modeladmin.message_user(request, f"{contador_exito} abonos han sido aprobados y los saldos actualizados.", messages.SUCCESS)


# --- Clases de Admin ---
class PropuestaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'estado', 'fecha_creacion', 'fecha_fin_votacion')
    list_filter = ('estado', 'villa')
    readonly_fields = ('villa', 'autor', 'titulo', 'descripcion', 'costo_estimado', 'beneficios')

class VehiculoInline(admin.TabularInline):
    model = Vehiculo
    readonly_fields = ('placa', 'marca', 'modelo', 'color')
    fields = ('placa', 'marca', 'modelo', 'color', 'estado', 'tarjeta_rfid')
    extra = 0

# en condominio/admin.py

# ... (tus otras clases de admin como CasaAdmin, TransaccionAdmin, etc.)

class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'casa', 'marca', 'modelo', 'estado', 'tarjeta_rfid')
    list_filter = ('estado', 'marca', 'casa__villa')
    search_fields = ('placa', 'casa__numero_casa', 'tarjeta_rfid')
    list_editable = ('estado', 'tarjeta_rfid') # Permite editar estos campos desde la lista
    actions = ['aprobar_vehiculos']

    def aprobar_vehiculos(self, request, queryset):
        queryset.update(estado='Aprobado')
        self.message_user(request, "Los vehículos seleccionados han sido aprobados.", messages.SUCCESS)
    aprobar_vehiculos.short_description = "Aprobar vehículos seleccionados"

class CasaConAdeudoAdmin(admin.ModelAdmin):
    list_display = ('numero_casa', 'propietario', 'saldo_coloreado')
    search_fields = ('numero_casa', 'propietario')
    ordering = ['-saldo']

    def get_queryset(self, request):
        # Esta es la magia: solo muestra casas con saldo > 0
        return super().get_queryset(request).filter(saldo__gt=0)

    @admin.display(description='Saldo Deudor', ordering='saldo')
    def saldo_coloreado(self, obj):
        return format_html(
            '<span style="color: red; font-weight: bold;">+${}</span>', obj.saldo
        )

class CasaAdmin(admin.ModelAdmin):
    inlines = [VehiculoInline]
    # --- CAMBIOS AQUÍ ---
    list_display = ('numero_casa', 'propietario', 'villa', 'saldo_coloreado', 'estatus_condominio')
    list_filter = ('estatus_condominio', 'villa')
    search_fields = ('numero_casa', 'propietario')
    readonly_fields = ('saldo',)

    # Ordenar por saldo por defecto (los que más deben, primero)
    ordering = ['-saldo']

    @admin.display(description='Saldo Actual', ordering='saldo')
    def saldo_coloreado(self, obj):
        if obj.saldo > 0:
            color = 'red'
            signo = '+'
        elif obj.saldo < 0:
            color = 'green'
            signo = '' # El negativo ya está en el número
        else:
            color = 'black'
            signo = ''

        return format_html(
            '<span style="color: {0}; font-weight: bold;">{1}${2}</span>',
            color, signo, obj.saldo
        )

class PaqueteAdmin(admin.ModelAdmin):
    list_display = ('casa', 'remitente', 'estado', 'fecha_llegada', 'fecha_entrega')
    list_filter = ('estado', 'casa__villa')
    search_fields = ('casa__numero_casa', 'remitente', 'numero_guia')

# --- Clase de Administración para Transaccion (VERSIÓN FINAL) ---
class TransaccionAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'casa', 'tipo', 'monto', 'concepto', 'estado_aprobacion_coloreado', 'vista_previa_comprobante', 'acciones_rapidas')
    list_filter = ('estado_aprobacion', 'tipo', 'casa')
    search_fields = ('concepto', 'casa__numero_casa')
    actions = [aprobar_abonos_seleccionados]
    date_hierarchy = 'fecha'

    def acciones_rapidas(self, obj):
        if obj.tipo == 'ABONO' and obj.estado_aprobacion == 'PENDIENTE':
            url = reverse('admin:transaccion-aprobar', args=[obj.id])
            return format_html('<a class="button" href="{}">Aprobar</a>', url)
        return "—"
    acciones_rapidas.short_description = 'Acción Rápida'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:transaccion_id>/aprobar/', self.admin_site.admin_view(self.aprobar_transaccion_view), name='transaccion-aprobar'),
        ]
        return custom_urls + urls

    def aprobar_transaccion_view(self, request, transaccion_id):
        transaccion = get_object_or_404(Transaccion, id=transaccion_id)
        if transaccion.tipo == 'ABONO' and transaccion.estado_aprobacion == 'PENDIENTE':
            aprobar_abonos_seleccionados(self, request, Transaccion.objects.filter(id=transaccion_id))
        else:
            self.message_user(request, "Esta transacción no se puede aprobar o ya fue procesada.", messages.WARNING)
        referer_url = request.META.get('HTTP_REFERER', reverse('admin:index'))
        return redirect(referer_url) # Redirige a la lista de transacciones

    def estado_aprobacion_coloreado(self, obj):
        if obj.estado_aprobacion == 'PENDIENTE': color = 'orange'
        elif obj.estado_aprobacion == 'APROBADO': color = 'green'
        elif obj.estado_aprobacion == 'RECHAZADO': color = 'red'
        else: color = 'black'
        return format_html('<span style="color: {0}; font-weight: bold;">{1}</span>', color, obj.get_estado_aprobacion_display())
    estado_aprobacion_coloreado.short_description = 'Estado'

    def vista_previa_comprobante(self, obj):
        if obj.comprobante:
            return format_html('<a href="{0}" target="_blank"><img src="{0}" width="75"/></a>', obj.comprobante.url)
        return "N/A"
    vista_previa_comprobante.short_description = 'Comprobante'

# --- Clase de Administración para Pago (MODELO LEGADO) ---
class PagoAdmin(admin.ModelAdmin):
    list_display = ('casa', 'monto', 'concepto', 'estado', 'fecha_vencimiento')
    list_filter = ('estado', 'casa')
    search_fields = ('casa__numero_casa', 'concepto')
# --- ADMINISTRACIÓN DE ESTACIONAMIENTOS ---

class LugarEstacionamientoAdmin(admin.ModelAdmin):
    list_display = ('casa', 'identificador', 'numero_de_casa_display')
    search_fields = ('casa__numero_casa', 'casa__propietario')
    list_filter = ('identificador', 'casa__villa')

    def numero_de_casa_display(self, obj):
        if obj.casa:
            return obj.casa.numero_casa
        return "Público" # O "Área Común"

    numero_de_casa_display.short_description = "Casa Asignada"



    # Colorear el estado para identificar rápido problemas
    def estado_ocupacion(self, obj):
        if obj.esta_ocupado_por_dueno:
            return format_html('<span style="color: red;">⛔ Ocupado por Dueño</span>')
        elif obj.asignado_a:
            return format_html('<span style="color: orange;">🤝 Prestado a Casa {}</span>', obj.asignado_a.numero_casa)
        else:
            return format_html('<span style="color: green;">✅ Disponible (Ofrecido)</span>')
    estado_ocupacion.short_description = 'Estado Actual'


# Registrar los nuevos modelos
admin.site.register(LugarEstacionamiento, LugarEstacionamientoAdmin)
admin.site.register(Villa)
admin.site.register(Casa, CasaAdmin)
admin.site.register(Pago, PagoAdmin)
admin.site.register(AreaComun)
admin.site.register(Reservacion)
admin.site.register(Visitante)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(ContadorFolio)
admin.site.register(Propuesta, PropuestaAdmin)
admin.site.register(Voto)
admin.site.register(Paquete, PaqueteAdmin)
admin.site.register(CasaConAdeudo, CasaConAdeudoAdmin)
admin.site.register(Vehiculo, VehiculoAdmin)
admin.site.register(Transaccion, TransaccionAdmin)
admin.site.register(ReservaEstacionamiento)