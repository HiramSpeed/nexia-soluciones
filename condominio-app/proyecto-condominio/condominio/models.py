# condominio/models.py

from django.db import models
from django.contrib.auth.models import User
from datetime import date
from decimal import Decimal
from django.utils import timezone

# --- BORRA ESTA LÍNEA: from .models import Casa, Transaccion ---

# --- MODELO DE CATEGORÍA ---
class CategoriaIncidencia(models.Model):
    nombre = models.CharField(max_length=50)
    monto_base = models.DecimalField(default=200.00, max_digits=6, decimal_places=2, help_text="Costo de la 1ra multa")

    def __str__(self):
        return self.nombre

# --- MODELO PRINCIPAL DE REPORTE ---
# condominio/models.py

from django.apps import apps # Necesario para la carga dinámica de modelos

# ... (asegúrate de que CategoriaIncidencia esté definido ANTES de esto, o usa comillas)

class ReporteIncidencia(models.Model):
    ESTADOS = [
        ('PENDIENTE', 'Pendiente de Revisión'),
        ('RECHAZADO', 'Rechazado / No Procede'),
        ('MULTA', 'Multa Aplicada'),
    ]

    # Relaciones con Casa (Usando comillas 'Casa' para evitar errores de orden)
    reportante = models.ForeignKey('Casa', related_name='reportes_realizados', on_delete=models.CASCADE)
    casa_infractora = models.ForeignKey('Casa', related_name='reportes_recibidos', on_delete=models.CASCADE)

    # Si CategoriaIncidencia está arriba, va sin comillas. Si está abajo, ponle comillas.
    categoria = models.ForeignKey(CategoriaIncidencia, on_delete=models.SET_NULL, null=True)

    descripcion = models.TextField()

    # Esta es la FOTO PRINCIPAL (la que sube el reportante original)
    evidencia_foto = models.ImageField(upload_to='evidencias/', null=True, blank=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    # Resolución
    estado = models.CharField(max_length=20, choices=ESTADOS, default='PENDIENTE')
    resolucion_admin = models.TextField(blank=True)
    monto_multa = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    # Relación con Transacción (Usando comillas)
    transaccion = models.OneToOneField('Transaccion', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"Reporte vs {self.casa_infractora} - {self.categoria}"

    # --- LÓGICA DE REINCIDENCIA ---
    def calcular_reincidencia(self):
        # Cuenta cuántas multas YA APROBADAS tiene esta casa por lo mismo
        conteo = ReporteIncidencia.objects.filter(
            casa_infractora=self.casa_infractora,
            categoria=self.categoria,
            estado='MULTA'
        ).exclude(id=self.id).count()
        return conteo

    def sugerir_monto(self):
        veces_previas = self.calcular_reincidencia()
        # Asegúrate de que CategoriaIncidencia tenga el campo 'monto_base'
        base = self.categoria.monto_base
        nuevo_monto = base * (veces_previas + 1)
        return nuevo_monto

    def aplicar_multa(self, admin_user, explicacion):
        """
        Genera la multa y la transacción contable automáticamente.
        """
        # Usamos apps.get_model para obtener Transaccion de forma segura
        # sin importar dónde esté definido en el archivo.
        Transaccion = apps.get_model('condominio', 'Transaccion')

        monto_a_cobrar = self.sugerir_monto()

        self.estado = 'MULTA'
        self.resolucion_admin = explicacion
        self.monto_multa = monto_a_cobrar

        # Crear la transacción financiera
        nueva_transaccion = Transaccion.objects.create(
            casa=self.casa_infractora,
            tipo='CARGO',
            monto=monto_a_cobrar,
            concepto=f"Multa (Reincidencia #{self.calcular_reincidencia() + 1}): {self.categoria.nombre}",
            estado_aprobacion='APROBADO'
        )
        self.transaccion = nueva_transaccion

        # Afectar el saldo de la casa
        self.casa_infractora.saldo += monto_a_cobrar
        self.casa_infractora.save()

        self.save()
class EvidenciaReporte(models.Model):
    """
    Modelo para guardar fotos adicionales de otros vecinos
    que se suman a un reporte existente.
    """
    reporte = models.ForeignKey(ReporteIncidencia, related_name='evidencias', on_delete=models.CASCADE)
    archivo = models.ImageField(upload_to='evidencias_incidencias/')

    # AQUÍ SÍ VA ESTE CAMPO: Para saber qué vecino "chismoso" ayudó con más pruebas
    subido_por = models.ForeignKey('Casa', on_delete=models.SET_NULL, null=True, help_text="Vecino que aportó esta evidencia extra")

    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Evidencia extra al reporte {self.reporte.id}"

class Villa(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=255, blank=True)
    logo = models.ImageField(upload_to='logos_villas/', null=True, blank=True)
    google_maps_link = models.URLField(max_length=500, blank=True, help_text="Enlace completo de Google Maps")

    def __str__(self):
        return self.nombre

# --- MODELOS DE CATÁLOGO Y CONFIGURACIÓN ---
class ContadorFolio(models.Model):
    ultimo_folio = models.PositiveIntegerField(default=1999)

    def __str__(self):
        return f"Último folio usado: {self.ultimo_folio}"


class Marca(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.nombre

class Modelo(models.Model):
    marca = models.ForeignKey('Marca', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.marca.nombre} {self.nombre}"

# --- MODELOS CENTRALES ---

class Casa(models.Model):
    ESTATUS_CHOICES = [('Al Corriente', 'Al Corriente'), ('Con Adeudo', 'Con Adeudo'), ('En Convenio', 'En Convenio de Pago')]
    TIPO_RESIDENTE_CHOICES = [('Propietario', 'Propietario'), ('Arrendatario', 'Arrendatario')]
    ESTADO_GAFETE_CHOICES = [('Pendiente', 'Pendiente'), ('Entregado', 'Entregado'), ('En Revision', 'En Revisión')]

    villa = models.ForeignKey('Villa', on_delete=models.CASCADE)

    # --- CAMPO DEL DUEÑO (MANTENER INTACTO) ---
    # Lo dejamos igual para que request.user.casa siga funcionando en tus vistas actuales.
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    # --- NUEVO CAMPO: INQUILINO / HABITANTE (SEGURO) ---
    # Este permite un segundo acceso sin borrar al dueño.
    # Se usa: request.user.casa_inquilino
    inquilino = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='casa_inquilino',
        help_text="Cuenta secundaria para inquilino o habitante adicional"
    )

    numero_casa = models.CharField(max_length=10)
    propietario = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15, blank=True)
    estatus_condominio = models.CharField(max_length=20, choices=ESTATUS_CHOICES, default='Al Corriente')
    tipo_residente = models.CharField(max_length=20, choices=TIPO_RESIDENTE_CHOICES, default='Propietario')
    estado_gafete = models.CharField(max_length=20, choices=ESTADO_GAFETE_CHOICES, default='Pendiente')

    # Este campo lleva el control del estado de cuenta de la casa.
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    class Meta:
        unique_together = ('villa', 'numero_casa')

    def __str__(self):
        return f"Casa {self.numero_casa} ({self.villa.nombre})"

class Transaccion(models.Model):
    TIPO_CHOICES = [
        ('CARGO', 'Cargo'),         # Para cuotas, multas, etc. (suma a la deuda)
        ('ABONO', 'Abono'),         # Para pagos de residentes (resta a la deuda)
        ('AJUSTE', 'Ajuste'),       # Para correcciones manuales
    ]
    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente de Aprobación'),
        ('APROBADO', 'Aprobado'),
        ('RECHAZADO', 'Rechazado'),
    ]

    casa = models.ForeignKey(Casa, on_delete=models.CASCADE, related_name='transacciones')
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    monto = models.DecimalField(max_digits=10, decimal_places=2, help_text="Siempre un valor positivo. El tipo determina si suma o resta.")
    concepto = models.CharField(max_length=255)
    fecha = models.DateTimeField(auto_now_add=True)

    # Campos específicos para los Abonos (pagos de residentes)
    comprobante = models.ImageField(upload_to='comprobantes_transacciones/', null=True, blank=True)
    estado_aprobacion = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='APROBADO', null=True, blank=True)

    # Campo opcional para vincular un cargo a un objeto Pago si quieres mantener la relación
    pago_original = models.ForeignKey('Pago', on_delete=models.SET_NULL, null=True, blank=True)
    recibo_pdf = models.FileField(upload_to='recibos_transacciones/', null=True, blank=True)

    def __str__(self):
        return f"{self.get_tipo_display()} de ${self.monto} para {self.casa}"



