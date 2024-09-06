from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def pregunta(request):
    return HttpResponse("<h1>Tengo sueño</h1>")

def presentacion(request):
    html="""
        <p>¿Hola como estás?.</p>
        <h2>Soy un subtítulo</h2> 
    """
    return HttpResponse(html)