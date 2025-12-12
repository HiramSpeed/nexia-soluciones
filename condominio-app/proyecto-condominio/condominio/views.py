# condominio/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Casa, Pago, Vehiculo, AreaComun, Reservacion, Villa, Propuesta, Voto, Paquete, DocumentoPropuesta, Visitante, Modelo, Transaccion, DocumentoPropuesta, ReporteIncidencia, ServicioVecino, Reconocimiento, LugarEstacionamiento, ReservaEstacionamiento, DisponibilidadEstacionamiento
from .forms import (
    VehiculoForm, ReservacionForm, VisitanteForm, VisitanteDocumentoForm,
    PropuestaForm, PaqueteResidenteForm, PaqueteGuardiaForm, AbonoForm, CustomLoginForm, ReporteForm, ServicioVecinoForm, ReservaEstacionamientoForm, PrestamoEstacionamientoForm)
from django.http import JsonResponse, HttpResponse
from django.db import IntegrityError
from django.contrib import messages
from django.urls import reverse
import secrets
from django.utils import timezone
from datetime import timedelta
from urllib.parse import quote
from django.db.models import Count, Sum, Q
from django.contrib.auth.models import Group
from django.views.decorators.http import require_POST
from django.db import transaction
from django.contrib.auth.views import LoginView
from decimal import Decimal
import io
from django.core.files.base import ContentFile
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from django.core.exceptions import ObjectDoesNotExist
from datetime import timedelta

def obtener_casa_usuario(user):
    """
    Detecta si el usuario es dueño O inquilino y devuelve la casa correcta.
    Evita errores si el usuario no tiene casa.
    """
    if hasattr(user, 'casa_propiedad'): # Es el dueño (compatibilidad anterior)
        return user.casa_propiedad
    elif hasattr(user, 'casa_rentada'): # Es el inquilino (nuevo)
        return user.casa_rentada
    elif hasattr(user, 'casa'): # Por si acaso Django mantiene el nombre viejo
        return user.casa
    else:
        return None

def lista_casas(request):
    todas_las_casas = Casa.objects.all()
    contexto = {
        'casas': todas_las_casas,
    }
    return render(request, 'condominio/lista_casas.html', contexto)

@login_required
def agregar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            try:
                vehiculo = form.save(commit=False)
                vehiculo.casa = request.user.casa
                vehiculo.save()
                messages.success(request, '¡Vehículo agregado con éxito! Será aprobado por la administración pronto.')
                # --- THIS IS THE CORRECTED LINE ---
                return redirect('condominio:dashboard')
            except IntegrityError:
                messages.error(request, 'Error: Ya existe un vehículo con esa placa.')
    else:
        form = VehiculoForm()

    contexto = {
        'form': form,
    }
    return render(request, 'condominio/agregar_vehiculo.html', contexto)

@login_required
def directorio_comunidad(request):
    # Obtenemos servicios activos
    servicios = ServicioVecino.objects.filter(activo=True).select_related('casa')

    # Obtenemos los vecinos "Más activos" (Top Stars)
    top_vecinos = Casa.objects.annotate(
        estrellas=Count('reconocimientos_recibidos')
    ).order_by('-estrellas')[:5]

    try:
        mi_servicio = request.user.casa.mi_servicio
    except ServicioVecino.DoesNotExist:
        mi_servicio = None

    context = {
        'servicios': servicios,
        'top_vecinos': top_vecinos,
        'mi_servicio': mi_servicio,
    }
    return render(request, 'condominio/comunidad.html', context)

@login_required
def publicar_servicio(request):
    try:
        servicio = request.user.casa.mi_servicio
    except ServicioVecino.DoesNotExist:
        servicio = None

    if request.method == 'POST':
        form = ServicioVecinoForm(request.POST, request.FILES, instance=servicio)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.casa = request.user.casa
            obj.save()
            messages.success(request, '¡Tu servicio ha sido publicado en la comunidad!')
            return redirect('condominio:directorio_comunidad')
    else:
        form = ServicioVecinoForm(instance=servicio)

    return render(request, 'condominio/publicar_servicio.html', {'form': form})

@login_required
def dar_reconocimiento(request, casa_id):
    destino = get_object_or_404(Casa, id=casa_id)
    origen = request.user.casa

    if destino == origen:
        messages.error(request, "No puedes darte estrellas a ti mismo.")
        return redirect('condominio:directorio_comunidad')

    # Toggle: Si ya le dio, se la quita; si no, se la pone
    reconocimiento = Reconocimiento.objects.filter(otorgado_por=origen, recibido_por=destino).first()

    if reconocimiento:
        reconocimiento.delete()
        messages.info(request, f"Has retirado tu reconocimiento a la Casa {destino.numero_casa}.")
    else:
        Reconocimiento.objects.create(otorgado_por=origen, recibido_por=destino, tipo='Conocido')
        messages.success(request, f"¡Has dado una estrella a la Casa {destino.numero_casa}!")

    return redirect('condominio:directorio_comunidad')

@login_required
def eliminar_vehiculo(request, vehiculo_id):
    # Busca el vehículo asegurándose de que pertenece a la casa del usuario
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id, casa=request.user.casa)

    # Solo permite eliminar si no está aprobado
    if vehiculo.estado != 'Aprobado':
        vehiculo.delete()
        messages.success(request, 'El vehículo ha sido eliminado con éxito.')
    else:
        messages.error(request, 'No puedes eliminar un vehículo que ya ha sido aprobado.')

    # --- THIS IS THE CORRECTED LINE ---
    return redirect('condominio:dashboard')

