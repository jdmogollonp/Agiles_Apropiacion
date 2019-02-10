from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Imagen, Audio, Video
import json
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse


@login_required(login_url='/galeria/login_user/')
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


def login_user(request):
    return render(request, "login.html")


@csrf_exempt
def logout_view(request):
    logout(request)
    return redirect("/")


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        jsonUser = json.loads(request.body)
        username = jsonUser['username']
        password = jsonUser['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            message = "ok"
        else:
            message = 'Nombre de usuario o password incorrectos'
        return JsonResponse({"message": message})
