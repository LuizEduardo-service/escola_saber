from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cursos, Avaliacao
from .serializers import AvaliacaoSerializer, CursosSerializer


class CursosAPIView(APIView):
    def get(self, request):
        cursos = Cursos.objects.all()
        serializer = CursosSerializer(cursos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CursosSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class AvaliacaoAPIView(APIView):
    def get(self, request):
        avaliacao = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacao, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)        