@login_required
def visita_generada(request, visitante_id):
    visitante = get_object_or_404(Visitante, id=visitante_id, casa=request.user.casa)

    # --- ¡AQUÍ ESTÁ LA CORRECCIÓN! ---
    # Construimos la URL completa usando reverse() y el prefijo correcto.
    ruta_relativa = reverse('condominio:vista_visitante', args=[visitante.token_acceso])
    url_acceso_completa = request.build_absolute_uri(ruta_relativa)

    # Creamos el enlace para compartir en WhatsApp
    mensaje_whatsapp = f"¡Hola! Tienes una visita programada. Por favor, completa tu registro aquí: {url_acceso_completa}"
    whatsapp_url = f"https://wa.me/?text={quote(mensaje_whatsapp)}"

    contexto = {
        'visitante': visitante,
        'url_acceso': url_acceso_completa,
        'whatsapp_url': whatsapp_url,
    }
    return render(request, 'condominio/visita_generada.html', contexto)



@login_required
def dashboard(request):
    # --- LÓGICA PARA EL ADMINISTRADOR (SUPERUSER) ---
    if request.user.is_superuser:
        transacciones_pendientes = Transaccion.objects.filter(estado_aprobacion='PENDIENTE').order_by('-fecha')
        vehiculos_pendientes = Vehiculo.objects.filter(estado='Pendiente')
        reportes_pendientes = ReporteIncidencia.objects.filter(estado='PENDIENTE').order_by('fecha_creacion')

        contexto = {
            'transacciones_pendientes': transacciones_pendientes,
            'vehiculos_pendientes': vehiculos_pendientes,
            'cantidad_transacciones_pendientes': transacciones_pendientes.count(),
            'cantidad_vehiculos_pendientes': vehiculos_pendientes.count(),
            'reportes_pendientes': reportes_pendientes,
        }
        return render(request, 'condominio/dashboard_admin.html', contexto)

    # --- LÓGICA PARA GUARDIAS (CORREGIDA) ---
    if request.user.groups.filter(name='Guardias').exists():
        # ¡AQUÍ ESTÁ LA CORRECCIÓN!
        return redirect('condominio:dashboard_vigilante')

    # --- LÓGICA PARA RESIDENTES ---
    try:
        casa_del_usuario = request.user.casa
    except Casa.DoesNotExist:
        return render(request, 'condominio/sin_casa_asignada.html')

    total_pendiente = casa_del_usuario.saldo if casa_del_usuario.saldo > 0 else 0
    total_adeudo_vencido = total_pendiente

    transacciones = casa_del_usuario.transacciones.all().order_by('-fecha')

    abono_form = AbonoForm()
    vehiculos_de_la_casa = casa_del_usuario.vehiculos.all()
    visitantes_de_la_casa = Visitante.objects.filter(casa=casa_del_usuario).order_by('-fecha_programada')
    paquetes_del_residente = Paquete.objects.filter(casa=casa_del_usuario).order_by('-fecha_llegada')
    propuestas_activas = Propuesta.objects.filter(villa=casa_del_usuario.villa, estado='Activa')
    mis_reportes = ReporteIncidencia.objects.filter(reportante=casa_del_usuario).order_by('-fecha_creacion')

    contexto = {
        'casa': casa_del_usuario,
        'transacciones': transacciones,
        'abono_form': abono_form,
        'vehiculos': vehiculos_de_la_casa,
        'visitantes': visitantes_de_la_casa,
        'paquetes': paquetes_del_residente,
        'propuestas_activas': propuestas_activas,
        'mis_reportes': mis_reportes,
        'total_pendiente': total_pendiente,
        'total_adeudo_vencido': total_adeudo_vencido,
    }

    return render(request, 'condominio/dashboard_residente_nuevo.html', contexto)

@login_required
@require_POST
def guardia_subir_foto_visitante(request, visitante_id):
    if not request.user.groups.filter(name='Guardias').exists():
        return JsonResponse({'status': 'error', 'message': 'Permiso denegado.'}, status=403)

    try:
        visitante = get_object_or_404(Visitante, id=visitante_id)
        photo_file = request.FILES.get('photo')
        photo_type = request.POST.get('photo_type')

        if not photo_file or not photo_type:
            return JsonResponse({'status': 'error', 'message': 'Faltan datos.'}, status=400)

        if photo_type == 'ine':
            visitante.foto_identificacion = photo_file
        elif photo_type == 'placas':
            visitante.foto_placas = photo_file
        else:
            return JsonResponse({'status': 'error', 'message': 'Tipo de foto no válido.'}, status=400)

        visitante.save()
        return JsonResponse({'status': 'success', 'message': 'Foto guardada correctamente.'})

    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)



@login_required
def registrar_abono(request):
    if request.method != 'POST':
        return redirect('condominio:dashboard')

    form = AbonoForm(request.POST, request.FILES)
    if form.is_valid():
        monto = form.cleaned_data['monto']
        casa = request.user.casa

        # --- 🛡️ LÓGICA ANTI-DUPLICADOS ---
        # 1. Definimos "reciente" como los últimos 10 minutos
        tiempo_limite = timezone.now() - timedelta(minutes=10)

        # 2. Buscamos si ya existe un abono igual
        duplicado = Transaccion.objects.filter(
            casa=casa,
            tipo='ABONO',
            monto=monto,
            fecha__gte=tiempo_limite # Creado después de hace 10 min
        ).exists()

        if duplicado:
            # 3. Si existe, NO guardamos y mandamos la señal 'error_duplicado'
            messages.error(request, 'Pago duplicado detectado', extra_tags='mostrar_modal_duplicado')
            return redirect('condominio:dashboard')
        # ----------------------------------

        Transaccion.objects.create(
            casa=casa,
            tipo='ABONO',
            monto=monto,
            comprobante=form.cleaned_data['comprobante'],
            concepto=f"Abono de ${monto}",
            estado_aprobacion='PENDIENTE'
        )

        messages.success(request, 'abono_exitoso', extra_tags='mostrar_modal_abono')

    else:
        messages.error(request, "Hubo un error con tu formulario.")

    return redirect('condominio:dashboard')

