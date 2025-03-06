from django.db import models

from professores.models import Professor


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    data_aula = models.DateTimeField()
    professor = models.ForeignKey(
        Professor, on_delete=models.CASCADE, related_name="alunos"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "alunos"
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"

    def __str__(self):
        return f"{self.nome} - {self.email}"
