# condominio/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CustomLoginView
from . import views

# El 'app_name' es una buena práctica para organizar URLs
app_name = 'condominio'

urlpatterns = [
    # --- URLs DE AUTENTICACIÓN Y DASHBOARD PRINCIPAL ---
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.dashboard, name='home'),
    path('api/reservaciones/', views.reservaciones_feed, name='reservaciones_feed'),

    # --- URLs DEL SISTEMA DE SALDOS Y TRANSACCIONES ---
    path('dashboard/registrar-abono/', views.registrar_abono, name='registrar_abono'),
    path('transaccion/<int:transaccion_id>/descargar-recibo/', views.descargar_recibo_transaccion, name='descargar_recibo_transaccion'),
    path('dashboard/reportar/', views.crear_reporte, name='crear_reporte'),

    # --- URLs DE GESTIÓN DE RESERVACIONES (ADMIN) ---
    path('reservacion/<int:reservacion_id>/aprobar/', views.aprobar_reservacion, name='aprobar_reservacion'),
    path('reservacion/<int:reservacion_id>/rechazar/', views.rechazar_reservacion, name='rechazar_reservacion'),

    # --- URLs DEL RESIDENTE ---
    path('casas/', views.lista_casas, name='lista_casas'),
    path('dashboard/agregar-vehiculo/', views.agregar_vehiculo, name='agregar_vehiculo'),
    path('vehiculo/<int:vehiculo_id>/eliminar/', views.eliminar_vehiculo, name='eliminar_vehiculo'),
    path('dashboard/reservaciones/', views.vista_reservaciones, name='vista_reservaciones'),
    path('dashboard/registrar-visita/', views.registrar_visita, name='registrar_visita'),
    path('visita/generada/<int:visitante_id>/', views.visita_generada, name='visita_generada'),
    path('dashboard/propuestas/', views.propuestas_lista, name='propuestas_lista'),
    path('dashboard/propuestas/crear/', views.propuesta_crear, name='propuesta_crear'),
    path('dashboard/propuesta/<int:propuesta_id>/', views.propuesta_detalle, name='propuesta_detalle'),
    path('dashboard/registrar-paquete/', views.residente_registrar_paquete, name='residente_registrar_paquete'),
    path('pago/<int:pago_id>/descargar-recibo/', views.descargar_recibo, name='descargar_recibo'),
    path('comunidad/', views.directorio_comunidad, name='directorio_comunidad'),
    path('comunidad/publicar/', views.publicar_servicio, name='publicar_servicio'),
    path('comunidad/estrella/<int:casa_id>/', views.dar_reconocimiento, name='dar_reconocimiento'),
    path('reservar-estacionamiento/', views.crear_reserva_estacionamiento, name='crear_reserva_estacionamiento'),
    path('estacionamiento/prestar/', views.prestar_estacionamiento, name='prestar_estacionamiento'),
    path('estacionamiento/prestar/eliminar/<int:prestamo_id>/', views.eliminar_prestamo, name='eliminar_prestamo'),

    # --- URLs DEL VIGILANTE ---
    path('vigilancia/', views.dashboard_vigilante, name='dashboard_vigilante'),
    path('vigilancia/entrega-gafetes/', views.dashboard_entrega_gafetes, name='dashboard_gafetes'),
    path('vigilancia/casa/<int:casa_id>/actualizar-gafete/', views.actualizar_estado_gafete, name='actualizar_estado_gafete'),
    path('visita/<int:visitante_id>/marcar-entrada/', views.marcar_entrada_visitante, name='marcar_entrada'),
    path('visita/<int:visitante_id>/marcar-salida/', views.marcar_salida_visitante, name='marcar_salida'),
    path('visita/<int:visitante_id>/guardia-subir-foto/', views.guardia_subir_foto_visitante, name='guardia_subir_foto'),
    path('reservacion/<int:reservacion_id>/iniciar/', views.iniciar_uso_reservacion, name='iniciar_reservacion'),
    path('reservacion/<int:reservacion_id>/finalizar/', views.finalizar_uso_reservacion, name='finalizar_reservacion'),
    path('paquete/<int:paquete_id>/entregar/', views.entregar_paquete, name='entregar_paquete'),
    path('vigilancia/registrar-paquete/', views.registrar_paquete, name='registrar_paquete'),
    path('paquete/<int:paquete_id>/confirmar-llegada/', views.confirmar_llegada_paquete, name='confirmar_llegada_paquete'),
    path('vigilancia/resetear-gafetes/', views.resetear_estado_gafetes, name='resetear_gafetes'),

    # --- URLs DEL ADMINISTRADOR ---
    path('vehiculos_pendientes/', views.vehiculos_pendientes, name='vehiculos_pendientes'),
    path('autorizar_vehiculo/<int:vehiculo_id>/', views.autorizar_vehiculo, name='autorizar_vehiculo'),
    path('dashboard/casas-con-adeudo/', views.lista_casas_con_adeudo, name='lista_casas_con_adeudo'),
    path('transaccion/<int:transaccion_id>/aprobar/', views.aprobar_transaccion, name='aprobar_transaccion'),
    path('transaccion/<int:transaccion_id>/descargar-recibo/', views.descargar_recibo_transaccion, name='descargar_recibo_transaccion'),
    path('reporte/<int:reporte_id>/resolver/', views.resolver_reporte, name='resolver_reporte'),

    # --- URLs PÚBLICAS Y AJAX ---
    path('visita/<str:token_acceso>/', views.vista_visitante, name='vista_visitante'),
    path('ajax/load-modelos/', views.load_modelos, name='ajax_load_modelos'),
]