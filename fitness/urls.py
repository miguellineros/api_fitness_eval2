from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, EjercicioViewSet, inicio

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'ejercicios', EjercicioViewSet)

urlpatterns = [
    # Ruta para el template HTML
    path('', inicio, name='inicio'),
    
    # Rutas para la API REST
    path('api/', include(router.urls)),
]