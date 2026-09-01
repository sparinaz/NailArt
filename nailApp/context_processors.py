from .models import SiteSetting

def sitesetting(request):
    return {
        'sitesetting': SiteSetting.objects.first()
    }