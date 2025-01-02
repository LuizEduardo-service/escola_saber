from rest_framework import serializers
from .models import Cursos, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):
    
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = ['id', 'curso', 'nome', 'comentario', 'avaliacao', 'criacao', 'ativo']

class CursosSerializer(serializers.ModelSerializer):

    avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # gera um link dos dados gerados
    # avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name = 'avaliacao-detail')
    
    # retorna a chave primaria 
    # avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Cursos
        fields = ['id', 'titulo', 'url', 'criacao', 'ativo', 'avaliacoes']