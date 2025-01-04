from django.db import models

# Create your models here.

class ResultadoPartido(models.Model):
    equipo1 = models.CharField(max_length=100)
    equipo2 = models.CharField(max_length=100)
    resultado = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'ResultadoPartido'
        verbose_name_plural = 'ResultadoPartidos'
    def __str__(self):
        return self.equipo1

class EquiposPartidos(models.Model):
    j = models.IntegerField()
    eq1 = models.CharField(max_length=100, default = 'Equipo')
    eq2 = models.CharField(max_length=100, default = 'Equipo')
    eq3 = models.CharField(max_length=100, default = 'Equipo')
    eq4 = models.CharField(max_length=100, default = 'Equipo')
    eq5 = models.CharField(max_length=100, default = 'Equipo')
    eq6 = models.CharField(max_length=100, default = 'Equipo')
    eq7 = models.CharField(max_length=100, default = 'Equipo')
    eq8 = models.CharField(max_length=100, default = 'Equipo')
    eq9 = models.CharField(max_length=100, default = 'Equipo')
    eq10 = models.CharField(max_length=100, default = 'Equipo')
    eq11 = models.CharField(max_length=100, default = 'Equipo')
    eq12 = models.CharField(max_length=100, default = 'Equipo')
    eq13 = models.CharField(max_length=100, default = 'Equipo')
    eq14 = models.CharField(max_length=100, default = 'Equipo')
    eq15 = models.CharField(max_length=100, default = 'Equipo')
    eq16 = models.CharField(max_length=100, default = 'Equipo')
    eq17 = models.CharField(max_length=100, default = 'Equipo')
    eq18 = models.CharField(max_length=100, default = 'Equipo')
    eq19 = models.CharField(max_length=100, default = 'Equipo')
    eq20 = models.CharField(max_length=100, default = 'Equipo')
    eq21 = models.CharField(max_length=100, default = 'Equipo')
    eq22 = models.CharField(max_length=100, default = 'Equipo')

    class Meta:
        verbose_name = 'EquiposPartidos'
        verbose_name_plural = 'EquiposPartidos'
    def __str__(self):
        return self.eq1

class Prediccion(models.Model):
    nombre = models.CharField(max_length=255)
    pJ1 = models.CharField(max_length=255, default = 'X, X, X, X, X, X, X, X, X, X, X')
    pJ2 = models.CharField(max_length=255, default = 'X, X, X, X, X, X, X, X, X, X, X')
    pJ3 = models.CharField(max_length=255, default = 'X, X, X, X, X, X, X, X, X, X, X')
    pJ4 = models.CharField(max_length=255, default = 'X, X, X, X, X, X, X, X, X, X, X')
    pJ5 = models.CharField(max_length=255, default = 'X, X, X, X, X, X, X, X, X, X, X')
    pJ6 = models.CharField(max_length=255, default = 'X, X, X, X, X, X, X, X, X, X, X')
    pJ7 = models.CharField(max_length=255, default = 'X, X, X, X, X, X, X, X, X, X, X')
    pJ8 = models.CharField(max_length=255, default = 'X, X, X, X, X, X, X, X, X, X, X')
    pJ9 = models.CharField(max_length=255, default = 'X, X, X, X, X, X, X, X, X, X, X')
    pJ10 = models.CharField(max_length=255, default = 'X, X, X, X, X, X, X, X, X, X, X')
    pJ11 = models.CharField(max_length=255, default = 'X, X, X, X, X, X, X, X, X, X, X')
    pJ12 = models.CharField(max_length=255, default = 'X, X, X, X, X, X, X, X, X, X, X')
    pJ13 = models.CharField(max_length=255, default = 'X, X, X, X, X, X, X, X, X, X, X')
    pJ14 = models.CharField(max_length=255, default = 'X, X, X, X, X, X, X, X, X, X, X')
    pJ15 = models.CharField(max_length=255, default = 'X, X, X, X, X, X, X, X, X, X, X')
    pJ16 = models.CharField(max_length=255, default = 'X, X, X, X, X, X, X, X, X, X, X')
    pJ17 = models.CharField(max_length=255, default = 'X, X, X, X, X, X, X, X, X, X, X')

    def __str__(self):
        return self.nombre

