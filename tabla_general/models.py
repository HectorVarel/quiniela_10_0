from django.db import models

# Create your models here.

class Jornadas(models.Model):
    nombre = models.CharField(max_length=25)
    j1 = models.IntegerField(default = 0)
    j2 = models.IntegerField(default = 0)
    j3 = models.IntegerField(default = 0)
    j4 = models.IntegerField(default = 0)
    j5 = models.IntegerField(default = 0)
    j6 = models.IntegerField(default = 0)
    j7 = models.IntegerField(default = 0)
    j8 = models.IntegerField(default = 0)
    j9 = models.IntegerField(default = 0)
    j10 = models.IntegerField(default = 0)
    j11 = models.IntegerField(default = 0)
    j12 = models.IntegerField(default = 0)
    j13 = models.IntegerField(default = 0)
    j14 = models.IntegerField(default = 0)
    j15 = models.IntegerField(default = 0)
    j16 = models.IntegerField(default = 0)
    j17 = models.IntegerField(default = 0)

    suma_j = models.IntegerField(blank=True, null=True)
    suma_j_c = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'Jornada'
        verbose_name_plural = 'Jornadas'
    def __str__(self):
        return self.nombre

class Equipos(models.Model):
    eq = models.CharField(max_length = 1000, default = 'EQUIPOS')
    j1 = models.CharField(max_length = 1000, default = 'X, X, X, X, X, X, X, X, X, X, X')
    j2 = models.CharField(max_length = 1000, default = 'X, X, X, X, X, X, X, X, X, X, X')
    j3 = models.CharField(max_length = 1000, default = 'X, X, X, X, X, X, X, X, X, X, X')
    j4 = models.CharField(max_length = 1000, default = 'X, X, X, X, X, X, X, X, X, X, X')
    j5 = models.CharField(max_length = 1000, default = 'X, X, X, X, X, X, X, X, X, X, X')
    j6 = models.CharField(max_length = 1000, default = 'X, X, X, X, X, X, X, X, X, X, X')
    j7 = models.CharField(max_length = 1000, default = 'X, X, X, X, X, X, X, X, X, X, X')
    j8 = models.CharField(max_length = 1000, default = 'X, X, X, X, X, X, X, X, X, X, X')
    j9 = models.CharField(max_length = 1000, default = 'X, X, X, X, X, X, X, X, X, X, X')
    j10 = models.CharField(max_length = 1000, default = 'X, X, X, X, X, X, X, X, X, X, X')
    j11 = models.CharField(max_length = 1000, default = 'X, X, X, X, X, X, X, X, X, X, X')
    j12 = models.CharField(max_length = 1000, default = 'X, X, X, X, X, X, X, X, X, X, X')
    j13 = models.CharField(max_length = 1000, default = 'X, X, X, X, X, X, X, X, X, X, X')
    j14 = models.CharField(max_length = 1000, default = 'X, X, X, X, X, X, X, X, X, X, X')
    j15 = models.CharField(max_length = 1000, default = 'X, X, X, X, X, X, X, X, X, X, X')
    j16 = models.CharField(max_length = 1000, default = 'X, X, X, X, X, X, X, X, X, X, X')
    j17 = models.CharField(max_length = 1000, default = 'X, X, X, X, X, X, X, X, X, X, X')

class Cartas(models.Model):
    nombre = models.CharField(max_length = 50)
    j1 = models.CharField(max_length = 10, default = 'NC')
    j2 = models.CharField(max_length = 10, default = 'NC')
    j3 = models.CharField(max_length = 10, default = 'NC')
    j4 = models.CharField(max_length = 10, default = 'NC')
    j5 = models.CharField(max_length = 10, default = 'NC')
    j6 = models.CharField(max_length = 10, default = 'NC')
    j7 = models.CharField(max_length = 10, default = 'NC')
    j8 = models.CharField(max_length = 10, default = 'NC')
    j9 = models.CharField(max_length = 10, default = 'NC')
    j10 = models.CharField(max_length = 10, default = 'NC')
    j11 = models.CharField(max_length = 10, default = 'NC')
    j12 = models.CharField(max_length = 10, default = 'NC')
    j13 = models.CharField(max_length = 10, default = 'NC')
    j14 = models.CharField(max_length = 10, default = 'NC')
    j15 = models.CharField(max_length = 10, default = 'NC')
    j16 = models.CharField(max_length = 10, default = 'NC')
    j17 = models.CharField(max_length = 10, default = 'NC')

    def __str__(self):
        return self.nombre

class Puntos_extra(models.Model):
    nombre = models.CharField(max_length=25)
    j1 = models.IntegerField(default = 0)
    j2 = models.IntegerField(default = 0)
    j3 = models.IntegerField(default = 0)
    j4 = models.IntegerField(default = 0)
    j5 = models.IntegerField(default = 0)
    j6 = models.IntegerField(default = 0)
    j7 = models.IntegerField(default = 0)
    j8 = models.IntegerField(default = 0)
    j9 = models.IntegerField(default = 0)
    j10 = models.IntegerField(default = 0)
    j11 = models.IntegerField(default = 0)
    j12 = models.IntegerField(default = 0)
    j13 = models.IntegerField(default = 0)
    j14 = models.IntegerField(default = 0)
    j15 = models.IntegerField(default = 0)
    j16 = models.IntegerField(default = 0)
    j17 = models.IntegerField(default = 0)
    def __str__(self):
        return self.nombre

