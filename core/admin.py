from django.contrib import admin

# Register your models here.
from .models import Sala, Reserva, Usuario


admin.site.register(Sala)
admin.site.register(Reserva)
admin.site.register(Usuario)