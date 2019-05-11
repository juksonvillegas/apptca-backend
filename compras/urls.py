from django.urls import path
from compras import views

urlpatterns = [
    path('compras/', views.ComprasLista.as_view()),
    path('compras_detalle/', views.Compra_detalleLista.as_view()),
    path('compras/<int:pk>/', views.ComprasDetalle.as_view()),
    path('compras_detalle/<int:pk>/', views.Compra_detalleDetalle.as_view()),
] 