from django.shortcuts import render
from .models import Imagen, Audio, Video
import json
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    lstImagen = Imagen.objects.all()
    lstAudio = Audio.objects.all()
    lstVideo = Video.objects.all()
    print('*********************************************************')
    print(lstImagen)
    return render(request, 'lista_galeria.html', context={'lstImagen': lstImagen, 'lstAudio': lstAudio, 'lstVideo': lstVideo})


@csrf_exempt
def registrar_usuario(request):
    return render(request, 'registrarUsuario.html')


@csrf_exempt
def agregar_usuario(request):
    if request.method == 'POST':
        jsonUser = json.load(request)
        nombre_usuario = jsonUser['nombre_usuario']
        nombre = jsonUser['nombre']
        apellido = jsonUser['apellido']
        contraseña = jsonUser['contraseña']
        correo_electronico = jsonUser['correo_electronico']

        user_model = User.objects.create_user(username=nombre_usuario, password=contraseña)
        user_model.first_name = nombre
        user_model.last_name = apellido
        user_model.email = correo_electronico
        user_model.save()
    return HttpResponse(serializers.serialize('json', [user_model]))