class Fotos_quiniela(models.Model):
    j1 = models.TextField(max_length = 1000000, default = 'NC')
    j2 = models.TextField(max_length = 1000000, default = 'NC')
    j3 = models.TextField(max_length = 1000000, default = 'NC')
    j4 = models.TextField(max_length = 1000000, default = 'NC')
    j5 = models.TextField(max_length = 1000000, default = 'NC')
    j6 = models.TextField(max_length = 1000000, default = 'NC')
    j7 = models.TextField(max_length = 1000000, default = 'NC')
    j8 = models.TextField(max_length = 1000000, default = 'NC')
    j9 = models.TextField(max_length = 1000000, default = 'NC')
    j10 = models.TextField(max_length = 1000000, default = 'NC')
    j11 = models.TextField(max_length = 1000000, default = 'NC')
    j12 = models.TextField(max_length = 1000000, default = 'NC')
    j13 = models.TextField(max_length = 1000000, default = 'NC')
    j14 = models.TextField(max_length = 1000000, default = 'NC')
    j15 = models.TextField(max_length = 1000000, default = 'NC')
    j16 = models.TextField(max_length = 1000000, default = 'NC')
    j17 = models.TextField(max_length = 1000000, default = 'NC')

class Estadisticas(models.Model):
    j1 = models.TextField(max_length = 1000000, default = 'NC')
    j2 = models.TextField(max_length = 1000000, default = 'NC')
    j3 = models.TextField(max_length = 1000000, default = 'NC')
    j4 = models.TextField(max_length = 1000000, default = 'NC')
    j5 = models.TextField(max_length = 1000000, default = 'NC')
    j6 = models.TextField(max_length = 1000000, default = 'NC')
    j7 = models.TextField(max_length = 1000000, default = 'NC')
    j8 = models.TextField(max_length = 1000000, default = 'NC')
    j9 = models.TextField(max_length = 1000000, default = 'NC')
    j10 = models.TextField(max_length = 1000000, default = 'NC')
    j11 = models.TextField(max_length = 1000000, default = 'NC')
    j12 = models.TextField(max_length = 1000000, default = 'NC')
    j13 = models.TextField(max_length = 1000000, default = 'NC')
    j14 = models.TextField(max_length = 1000000, default = 'NC')
    j15 = models.TextField(max_length = 1000000, default = 'NC')
    j16 = models.TextField(max_length = 1000000, default = 'NC')
    j17 = models.TextField(max_length = 1000000, default = 'NC')

class Momios(models.Model):
    j1 = models.TextField(max_length = 1000000, default = 'NC')
    j2 = models.TextField(max_length = 1000000, default = 'NC')
    j3 = models.TextField(max_length = 1000000, default = 'NC')
    j4 = models.TextField(max_length = 1000000, default = 'NC')
    j5 = models.TextField(max_length = 1000000, default = 'NC')
    j6 = models.TextField(max_length = 1000000, default = 'NC')
    j7 = models.TextField(max_length = 1000000, default = 'NC')
    j8 = models.TextField(max_length = 1000000, default = 'NC')
    j9 = models.TextField(max_length = 1000000, default = 'NC')
    j10 = models.TextField(max_length = 1000000, default = 'NC')
    j11 = models.TextField(max_length = 1000000, default = 'NC')
    j12 = models.TextField(max_length = 1000000, default = 'NC')
    j13 = models.TextField(max_length = 1000000, default = 'NC')
    j14 = models.TextField(max_length = 1000000, default = 'NC')
    j15 = models.TextField(max_length = 1000000, default = 'NC')
    j16 = models.TextField(max_length = 1000000, default = 'NC')
    j17 = models.TextField(max_length = 1000000, default = 'NC')

class imagenes_cartas(models.Model):
    M = models.TextField(max_length = 1000000, default = 'NC')
    DQ = models.TextField(max_length = 1000000, default = 'NC')
    OD = models.TextField(max_length = 1000000, default = 'NC')
    OT = models.TextField(max_length = 1000000, default = 'NC')
    MA = models.TextField(max_length = 1000000, default = 'NC')
    IQ = models.TextField(max_length = 1000000, default = 'NC')
    J = models.TextField(max_length = 1000000, default = 'NC')
    NC = models.TextField(max_length = 1000000, default = 'NC')
    RC = models.TextField(max_length = 1000000, default = 'NC')
    T = models.TextField(max_length = 1000000, default = 'NC')
    E = models.TextField(max_length = 1000000, default = 'NC')

