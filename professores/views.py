from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Professor
from .permissions import ProfessorListPermission
from .serializers import ProfessorFotoPerfilSerializer, ProfessorSerializer


class ProfessorList(APIView):
    permission_classes = (ProfessorListPermission,)

    def get(self, request):
        q = request.query_params.get("q", "")
        professores = Professor.objects.filter(descricao__icontains=q)
        serializer = ProfessorSerializer(professores, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfessorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request):
        serializer = ProfessorSerializer(request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request):
        request.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProfessorDetail(APIView):
    def get(self, request, pk):
        professor = get_object_or_404(Professor, pk=pk)
        serializer = ProfessorSerializer(professor)
        return Response(serializer.data)


class MeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = ProfessorSerializer(request.user)
        return Response(serializer.data)


class ProfessorFotoPerfilView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = ProfessorFotoPerfilSerializer(request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Foto de perfil atualizada com sucesso"})
