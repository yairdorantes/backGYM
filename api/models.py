from django.db import models
from datetime import datetime


class Cliente(models.Model):
    nombre = models.CharField(
        max_length=100, verbose_name='Nombre', default="")
    apellido_p = models.CharField(
        max_length=150, verbose_name='Apellido paterno', default="")
    apellido_m = models.CharField(
        max_length=150, verbose_name='Apellido materno', default="")
    genero = models.CharField(
        max_length=100, verbose_name='Genero', default="")
    fecha_nacimiento = models.CharField(
        max_length=15, verbose_name='Fecha nacimiento', blank=True, null=True, default=None)
    direccion = models.CharField(
        max_length=150, verbose_name='Residencia', default="")
    telefono = models.IntegerField(verbose_name='Teléfono', default=0)
    correo = models.CharField(
        max_length=100, verbose_name='Correo', default="")
    estatura = models.FloatField(verbose_name='Estatura', default=0)
    peso = models.FloatField(verbose_name='Peso', default=0)
    enfermedades = models.CharField(
        max_length=250, verbose_name='Enfermedades', default="")
    alergias = models.CharField(
        max_length=200, verbose_name='Alergias', default="")
    dulces = models.BooleanField(default=False)
    hr_entrenamiento = models.CharField(max_length=10)
    hr_despertar = models.CharField(max_length=10)
    foto_actual = models.TextField(
        verbose_name="foto panza", default="", blank=True)
    hr_dormir = models.CharField(max_length=20)
    proteinas = models.CharField(
        max_length=700, verbose_name='Proteinas', default="")
    carbohidratos = models.CharField(
        max_length=700, verbose_name='Carbohidratos', default="")
    comidas = models.CharField(
        max_length=400, verbose_name='Comidas favoritas', default="", blank=True, null=True)
    objetivo = models.CharField(
        max_length=300, verbose_name='Objetivo(s)', blank=True, null=True, default=None)

    def __str__(self):

        return self.nombre
#    kakakak

# Create your models here.


class Pagos (models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True)
    servicio_contratado = models.CharField(
        max_length=60, verbose_name='Tipo de servicio contratado', default="")
    tipo_pago = models.CharField(max_length=150,   verbose_name='Tipo de pago')
    costo = models.IntegerField(verbose_name='Costo del servicio', default=0)
    # ficha_pago=
    aceptado = models.BooleanField(default=False, verbose_name='Aceptar?')

    def __str__(self):
        return self.cliente


class Seguimiento (models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True)
    estatura = models.FloatField(verbose_name='Estatura', default=0)
    peso = models.FloatField(verbose_name='Peso', default=0)
    # foto_actual=models.TextField(verbose_name)
    medidas = models.CharField(max_length=15, verbose_name='Medidas')