class Pago(models.Model):
    ESTADO_PAGO = [('Pendiente', 'Pendiente'), ('Pagado', 'Pagado'), ('Atrasado', 'Atrasado'), ('En Verificación', 'En Verificación')]
    casa = models.ForeignKey('Casa', on_delete=models.CASCADE)
    concepto = models.CharField(max_length=100, default="Mantenimiento Mensual")
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_generacion = models.DateField(auto_now_add=True)
    fecha_vencimiento = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADO_PAGO, default='Pendiente')
    comprobante = models.ImageField(upload_to='comprobantes/', null=True, blank=True)
    es_deuda_anterior = models.BooleanField(default=False, help_text="Marcar si este pago es anterior a Junio 2025")
    folio = models.PositiveIntegerField(unique=True, null=True, blank=True, help_text="Número de folio del recibo")
    recibo_pdf = models.FileField(upload_to='recibos/', null=True, blank=True, help_text="PDF del recibo generado")

    @property
    def monto_a_pagar(self):
        if self.estado in ['Pendiente', 'Atrasado'] and date.today() > self.fecha_vencimiento:
            return self.monto + Decimal('100.00')
        return self.monto

    def __str__(self):
        return f"{self.concepto} - Casa {self.casa.numero_casa} - ${self.monto}"

