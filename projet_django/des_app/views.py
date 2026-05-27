import sys
import os
from django.shortcuts import render

# On ajoute le chemin racine pour pouvoir importer generateur.py
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import generateur


def des_accueil(request):
    code_module = (
        "import random\n\n"
        "def lancer_des():\n"
        "    de1 = random.randint(1, 6)\n"
        "    de2 = random.randint(1, 6)\n"
        "    return de1, de2\n\n"
        "def test(de1, de2):\n"
        "    return de1 == de2\n\n"
        "def simulation(n):\n"
        "    nb_egalites = 0\n"
        "    for i in range(n):\n"
        "        de1, de2 = lancer_des()\n"
        "        if test(de1, de2):\n"
        "            nb_egalites += 1\n"
        "    return nb_egalites / n"
    )
    contexte = {
        'titre': 'Simulation des Des - Exercice 7',
        'probabilite_theorique': round(6 / 36, 4),
        'code_module': code_module,
    }
    return render(request, 'des_app/accueil.html', contexte)


def lancer_view(request):
    # On recupere le nombre de lancers depuis l URL (?nb=10)
    try:
        nb = int(request.GET.get('nb', 10))
        nb = max(1, min(1000, nb))
    except ValueError:
        nb = 10

    lancers = []
    nb_egalites = 0

    for i in range(nb):
        d1, d2 = generateur.lancer_des()
        egal = generateur.test(d1, d2)
        if egal:
            nb_egalites += 1
        lancers.append({
            'numero': i + 1,
            'de1': d1,
            'de2': d2,
            'egal': egal,
            'statut': 'EGAUX' if egal else 'differents',
        })

    probabilite = round(nb_egalites / nb, 4) if nb > 0 else 0

    contexte = {
        'titre': 'Lancer des deux des',
        'lancers': lancers,
        'nb': nb,
        'nb_egalites': nb_egalites,
        'probabilite': probabilite,
        'probabilite_theorique': round(6 / 36, 4),
    }
    return render(request, 'des_app/lancer.html', contexte)


def test_view(request):
    resultats = []
    nb_egalites = 0

    for i in range(10):
        d1, d2 = generateur.lancer_des()
        egal = generateur.test(d1, d2)
        if egal:
            nb_egalites += 1
        resultats.append({
            'numero': i + 1,
            'de1': d1,
            'de2': d2,
            'egal': egal,
            'statut': 'EGAUX' if egal else 'differents',
        })

    contexte = {
        'titre': "Test d'egalite des deux des",
        'resultats': resultats,
        'nb_egalites': nb_egalites,
        'nb_total': 10,
    }
    return render(request, 'des_app/test.html', contexte)


def probabilites_view(request):
    valeurs_n = [1, 10, 20, 100, 1000, 5000, 10000, 100000]
    resultats = []

    for n in valeurs_n:
        res = generateur.simulation(n)
        resultats.append({
            'n': n,
            'nb_egalites': res['nb_egalites'],
            'probabilite': res['probabilite'],
            'probabilite_theorique': res['probabilite_theorique'],
            'ecart': res['ecart'],
            'ecart_pct': round(res['ecart'] * 100, 2),
        })

    contexte = {
        'titre': 'Tableau des Probabilites',
        'resultats': resultats,
        'probabilite_theorique': round(6 / 36, 4),
        'fraction': '6/36',
    }
    return render(request, 'des_app/probabilites.html', contexte)


def simulation_view(request):
    # L utilisateur choisit son propre n et on lance la simulation
    resultat = None
    n_choisi = None

    if request.method == 'POST':
        try:
            n_choisi = int(request.POST.get('n', 100))
            n_choisi = max(1, min(100000, n_choisi))
            resultat = generateur.simulation(n_choisi)
        except ValueError:
            n_choisi = None

    contexte = {
        'titre': 'Simulation personnalisee',
        'resultat': resultat,
        'n_choisi': n_choisi,
        'probabilite_theorique': round(6 / 36, 4),
    }
    return render(request, 'des_app/simulation.html', contexte)