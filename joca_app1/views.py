from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def primer(request):
    html="<title>View1</title> <h1> Este es el primer view de la primera Aplicacion</h1><br><p>Desde aqui se puede acceder a Google c:</p><a href='http://google.com' class='button'>Ir a Google</a>"
    return HttpResponse(html)


