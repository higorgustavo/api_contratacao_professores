from django.urls import path

from .views import AlunoList

app_name = "alunos"
urlpatterns = [
    path("professores/<int:professor_pk>/alunos", AlunoList.as_view(), name="list"),
]
