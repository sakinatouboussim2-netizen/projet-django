import sys
import os

# Ajout du chemin racine pour importer generateur.py
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from django.shortcuts import render
import generateur


def des_accueil(request):
    """Page d'accueil de la section des."""
    contexte = {
        'titre': 'Simulation de des - Exercice 7',
        'description': (
            'Simulation du lancer de deux des a six faces. '
            'On calcule la probabilite d\'obtenir deux valeurs identiques.'
        ),
    }
    return render(request, 'des_app/accueil.html', contexte)


def lancer_view(request):
    """Lance n fois deux des et affiche les resultats."""
    nb = int(request.GET.get('nb', 10))
    if nb < 1:
        nb = 1
    if nb > 100:
        nb = 100

    lancers = []
    for i in range(nb):
        de1, de2 = generateur.lancer_des()
        egal = generateur.test(de1, de2)
        lancers.append({
            'numero': i + 1,
            'de1': de1,
            'de2': de2,
            'egal': egal,
        })

    nb_egalites = sum(1 for l in lancers if l['egal'])

    contexte = {
        'titre': 'Lancer des des',
        'nb': nb,
        'lancers': lancers,
        'nb_egalites': nb_egalites,
    }
    return render(request, 'des_app/lancer.html', contexte)


def test_view(request):
    """Teste la fonction test() avec 10 exemples."""
    exemples = []
    for i in range(10):
        de1, de2 = generateur.lancer_des()
        resultat = generateur.test(de1, de2)
        exemples.append({
            'numero': i + 1,
            'de1': de1,
            'de2': de2,
            'resultat': resultat,
        })

    contexte = {
        'titre': 'Test de la fonction test()',
        'exemples': exemples,
    }
    return render(request, 'des_app/test.html', contexte)


def probabilites_view(request):
    """Lance des simulations avec differentes valeurs de n."""
    valeurs_n = [1, 10, 20, 100, 1000, 5000, 10000, 100000]
    resultats = []

    for n in valeurs_n:
        res = generateur.simulation(n)
        resultats.append(res)

    contexte = {
        'titre': 'Calcul des probabilites',
        'resultats': resultats,
        'probabilite_theorique': round(6 / 36, 4),
    }
    return render(request, 'des_app/probabilites.html', contexte)
