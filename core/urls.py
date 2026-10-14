"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from fitness.views import inicio, vista_protegida_fbv, VistaProtegidaCBV

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('fitness.urls')), # Tu API existente
    
    # Rutas de autenticación (Login/Logout)
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Rutas de vistas estándar (Públicas y Protegidas)
    path('', inicio, name='inicio'),
    path('protegida-fbv/', vista_protegida_fbv, name='protegida_fbv'),
    path('protegida-cbv/', VistaProtegidaCBV.as_view(), name='protegida_cbv'),
]