from .models import Configuracion


def config_global(request):

    config, created = Configuracion.objects.get_or_create(id=1)

    return {
        'config_global': config
    }