class Colores(models.Model):
    nombre = models.CharField(max_length = 50)
    j1 = models.CharField(max_length = 500, default = 'lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon')
    j2 = models.CharField(max_length = 500, default = 'lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon')
    j3 = models.CharField(max_length = 500, default = 'lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon')
    j4 = models.CharField(max_length = 500, default = 'lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon')
    j5 = models.CharField(max_length = 500, default = 'lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon')
    j6 = models.CharField(max_length = 500, default = 'lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon')
    j7 = models.CharField(max_length = 500, default = 'lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon')
    j8 = models.CharField(max_length = 500, default = 'lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon')
    j9 = models.CharField(max_length = 500, default = 'lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon')
    j10 = models.CharField(max_length = 500, default = 'lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon')
    j11 = models.CharField(max_length = 500, default = 'lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon')
    j12 = models.CharField(max_length = 500, default = 'lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon')
    j13 = models.CharField(max_length = 500, default = 'lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon')
    j14 = models.CharField(max_length = 500, default = 'lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon')
    j15 = models.CharField(max_length = 500, default = 'lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon')
    j16 = models.CharField(max_length = 500, default = 'lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon')
    j17 = models.CharField(max_length = 500, default = 'lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon, lightsalmon')
    def __str__(self):
        return self.nombre
class Cartas_aux(models.Model):
    nombre = models.CharField(max_length = 50)
    j1 = models.CharField(max_length = 100, default = 'NA')
    j2 = models.CharField(max_length = 100, default = 'NA')
    j3 = models.CharField(max_length = 100, default = 'NA')
    j4 = models.CharField(max_length = 100, default = 'NA')
    j5 = models.CharField(max_length = 100, default = 'NA')
    j6 = models.CharField(max_length = 100, default = 'NA')
    j7 = models.CharField(max_length = 100, default = 'NA')
    j8 = models.CharField(max_length = 100, default = 'NA')
    j9 = models.CharField(max_length = 100, default = 'NA')
    j10 = models.CharField(max_length = 100, default = 'NA')
    j11 = models.CharField(max_length = 100, default = 'NA')
    j12 = models.CharField(max_length = 100, default = 'NA')
    j13 = models.CharField(max_length = 100, default = 'NA')
    j14 = models.CharField(max_length = 100, default = 'NA')
    j15 = models.CharField(max_length = 100, default = 'NA')
    j16 = models.CharField(max_length = 100, default = 'NA')
    j17 = models.CharField(max_length = 100, default = 'NA')
    def __str__(self):
        return self.nombre
    
class jugadores_gol(models.Model):
    j1 = models.CharField(max_length = 1000, default = 'NA')
    j2 = models.CharField(max_length = 1000, default = 'NA')
    j3 = models.CharField(max_length = 1000, default = 'NA')
    j4 = models.CharField(max_length = 1000, default = 'NA')
    j5 = models.CharField(max_length = 1000, default = 'NA')
    j6 = models.CharField(max_length = 1000, default = 'NA')
    j7 = models.CharField(max_length = 1000, default = 'NA')
    j8 = models.CharField(max_length = 1000, default = 'NA')
    j9 = models.CharField(max_length = 1000, default = 'NA')
    j10 = models.CharField(max_length = 1000, default = 'NA')
    j11 = models.CharField(max_length = 1000, default = 'NA')
    j12 = models.CharField(max_length = 1000, default = 'NA')
    j13 = models.CharField(max_length = 1000, default = 'NA')
    j14 = models.CharField(max_length = 1000, default = 'NA')
    j15 = models.CharField(max_length = 1000, default = 'NA')
    j16 = models.CharField(max_length = 1000, default = 'NA')
    j17 = models.CharField(max_length = 1000, default = 'NA')

class Num_quiniela(models.Model):
    num_jor = models.CharField(max_length = 10)

class Puntos_cartas(models.Model):
    nombre = models.CharField(max_length=25)
    j1 = models.IntegerField(default = 0)
    j2 = models.IntegerField(default = 0)
    j3 = models.IntegerField(default = 0)
    j4 = models.IntegerField(default = 0)
    j5 = models.IntegerField(default = 0)
    j6 = models.IntegerField(default = 0)
    j7 = models.IntegerField(default = 0)
    j8 = models.IntegerField(default = 0)
    j9 = models.IntegerField(default = 0)
    j10 = models.IntegerField(default = 0)
    j11 = models.IntegerField(default = 0)
    j12 = models.IntegerField(default = 0)
    j13 = models.IntegerField(default = 0)
    j14 = models.IntegerField(default = 0)
    j15 = models.IntegerField(default = 0)
    j16 = models.IntegerField(default = 0)
    j17 = models.IntegerField(default = 0)
    def __str__(self):
        return self.nombre

class tiempo(models.Model):
    j1 = models.CharField(max_length = 1000, default = 'NA')
    j2 = models.CharField(max_length = 1000, default = 'NA')
    j3 = models.CharField(max_length = 1000, default = 'NA')
    j4 = models.CharField(max_length = 1000, default = 'NA')
    j5 = models.CharField(max_length = 1000, default = 'NA')
    j6 = models.CharField(max_length = 1000, default = 'NA')
    j7 = models.CharField(max_length = 1000, default = 'NA')
    j8 = models.CharField(max_length = 1000, default = 'NA')
    j9 = models.CharField(max_length = 1000, default = 'NA')
    j10 = models.CharField(max_length = 1000, default = 'NA')
    j11 = models.CharField(max_length = 1000, default = 'NA')
    j12 = models.CharField(max_length = 1000, default = 'NA')
    j13 = models.CharField(max_length = 1000, default = 'NA')
    j14 = models.CharField(max_length = 1000, default = 'NA')
    j15 = models.CharField(max_length = 1000, default = 'NA')
    j16 = models.CharField(max_length = 1000, default = 'NA')
    j17 = models.CharField(max_length = 1000, default = 'NA')