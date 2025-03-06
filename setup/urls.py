from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("professores.urls", namespace="professores")),
    path("api/", include("alunos.urls", namespace="alunos")),
    path("api/auth/", include("autenticacao.urls"), name="autenticacao"),
]
