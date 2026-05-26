"""
=============================================================
  Fichier : poo_app/views.py
  Role    : Vues Django pour la demonstration POO Python
=============================================================
"""

from django.shortcuts import render
from .modeles_poo import Animal, Chien, Chat


def poo_accueil(request):
    """Page d'accueil POO - presentation des concepts."""
    code_animal = (
        "class Animal:\n"
        "    nb_animaux = 0  # Attribut de CLASSE\n\n"
        "    def __init__(self, nom, age, espece):\n"
        "        self.__nom  = nom    # Attribut PRIVE\n"
        "        self.__age  = age    # Attribut PRIVE\n"
        "        self.espece = espece # Attribut PUBLIC\n"
        "        Animal.nb_animaux += 1\n\n"
        "    def get_nom(self):      # GETTER\n"
        "        return self.__nom\n\n"
        "    def parler(self):       # Methode polymorphe\n"
        "        return f'{self.__nom} fait un son...'"
    )

    code_chien = (
        "class Chien(Animal):        # HERITAGE\n\n"
        "    def __init__(self, nom, age, race):\n"
        "        super().__init__(nom, age, 'Chien')  # super()\n"
        "        self.race = race\n\n"
        "    def parler(self):       # POLYMORPHISME (override)\n"
        "        return f'{self.get_nom()} dit : Wouf !'\n\n"
        "    def rapporter(self):    # Methode specifique\n"
        "        return f'{self.get_nom()} rapporte la balle !'"
    )

    concepts = [
        {
            'nom': 'Encapsulation',
            'description': (
                "Les attributs prives (__nom, __age) ne sont pas accessibles "
                "directement depuis l'exterieur de la classe. "
                "On utilise des getters et setters."
            ),
        },
        {
            'nom': 'Heritage',
            'description': (
                "Chien et Chat heritent d'Animal avec 'class Chien(Animal)'. "
                "Ils recuperent toutes les methodes d'Animal "
                "et peuvent en ajouter de nouvelles."
            ),
        },
        {
            'nom': 'Polymorphisme',
            'description': (
                "La methode parler() est definie dans Animal et REDEFINIE "
                "dans Chien et Chat. Chaque classe retourne sa propre version."
            ),
        },
        {
            'nom': 'Constructeur __init__',
            'description': (
                "__init__ est appele automatiquement a la creation de l'objet. "
                "super().__init__() appelle le constructeur de la classe parente."
            ),
        },
    ]

    contexte = {
        'titre': 'Programmation Orientee Objet en Python',
        'code_animal': code_animal,
        'code_chien': code_chien,
        'concepts': concepts,
    }
    return render(request, 'poo_app/accueil.html', contexte)


def animaux_view(request):
    """Vue : creation et affichage d'objets."""
    Animal.nb_animaux = 0

    chien1 = Chien("Rex",   4, "Labrador")
    chien2 = Chien("Buddy", 1, "Berger Allemand")
    chat1  = Chat("Mimi",   3, "blanche")
    chat2  = Chat("Felix",  7, "noir")

    objets = [
        chien1.to_dict(),
        chien2.to_dict(),
        chat1.to_dict(),
        chat2.to_dict(),
    ]

    code_creation = (
        "# Creation des objets\n"
        "chien1 = Chien('Rex',   4, 'Labrador')\n"
        "chien2 = Chien('Buddy', 1, 'Berger Allemand')\n"
        "chat1  = Chat('Mimi',   3, 'blanche')\n"
        "chat2  = Chat('Felix',  7, 'noir')\n\n"
        "# Appel des methodes\n"
        "print(chien1.parler())       # --> Rex dit : Wouf !\n"
        "print(chat1.parler())        # --> Mimi dit : Miaou !\n"
        "print(Animal.nb_animaux)     # --> 4"
    )

    contexte = {
        'titre': "Creation et Affichage d'Objets",
        'objets': objets,
        'nb_animaux': Animal.nb_animaux,
        'code_creation': code_creation,
    }
    return render(request, 'poo_app/animaux.html', contexte)


