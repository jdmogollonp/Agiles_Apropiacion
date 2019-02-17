from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('galeria', views.index, name='galeria'),
    path('viewImages', views.viewImages, name='viewImages'),
    path('galeria/', views.index, name='galeria'),
    path('agregarUsuario/', views.agregar_usuario, name='agregarUsuario'),
    path('registrarUsuario/', views.registrar_usuario, name='registrarUsuario'),
    path('registrarUsuario/<int:id>/', views.editar_usuario, name='editarUsuario'),
    path('<str:tipo>/<int:idbd>/', views.detalle, name='detalleGal'),
    path('<str:tipo>/<int:idbd>/agregarClip/', views.agregarClip, name='agregarClip'),
    path('login_user/', views.login_user, name='login_user'),
    path('login_view/', views.login_view, name='login'),
    path('logout_view/', views.logout_view, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
