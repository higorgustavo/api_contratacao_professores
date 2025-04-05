from django.urls import path

from .views import AlunoList, ProfessorAlunosList

app_name = "alunos"
urlpatterns = [
    path("professores/<int:professor_pk>/alunos", AlunoList.as_view(), name="list"),
    path("professores/alunos", ProfessorAlunosList.as_view(), name="teacher-students"),
]
