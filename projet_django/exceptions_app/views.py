"""
=============================================================
  Fichier : exceptions_app/views.py
  Role    : Vues Django pour la gestion des exceptions Python
=============================================================
"""

from django.shortcuts import render


def exceptions_accueil(request):
    """Page principale - explication theorique des exceptions."""
    exemples_code = [
        {
            'titre': 'Structure try / except / finally',
            'code': (
                "try:\n"
                "    resultat = 10 / 0\n\n"
                "except ZeroDivisionError as e:\n"
                "    print('Erreur :', e)\n\n"
                "finally:\n"
                "    print('Bloc finally execute.')"
            ),
            'explication': (
                "Le bloc try contient le code risque. "
                "Le bloc except capture l'exception. "
                "Le bloc finally s'execute toujours."
            ),
        },
        {
            'titre': 'Plusieurs except',
            'code': (
                "try:\n"
                "    x = int(input('Entrez un nombre : '))\n"
                "    resultat = 100 / x\n\n"
                "except ZeroDivisionError:\n"
                "    print('Erreur : division par zero !')\n\n"
                "except ValueError:\n"
                "    print('Erreur : entier invalide.')\n\n"
                "finally:\n"
                "    print('Fin du programme.')"
            ),
            'explication': (
                "On peut avoir plusieurs blocs except pour capturer "
                "differents types d'exceptions."
            ),
        },
    ]
    contexte = {
        'titre': 'Gestion des Exceptions Python',
        'exemples_code': exemples_code,
    }
    return render(request, 'exceptions_app/accueil.html', contexte)


def division_view(request):
    """Demonstration interactive de ZeroDivisionError."""
    resultat = None
    erreur = None
    erreur_type = None
    code_execute = None
    finally_msg = "Le bloc finally s'est execute (toujours)."

    if request.method == 'POST':
        dividende_str = request.POST.get('dividende', '')
        diviseur_str  = request.POST.get('diviseur', '')

        code_execute = (
            f"try:\n"
            f"    dividende = int('{dividende_str}')\n"
            f"    diviseur  = int('{diviseur_str}')\n"
            f"    resultat  = dividende / diviseur\n\n"
            f"except ZeroDivisionError as e:\n"
            f"    print('Erreur ZeroDivisionError :', e)\n\n"
            f"except ValueError as e:\n"
            f"    print('Erreur ValueError :', e)\n\n"
            f"finally:\n"
            f"    print('Bloc finally execute.')"
        )

        try:
            dividende = int(dividende_str)
            diviseur  = int(diviseur_str)
            resultat  = dividende / diviseur

        except ZeroDivisionError as e:
            erreur      = f"ZeroDivisionError : {e}"
            erreur_type = "ZeroDivisionError"

        except ValueError as e:
            erreur      = f"ValueError : {e}"
            erreur_type = "ValueError"

        finally:
            pass

    contexte = {
        'titre': 'Exemple 1 - Division et ZeroDivisionError',
        'resultat': resultat,
        'erreur': erreur,
        'erreur_type': erreur_type,
        'finally_msg': finally_msg,
        'code_execute': code_execute,
    }
    return render(request, 'exceptions_app/division.html', contexte)


def conversion_view(request):
    """Demonstration interactive de ValueError."""
    resultat = None
    erreur = None
    code_execute = None
    finally_msg = "Le bloc finally s'est execute (toujours)."

    if request.method == 'POST':
        valeur_str = request.POST.get('valeur', '')

        code_execute = (
            f"try:\n"
            f"    valeur = '{valeur_str}'\n"
            f"    nombre = int(valeur)\n"
            f"    print('Conversion reussie :', nombre)\n\n"
            f"except ValueError as e:\n"
            f"    print('Erreur ValueError :', e)\n\n"
            f"finally:\n"
            f"    print('Fin de la tentative.')"
        )

        try:
            nombre = int(valeur_str)
            resultat = f"Conversion reussie ! int('{valeur_str}') = {nombre}"

        except ValueError as e:
            erreur = f"ValueError : impossible de convertir '{valeur_str}' en entier. ({e})"

        finally:
            pass

    contexte = {
        'titre': 'Exemple 2 - Conversion et ValueError',
        'resultat': resultat,
        'erreur': erreur,
        'finally_msg': finally_msg,
        'code_execute': code_execute,
    }
    return render(request, 'exceptions_app/conversion.html', contexte)


def liste_view(request):
    """Demonstration interactive de IndexError."""
    ma_liste = [10, 20, 30, 40, 50]
    resultat = None
    erreur = None
    code_execute = None
    finally_msg = "Le bloc finally s'est execute (toujours)."

    if request.method == 'POST':
        index_str = request.POST.get('index', '')

        code_execute = (
            f"ma_liste = [10, 20, 30, 40, 50]\n\n"
            f"try:\n"
            f"    index = int('{index_str}')\n"
            f"    valeur = ma_liste[index]\n"
            f"    print('ma_liste[{index_str}] =', valeur)\n\n"
            f"except IndexError as e:\n"
            f"    print('Erreur IndexError :', e)\n\n"
            f"except ValueError as e:\n"
            f"    print('Erreur ValueError :', e)\n\n"
            f"finally:\n"
            f"    print('Acces a la liste termine.')"
        )

        try:
            index = int(index_str)
            valeur = ma_liste[index]
            resultat = f"ma_liste[{index}] = {valeur}"

        except IndexError as e:
            erreur = (
                f"IndexError : index {index_str} hors bornes. "
                f"La liste a {len(ma_liste)} elements "
                f"(indices 0 a {len(ma_liste)-1}). ({e})"
            )

        except ValueError as e:
            erreur = f"ValueError : '{index_str}' n'est pas un entier valide. ({e})"

        finally:
            pass

    contexte = {
        'titre': 'Exemple 3 - Acces a une liste et IndexError',
        'ma_liste': ma_liste,
        'resultat': resultat,
        'erreur': erreur,
        'finally_msg': finally_msg,
        'code_execute': code_execute,
        'index_str': index_str if request.method == 'POST' else '',
    }
    return render(request, 'exceptions_app/liste.html', contexte)
