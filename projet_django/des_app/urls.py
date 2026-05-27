from django.urls import path
from . import views

app_name = 'des_app'

urlpatterns = [
    path('', views.des_accueil, name='accueil'),
    path('lancer/', views.lancer_view, name='lancer'),
    path('test/', views.test_view, name='test'),
    path('probabilites/', views.probabilites_view, name='probabilites'),
    path('simulation/', views.simulation_view, name='simulation'),
]