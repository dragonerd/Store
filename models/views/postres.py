import os
from django.shortcuts import render

def postres(request):
    # Ruta a la carpeta de imágenes
    carpeta_imagenes = 'static/postres/'

    # Obtener una lista de los nombres de las imágenes
    lista_imagenes = os.listdir(carpeta_imagenes)

    # Filtrar solo los archivos .jpg (opcional)
    lista_imagenes = [img for img in lista_imagenes if img.endswith('.jpg')]

    # Pasar la lista al contexto
    context = {'imagenes': lista_imagenes}
    return render(request, 'postres.html', context)
