from django.urls import path
from . import views

urlpatterns  = [
    path('', views.login, name="login"),
    path('registro', views.registro, name="registro"),
    path('aportador/inicio', views.inicioAportador, name="inicioAportador"),
    path('aportador/modificar', views.modificarAporte, name="modificarAporte"),
    path('aportador/aportar', views.aportar, name="aportar"),
    path('colaborador', views.loginColaborador, name='loginColaborador')
]