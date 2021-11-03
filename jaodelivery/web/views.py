from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import jaodelivery_forms as jaoforms
from .models import Categoria, Produto


# Create your views here.

def index(request):
  return render(request, 'web/index.html')


def login_view(request):
  return render(request, 'web/login.html')

def login_submit(request):
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    usuario = authenticate(username=username, password=password)
    if usuario is not None:
      login(request, usuario)
      return redirect('home')
    else:
      messages.error(request, 'Usuário ou senha inválido!')
  return redirect('login-view')

@login_required(login_url='/web/login/')
def home(request):
  usuario = request.user
  return render(request, 'web/home.html', {'usuario': usuario})

@login_required(login_url='/web/login/')
def logout_user(request):
  logout(request)
  return redirect('index')

@login_required(login_url='/web/login/')
def conta(request):
  if request.method == "POST":
    form_senha = PasswordChangeForm(request.user, request.POST)
    if form_senha.is_valid():
        user = form_senha.save()
        update_session_auth_hash(request, user)
        return redirect('login-view')
  else:
    form_senha = PasswordChangeForm(request.user)
  return render(request, 'web/conta.html', {'form_senha': form_senha})

@login_required(login_url='/web/login/')
def add_usuario(request):
  if request.method == "POST":
    form_usuario = UserCreationForm(request.POST)
    if form_usuario.is_valid():
      form_usuario.save()
      return redirect('add-usuario')
  else:
    form_usuario = UserCreationForm()
  return render(request, 'web/add_user.html', {'form_usuario': form_usuario})


# =-=-=-=-=-=- PRODUTOS -=-=-=-=-=-=-=
@login_required(login_url='/web/login/')
def estoque_view(request):
  produtos = Produto.objects.all()
  return render(request, 'web/produtos.html', {'produtos': produtos})

@login_required(login_url='/web/login/')
def cadastrar_produto(request):
  if request.method == "POST":
    formulario = jaoforms.ProdutoForm(request.POST, request.FILES)
    if formulario.is_valid():
      formulario.save()
      return redirect('estoque-produtos')
  else:
    formulario = jaoforms.ProdutoForm()
  
  return render(request, 'web/formularios.html', {'formulario': formulario, 'titulo': 'Cadastrar produto', 'banco_dados': 'produtos'})

@login_required(login_url='/web/login/')
def editar_produto(request, id):
  produto = Produto.objects.get(id=id) 
  if request.method == "POST":
    formulario = jaoforms.ProdutoForm(request.POST, request.FILES, instance=produto)
    if formulario.is_valid():
      formulario.save()
      return redirect('estoque-produtos')
  else:
    formulario = jaoforms.ProdutoForm(instance=produto)

  return render(request, 'web/formularios.html', {'formulario': formulario, 'titulo': 'Editar produto', 'banco_dados': 'produtos'})

@login_required(login_url='/web/login/')
def remover_produto(request, id):
  produto = Produto.objects.get(id=id)
  produto.delete()

  return redirect('estoque-produtos')


#=-=-=-=-=-= CATEGORIAS -=-=-=-=-=-=-=
@login_required(login_url='/web/login/')
def categ_view(request):
  categorias = Categoria.objects.all()
  return render(request, 'web/categorias.html', {'categorias': categorias})

@login_required(login_url='/web/login/')
def cadastrar_categ(request):
  if request.method == "POST":
    formulario = jaoforms.CategoriaForm(request.POST, request.FILES)
    if formulario.is_valid():
      formulario.save()
      return redirect('estoque-categorias')
  else:
    formulario = jaoforms.CategoriaForm()

  return render(request, 'web/formularios.html', 
    {'formulario': formulario, 'titulo': 'Cadastrar categoria', 'banco_dados': 'categorias'})

@login_required(login_url='/web/login/')
def editar_categ(request, id):
  categoria = Categoria.objects.get(id=id)
  if request.method == "POST":
    formulario = jaoforms.CategoriaForm(request.POST, request.FILES, instance=categoria)
    if formulario.is_valid():
      formulario.save()
      return redirect('estoque-categorias')
  else:
    formulario = jaoforms.CategoriaForm(instance=categoria)

  return render(request, 'web/formularios.html', 
    {'formulario': formulario, 'titulo':'Editar categoria', 'banco_dados': 'categorias'})

@login_required(login_url='/web/login/')
def remover_categ(request, id):
  categoria = Categoria.objects.get(id=id)
  categoria.delete()
  return redirect('estoque-categorias')
