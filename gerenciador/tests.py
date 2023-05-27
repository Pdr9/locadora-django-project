from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_locacoes, name='listar_locacoes'),
    path('criar_locacao/', views.criar_locacao, name='criar_locacao'),
    path('editar_locacao/<int:id>/', views.editar_locacao, name='editar_locacao'),
    path('excluir_locacao/<int:id>/', views.excluir_locacao, name='excluir_locacao'),
    path('listar_filmes/', views.listar_filmes, name='listar_filmes'),
    path('criar_filme/', views.criar_filme, name='criar_filme'),
    path('editar_filme/<int:id>/', views.editar_filme, name='editar_filme'),
    path('excluir_filme/<int:id>/', views.excluir_filme, name='excluir_filme'),
]
