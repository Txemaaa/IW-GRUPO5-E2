from django.contrib import admin
from .models import Empleado, Turno, Parte_Trabajo

admin.site.register(Empleado)
admin.site.register(Turno)
admin.site.register(Parte_Trabajo)