@login_required
def aprobar_transaccion(request, transaccion_id):
    if not request.user.is_superuser:
        messages.error(request, "Acceso denegado.")
        return redirect('condominio:dashboard')

    transaccion_obj = get_object_or_404(Transaccion, id=transaccion_id, estado_aprobacion='PENDIENTE')

    # Usamos transaction.atomic para asegurar que todo se complete con éxito
    with transaction.atomic():
        casa = Casa.objects.select_for_update().get(id=transaccion_obj.casa.id)

        if transaccion_obj.tipo == 'ABONO':
            casa.saldo -= transaccion_obj.monto
        elif transaccion_obj.tipo == 'CARGO':
            casa.saldo += transaccion_obj.monto

        casa.save()

        transaccion_obj.estado_aprobacion = 'APROBADO'
        transaccion_obj.save()

        # --- ¡AQUÍ ESTÁ LA MAGIA! ---
        # Si la transacción es un Abono APROBADO, generamos su recibo.
        if transaccion_obj.tipo == 'ABONO':
            generar_y_guardar_recibo_transaccion(transaccion_obj)

    messages.success(request, f"La transacción para la casa {casa.numero_casa} ha sido aprobada.")
    return redirect('condominio:dashboard')


# en condominio/views.py

# condominio/views.py

@login_required
def vista_reservaciones(request):
    # Primero, verificamos si el usuario tiene una casa asignada
    if not hasattr(request.user, 'casa'):
        messages.error(request, "No tienes una casa asignada. Contacta al administrador.")
        return redirect('condominio:dashboard')

    # Verificamos si el residente tiene adeudos
    if request.user.casa.saldo > 0:
        messages.error(request, 'No puedes realizar reservaciones mientras tengas un adeudo pendiente.')
        # Pasamos un contexto para que la página no se rompa
        return render(request, 'condominio/reservaciones.html', {'form': None})

    # Si se envía el formulario (POST)
    if request.method == 'POST':
        # Instanciamos el formulario con los datos y la casa del usuario
        form = ReservacionForm(request.POST, casa=request.user.casa)
        if form.is_valid():
            reservacion = form.save(commit=False)
            reservacion.casa = request.user.casa

            # --- CAMBIO PRINCIPAL: SE APRUEBA AUTOMÁTICAMENTE ---
            reservacion.estado = 'Aprobada'

            reservacion.save()

            # --- MENSAJE DE ÉXITO ACTUALIZADO ---
            messages.success(request, '¡Tu reservación ha sido confirmada exitosamente!')

            return redirect('condominio:vista_reservaciones')
        else:
            # Si hay errores, los mostramos
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error en {field}: {error}")

    # Si se carga la página por primera vez (GET)
    else:
        form = ReservacionForm(casa=request.user.casa)

    # Obtenemos las reservaciones existentes del usuario
    mis_reservaciones = Reservacion.objects.filter(casa=request.user.casa).order_by('-fecha_hora_inicio')

    # Creamos la lista de horas disponibles (de 9 AM a 8 PM)
    horas_disponibles = [f"{h:02d}:00" for h in range(7, 21)]

    # Preparamos todos los datos para enviar a la plantilla
    contexto = {
        'form': form,
        'mis_reservaciones': mis_reservaciones,
        'horas_disponibles': horas_disponibles,
    }

    # Renderizamos la plantilla correcta con todos los datos
    return render(request, 'condominio/reservaciones.html', contexto)

def reservaciones_feed(request):
    # Usamos select_related para optimizar la consulta a la base de datos
    reservaciones = Reservacion.objects.filter(estado='Aprobada').select_related('area_comun', 'casa')

    eventos = []
    for reservacion in reservaciones:
        eventos.append({
            # TÍTULO CORTO Y CLARO
            'title': f"{reservacion.area_comun.nombre}: {reservacion.casa.numero_casa}",

            # GUARDAMOS EL TÍTULO COMPLETO PARA EL TOOLTIP
            'extendedProps': {
                'fullTitle': f"{reservacion.area_comun.nombre} - Casa {reservacion.casa.propietario} ({reservacion.casa.numero_casa})"
            },

            'start': reservacion.fecha_hora_inicio.isoformat(),
            'end': reservacion.fecha_hora_fin.isoformat(),
            'color': '#28a745' # Verde para eventos aprobados
        })
    return JsonResponse(eventos, safe=False)

