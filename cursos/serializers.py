from rest_framework import serializers
from .models import Cursos, Avaliacao
from django.db.models import Avg


class AvaliacaoSerializer(serializers.ModelSerializer):
    
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = ['id', 'curso', 'nome', 'comentario', 'avaliacao', 'criacao', 'ativo']

    def validacao_avaliacao(self, valor):
        if valor in range(1,6):
            return valor
        return serializers.ValidationError('Avaliação deve ser entre 1 e 5')

class CursosSerializer(serializers.ModelSerializer):

    avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    media_avaliacoes = serializers.SerializerMethodField()
    # gera um link dos dados gerados
    # avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name = 'avaliacao-detail')
    
    # retorna a chave primaria 
    # avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Cursos
        fields = ['id', 'titulo', 'url', 'criacao', 'ativo', 'avaliacoes', 'media_avaliacoes']

    def get_media_avaliacoes(self, obj):
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')
        if media is None:
            return 0
        return (media*2)/2