from .models import Redsocial


def redes_sociales(request):
    return {'redes_sociales': Redsocial.objects.all()}