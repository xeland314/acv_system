"""administracion_vehicular URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from rest_framework.authtoken import views
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('api_generate_token/', views.obtain_auth_token),
    path('conductores/', include('conductores.urls')),
    path('empresas/', include('empresas.urls')),
    path('dashboard/', admin.site.urls),
    path('docs/', include_docs_urls(title='Users API')),
    path('ordenes_mantenimiento/', include('ordenes_de_mantenimiento.urls')),
    path('ordenes_trabajo/', include('ordenes_de_trabajo.urls')),
    path('representantes/', include('representantes.urls')),
    path('suscripciones/', include('suscripciones.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('vehiculos/', include('vehiculos.urls')),
]
