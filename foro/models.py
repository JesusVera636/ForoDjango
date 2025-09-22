from django.conf import settings
from django.db import models

# Create your models here.

class Hilo(models.Model):
    idHilo = models.AutoField(primary_key=True, verbose_name="Id del Hilo")
    tituloHilo = models.CharField(max_length=25, verbose_name="Titulo del Hilo")
    cuerpoHilo = models.CharField(max_length=255, verbose_name="Cuerpo del Hilo")
    puntosHilo = models.IntegerField(verbose_name="Puntuacion Hilo")
    autorHilo = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Comentario(models.Model):
    idComentario = models.AutoField(primary_key=True, verbose_name="Id del Comentario")
    cuerpoComentario = models.CharField(max_length=150, verbose_name="Cuerpo del Comentario")
    autorComentario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    padreComentario = models.ForeignKey(Hilo, on_delete=models.CASCADE)
