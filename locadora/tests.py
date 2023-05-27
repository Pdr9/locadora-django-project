from django.test import TestCase
from django.urls import reverse
from .models import Locacao, Filme

class LocacaoTests(TestCase):
    def setUp(self):
        self.locacao = Locacao.objects.create(nome='Locacao de Teste', data='2023-01-01', cliente='Cliente de Teste')

    def test_listar_locacoes(self):
        response = self.client.get(reverse('listar_locacoes'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.locacao.nome)

    def test_criar_locacao(self):
        response = self.client.post(reverse('criar_locacao'), {'nome': 'Nova Locacao', 'data': '2023-02-01', 'cliente': 'Novo Cliente'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Locacao.objects.count(), 2)
        nova_locacao = Locacao.objects.get(nome='Nova Locacao')
        self.assertEqual(nova_locacao.cliente, 'Novo Cliente')

    def test_editar_locacao(self):
        response = self.client.post(reverse('editar_locacao', args=[self.locacao.id]), {'nome': 'Locacao Editada', 'data': '2023-03-01', 'cliente': 'Cliente Editado'})
        self.assertEqual(response.status_code, 302)
        locacao_editada = Locacao.objects.get(id=self.locacao.id)
        self.assertEqual(locacao_editada.nome, 'Locacao Editada')
        self.assertEqual(locacao_editada.cliente, 'Cliente Editado')

    def test_excluir_locacao(self):
        response = self.client.post(reverse('excluir_locacao', args=[self.locacao.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Locacao.objects.count(), 0)

    def test_listar_filmes(self):
        filme = Filme.objects.create(titulo='Filme de Teste', valor=10.99, categoria='Ação')
        response = self.client.get(reverse('listar_filmes'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, filme.titulo)

    def test_criar_filme(self):
        response = self.client.post(reverse('criar_filme'), {'titulo': 'Novo Filme', 'valor': 9.99, 'categoria': 'Comédia'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Filme.objects.count(), 1)
        novo_filme = Filme.objects.get(titulo='Novo Filme')
        self.assertEqual(novo_filme.valor, 9.99)

    def test_editar_filme(self):
        filme = Filme.objects.create(titulo='Filme de Teste', valor=10.99, categoria='Ação')
        response = self.client.post(reverse('editar_filme', args=[filme.id]), {'titulo': 'Filme Editado', 'valor': 15.99, 'categoria': 'Drama'})
        self.assertEqual(response.status_code, 302)
        filme_editado = Filme.objects.get(id=filme.id)
        self.assertEqual(filme_editado.titulo, 'Filme Editado')
        self.assertEqual(filme_editado.valor, 15.99)

    def test_excluir_filme(self):
        filme = Filme.objects.create(titulo='Filme de Teste', valor=10.99, categoria='Ação')
        response = self.client.post(reverse('excluir_filme', args=[filme.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Filme.objects.count(), 0)
