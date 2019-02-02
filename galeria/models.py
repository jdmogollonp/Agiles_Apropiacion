from django.db import models


class Categoria(models.model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    nombres = models.CharField(max_length=50)
    appellidos = models.CharField(max_length=50)
    pais = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=20)
    correo = models.CharField(max_length=50)
    autenticado = models.BooleanField()
    categoria_favorita = models.ForeignKey(Categoria, on_delete=models.SET_NULL())
    foto = models.ImageField(upload_to='archivos/fotos_usuarios/')

    def __str__(self):
        return 'Usuario: ' + self.nombres + ' ' + self.appellidos


class Multimedia(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField('fecha creacion')
    ciudad = models.CharField(max_length=20)
    pais = models.CharField(max_length=20)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL())
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL())

    class Meta:
        abstract = True


class Imagen(Multimedia):
    contenido: models.ImageField(upload_to='archivos/imagenes/')

    def __str__(self):
        return 'Imagen: ' + self.titulo + '(' + self.fecha_creacion + ')'

class Reproducible(Multimedia):
    pass

class Audio(Reproducible):
    contenido = models.FileField(upload_to='archivos/audios/')

    def __str__(self):
        return 'Audio: ' + self.titulo + '(' + self.fecha_creacion + ')'


class Video(Reproducible):
    contenido = models.FileField(upload_to='archivos/videos/')

    def __str__(self):
        return 'Video: ' + self.titulo + '(' + self.fecha_creacion + ')'


class Clip(models.Model):
    nombre = models.CharField(max_length=50)
    segundo_inicio = models.DecimalField(decimal_places=2)
    segundo_fin = models.DecimalField(decimal_places=2)
    referencia = models.ForeignKey(Reproducible)




