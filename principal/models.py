from django.db import models

# Create your models here.
class Fotos_portada(models.Model):
    podium = models.TextField(max_length = 1000000, default = 'NC')
    historico = models.TextField(max_length = 1000000, default = 'NC')
    descenso = models.TextField(max_length = 1000000, default = 'NC')