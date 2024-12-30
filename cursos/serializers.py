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
    
    class Meta:
        model = Cursos
        fields = '__all__'