from rest_framework import generics
from .models import Cursos, Avaliacao
from .serializers import AvaliacaoSerializer, CursosSerializer
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

# ########################################################### API V1 ##################################

class CursosAPIView(generics.ListCreateAPIView):
    queryset = Cursos.objects.all()
    serializer_class = CursosSerializer

class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cursos.objects.all()
    serializer_class = CursosSerializer

class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))
        return self.queryset.all()
    
class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(), 
                                     curso_id=self.kwargs.get('curso_pk'), 
                                     pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))


# ########################################################### API V2 ##################################

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Cursos.objects.all()
    serializer_class = CursosSerializer

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        curso = self.get_object()
        serializer = AvaliacaoSerializer(curso.avaliacoes.all(), many= True)
        return Response(serializer.data)
    
# class AvaliacaoViewSet(viewsets.ModelViewSet):
#     queryset = Avaliacao.objects.all()
#     serializer_class = AvaliacaoSerializer
    
      
class AvaliacaoViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
