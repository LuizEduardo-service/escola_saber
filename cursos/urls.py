
from django.urls import path, include
from .views import AvaliacoesAPIView, CursosAPIView, CursoAPIView,AvaliacaoAPIView, CursoViewSet, AvaliacaoViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('cursos', CursoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)
app = 'cursos'
urlpatterns = [
    path('cursos/',CursosAPIView.as_view(), name='cursos'),
    path('cursos/<int:curso_pk>/',CursoAPIView.as_view(), name='curso'),
    path('cursos/<int:curso_pk>/avaliacoes/', AvaliacoesAPIView.as_view(), name='curso_avaliacoes'),
    path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>/',AvaliacoesAPIView.as_view(), name='curso_avaliacao'),
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('avaliacao/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='avaliacao'),
]

