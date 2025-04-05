from uuid import uuid4

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

from .managers import ProfessorManager


def nome_arquivo_foto_perfil(instance, filename):
    return f"fotos_perfil/{uuid4()}-{filename}"


class Professor(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=255)
    idade = models.PositiveIntegerField(null=True)
    descricao = models.TextField(null=True)
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    foto_perfil = models.ImageField(null=True, upload_to=nome_arquivo_foto_perfil)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nome"]

    objects = ProfessorManager()

    class Meta:
        db_table = "professores"
        verbose_name = "Professor"
        verbose_name_plural = "Professores"

    def __str__(self):
        return f"{self.nome} - {self.email}"

    def delete(self, *args, **kwargs):
        if self.foto_perfil:
            self.foto_perfil.delete(save=False)
        super().delete(*args, **kwargs)
