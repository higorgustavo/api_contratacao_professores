from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from professores.models import Professor

from .serializers import AlunoSerializer


class AlunoList(APIView):
    def post(self, request, professor_pk):
        professor = get_object_or_404(Professor, pk=professor_pk)
        serializer = AlunoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(professor=professor)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProfessorAlunosList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        alunos = request.user.alunos.all()
        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data)
