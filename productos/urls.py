from django.urls import path
from productos import views

urlpatterns = [
    path('productos/', views.ProductosLista.as_view()),
    path('productos/<int:pk>/', views.ProductoDetalle.as_view()),
]