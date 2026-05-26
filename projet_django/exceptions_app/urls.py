from django.urls import path
from . import views

app_name = 'exceptions_app'

urlpatterns = [
    path('', views.exceptions_accueil, name='accueil'),
    path('division/', views.division_view, name='division'),
    path('conversion/', views.conversion_view, name='conversion'),
    path('liste/', views.liste_view, name='liste'),
]
