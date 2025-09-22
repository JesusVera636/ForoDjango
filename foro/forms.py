from django import forms
from django.forms import ModelForm
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class UserForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Ingrese la Contraseña'}))
    password2 = forms.CharField(label='Confirmar Contraseña',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirme la Contraseña'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Primer Nombre'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Apellido'}),
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre de Usuario'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Correo Electronico'}),
        }

        labels={
            'first_name':'Primer Nombre',
            'last_name':'Apellido',
            'username':'Usuario',
            'email':'Correo',
        }

class PostForm(ModelForm):

    class Meta:
        model = Hilo
        fields = ['tituloHilo', 'cuerpoHilo', 'autorHilo', 'puntosHilo']

        widgets = {
            'tituloHilo':forms.TextInput(attrs={'class':'form-control','placeholder':'Dame un Titulo'}),
            'cuerpoHilo':forms.TextInput(attrs={'class':'form-control','placeholder':'El Cuerpo está Aqui'}),
        }

        labels={
            'tituloHilo':'Titulo',
            'cuerpoHilo':'Cuerpo',
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comentario
        fields = ['cuerpoComentario', 'autorComentario', 'padreComentario']

        widgets = {
            'cuerpoComentario':forms.TextInput(attrs={'class':'form-control','placeholder':'Deja tu Opinion'}),
        }
