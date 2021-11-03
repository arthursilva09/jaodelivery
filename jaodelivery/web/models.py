from django.db import models

# Create your models here.

class Categoria(models.Model):
  nome = models.CharField(max_length=30, null=False, blank=False)
  foto = models.ImageField(null=False, blank=False)
  disponibilidade = models.BooleanField(default=True)

  def __str__(self):
    return self.nome

class Produto(models.Model):
  nome = models.CharField(max_length=30, null=False, blank=False)
  categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
  quantidade = models.IntegerField(null=False, blank=False)
  preco = models.fields.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
  imagem = models.ImageField(null=False, blank=True)
  disponibilidade = models.BooleanField(default=True)

  def __str__(self):
    return self.nome
