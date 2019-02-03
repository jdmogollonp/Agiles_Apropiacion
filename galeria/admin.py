from django.contrib import admin

from .models import Categoria, Perfil, Imagen, Audio, Video, Clip

admin.site.register(Categoria)
admin.site.register(Perfil)
admin.site.register(Imagen)
admin.site.register(Audio)
admin.site.register(Video)
admin.site.register(Clip)


