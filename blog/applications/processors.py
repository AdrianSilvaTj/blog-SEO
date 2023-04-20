""" Context Proccesor, aca se pueden realizar procesos que van a estar disponibles desde
cualquier contexto del proyecto. Se debe agregar en base.py """
from applications.home.models import Home

# procesor para recuperar teléfono y numero de tlf del registro Home

def home_contact(request):
    home = Home.objects.latest('created')
    return {
        'phone': home.phone,
        'correo': home.contact_email,
    }