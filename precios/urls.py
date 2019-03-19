from django.urls import path
from precios import views

urlpatterns = [
    path('precios/', views.PreciosLista.as_view()),
    path('precios/<int:pk>/', views.PrecioDetalle.as_view()),
]