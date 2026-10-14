from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from rest_framework import viewsets
from .models import Categoria, Ejercicio # O como se llamen tus modelos
from .serializer import CategoriaSerializer, EjercicioSerializer # O como se llamen tus serializadores

# --- TU CÓDIGO ANTIGUO (LA API REST) ---
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class EjercicioViewSet(viewsets.ModelViewSet):
    queryset = Ejercicio.objects.all()
    serializer_class = EjercicioSerializer


# --- TU CÓDIGO NUEVO (AUTENTICACIÓN Y VISTAS) ---
# 1. Vista Pública (Sin protección)
def inicio(request):
    return render(request, 'inicio.html')

# 2. Function Based View (FBV) Protegida con Decorador
@login_required
def vista_protegida_fbv(request):
    return render(request, 'protegida.html', {'tipo': 'FBV (Basada en Funciones)'})

# 3. Class Based View (CBV) Protegida con Mixin
class VistaProtegidaCBV(LoginRequiredMixin, TemplateView):
    template_name = 'protegida.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipo'] = 'CBV (Basada en Clases)'
        return context