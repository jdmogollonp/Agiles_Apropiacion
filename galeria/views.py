from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Imagen, Audio, Video
from django.conf import settings

# Create your views here.
def index(request):
    lstImagen = Imagen.objects.all()
    lstAudio = Audio.objects.all()
    lstVideo = Video.objects.all()
    print('*********************************************************')
    print(lstImagen)
    return render(request, 'lista_galeria.html', context={'lstImagen': lstImagen, 'lstAudio': lstAudio, 'lstVideo': lstVideo})


def detalle(request, tipo, idbd):
    if tipo==settings.IMAGEN:
        multimedia=get_object_or_404(Imagen,id=idbd)
        imagenUrl=multimedia.contenido.url
        print('contenido')
        print(multimedia.contenido)

    if tipo==settings.VIDEO:
        multimedia=get_object_or_404(Video,id=idbd)

    if tipo==settings.AUDIO:
        multimedia=get_object_or_404(Audio,id=idbd)
        audioUrl=multimedia.contenido.url

    titulo=multimedia.titulo
    autor=multimedia.autor
    fecha_creacion=multimedia.fecha_creacion.strftime("%d/%m/%Y %H:%M")
    categoria=multimedia.categoria
    usuario=multimedia.usuario
    ciudad=multimedia.ciudad
    pais=multimedia.pais

    context={'tipo':tipo,'titulo':titulo,'autor':autor,'fecha_creacion':fecha_creacion,'categoria':categoria,
             'usuario':usuario,'ciudad':ciudad,'pais':pais,'imagenUrl':imagenUrl,'audioUrl':audioUrl}

    return render(request, 'detalle.html',context)
