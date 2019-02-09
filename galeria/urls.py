from django.urls import path


from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('<str:tipo>/<int:idbd>',views.detalle,name='detalleGal')

]