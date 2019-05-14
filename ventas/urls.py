from django.urls import path
from ventas import views

urlpatterns = [
    path('ventas/', views.VentasLista.as_view()),
    path('ventas_detalle/', views.Venta_detalleLista.as_view()),
    path('ventas/<int:pk>/', views.VentasDetalle.as_view()),
    path('ventas_detalle/<int:pk>/', views.Venta_detalleDetalle.as_view()),
] 