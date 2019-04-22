from django.urls import path
from compras import views

urlpatterns = [
    path('compras/', views.ComprasLista.as_view()),
    path('compras_detalle/', views.ComprasDetalle.as_view()),
    # path('compras/<int:pk>/', views.MarcaDetalle.as_view()),
    # path('compras_detalle/<int:pk>/', views.ModeloDetalle.as_view()),
] 