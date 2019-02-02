from django.contrib import admin

from .models import Categoria, Usuario, Imagen, Audio, Video, Clip

admin.site.register(Categoria)
admin.site.register(Usuario)
admin.site.register(Imagen)
admin.site.register(Audio)
admin.site.register(Video)
admin.site.register(Clip)


