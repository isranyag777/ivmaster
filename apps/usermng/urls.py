#Este archivo gestionará las rutas únicamente de la app usermng
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('users/<name>', views.listusers),
    path('newuser/', views.newuser),
    path('crearusuario/', views.createuser),
    path('edit/<username>', views.edituser),
    path('updateuser/<username>', views.updateuser),

    path('cortar/<username>', views.banuser),
    path('activar/<username>', views.unbanuser),
    path('suspender/<username>', views.disableuser),
    path('habilitar/<username>', views.enableuser),
    path('eliminar/<username>', views.deleteuser),

]