
from django.urls import path, include
from .views import AvaliacaoAPIView, CursosAPIView
app = 'cursos'
urlpatterns = [
    path('cursos/',CursosAPIView.as_view(), name='cursos'),
    path('avaliacao/', AvaliacaoAPIView.as_view(), name='avaliacao'),
]

