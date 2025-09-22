from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('login', login, name="login"),
    path('post/<id>', post, name="post"),
    path('register', register, name="register"),
    path('nuevo_post', nuevo_post, name="nuevo_post"),
    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),
    path('puntuacion/<id>/<type>', puntuacion, name="puntuacion"),
    path('borrar_post/<id>', borrar_post, name="borrar_post")
]