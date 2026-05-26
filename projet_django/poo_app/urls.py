from django.urls import path
from . import views

app_name = 'poo_app'

urlpatterns = [
    path('', views.poo_accueil, name='accueil'),
    path('animaux/', views.animaux_view, name='animaux'),
    path('heritage/', views.heritage_view, name='heritage'),
    path('polymorphisme/', views.polymorphisme_view, name='polymorphisme'),
]
