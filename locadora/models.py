from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Locacao(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    filmes = models.ManyToManyField(Filme)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Locação'
        verbose_name_plural = 'Locações'

    def __str__(self):
        return self.nome
