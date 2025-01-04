from django.contrib import admin
from .models import Jornadas, Equipos, Cartas, Puntos_extra, Colores, Cartas_aux, jugadores_gol, Num_quiniela, Puntos_cartas, tiempo
# Register your models here.

admin.site.register(Jornadas)
admin.site.register(Equipos)
admin.site.register(Cartas)
admin.site.register(Puntos_extra)
admin.site.register(Colores)
admin.site.register(Cartas_aux)
admin.site.register(jugadores_gol)
admin.site.register(Num_quiniela)
admin.site.register(Puntos_cartas)
admin.site.register(tiempo)