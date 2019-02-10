def validar_imagen(value):
    import os
    from django.core.exceptions import ValidationError
    extension = os.path.splitext(value.name)[1]
    permitidas = ['.png', '.bmp', '.gif', '.jpg', '.jpeg', '.tif', '.tiff']
    if not extension.lower() in permitidas:
        raise ValidationError(u'No es una imagen.')

def validar_audio(value):
    import os
    from django.core.exceptions import ValidationError
    extension = os.path.splitext(value.name)[1]
    permitidas = ['.mp3', '.wav', '.ogg', '.midi', '.wma']
    if not extension.lower() in permitidas:
        raise ValidationError(u'No es un audio.')

def validar_video(value):
    import os
    from django.core.exceptions import ValidationError
    extension = os.path.splitext(value.name)[1]
    permitidas = ['.avi', '.mpeg', '.mov', '.wmv', '.rm', '.flv', '.mp4', '.mkv']
    if not extension.lower() in permitidas:
        raise ValidationError(u'No es un video.')