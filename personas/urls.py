from django.urls import path
from personas import views

urlpatterns = [
    path('clientes/', views.PersonasLista.as_view()),
    path('proveedores/', views.ProveedoresLista.as_view()),
    path('clientes/<int:pk>/', views.PersonasDetalle.as_view()),
    path('proveedores/<int:pk>/', views.ProveedorDetalle.as_view()),
] 