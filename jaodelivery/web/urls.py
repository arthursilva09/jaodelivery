from django.urls import path

import web.views as views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login-view'),
    path('login/submit/', views.login_submit, name='login-submit'),
    path('logout/', views.logout_user, name='logout'),
    path('home/', views.home, name='home'),
    path('produtos/', views.estoque_view, name='estoque-produtos'),
    path('produtos/cadastrar/', views.cadastrar_produto, name='cadastrar-produtos'),
    path('produtos/editar/<int:id>/', views.editar_produto, name='atualizar-produto'),
    path('produtos/remover/<int:id>/', views.remover_produto, name="apagar-produto"),
    path('categorias/', views.categ_view, name='estoque-categorias'),
    path('categorias/cadastrar/', views.cadastrar_categ, name='cadastrar-categorias'),
    path('categorias/editar/<int:id>', views.editar_categ, name='editar-categorias'),
    path('categorias/remover/<int:id>', views.remover_categ, name='remover-categorias'),
    path('conta/', views.conta, name='conta'),
    path('conta/add/', views.add_usuario, name='add-usuario'),
]