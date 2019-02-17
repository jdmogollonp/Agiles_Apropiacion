from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Imagen, Audio, Video, Clip
import json
from django.core import serializers
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


@csrf_exempt
def index(request):
    lstImagen = list(Imagen.objects.all())
    lstAudio = list(Audio.objects.all())
    lstVideo = list(Video.objects.all())
    allObjects = lstImagen + lstAudio + lstVideo
    print(lstImagen)
    return HttpResponse(serializers.serialize('json', allObjects))


@csrf_exempt
def viewImages(request):
    return render(request, "lista_galeria.html")


@csrf_exempt
@login_required(login_url='/galeria/login_user/')
def detalle(request, tipo, idbd):
    iUrl = None
    if tipo == settings.IMAGEN:
        multimedia = get_object_or_404(Imagen, id=idbd)
        iUrl = multimedia.contenido.url

    if tipo == settings.VIDEO:
        multimedia = get_object_or_404(Video, id=idbd)
        iUrl=multimedia.contenido.url
        cont = multimedia.contenido

    if tipo == settings.AUDIO:
        multimedia = get_object_or_404(Audio, id=idbd)
        iUrl = multimedia.contenido.url

    titulo = multimedia.titulo
    autor = multimedia.autor
    fecha_creacion = multimedia.fecha_creacion.strftime("%d/%m/%Y %H:%M")
    categoria = multimedia.categoria
    usuario = multimedia.usuario
    ciudad = multimedia.ciudad
    pais = multimedia.pais


    clips = None
    if tipo == "audio" or tipo == "video" :
        clips = Clip.objects.filter(referencia = idbd)
    
    context = {'tipo': tipo, 'titulo': titulo, 'autor': autor, 'fecha_creacion': fecha_creacion, 'categoria': categoria,
             'usuario':usuario,'ciudad':ciudad,'pais':pais,'iUrl':iUrl, 'clips': clips, 'idbd': idbd}

    return render(request, 'detalle.html', context)


@login_required(login_url='/galeria/login_user/')
def agregarClip(request, tipo, idbd):
    reproducible = None
    if tipo == settings.VIDEO:
        reproducible = get_object_or_404(Video, id=idbd)
    elif tipo == settings.AUDIO:
        reproducible = get_object_or_404(Audio, id=idbd)
    else:
        return HttpResponseBadRequest('No se puede agregar un clip a una imagen')
    if request.method == 'POST':
        inicio = request.POST['inicio']
        fin = request.POST['fin']
        nombre = request.POST['nombre']
        clip = Clip(nombre=nombre, segundo_inicio=inicio, segundo_fin=fin, referencia=reproducible)
        clip.save()
        return HttpResponseRedirect(reverse('detalleGal', args=(tipo,idbd)))


@csrf_exempt
def registrar_usuario(request):
    return render(request, 'registrarUsuario.html')


@csrf_exempt
@login_required(login_url='/galeria/login_user/')
def editar_usuario(request, id):
    if id != request.user.id:
        logout(request)
        return redirect("/")
    user = get_object_or_404(User, id=id)
    context = {'id': id, 'nombre': user.first_name, 'apellido': user.last_name, 'correo_electronico': user.email}
    return render(request, 'registrarUsuario.html', context)


@csrf_exempt
def agregar_usuario(request):
    if request.method == 'POST':
        jsonUser = json.load(request)
        id = jsonUser['id']

        if id == '':
            nombre_usuario = jsonUser['nombre_usuario']

        nombre = jsonUser['nombre']
        apellido = jsonUser['apellido']
        contraseña = jsonUser['contraseña']
        correo_electronico = jsonUser['correo_electronico']

        print('este es el id:' + str(id))

        if id:
            user_model = get_object_or_404(User, id=id)
            user_model.set_password(contraseña)
        else:
            user_model = User.objects.create_user(username=nombre_usuario, password=contraseña)

        user_model.first_name = nombre
        user_model.last_name = apellido
        user_model.email = correo_electronico
        user_model.save()
    return HttpResponse(serializers.serialize('json', [user_model]))


@csrf_exempt
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