def heritage_view(request):
    """Vue : demonstration de l'heritage."""
    Animal.nb_animaux = 0

    rex  = Chien("Rex",  4, "Labrador")
    mimi = Chat("Mimi",  3, "blanche")

    heritage_info = [
        {
            'expression': 'isinstance(rex, Chien)',
            'resultat': str(isinstance(rex, Chien)),
            'explication': 'rex est une instance de Chien',
        },
        {
            'expression': 'isinstance(rex, Animal)',
            'resultat': str(isinstance(rex, Animal)),
            'explication': 'rex EST aussi un Animal (heritage)',
        },
        {
            'expression': 'isinstance(mimi, Chat)',
            'resultat': str(isinstance(mimi, Chat)),
            'explication': 'mimi est une instance de Chat',
        },
        {
            'expression': 'isinstance(mimi, Chien)',
            'resultat': str(isinstance(mimi, Chien)),
            'explication': "mimi n'est PAS un Chien",
        },
        {
            'expression': 'Chien.__bases__',
            'resultat': str(Chien.__bases__),
            'explication': 'La classe parente de Chien est Animal',
        },
    ]

    code_heritage = (
        "class Animal:               # Classe parente\n"
        "    def __init__(self, nom, age, espece):\n"
        "        ...\n\n"
        "class Chien(Animal):        # Chien HERITE d'Animal\n"
        "    def __init__(self, nom, age, race):\n"
        "        super().__init__(nom, age, 'Chien')  # appel parent\n"
        "        self.race = race\n\n"
        "# Verification\n"
        "isinstance(rex, Chien)    # True\n"
        "isinstance(rex, Animal)   # True (heritage)\n"
        "isinstance(mimi, Chien)   # False"
    )

    contexte = {
        'titre': "Heritage - Chien et Chat heritent d'Animal",
        'rex': rex.to_dict(),
        'mimi': mimi.to_dict(),
        'heritage_info': heritage_info,
        'code_heritage': code_heritage,
        'rex_race': rex.race,
        'mimi_couleur': mimi.couleur,
        'rex_action': rex.rapporter(),
        'mimi_action': mimi.ronronner(),
    }
    return render(request, 'poo_app/heritage.html', contexte)


def polymorphisme_view(request):
    """Vue : demonstration du polymorphisme."""
    Animal.nb_animaux = 0

    animaux = [
        Chien("Rex",    4, "Labrador"),
        Chat("Mimi",    3, "blanche"),
        Chien("Buddy",  1, "Berger"),
        Chat("Felix",   7, "noir"),
        Animal("Tweety", 2, "Oiseau"),
    ]

    resultats_poly = []
    for animal in animaux:
        resultats_poly.append({
            'nom':          animal.get_nom(),
            'classe':       type(animal).__name__,
            'parole':       animal.parler(),
            'presentation': animal.se_presenter(),
        })

    code_polymorphisme = (
        "animaux = [\n"
        "    Chien('Rex',    4, 'Labrador'),\n"
        "    Chat('Mimi',    3, 'blanche'),\n"
        "    Animal('Tweety', 2, 'Oiseau'),\n"
        "]\n\n"
        "# Meme appel parler() sur tous les animaux\n"
        "for animal in animaux:\n"
        "    print(animal.parler())\n\n"
        "# Resultat :\n"
        "# Rex dit : Wouf !       <- Chien.parler()\n"
        "# Mimi dit : Miaou !     <- Chat.parler()\n"
        "# Tweety fait un son...  <- Animal.parler()"
    )

    contexte = {
        'titre': 'Polymorphisme - Une methode, des comportements differents',
        'resultats_poly': resultats_poly,
        'code_polymorphisme': code_polymorphisme,
    }
    return render(request, 'poo_app/polymorphisme.html', contexte)