class Equipos_gol(models.Model):
    nombre = models.CharField(max_length=255)
    atlas = models.CharField(max_length = 1, default='1')
    america = models.CharField(max_length = 1, default='1')
    chivas = models.CharField(max_length = 1, default='1')
    cruz_azul = models.CharField(max_length = 1, default='1')
    tijuana = models.CharField(max_length = 1, default='1')
    puebla = models.CharField(max_length = 1, default='1')
    queretaro = models.CharField(max_length = 1, default='1')
    pumas = models.CharField(max_length = 1, default='1')
    toluca = models.CharField(max_length = 1, default='1')
    santos = models.CharField(max_length = 1, default='1')
    monterrey = models.CharField(max_length = 1, default='1')
    tigres = models.CharField(max_length = 1, default='1')
    mazatlan = models.CharField(max_length = 1, default='1')
    necaxa = models.CharField(max_length = 1, default='1')
    san_luis = models.CharField(max_length = 1, default='1')
    leon = models.CharField(max_length = 1, default='1')
    juarez = models.CharField(max_length = 1, default='1')
    pachuca = models.CharField(max_length = 1, default='1')

    def __str__(self):
        return self.nombre

class Equipos_tiempo(models.Model):
    nombre = models.CharField(max_length=255)
    atlas = models.CharField(max_length = 1, default='1')
    america = models.CharField(max_length = 1, default='1')
    chivas = models.CharField(max_length = 1, default='1')
    cruz_azul = models.CharField(max_length = 1, default='1')
    tijuana = models.CharField(max_length = 1, default='1')
    puebla = models.CharField(max_length = 1, default='1')
    queretaro = models.CharField(max_length = 1, default='1')
    pumas = models.CharField(max_length = 1, default='1')
    toluca = models.CharField(max_length = 1, default='1')
    santos = models.CharField(max_length = 1, default='1')
    monterrey = models.CharField(max_length = 1, default='1')
    tigres = models.CharField(max_length = 1, default='1')
    mazatlan = models.CharField(max_length = 1, default='1')
    necaxa = models.CharField(max_length = 1, default='1')
    san_luis = models.CharField(max_length = 1, default='1')
    leon = models.CharField(max_length = 1, default='1')
    juarez = models.CharField(max_length = 1, default='1')
    pachuca = models.CharField(max_length = 1, default='1')

    def __str__(self):
        return self.nombre

class Equipos_fotos(models.Model):
    nombre = models.TextField(max_length = 1000000, default = 'NC')
    atlas = models.TextField(max_length = 1000000, default = 'NC')
    america = models.TextField(max_length = 1000000, default = 'NC')
    chivas = models.TextField(max_length = 1000000, default = 'NC')
    cruz_azul = models.TextField(max_length = 1000000, default = 'NC')
    tijuana = models.TextField(max_length = 1000000, default = 'NC')
    puebla = models.TextField(max_length = 1000000, default = 'NC')
    queretaro = models.TextField(max_length = 1000000, default = 'NC')
    pumas = models.TextField(max_length = 1000000, default = 'NC')
    toluca = models.TextField(max_length = 1000000, default = 'NC')
    santos = models.TextField(max_length = 1000000, default = 'NC')
    monterrey = models.TextField(max_length = 1000000, default = 'NC')
    tigres = models.TextField(max_length = 1000000, default = 'NC')
    mazatlan = models.TextField(max_length = 1000000, default = 'NC')
    necaxa = models.TextField(max_length = 1000000, default = 'NC')
    san_luis = models.TextField(max_length = 1000000, default = 'NC')
    leon = models.TextField(max_length = 1000000, default = 'NC')
    juarez = models.TextField(max_length = 1000000, default = 'NC')
    pachuca = models.TextField(max_length = 1000000, default = 'NC')
    inter = models.TextField(max_length = 1000000, default = 'NC')

    def __str__(self):
        return self.nombre

class Juegos_pendientes(models.Model):
    j1 = models.TextField(max_length = 1000000, default = 'NC')
    j2 = models.TextField(max_length = 1000000, default = 'NC')
    j3 = models.TextField(max_length = 1000000, default = 'NC')
    j4 = models.TextField(max_length = 1000000, default = 'NC')
    j5 = models.TextField(max_length = 1000000, default = 'NC')
    j6 = models.TextField(max_length = 1000000, default = 'NC')
    j7 = models.TextField(max_length = 1000000, default = 'NC')
    j8 = models.TextField(max_length = 1000000, default = 'NC')
    j9 = models.TextField(max_length = 1000000, default = 'NC')
    j10 = models.TextField(max_length = 1000000, default = 'NC')
    j11 = models.TextField(max_length = 1000000, default = 'NC')
    j12 = models.TextField(max_length = 1000000, default = 'NC')
    j13 = models.TextField(max_length = 1000000, default = 'NC')
    j14 = models.TextField(max_length = 1000000, default = 'NC')
    j15 = models.TextField(max_length = 1000000, default = 'NC')
    j16 = models.TextField(max_length = 1000000, default = 'NC')
    j17 = models.TextField(max_length = 1000000, default = 'NC')