class CasaConAdeudo(Casa):
    class Meta:
        proxy = True
        verbose_name = 'Casa con Adeudo'
        verbose_name_plural = 'Casas con Adeudo'

class Vehiculo(models.Model):
    ESTADO_VEHICULO = [('Pendiente', 'Pendiente de Aprobación'), ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')]
    casa = models.ForeignKey('Casa', related_name='vehiculos', on_delete=models.CASCADE)
    marca = models.ForeignKey('Marca', on_delete=models.SET_NULL, null=True)
    modelo = models.ForeignKey('Modelo', on_delete=models.SET_NULL, null=True)
    placa = models.CharField(max_length=10, unique=True, help_text="Matrícula del vehículo")
    color = models.CharField(max_length=30)
    tarjeta_rfid = models.CharField(max_length=50, unique=True, null=True, blank=True, help_text="ID único de la tarjeta de acceso")
    estado = models.CharField(max_length=20, choices=ESTADO_VEHICULO, default='Pendiente')

    def __str__(self):
        return f"{self.placa} ({self.marca}) - {self.estado}"


class AreaComun(models.Model):
    villa = models.ForeignKey('Villa', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)
    capacidad_personas = models.PositiveIntegerField(default=1, help_text="Para áreas como Terraza o Alberca")
    cantidad_espacios = models.PositiveIntegerField(default=1, help_text="Para áreas con múltiples espacios idénticos (ej. Estacionamientos)")

    class Meta:
        unique_together = ('villa', 'nombre')

    def __str__(self):
        return self.nombre

# condominio/models.py

class Reservacion(models.Model):
    ESTADO_RESERVACION = [
        ('Pendiente', 'Pendiente'),
        ('Aprobada', 'Aprobada'),
        ('Rechazada', 'Rechazada'),
        ('En Uso', 'En Uso'),
        ('Completada', 'Completada'),
    ]
    area_comun = models.ForeignKey('AreaComun', on_delete=models.CASCADE)
    casa = models.ForeignKey('Casa', on_delete=models.CASCADE)
    fecha_hora_inicio = models.DateTimeField()
    fecha_hora_fin = models.DateTimeField()
    estado = models.CharField(max_length=20, choices=ESTADO_RESERVACION, default='Pendiente')
    cantidad_personas = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Número de invitados (si aplica)"
    )

    guardia_entrega = models.ForeignKey(
        User,
        related_name='reservaciones_entregadas', # <-- Nombre único
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    fecha_hora_entrega = models.DateTimeField(null=True, blank=True)

    guardia_devolucion = models.ForeignKey(
        User,
        related_name='reservaciones_devueltas', # <-- Nombre único
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    fecha_hora_devolucion = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Reservación de {self.area_comun.nombre} por Casa {self.casa.numero_casa}"


class Visitante(models.Model):
    ESTADO_VISITA = [('Esperando', 'Esperando'), ('Adentro', 'Adentro'), ('Completada', 'Completada')]
    casa = models.ForeignKey('Casa', on_delete=models.CASCADE)
    nombre_visitante = models.CharField(max_length=100)
    token_acceso = models.CharField(max_length=32, unique=True, null=True, blank=True)
    foto_identificacion = models.ImageField(upload_to='identificaciones/', null=True, blank=True)
    foto_placas = models.ImageField(upload_to='placas/', null=True, blank=True)
    fecha_programada = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADO_VISITA, default='Esperando')
    fecha_programada = models.DateTimeField()
    guardia_entrada = models.ForeignKey(User, related_name='visitantes_ingresados', on_delete=models.SET_NULL, null=True, blank=True)
    fecha_hora_entrada = models.DateTimeField(null=True, blank=True)
    guardia_salida = models.ForeignKey(User, related_name='visitantes_salida', on_delete=models.SET_NULL, null=True, blank=True)
    fecha_hora_salida = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Visita de {self.nombre_visitante} para Casa {self.casa.numero_casa}"


class Propuesta(models.Model):
    ESTADO_PROPUESTA = [
        ('Pendiente', 'Pendiente de Aprobación'),
        ('Activa', 'Activa para Votar'),
        ('Aprobada', 'Resultado: Aprobada'),
        ('Rechazada', 'Resultado: Rechazada'),
        ('Cancelada', 'Cancelada'),
    ]

    villa = models.ForeignKey('Villa', on_delete=models.CASCADE)
    autor = models.ForeignKey('Casa', on_delete=models.SET_NULL, null=True, help_text="Casa que origina la propuesta")

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(help_text="Explica detalladamente la propuesta.")
    costo_estimado = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    beneficios = models.TextField(help_text="Describe los beneficios para la comunidad.")

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_fin_votacion = models.DateTimeField(null=True, blank=True, help_text="El administrador establece esta fecha al aprobar.")

    estado = models.CharField(max_length=20, choices=ESTADO_PROPUESTA, default='Pendiente')

    def __str__(self):
        return self.titulo



class Voto(models.Model):
    DECISION_CHOICES = [
        ('A Favor', 'A Favor'),
        ('En Contra', 'En Contra'),
        ('Abstencion', 'Abstención'),
    ]

    propuesta = models.ForeignKey(Propuesta, on_delete=models.CASCADE, related_name='votos')
    casa = models.ForeignKey('Casa', on_delete=models.CASCADE)
    decision = models.CharField(max_length=10, choices=DECISION_CHOICES)
    fecha_voto = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Regla clave: Cada casa solo puede votar una vez por cada propuesta
        unique_together = ('propuesta', 'casa')

    def __str__(self):
        return f"Voto de Casa {self.casa.numero_casa} en '{self.propuesta.titulo}'"

# condominio/models.py

class DocumentoPropuesta(models.Model):
    propuesta = models.ForeignKey(Propuesta, on_delete=models.CASCADE, related_name='documentos')
    documento = models.FileField(upload_to='propuestas_documentos/')
    nombre_documento = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        if not self.nombre_documento:
            self.nombre_documento = self.documento.name
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Documento para '{self.propuesta.titulo}'"

# condominio/models.py
# ... (tus otros modelos) ...

class Paquete(models.Model):
    ESTADO_PAQUETE = [
        ('En Vigilancia', 'En Vigilancia'),
        ('Entregado', 'Entregado'),
        ('Esperando Llegada', 'Esperando Llegada'), # Para códigos pre-registrados
    ]

    casa = models.ForeignKey('Casa', on_delete=models.CASCADE, related_name='paquetes')
    remitente = models.CharField(max_length=100, help_text="Ej: Amazon, Mercado Libre, etc.")
    numero_guia = models.CharField(max_length=100, blank=True, help_text="Número de rastreo (opcional)")

    # Para la funcionalidad de códigos de recogida
    codigo_recogida = models.CharField(max_length=50, blank=True, help_text="Código necesario para recibir el paquete")

    # Registro de auditoría
    registrado_por = models.ForeignKey(User, related_name='paquetes_registrados', on_delete=models.SET_NULL, null=True, blank=True)
    fecha_llegada = models.DateTimeField(auto_now_add=True)
    entregado_a_residente_por = models.ForeignKey(User, related_name='paquetes_entregados', on_delete=models.SET_NULL, null=True, blank=True)
    fecha_entrega = models.DateTimeField(null=True, blank=True)

    estado = models.CharField(max_length=20, choices=ESTADO_PAQUETE, default='En Vigilancia')

    def __str__(self):
        return f"Paquete de {self.remitente} para Casa {self.casa.numero_casa}"

# --- MÓDULO DE COMUNIDAD ---

class ServicioVecino(models.Model):
    CATEGORIAS = [
        ('Oficio', '🛠️ Oficio / Reparaciones (Plomero, Electricista...)'),
        ('Comida', '🍔 Comida / Postres'),
        ('Producto', '📦 Venta de Productos (Catálogo, Ropa...)'),
        ('Profesional', 'immo Servicios Profesionales (Contador, Abogado...)'),
        ('Clases', '🎓 Clases / Enseñanza'),
    ]

    casa = models.OneToOneField('Casa', on_delete=models.CASCADE, related_name='mi_servicio')
    titulo = models.CharField(max_length=100, help_text="Ej: Plomería García o Postres Caseros")
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    descripcion = models.TextField(help_text="Describe qué haces, horarios, etc.")
    telefono_contacto = models.CharField(max_length=15, help_text="Número para WhatsApp")
    imagen_promo = models.ImageField(upload_to='servicios_vecinos/', null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - Casa {self.casa.numero_casa}"

class Reconocimiento(models.Model):
    TIPOS = [
        ('Conocido', '👋 Lo conozco / Buen vecino'),
        ('Recomendado', '⭐ Recomiendo su servicio'),
        ('Ayuda', '🤝 Me ha ayudado en algo'),
    ]

    # Quién da la estrella
    otorgado_por = models.ForeignKey('Casa', related_name='reconocimientos_dados', on_delete=models.CASCADE)
    # Quién recibe la estrella
    recibido_por = models.ForeignKey('Casa', related_name='reconocimientos_recibidos', on_delete=models.CASCADE)

    tipo = models.CharField(max_length=20, choices=TIPOS)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('otorgado_por', 'recibido_por') # Solo puedes dar 1 estrella por vecino

    def __str__(self):
        return f"{self.otorgado_por} reconoce a {self.recibido_por}"

# --- MÓDULO DE ESTACIONAMIENTO (Refactorizado) ---

class LugarEstacionamiento(models.Model):
    TIPOS_IDENTIFICADOR = [
        ('A', 'Lugar A (Privado)'),
        ('B', 'Lugar B (Privado)'),
        ('P', 'Público / Visitas')
    ]

    # Ahora la casa es OPCIONAL. Si es null, es un lugar PÚBLICO de la Villa.
    casa = models.ForeignKey(Casa, related_name='lugares_propiedad', on_delete=models.SET_NULL, null=True, blank=True)

    identificador = models.CharField(max_length=10, help_text="Ej: A, B, o V1, V2 para visitas")
    es_publico = models.BooleanField(default=False, help_text="Marcar True si es un cajón de uso común/visitas")

    # Campo auxiliar para saber rápidamente quién está ahí (útil para la lógica de Eventos)
    ocupado_actualmente_por = models.ForeignKey(Casa, related_name='lugar_en_uso', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        # Quitamos unique_together antiguo porque los públicos no tienen casa
        verbose_name = "Lugar de Estacionamiento"
        verbose_name_plural = "Lugares de Estacionamiento"

    def __str__(self):
        propiedad = f"Casa {self.casa.numero_casa}" if self.casa else "PÚBLICO"
        return f"Lugar {self.identificador} ({propiedad})"


class ReservaEstacionamiento(models.Model):
    ESTADOS_RESERVA = [
        ('PENDIENTE', 'Pendiente de Aprobación (>24h)'),
        ('CONFIRMADA', 'Confirmada'),
        ('ACTIVA', 'En Uso Actualmente'), # El auto está ahí
        ('FINALIZADA', 'Finalizada'),
        ('RECHAZADA', 'Rechazada'),
        ('EN_REVISION_EVENTO', 'Solicitado mover por Evento'), # Estado crítico para tu lógica
    ]

    casa_solicitante = models.ForeignKey(Casa, related_name='reservas_estacionamiento', on_delete=models.CASCADE)
    lugar = models.ForeignKey(LugarEstacionamiento, related_name='reservas', on_delete=models.CASCADE)

    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()

    # Datos del vehículo que ocupará el lugar (puede ser del vecino o una visita)
    placa_vehiculo = models.CharField(max_length=15)
    modelo_vehiculo = models.CharField(max_length=50, blank=True)

    estado = models.CharField(max_length=25, choices=ESTADOS_RESERVA, default='CONFIRMADA')

    # Para la regla de aprobación > 24 horas
    requiere_aprobacion_admin = models.BooleanField(default=False)
    motivo_rechazo = models.TextField(blank=True, null=True, help_text="Razón si el admin rechaza la reserva larga")

    # Para la regla de "Evento en la Villa"
    notificado_por_evento = models.BooleanField(default=False, help_text="Si se le avisó que debe mover el auto")
    causa_mayor_reportada = models.BooleanField(default=False, help_text="El vecino indicó que NO puede moverlo (causa mayor)")

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Lógica automática: Si la duración es mayor a 24 horas y es nueva, requiere aprobación
        if not self.pk:  # Solo al crear
            duracion = self.fecha_fin - self.fecha_inicio
            if duracion.total_seconds() > 86400: # 86400 segundos = 24 horas
                self.requiere_aprobacion_admin = True
                self.estado = 'PENDIENTE'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Reserva {self.casa_solicitante} en {self.lugar} ({self.estado})"

class DisponibilidadEstacionamiento(models.Model):
    """
    Tabla donde los vecinos 'sueltan' su cajón para que otros lo usen temporalmente.
    """
    lugar = models.ForeignKey(LugarEstacionamiento, on_delete=models.CASCADE, related_name='disponibilidades')
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()

    # Opcional: Para saber quién lo prestó (aunque se saca del lugar.casa)
    publicado_por = models.ForeignKey(Casa, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.lugar} disponible de {self.fecha_inicio} a {self.fecha_fin}"
