from django.shortcuts import render
from rest_framework import viewsets
from .models import Categoria, Ejercicio
from .serializer import CategoriaSerializer, EjercicioSerializer

# Vista tradicional para el template de inicio
def inicio(request):
    return render(request, 'inicio.html')

# Vistas de la API REST
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class EjercicioViewSet(viewsets.ModelViewSet):
    queryset = Ejercicio.objects.all()
    serializer_class = EjercicioSerializer