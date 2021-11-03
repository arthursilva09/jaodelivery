from django import forms
from ..models import Categoria, Produto


class CategoriaForm(forms.ModelForm):
  class Meta:
    model = Categoria
    exclude = ('disponibilidade',)

class ProdutoForm(forms.ModelForm):
  class Meta:
    model = Produto
    exclude = ('disponibilidade',)  
