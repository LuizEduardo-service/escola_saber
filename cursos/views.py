from rest_framework import generics
from .models import Cursos, Avaliacao
from .serializers import AvaliacaoSerializer, CursosSerializer


class CursosAPIView(generics.ListCreateAPIView):
    queryset = Cursos.objects.all()
    serializer_class = CursosSerializer

class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cursos.objects.all()
    serializer_class = CursosSerializer

class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
      
