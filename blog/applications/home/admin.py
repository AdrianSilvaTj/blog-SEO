from django.contrib import admin
from .models import Suscribers, Contact, Home


admin.site.register([Suscribers, Contact, Home])
