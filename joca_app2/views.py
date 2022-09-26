from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def lista(request):
    htmll="<title>Puntaje</title><h3>Esta es la escala de notas</h3><li><b>Lista</b> <ol>Creación del proyecto base con un commit con un mensaje que indique que es el proyecto base. El proyecto base debe contener el archivo .gitignore con las correspondientes extensiones.	15 puntos</ol><ol>App1 funcionando en la rama 1 con todo lo solicitado desde el navegador. 15 puntos </ol> <ol>App2 funcionando en la rama 2 con todo lo solicitado desde el navegador 15 pts </ol><ol>Proyecto completo en la rama principal funcionando desde el navegador. 30 puntos</ol><ol>Subir las tres ramas correctamente a GitHub y compartirlas con mi usuario (confirmar que fue compartida correctamente). 15 puntos</ol> <ol>Utiliza en cada vista por lo menos 5 etiquetas html. 10 puntos </ol></li>"
    return HttpResponse(htmll)