@login_required
def descargar_recibo(request, pago_id):
    pago = get_object_or_404(Pago, id=pago_id)
    if pago.casa.usuario != request.user and not request.user.is_superuser:
        return redirect('condominio:dashboard')
    if not pago.recibo_pdf:
        messages.error(request, "No se encontró un recibo para este pago.")
        return redirect('condominio:dashboard')
    try:
        pago.recibo_pdf.open(mode='rb')
        pdf_content = pago.recibo_pdf.read()
    finally:
        pago.recibo_pdf.close()
    response = HttpResponse(pdf_content, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="recibo_folio_{pago.folio}.pdf"'
    return response

@login_required
def descargar_recibo_transaccion(request, transaccion_id):
    transaccion = get_object_or_404(Transaccion, id=transaccion_id, casa=request.user.casa)
    if not transaccion.recibo_pdf:
        messages.error(request, "No se encontró un recibo para esta transacción.")
        return redirect('condominio:dashboard')

    # Devuelve el archivo PDF
    response = HttpResponse(transaccion.recibo_pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="recibo_folio_{transaccion.id}.pdf"'
    return response

@login_required
def registrar_visita(request):
    # --- VERIFICACIÓN DE SEGURIDAD AÑADIDA ---
    # Revisa si el usuario tiene una casa asignada ANTES de hacer cualquier otra cosa.
    if not hasattr(request.user, 'casa'):
        messages.error(request, "Error: Tu cuenta no está asignada a ninguna casa. No puedes registrar visitas.")
        return redirect('condominio:dashboard') # Redirige al panel principal si no hay casa

    # --- El resto de tu código original se mantiene intacto ---
    if request.method == 'POST':
        form = VisitanteForm(request.POST)
        if form.is_valid():
            visitante = form.save(commit=False)
            datetime_from_form = form.cleaned_data['fecha_programada']
            if timezone.is_aware(datetime_from_form):
                visitante.fecha_programada = timezone.make_naive(datetime_from_form)
            else:
                visitante.fecha_programada = datetime_from_form

            # Esta línea ahora es segura gracias a la verificación de arriba
            visitante.casa = request.user.casa
            visitante.token_acceso = secrets.token_hex(16)
            visitante.save()

            if form.cleaned_data.get('requiere_estacionamiento'):
                try:
                    area_estacionamiento = AreaComun.objects.get(nombre__icontains='Estacionamiento de Visitas', villa=visitante.casa.villa)
                    inicio = visitante.fecha_programada
                    fin = inicio + timedelta(hours=4)
                    reservaciones_empalmadas = Reservacion.objects.filter(
                        area_comun=area_estacionamiento,
                        estado='Aprobada',
                        fecha_hora_inicio__lt=fin,
                        fecha_hora_fin__gt=inicio
                    ).count()
                    if reservaciones_empalmadas < area_estacionamiento.cantidad_espacios:
                        Reservacion.objects.create(
                            area_comun=area_estacionamiento,
                            casa=visitante.casa,
                            fecha_hora_inicio=inicio,
                            fecha_hora_fin=fin,
                            estado='Aprobada',
                            cantidad_personas=1
                        )
                        messages.success(request, f'Visita para "{visitante.nombre_visitante}" registrada con éxito Y se le ha asignado un lugar de estacionamiento.')
                    else:
                        messages.warning(request, f'Visita para "{visitante.nombre_visitante}" registrada, pero NO se pudo asignar un estacionamiento por falta de disponibilidad.')
                except AreaComun.DoesNotExist:
                    messages.error(request, 'Error: El área de estacionamiento no está configurada. Contacta al administrador.')
            else:
                messages.success(request, f'Visita para "{visitante.nombre_visitante}" registrada correctamente (sin estacionamiento).')

            return redirect('condominio:visita_generada', visitante_id=visitante.id)
    else:
        form = VisitanteForm()

    return render(request, 'condominio/registrar_visita.html', {'form': form})


def vista_visitante(request, token_acceso):
    visitante = get_object_or_404(Visitante, token_acceso=token_acceso)
    villa_actual = visitante.casa.villa
    if visitante.foto_identificacion:
        return render(request, 'condominio/visitante_gracias.html', {'villa_actual': villa_actual})
    if request.method == 'POST':
        form = VisitanteDocumentoForm(request.POST, request.FILES, instance=visitante)
        if form.is_valid():
            form.save()
            return render(request, 'condominio/visitante_gracias.html', {'villa_actual': villa_actual})
    else:
        form = VisitanteDocumentoForm(instance=visitante)
    contexto = {
        'form': form,
        'visitante': visitante,
        'villa_actual': villa_actual,
    }
    return render(request, 'condominio/vista_visitante.html', contexto)

def load_modelos(request):
    marca_id = request.GET.get('marca_id')
    modelos = Modelo.objects.filter(marca_id=marca_id).order_by('nombre')
    return JsonResponse(list(modelos.values('id', 'nombre')), safe=False)

@login_required
def marcar_entrada_visitante(request, visitante_id):
    if not request.user.groups.filter(name='Guardias').exists():
        return redirect('condominio:dashboard')
    visitante = get_object_or_404(Visitante, id=visitante_id)
    visitante.estado = 'Adentro'
    visitante.fecha_hora_entrada = timezone.now()
    visitante.save()
    return redirect('condominio:dashboard_vigilante')

@login_required
def marcar_salida_visitante(request, visitante_id):
    if not request.user.groups.filter(name='Guardias').exists():
        return redirect('condominio:dashboard')
    visitante = get_object_or_404(Visitante, id=visitante_id)
    visitante.estado = 'Completada'
    visitante.save()
    return redirect('condominio:dashboard_vigilante')

@login_required
def dashboard_vigilante(request):
    # Verifica que el usuario pertenezca al grupo de 'Guardias'
    if not request.user.groups.filter(name='Guardias').exists():
        return redirect('condominio:dashboard')

    # Obtiene la villa actual (puedes ajustar esto si tienes múltiples villas)
    villa_actual = Villa.objects.first()

    # Si no hay ninguna villa configurada, muestra el dashboard vacío
    if not villa_actual:
        return render(request, 'condominio/dashboard_vigilante.html', {
            'visitas': [],
            'reservaciones': [],
            'paquetes': [],
            'fecha_hoy': timezone.localtime(timezone.now())
        })

    # Obtenemos la hora actual y la convertimos a la zona horaria local de settings.py
    ahora_local = timezone.localtime(timezone.now())

    # Calculamos el inicio y fin del día BASADO en la hora local
    inicio_del_dia = ahora_local.replace(hour=0, minute=0, second=0, microsecond=0)
    fin_del_dia = inicio_del_dia + timedelta(days=1)

    # Filtra las visitas programadas para el día de hoy en la zona horaria local
    visitas_del_dia = Visitante.objects.filter(
        casa__villa=villa_actual,
        fecha_programada__gte=inicio_del_dia,
        fecha_programada__lt=fin_del_dia
    ).exclude(estado='Completada').select_related('casa', 'guardia_entrada').order_by('fecha_programada')

    # Filtra las reservaciones para el día de hoy
    reservaciones_del_dia = Reservacion.objects.filter(
        casa__villa=villa_actual,
        fecha_hora_inicio__gte=inicio_del_dia,
        fecha_hora_inicio__lt=fin_del_dia,
        estado__in=['Aprobada', 'En Uso']
    ).select_related('casa', 'area_comun').order_by('fecha_hora_inicio')

    # Obtiene los paquetes que no han sido entregados
    paquetes_pendientes = Paquete.objects.filter(
        casa__villa=villa_actual,
        estado__in=['En Vigilancia', 'Esperando Llegada']
    ).select_related('casa').order_by('fecha_llegada')

    # Prepara el contexto para la plantilla
    contexto = {
        'visitas': visitas_del_dia,
        'reservaciones': reservaciones_del_dia,
        'paquetes': paquetes_pendientes,
        'fecha_hoy': inicio_del_dia,
    }

    return render(request, 'condominio/dashboard_vigilante.html', contexto)

@login_required
def iniciar_uso_reservacion(request, reservacion_id):
    if not request.user.groups.filter(name='Guardias').exists():
        return redirect('condominio:dashboard')
    reservacion = get_object_or_404(Reservacion, id=reservacion_id)
    reservacion.estado = 'En Uso'
    reservacion.guardia_entrega = request.user
    reservacion.fecha_hora_entrega = timezone.now()
    reservacion.save()
    return redirect('condominio:dashboard_vigilante')

@login_required
def finalizar_uso_reservacion(request, reservacion_id):
    if not request.user.groups.filter(name='Guardias').exists():
        return redirect('condominio:dashboard')
    reservacion = get_object_or_404(Reservacion, id=reservacion_id)
    reservacion.estado = 'Completada'
    reservacion.guardia_devolucion = request.user
    reservacion.fecha_hora_devolucion = timezone.now()
    reservacion.save()
    return redirect('condominio:dashboard_vigilante')

@login_required

def propuestas_lista(request):
    # 1. Intentamos obtener la casa de forma segura
    try:
        casa = request.user.casa
    except ObjectDoesNotExist:
        # Si el usuario es admin pero no tiene casa, definimos casa como None
        # o lo redirigimos a crear su perfil.
        casa = None

        # Opcional: Si es superusuario, quizás quieras dejarlo pasar sin casa
        if not request.user.is_superuser:
            # Si es un usuario normal sin casa, mostrar error o redirigir
            return render(request, 'condominio/error_sin_casa.html')

    # 2. Tu lógica normal (asegúrate de que funcione si casa es None)
    propuestas = Propuesta.objects.all().order_by('-fecha_creacion')

    context = {
        'propuestas': propuestas,
        'casa': casa, # Pasamos la variable, aunque sea None
    }
    return render(request, 'condominio/propuestas_lista.html', context)


@login_required
def propuesta_crear(request):
    if request.method == 'POST':
        form = PropuestaForm(request.POST)

        # Obtenemos los archivos
        archivos = request.FILES.getlist('documentos_adjuntos')

        if form.is_valid():
            nueva_propuesta = form.save(commit=False)

            # 1. Obtenemos la casa del usuario
            try:
                casa_usuario = request.user.casa
            except:
                # Manejo de error si es admin sin casa
                return render(request, 'condominio/error_sin_casa.html')

            # 2. Asignamos el Autor (Casa)
            nueva_propuesta.autor = casa_usuario

            # 3. Asignamos la VILLA (--- ESTO ES LO QUE FALTABA ---)
            # Asumimos que tu modelo Casa tiene una relación 'villa'
            nueva_propuesta.villa = casa_usuario.villa

            # 4. Ahora sí guardamos
            nueva_propuesta.save()

            # 5. Guardamos los archivos adjuntos
            for f in archivos:
                DocumentoPropuesta.objects.create(
                    propuesta=nueva_propuesta,
                    documento=f,

                )

            return redirect('condominio:propuestas_lista')
    else:
        form = PropuestaForm()

    return render(request, 'condominio/propuesta_crear.html', {'form': form})

@login_required
def propuesta_detalle(request, propuesta_id):
    propuesta = get_object_or_404(Propuesta, id=propuesta_id, villa=request.user.casa.villa)
    voto_usuario = Voto.objects.filter(propuesta=propuesta, casa=request.user.casa).first()
    if request.method == 'POST' and not voto_usuario and propuesta.estado == 'Activa':
        decision = request.POST.get('decision')
        if decision in ['A Favor', 'En Contra', 'Abstencion']:
            Voto.objects.create(
                propuesta=propuesta,
                casa=request.user.casa,
                decision=decision
            )
            messages.success(request, '¡Gracias! Tu voto ha sido registrado.')
            return redirect('condominio:propuesta_detalle', propuesta_id=propuesta.id)
    resultados = {
        'a_favor': Voto.objects.filter(propuesta=propuesta, decision='A Favor').count(),
        'en_contra': Voto.objects.filter(propuesta=propuesta, decision='En Contra').count(),
        'abstencion': Voto.objects.filter(propuesta=propuesta, decision='Abstencion').count(),
    }
    puede_votar = (propuesta.estado == 'Activa' and not voto_usuario)
    contexto = {
        'propuesta': propuesta,
        'voto_usuario': voto_usuario,
        'puede_votar': puede_votar,
        'resultados': resultados,
    }
    return render(request, 'condominio/propuesta_detalle.html', contexto)

@login_required
def registrar_paquete(request):
    if not request.user.groups.filter(name='Guardias').exists():
        return redirect('condominio:dashboard')
    if request.method == 'POST':
        form = PaqueteGuardiaForm(request.POST)
        if form.is_valid():
            paquete = form.save(commit=False)
            paquete.registrado_por = request.user
            paquete.estado = 'En Vigilancia'
            paquete.save()
            messages.success(request, f"Paquete para la casa {paquete.casa.numero_casa} registrado con éxito.")
            return redirect('condominio:dashboard_vigilante')
    else:
        form = PaqueteGuardiaForm()
    return render(request, 'condominio/registrar_paquete.html', {'form': form})

@login_required
def entregar_paquete(request, paquete_id):
    if not request.user.groups.filter(name='Guardias').exists():
        return redirect('condominio:dashboard')
    paquete = get_object_or_404(Paquete, id=paquete_id)
    paquete.estado = 'Entregado'
    paquete.entregado_a_residente_por = request.user
    paquete.fecha_entrega = timezone.now()
    paquete.save()
    messages.success(request, f"Paquete de {paquete.remitente} para la casa {paquete.casa.numero_casa} ha sido marcado como entregado.")
    return redirect('condominio:dashboard_vigilante')

@login_required
# en condominio/views.py

@login_required
def residente_registrar_paquete(request):
    if request.method == 'POST':
        form = PaqueteResidenteForm(request.POST)
        if form.is_valid():
            paquete = form.save(commit=False)
            paquete.casa = request.user.casa
            paquete.estado = 'Esperando Llegada'
            paquete.save()
            messages.success(request, 'Has pre-registrado tu paquete con éxito. El guardia será notificado.')

            # --- ¡AQUÍ ESTÁ LA LÍNEA CORREGIDA! ---
            return redirect('condominio:dashboard')
    else:
        form = PaqueteResidenteForm()

    return render(request, 'condominio/residente_registrar_paquete.html', {'form': form})

@login_required
def confirmar_llegada_paquete(request, paquete_id):
    if not request.user.groups.filter(name='Guardias').exists():
        return redirect('condominio:dashboard')
    paquete = get_object_or_404(Paquete, id=paquete_id)
    paquete.estado = 'En Vigilancia'
    paquete.registrado_por = request.user
    paquete.fecha_llegada = timezone.now()
    paquete.save()
    messages.success(request, f"Se ha confirmado la llegada del paquete de {paquete.remitente}.")
    return redirect('condominio:dashboard_vigilante')

@login_required
def autorizar_vehiculo(request, vehiculo_id):
    if not request.user.is_superuser:
        messages.error(request, "No tienes permiso para realizar esta acción.")
        return redirect('condominio:dashboard')
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    vehiculo.estado = 'Aprobado'
    vehiculo.save()
    messages.success(request, f"Vehículo con placa {vehiculo.placa} ha sido aprobado.")
    return redirect('condominio:vehiculos_pendientes')

@login_required
def vehiculos_pendientes(request):
    if not request.user.is_superuser:
        messages.error(request, "No tienes permiso para ver esta página.")
        return redirect('condominio:dashboard')
    vehiculos_por_aprobar = Vehiculo.objects.filter(estado='Pendiente').order_by('-id')
    return render(request, 'condominio/vehiculos_pendientes.html', {'vehiculos': vehiculos_por_aprobar})

# condominio/views.py

@login_required
def dashboard_entrega_gafetes(request):
    # --- CAMBIO AQUÍ ---
    # Volvemos a la consulta original para obtener TODAS las casas,
    # incluyendo las que ya fueron entregadas.
    casas = Casa.objects.annotate(
        vehiculos_aprobados_count=Count('vehiculos', filter=Q(vehiculos__estado='Aprobado'))
    ).order_by('numero_casa')

    # Volvemos a calcular los tres contadores.
    pendientes_count = Casa.objects.filter(estado_gafete='Pendiente').count()
    entregados_count = Casa.objects.filter(estado_gafete='Entregado').count()
    en_revision_count = Casa.objects.filter(estado_gafete='En Revision').count()

    contexto = {
        'casas': casas,
        'pendientes_count': pendientes_count,
        'entregados_count': entregados_count, # <-- Añadimos de nuevo este contador
        'en_revision_count': en_revision_count,
    }
    return render(request, 'condominio/dashboard_gafetes.html', contexto)


# --- NUEVA VISTA PARA RESETEAR GAFETES ---
@login_required
@user_passes_test(lambda u: u.is_superuser) # Solo el Admin puede hacer esto
@require_POST # Solo permite esta acción vía POST para más seguridad
def resetear_estado_gafetes(request):
    """
    Resetea el estado de gafete de TODAS las casas a 'Pendiente'.
    """
    try:
        # Esta es la línea clave: actualiza todos los objetos Casa
        casas_actualizadas = Casa.objects.all().update(estado_gafete='Pendiente')
        messages.success(request, f"¡Éxito! Se han reseteado los gafetes de {casas_actualizadas} casas al estado 'Pendiente'.")
    except Exception as e:
        messages.error(request, f"Hubo un error al resetear los gafetes: {e}")

    # Redirige de vuelta al dashboard de gafetes
    return redirect('condominio:dashboard_gafetes')
# --- FIN DE LA NUEVA VISTA ---


@login_required
@user_passes_test(lambda u: u.is_superuser) # Solo para administradores
def lista_casas_con_adeudo(request):
    # La misma lógica que usamos en el admin, pero para nuestra propia vista
    casas_con_adeudo = Casa.objects.filter(saldo__gt=0).order_by('-saldo')

    contexto = {
        'casas_con_adeudo': casas_con_adeudo
    }
    return render(request, 'condominio/casas_con_adeudo.html', contexto)

@login_required
def actualizar_estado_gafete(request, casa_id):
    if not request.user.groups.filter(name='Guardias').exists():
        return JsonResponse({'status': 'error', 'message': 'No autorizado'}, status=403)
    if request.method == 'POST':
        try:
            casa = Casa.objects.get(id=casa_id)
            nuevo_estado = request.POST.get('estado')
            if nuevo_estado in ['Entregado', 'En Revision']:
                casa.estado_gafete = nuevo_estado
                casa.save()
                return JsonResponse({'status': 'success', 'message': 'Estado actualizado correctamente.'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Estado no válido.'}, status=400)
        except Casa.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'La casa no existe.'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'}, status=405)

@login_required
@require_POST
def aprobar_reservacion(request, reservacion_id):
    if not request.user.is_superuser:
        messages.error(request, "Acceso denegado.")
        return redirect('condominio:dashboard')
    reservacion = get_object_or_404(Reservacion, id=reservacion_id)
    reservacion.estado = 'Aprobada'
    reservacion.save()
    messages.success(request, f"La reservación de {reservacion.area_comun.nombre} para la casa {reservacion.casa.numero_casa} ha sido aprobada.")
    return redirect('condominio:dashboard')

@login_required
@require_POST
def rechazar_reservacion(request, reservacion_id):
    if not request.user.is_superuser:
        messages.error(request, "Acceso denegado.")
        return redirect('condominio:dashboard')
    reservacion = get_object_or_404(Reservacion, id=reservacion_id)
    reservacion.estado = 'Rechazada'
    reservacion.save()
    messages.warning(request, f"La reservación de {reservacion.area_comun.nombre} para la casa {reservacion.casa.numero_casa} ha sido rechazada.")
    return redirect('condominio:dashboard')

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'registration/login.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['villa'] = Villa.objects.first()
        return context

def generar_y_guardar_recibo_transaccion(transaccion):
    """
    Genera un PDF para una transacción y lo guarda en su campo recibo_pdf.
    """
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter # Obtenemos el tamaño de la hoja

    # --- Aquí dibujas tu recibo ---
    # (Este es un ejemplo muy básico, puedes personalizarlo como quieras)
    p.drawString(inch, height - inch, f"Recibo de Transacción")
    p.drawString(inch, height - (1.5 * inch), f"Folio de Transacción: {transaccion.id}")
    p.drawString(inch, height - (1.7 * inch), f"Fecha: {transaccion.fecha.strftime('%d/%m/%Y %H:%M')}")
    p.drawString(inch, height - (2.2 * inch), f"Casa: {transaccion.casa.numero_casa}")
    p.drawString(inch, height - (2.4 * inch), f"Propietario: {transaccion.casa.propietario}")
    p.drawString(inch, height - (2.9 * inch), f"Concepto: {transaccion.concepto}")
    p.drawString(inch, height - (3.1 * inch), f"Monto: ${transaccion.monto}")
    p.drawString(inch, height - (3.3 * inch), f"Tipo: {transaccion.get_tipo_display()}")

    p.showPage()
    p.save()

    # Mover el "cursor" del buffer al inicio
    buffer.seek(0)

    # Crear un nombre de archivo único
    nombre_archivo = f'recibo_transaccion_{transaccion.id}.pdf'

    # Guardar el contenido del buffer en el campo FileField del modelo
    transaccion.recibo_pdf.save(nombre_archivo, ContentFile(buffer.read()), save=True)

@login_required
def crear_reporte(request):
    try:
        mi_casa = request.user.casa
    except Casa.DoesNotExist:
        return redirect('condominio:home')

    if request.method == 'POST':
        form = ReporteForm(request.POST, request.FILES)
        if form.is_valid():
            reporte = form.save(commit=False)
            reporte.reportante = mi_casa  # Asignamos quién reporta automáticamente
            reporte.save()
            messages.success(request, 'Reporte enviado confidencialmente. La administración lo revisará.')
            return redirect('condominio:dashboard')
    else:
        form = ReporteForm()

    return render(request, 'condominio/crear_reporte.html', {'form': form})

@login_required
def resolver_reporte(request, reporte_id):
    if not request.user.is_superuser:
        return redirect('condominio:dashboard')

    reporte = get_object_or_404(ReporteIncidencia, id=reporte_id)

    # Calculamos datos para mostrar en la plantilla
    reincidencias = reporte.calcular_reincidencia()
    monto_sugerido = reporte.sugerir_monto()

    if request.method == 'POST':
        accion = request.POST.get('accion')
        comentario = request.POST.get('resolucion_admin')

        if accion == 'multar':
            # Aplicamos la multa usando el método del modelo
            reporte.aplicar_multa(request.user, comentario)
            messages.success(request, f"Multa de ${reporte.monto_multa} aplicada a Casa {reporte.casa_infractora.numero_casa}.")

        elif accion == 'rechazar':
            reporte.estado = 'RECHAZADO'
            reporte.resolucion_admin = comentario
            reporte.save()
            messages.warning(request, "Reporte rechazado y archivado.")

        elif accion == 'amonestar':
             # Lógica simple para amonestación (sin cobro)
            reporte.estado = 'RECHAZADO' # O podrías crear un estado 'AMONESTACION'
            reporte.resolucion_admin = f"AMONESTACIÓN VERBAL: {comentario}"
            reporte.save()
            messages.info(request, "Se ha registrado la amonestación.")

        return redirect('condominio:dashboard')

    return render(request, 'condominio/resolver_reporte.html', {
        'reporte': reporte,
        'reincidencias': reincidencias,
        'monto_sugerido': monto_sugerido
    })
@login_required
@transaction.atomic
def crear_reserva_estacionamiento(request):
    # 1. Seguridad: Verificar que el usuario tenga casa
    try:
        casa_solicitante = request.user.casa
    except Casa.DoesNotExist: # O el error correspondiente según tu lógica de usuario
        messages.error(request, "Debes tener una casa asignada para reservar.")
        return redirect('condominio:dashboard')

    if request.method == 'POST':
        # Pasamos 'casa' al formulario para filtrar el dropdown de vehículos
        form = ReservaEstacionamientoForm(request.POST, casa=casa_solicitante)

        if form.is_valid():
            # 2. Extracción de datos limpios
            data = form.cleaned_data
            fecha_inicio = data['fecha_inicio']
            fecha_fin = data['fecha_fin']
            vehiculo_obj = data['vehiculo'] # Objeto Vehiculo seleccionado

            # Convertimos a string para el historial (snapshot)
            placa_str = vehiculo_obj.placa
            modelo_str = str(vehiculo_obj.modelo) # "Marca Modelo" gracias al __str__

            # 3. Lógica de Negocio: Duración > 24h
            duracion = fecha_fin - fecha_inicio
            requiere_aprobacion = duracion > timedelta(hours=24)
            estado_inicial = 'PENDIENTE' if requiere_aprobacion else 'CONFIRMADA'

            # 4. Lógica de Asignación Inteligente (Función interna)
            # ... dentro de crear_reserva_estacionamiento ...

            # 4. Lógica de Asignación Inteligente (CORREGIDA)
            def buscar_lugar_disponible():
                # A) Buscamos Públicos
                candidatos_publicos = LugarEstacionamiento.objects.filter(es_publico=True)

                # B) Buscamos Privados que estén en la tabla de Disponibilidad (Prestados)
                #    y que cubran TOTALMENTE el horario que pido.
                ids_prestados = DisponibilidadEstacionamiento.objects.filter(
                    fecha_inicio__lte=fecha_inicio, # El préstamo empieza antes o igual a mi reserva
                    fecha_fin__gte=fecha_fin        # El préstamo termina después o igual a mi reserva
                ).values_list('lugar__id', flat=True)

                candidatos_prestados = LugarEstacionamiento.objects.filter(id__in=ids_prestados)

                # C) Unimos ambos grupos (Públicos + Prestados)
                candidatos_totales = candidatos_publicos | candidatos_prestados

                # 🚨 REGLA DE ORO: EXCLUIR MIS PROPIOS CAJONES 🚨
                # No tiene sentido reservarme a mí mismo si pido un adicional.
                candidatos_totales = candidatos_totales.exclude(casa=casa_solicitante)

                # D) Filtrar los que YA están reservados (Ocupados por otra reserva)
                # (Misma lógica de solapamiento que teníamos antes)
                ocupados = ReservaEstacionamiento.objects.filter(
                    lugar__in=candidatos_totales,
                    estado__in=['PENDIENTE', 'CONFIRMADA', 'ACTIVA'],
                    fecha_inicio__lt=fecha_fin,
                    fecha_fin__gt=fecha_inicio
                ).values_list('lugar__id', flat=True)

                # E) Retornar el primero libre
                return candidatos_totales.exclude(id__in=ocupados).first()

            # Ejecutamos la búsqueda única
            lugar_asignado = buscar_lugar_disponible()



            # 5. Guardar o Rechazar
            if lugar_asignado:
                ReservaEstacionamiento.objects.create(
                    casa_solicitante=casa_solicitante,
                    lugar=lugar_asignado,
                    fecha_inicio=fecha_inicio,
                    fecha_fin=fecha_fin,
                    placa_vehiculo=placa_str,
                    modelo_vehiculo=modelo_str,
                    estado=estado_inicial,
                    requiere_aprobacion_admin=requiere_aprobacion
                )

                msg = f"Reserva exitosa en {lugar_asignado}."
                if requiere_aprobacion:
                    messages.warning(request, f"{msg} Estado: PENDIENTE (duración > 24h).")
                else:
                    messages.success(request, f"{msg} Estado: CONFIRMADA.")

                return redirect('condominio:dashboard')
            else:
                messages.error(request, "Lo sentimos, no hay lugares disponibles (ni públicos ni privados) para ese horario.")
        else:
            # Errores de formulario
            messages.error(request, "Por favor corrige los errores en el formulario.")
    else:
        # GET: Formulario vacío con vehículos filtrados
        form = ReservaEstacionamientoForm(casa=casa_solicitante)

    return render(request, 'condominio/crear_reserva_parking.html', {'form': form})

@login_required
def prestar_estacionamiento(request):
    try:
        mi_casa = request.user.casa
    except Casa.DoesNotExist:
        return redirect('condominio:dashboard')

    if request.method == 'POST':
        form = PrestamoEstacionamientoForm(request.POST, casa=mi_casa)
        if form.is_valid():
            prestamo = form.save(commit=False)
            prestamo.publicado_por = mi_casa # Guardamos quién lo prestó
            prestamo.save()
            messages.success(request, "¡Gracias! Tu cajón ahora está disponible para tus vecinos.")
            return redirect('condominio:prestar_estacionamiento')
    else:
        form = PrestamoEstacionamientoForm(casa=mi_casa)

    # Listar mis préstamos activos (futuros o actuales) para poder verlos
    mis_prestamos = DisponibilidadEstacionamiento.objects.filter(
        lugar__casa=mi_casa,
        fecha_fin__gte=timezone.now()
    ).order_by('fecha_inicio')

    return render(request, 'condominio/prestar_estacionamiento.html', {
        'form': form,
        'mis_prestamos': mis_prestamos
    })

@login_required
def eliminar_prestamo(request, prestamo_id):
    # Permite cancelar un préstamo si te arrepientes
    prestamo = get_object_or_404(DisponibilidadEstacionamiento, id=prestamo_id)

    # Seguridad: Solo el dueño de la casa puede borrarlo
    if prestamo.lugar.casa == request.user.casa:
        prestamo.delete()
        messages.info(request, "Oferta de préstamo cancelada.")

    return redirect('condominio:prestar_estacionamiento')