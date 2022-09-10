from django.urls import path
from .views import vistaPaginaInicio

urlpatterns = [
    path('',vistaPaginaInicio,name='Inicio')
]