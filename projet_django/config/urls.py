from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def accueil(request):
    return render(request, 'accueil.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accueil, name='accueil'),
    path('des/', include('des_app.urls')),
    path('exceptions/', include('exceptions_app.urls')),
    path('poo/', include('poo_app.urls')),
]
