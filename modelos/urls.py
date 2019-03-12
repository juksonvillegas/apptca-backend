from django.urls import path
from modelos import views

urlpatterns = [
    path('marcas/', views.MarcasLista.as_view()),
    path('modelos/', views.ModelosLista.as_view()),
    path('marcas/<int:pk>/', views.MarcaDetalle.as_view()),
    path('modelos/<int:pk>/', views.ModeloDetalle.as_view()),
] 