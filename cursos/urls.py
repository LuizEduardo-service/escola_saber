
from django.urls import path, include
from .views import AvaliacoesAPIView, CursosAPIView
app = 'cursos'
urlpatterns = [
    path('cursos/',CursosAPIView.as_view(), name='cursos'),
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
]

