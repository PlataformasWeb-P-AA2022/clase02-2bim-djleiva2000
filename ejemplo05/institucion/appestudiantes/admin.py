from django.contrib import admin

# Register your models here.
from appestudiantes.models import Estudiante, ciclo

admin.site.register(Estudiante)
admin.site.register(ciclo)
