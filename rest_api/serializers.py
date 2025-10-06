from rest_framework import serializers
from foro.models import *

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hilo
        fields = ['idHilo','tituloHilo', 'cuerpoHilo', 'autorHilo', 'puntosHilo']