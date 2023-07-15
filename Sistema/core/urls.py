from django.contrib import admin
from django.urls import path , include
from .views import home ,registrarHoras
from . import views


# determinar quais informações queremos exibir em nossas páginas 
# e definir os URLs a serem usados para retornar esses recursos.

urlpatterns = [
    path('',home),
    path('registrarHoras/', views.registrarHoras),
    path('edicaoHoras/<codigo>', views.edicaoHoras),
    path('editarHoras/', views.editarHoras),
    path('deletarHoras/<codigo>', views.deletarHoras),

    

   
]

