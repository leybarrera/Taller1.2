from django.urls import path
from . import views  # Asegúrate de que las vistas estén importadas correctamente

urlpatterns = [
    path('', views.index, name='index'),
    path('orden/<int:id>/', views.detalle_orden, name='detalle_orden'),
]
