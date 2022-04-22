#Este archivo gestionará las rutas únicamente de la app usermng
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('<sucursalname>', views.listusers),                        #view
    path('logs/<sucursalname>', views.showlogs),                          #view
    path('newuser/<sucursalname>', views.newuser),                  #view
    path('crearusuario/<sucursalname>', views.createuser),                #action
    path('<sucursalname>/<username>', views.edituser),              #view
    path('<sucursalname>/updateuser/<username>', views.updateuser),        #action

    path('<sucursalname>/cortar/<username>', views.banuser),               #action
    path('<sucursalname>/activar/<username>', views.unbanuser),            #action
    path('<sucursalname>/suspender/<username>', views.disableuser),        #action
    path('<sucursalname>/habilitar/<username>', views.enableuser),         #action
    path('<sucursalname>/eliminar/<username>', views.deleteuser),          #action
]