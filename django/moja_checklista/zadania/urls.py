from django. urls import path
from . import views

urlpatterns = [
    path('', views.lista_zadan, name='lista'),
    path('toggle/<int:zadanie_id>/', views.zmien_status, name='zmien_status'),
]
