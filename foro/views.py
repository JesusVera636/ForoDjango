from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.db.models import Max
from .forms import *

# Create your views here.

def home(request):
    posts = Hilo.objects.all()
    postDia = Hilo.objects.latest('puntosHilo')

    datos = {
        'posts': posts,
        'postDia': postDia
    }
    return render(request, 'foro/home.html', datos)

@login_required(login_url='login')
def post(request, id):
    post = Hilo.objects.get(idHilo=id)
    comentarios = Comentario.objects.all().filter(padreComentario=id)
    puntos = PostForm(instance=post)
    datos = {
        'form' : CommentForm(),
        'post': post,
        'puntos': puntos,
        'comentarios': comentarios
    }

    if request.method == 'POST':
        formulario = CommentForm(request.POST)

        if formulario.is_valid():
            formulario.save()

    return render(request, 'foro/post.html', datos)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(to="home")
    else:
        form = AuthenticationForm()
    return render(request, 'foro/login.html', {"form": form})

@login_required(login_url='login')
def nuevo_post(request):
    datos = {
        'form': PostForm()
    }
    if request.method == 'POST':
        formulario = PostForm(request.POST)
    
        if formulario.is_valid():
            formulario.save()
            formulario.puntosHilo = 0
            datos['mensaje'] = "Guardado correctamente"

    
    return render(request, 'foro/nuevo_post.html', datos)

def register(request):
    datos = {
        'form': UserForm()
    }
    
    if request.method == 'POST':
        formulario = UserForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Guardado correctamente"
            
            
    return render(request, 'foro/register.html', datos)

@login_required(login_url='login')
def puntuacion(request, id, type):
    post = Hilo.objects.get(idHilo=id)
    puntos = post.puntosHilo
    
    if type == 'menos':
        post.puntosHilo = puntos - 1
    else:
        post.puntosHilo = puntos + 1

    post.save()

    return redirect("/post/" + id)

@login_required(login_url='login')
def borrar_post(request, id):
    post = Hilo.objects.get(idHilo=id)
    post.delete()

    return redirect(to="home")

def cerrar_sesion(request):
    logout(request)
    return redirect(to="home")