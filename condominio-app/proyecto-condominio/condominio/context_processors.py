# condominio/context_processors.py

from .models import Villa

def villa_context(request):
    # Esta función se ejecuta en cada página
    if request.user.is_authenticated:
        if hasattr(request.user, 'casa'):
            # Si el usuario es un RESIDENTE, obtenemos la villa a través de su casa
            villa_actual = request.user.casa.villa
            return {'villa_actual': villa_actual}
        
        elif request.user.groups.filter(name='Guardias').exists():
            # Si el usuario es un GUARDIA, le asignamos la primera villa que exista
            # (asumiendo que los guardias trabajan para una villa principal)
            villa_actual = Villa.objects.first()
            return {'villa_actual': villa_actual}
            
    return {}