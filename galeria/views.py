from django.shortcuts import render
from django.http import HttpResponse
from .models import Imagen, Audio, Video
# Create your views here.
def index(request):
    lstImagen = Imagen.objects.all()
    lstAudio = Audio.objects.all()
    lstVideo = Video.objects.all()
    print('*********************************************************')
    print(lstImagen)
    return render(request, 'lista_galeria.html', context={'lstImagen': lstImagen, 'lstAudio': lstAudio, 'lstVideo': lstVideo})