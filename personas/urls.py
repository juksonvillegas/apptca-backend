from django.urls import path
from personas import views

urlpatterns = [
    path('clientes/', views.PersonasLista.as_view()),
    path('clientes/<int:pk>/', views.PersonasDetalle.as_view()),
]