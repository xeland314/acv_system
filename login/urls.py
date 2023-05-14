from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from .views import UsuarioView

router = routers.DefaultRouter()
router.register(r"users", UsuarioView, "users")

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('docs/', include_docs_urls(title='Users API')),
]
