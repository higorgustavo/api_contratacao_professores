from django.urls import path

from .views import MeView, ProfessorDetail, ProfessorFotoPerfilView, ProfessorList

app_name = "professores"
urlpatterns = [
    path("professores", ProfessorList.as_view(), name="list"),
    path("professores/<int:pk>", ProfessorDetail.as_view(), name="detail"),
    path("me", MeView.as_view(), name="me"),
    path("professores/foto", ProfessorFotoPerfilView.as_view(), name="profile-image"),
]
