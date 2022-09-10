from urllib import request
from django.http import HttpResponse

# Create your views here.
def vistaPaginaInicio (request):
    return HttpResponse('Hola mundo ya estoy hasta la madre')