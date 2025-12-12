# condominio/forms.py

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Transaccion, Vehiculo, Reservacion, Visitante, Marca, Modelo, Propuesta, Casa, Paquete, AreaComun, ReporteIncidencia, ServicioVecino, ReservaEstacionamiento, DisponibilidadEstacionamiento, LugarEstacionamiento
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from datetime import date, time, datetime
from .models import Paquete
from django.utils import timezone
from django.conf import settings
from zoneinfo import ZoneInfo

# --- FORMULARIO DE VEHÍCULO ---
class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['placa', 'marca', 'modelo', 'color']
        widgets = {
            'placa': forms.TextInput(attrs={
                'placeholder': 'Ej: GWE-162-E o ABC-12-34',
                'onkeyup': "this.value = this.value.toUpperCase().replace(/ /g, '')"
            })
        }

class ServicioVecinoForm(forms.ModelForm):
    class Meta:
        model = ServicioVecino
        fields = ['titulo', 'categoria', 'descripcion', 'telefono_contacto', 'imagen_promo']
        labels = {
            'titulo': 'Título de tu Servicio/Negocio',
            'telefono_contacto': 'WhatsApp de contacto',
            'imagen_promo': 'Foto de tu producto o logo (Opcional)'
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Ej: Hago pasteles bajo pedido...'}),
        }


