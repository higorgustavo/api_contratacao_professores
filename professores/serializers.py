from decimal import Decimal

from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import Professor


class ProfessorSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(required=True, min_length=3, max_length=100)
    idade = serializers.IntegerField(required=True, min_value=18, max_value=100)
    descricao = serializers.CharField(required=True, min_length=10, max_length=500)
    password_confirmation = serializers.CharField(write_only=True)
    valor_hora = serializers.DecimalField(
        required=True,
        min_value=Decimal(10),
        max_value=Decimal(500),
        max_digits=5,
        decimal_places=2,
    )

    class Meta:
        model = Professor
        fields = (
            "id",
            "nome",
            "email",
            "idade",
            "descricao",
            "valor_hora",
            "created_at",
            "updated_at",
            "password",
            "password_confirmation",
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }

    def validate_password_confirmation(self, value):
        if self.initial_data["password"] != value:
            raise serializers.ValidationError("As senhas informadas não são iguais")
        return value

    def create(self, validated_data):
        del validated_data["password_confirmation"]
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        del validated_data["password_confirmation"]
        validated_data["password"] = make_password(validated_data["password"])
        return super().update(instance, validated_data)
