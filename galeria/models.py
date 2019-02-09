from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .validators import validar_imagen
from .validators import validar_audio
from .validators import validar_video

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

# TODO: Incorporar a los usuarios de Django
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    pais = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=20)
    categorias_favoritas = models.ManyToManyField(Categoria)
    foto = models.ImageField(upload_to='archivos/fotos_usuarios')

    def __str__(self):
        return self.usuario.username


@receiver(post_save, sender=User)
def crear_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)


@receiver(post_save, sender=User)
def guardar_perfil(sender, instance, **kwargs):
    instance.perfil.save()


class Multimedia(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField('fecha creacion')
    ciudad = models.CharField(max_length=20)
    pais = models.CharField(max_length=20)
    categoria = models.ForeignKey(Categoria, null=True, on_delete=models.SET_NULL)
    usuario = models.ForeignKey(Perfil, null=True, on_delete=models.SET_NULL)

    class Meta:
        abstract = True


class Imagen(Multimedia):
    contenido = models.FileField(blank=True, null=True, upload_to='imagenes/%Y%m%D/', validators=[validar_imagen])

    def __str__(self):
        return self.titulo #+ '(' + self.fecha_creacion + ')'


class Reproducible(Multimedia):
    pass


class Audio(Reproducible):
    contenido = models.FileField(upload_to='audios/%Y%m%D/', validators=[validar_audio])

    def __str__(self):
        return self.titulo #+ '(' + self.fecha_creacion + ')'


class Video(Reproducible):
    contenido = models.FileField(upload_to='videos/%Y%m%D/', validators=[validar_video])

    def __str__(self):
        return self.titulo #+ '(' + self.fecha_creacion + ')'


class Clip(models.Model):
    nombre = models.CharField(max_length=50)
    segundo_inicio = models.IntegerField(blank=True, null=True)
    segundo_fin = models.IntegerField(blank=True, null=True)
    referencia = models.ForeignKey(Reproducible, on_delete=models.CASCADE)




