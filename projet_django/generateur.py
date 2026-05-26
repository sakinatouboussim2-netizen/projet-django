import random


def lancer_des():
    """Lance deux des a six faces et retourne les resultats."""
    de1 = random.randint(1, 6)
    de2 = random.randint(1, 6)
    return de1, de2


def test(de1, de2):
    """Teste si les deux des ont la meme valeur."""
    return de1 == de2


def simulation(n):
    """
    Simule n lancers de deux des et calcule la probabilite d'egalite.
    Retourne un dictionnaire avec les statistiques.
    """
    nb_egalites = 0
    details = []

    for i in range(n):
        de1, de2 = lancer_des()
        egal = test(de1, de2)
        if egal:
            nb_egalites += 1
        if i < 10:
            details.append({
                'numero': i + 1,
                'de1': de1,
                'de2': de2,
                'egal': egal
            })

    probabilite = nb_egalites / n if n > 0 else 0

    return {
        'n': n,
        'nb_egalites': nb_egalites,
        'probabilite': round(probabilite, 4),
        'probabilite_theorique': round(6 / 36, 4),
        'details': details,
        'ecart': round(abs(probabilite - 6 / 36), 4)
    }


if __name__ == '__main__':
    # Test autonome du module
    print("=== Test du module generateur ===")
    d1, d2 = lancer_des()
    print(f"Lancer : de1={d1}, de2={d2}, egal={test(d1, d2)}")
    resultat = simulation(1000)
    print(f"Simulation 1000 lancers : probabilite={resultat['probabilite']}")
    print(f"Probabilite theorique   : {resultat['probabilite_theorique']}")
