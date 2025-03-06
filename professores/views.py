from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Professor
from .serializers import ProfessorSerializer


class ProfessorList(APIView):
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
