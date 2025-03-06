from django.urls import path

from .views import MeView, ProfessorDetail, ProfessorList

app_name = "professores"
urlpatterns = [
    path("professores", ProfessorList.as_view(), name="list"),
    path("professores/<int:pk>", ProfessorDetail.as_view(), name="detail"),
    path("me", MeView.as_view(), name="me"),
]