class ReservacionForm(forms.ModelForm):
    # Definimos el campo 'acepta_reglas' que no está en el modelo.
    # Es solo para la validación en el formulario.
    acepta_reglas = forms.BooleanField(
        required=False,
        label="He leído y acepto las reglas del área."
    )

    class Meta:
        model = Reservacion
        # --- CORRECCIÓN CLAVE ---
        # Usamos los campos del modelo y NO incluimos 'acepta_reglas' aquí.
        fields = ['area_comun', 'fecha_hora_inicio', 'fecha_hora_fin', 'cantidad_personas']

        # Estos widgets son para los campos ocultos. No afectan la selección
        # de hora/duración, pero aseguran que Django entienda el formato.
        widgets = {
            'fecha_hora_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fecha_hora_fin': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        labels = {
            'area_comun': 'Área Común a Reservar',
            'cantidad_personas': 'Número de Invitados (opcional)',
        }

    def __init__(self, *args, **kwargs):
        casa_usuario = kwargs.pop('casa', None)
        super().__init__(*args, **kwargs)
        if casa_usuario:
            self.fields['area_comun'].queryset = AreaComun.objects.filter(villa=casa_usuario.villa)

    def clean(self):
        cleaned_data = super().clean()
        area = cleaned_data.get("area_comun")
        inicio = cleaned_data.get("fecha_hora_inicio")
        fin = cleaned_data.get("fecha_hora_fin")

        if not (area and inicio and fin):
            return cleaned_data

        # --- Tu excelente lógica de validación se mantiene ---
        tz = ZoneInfo(getattr(settings, "TIME_ZONE", "America/Mexico_City"))

        if timezone.is_naive(inicio):
            inicio = inicio.replace(tzinfo=tz)
        else:
            inicio = inicio.astimezone(tz)

        if timezone.is_naive(fin):
            fin = fin.replace(tzinfo=tz)
        else:
            fin = fin.astimezone(tz)

        now_local = timezone.now().astimezone(tz)

        if inicio < now_local:
            raise ValidationError("No puedes realizar una reservación en una fecha u hora pasada.")

        if fin <= inicio:
            raise ValidationError("La hora de finalización debe ser posterior a la hora de inicio.")

        if "alberca" in ((getattr(area, "nombre", "") or "").lower()):
            # Ahora la validación de 'acepta_reglas' funcionará correctamente
            if not cleaned_data.get("acepta_reglas"):
                raise ValidationError("Debes aceptar las reglas para reservar la alberca.")

            apertura_t = time(7, 0)
            cierre_t   = time(20, 0)

            if inicio.date() != fin.date():
                raise ValidationError("La reservación de la alberca debe ser dentro del mismo día.")

            apertura_dt = datetime.combine(inicio.date(), apertura_t).replace(tzinfo=tz)
            cierre_dt   = datetime.combine(inicio.date(), cierre_t).replace(tzinfo=tz)

            if not (apertura_dt <= inicio and fin <= cierre_dt):
                raise ValidationError("Error de horario. La reservación para la alberca debe estar dentro del rango de 9:00 AM a 8:00 PM.")

        return cleaned_data



class VisitanteForm(forms.ModelForm):
    requiere_estacionamiento = forms.BooleanField(
        required=False,
        label="¿El visitante requiere un lugar de estacionamiento?"
    )

    class Meta:
        model = Visitante
        fields = ['nombre_visitante', 'fecha_programada']
        widgets = {
            'fecha_programada': forms.DateTimeInput(
                attrs={'type': 'datetime-local'}
            ),
        }
        labels = {
            'fecha_programada': 'Fecha y Hora Programada'
        }

class VisitanteDocumentoForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = ['foto_identificacion', 'foto_placas']
        labels = {
            'foto_identificacion': 'Foto de Identificación Oficial (INE, Pasaporte)',
            'foto_placas': 'Foto de las Placas del Vehículo',
        }

class PropuestaForm(forms.ModelForm):
    class Meta:
        model = Propuesta
        fields = ['titulo', 'descripcion', 'costo_estimado', 'beneficios']
        labels = {
            'titulo': 'Título de la Propuesta',
            'descripcion': 'Descripción Detallada',
            'costo_estimado': 'Costo Estimado ($)',
            'beneficios': 'Beneficios para la Comunidad',
        }

class PaqueteGuardiaForm(forms.ModelForm):
    casa = forms.ModelChoiceField(
        queryset=Casa.objects.all().order_by('numero_casa'),
        label="Casa del Residente"
    )

    class Meta:
        model = Paquete
        fields = ['casa', 'remitente', 'numero_guia']

class PaqueteResidenteForm(forms.ModelForm):
    class Meta:
        model = Paquete
        fields = ['remitente', 'codigo_recogida']
        labels = {
            'remitente': 'Paquetería o Remitente (Ej: Amazon)',
            'codigo_recogida': 'Código de Recogida (si aplica)',
        }

# --- FORMULARIO DE LOGIN PERSONALIZADO ---
class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Clases de Tailwind para los campos de texto
        tailwind_classes = 'mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm'

        # Aplicar las clases al campo de usuario
        self.fields['username'].widget.attrs.update({
            'class': tailwind_classes,
            'placeholder': 'nombredeusuario'
        })

        # Aplicar las clases al campo de contraseña
        self.fields['password'].widget.attrs.update({
            'class': tailwind_classes,
            'placeholder': '••••••••'
        })



class AbonoForm(forms.ModelForm):
    """Formulario para que el residente registre un pago."""
    class Meta:
        model = Transaccion
        fields = ['monto', 'comprobante']
        labels = {
            'monto': 'Monto del Pago',
            'comprobante': 'Comprobante de Pago (imagen o PDF)',
        }
        widgets = {
            'monto': forms.NumberInput(attrs={'min': '0.01', 'step': '0.01'}),
        }

class ReporteForm(forms.ModelForm):
    class Meta:
        model = ReporteIncidencia
        fields = ['casa_infractora', 'categoria', 'descripcion', 'evidencia_foto']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3, 'class': 'w-full p-2 border rounded'}),
            'casa_infractora': forms.Select(attrs={'class': 'w-full p-2 border rounded'}),
            'categoria': forms.Select(attrs={'class': 'w-full p-2 border rounded'}),
            'evidencia_foto': forms.FileInput(attrs={'class': 'w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-red-50 file:text-red-700 hover:file:bg-red-100'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtramos para que aparezcan ordenadas
        self.fields['casa_infractora'].queryset = Casa.objects.all().order_by('numero_casa')
        self.fields['casa_infractora'].label = "Casa que cometió la falta"
        self.fields['evidencia_foto'].label = "Evidencia (Foto)"

class ReservaEstacionamientoForm(forms.ModelForm):
    # Selector de vehículo filtrado
    vehiculo = forms.ModelChoiceField(
        queryset=Vehiculo.objects.none(), # Se llena en el __init__
        label="Selecciona tu Vehículo",
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = ReservaEstacionamiento
        fields = ['fecha_inicio', 'fecha_fin']
        widgets = {
            # datetime-local es el estándar HTML5 para inputs de fecha y hora
            'fecha_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'fecha_fin': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        # Extraemos 'casa' de los argumentos para filtrar los coches
        casa = kwargs.pop('casa', None)
        super().__init__(*args, **kwargs)

        if casa:
            # Solo mostramos vehículos APROBADOS de esa casa
            self.fields['vehiculo'].queryset = Vehiculo.objects.filter(
                casa=casa,
                estado='Aprobado'
            )

    # Validación extra: No permitir reservas en el pasado
    def clean_fecha_inicio(self):
        inicio = self.cleaned_data['fecha_inicio']
        if inicio < timezone.now():
            raise forms.ValidationError("La reserva no puede iniciar en el pasado.")
        return inicio

    # Validación extra: Fecha fin debe ser después de inicio
    def clean(self):
        cleaned_data = super().clean()
        inicio = cleaned_data.get("fecha_inicio")
        fin = cleaned_data.get("fecha_fin")

        if inicio and fin:
            if fin <= inicio:
                raise forms.ValidationError("La fecha de fin debe ser posterior a la de inicio.")
        return cleaned_data

class PrestamoEstacionamientoForm(forms.ModelForm):
    lugar = forms.ModelChoiceField(
        queryset=LugarEstacionamiento.objects.none(), # Se llena dinámicamente
        label="¿Qué cajón quieres prestar?",
        empty_label="Selecciona un cajón",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = DisponibilidadEstacionamiento
        fields = ['lugar', 'fecha_inicio', 'fecha_fin']
        widgets = {
            'fecha_inicio': forms.DateTimeInput(attrs={'class': 'datetime-picker'}),
            'fecha_fin': forms.DateTimeInput(attrs={'class': 'datetime-picker'}),
        }

    def __init__(self, *args, **kwargs):
        casa = kwargs.pop('casa', None)
        super().__init__(*args, **kwargs)

        if casa:
            # Solo muestro los cajones PRIVADOS que pertenecen a ESA casa
            self.fields['lugar'].queryset = LugarEstacionamiento.objects.filter(
                casa=casa,
                es_publico=False
            )

    def clean(self):
        cleaned_data = super().clean()
        inicio = cleaned_data.get("fecha_inicio")
        fin = cleaned_data.get("fecha_fin")

        if inicio and fin:
            if fin <= inicio:
                raise forms.ValidationError("La fecha de fin debe ser posterior al inicio.")
        return cleaned_data