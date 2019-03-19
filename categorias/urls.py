from django.urls import path
from categorias import views

urlpatterns = [
    path('categorias/', views.CategoriasLista.as_view()),
    path('categorias/<int:pk>/', views.CategoriaDetalle.as_view()),
] 