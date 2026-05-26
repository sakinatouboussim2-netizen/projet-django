"""
=============================================================
  Fichier : poo_app/modeles_poo.py
  Role    : Classes Python pour demontrer la POO
=============================================================

Concepts demontres :
  1. ENCAPSULATION   : attributs prives avec getters/setters
  2. HERITAGE        : Chien et Chat heritent d'Animal
  3. POLYMORPHISME   : chaque classe redefinie parler()
  4. CONSTRUCTEURS   : __init__ avec parametres
=============================================================
"""


class Animal:
    """
    Classe de base representant un animal generique.

    Attributs :
        __nom    (str) : nom de l'animal (prive)
        __age    (int) : age en annees (prive)
        espece   (str) : espece (public)
    """

    nb_animaux = 0  # Attribut de classe partage par toutes les instances

    def __init__(self, nom, age, espece):
        """Constructeur : initialise un animal."""
        self.__nom  = nom
        self.__age  = age
        self.espece = espece
        Animal.nb_animaux += 1

    # --- Getters ---
    def get_nom(self):
        """Retourne le nom de l'animal."""
        return self.__nom

    def get_age(self):
        """Retourne l'age de l'animal."""
        return self.__age

    # --- Setters ---
    def set_age(self, age):
        """Modifie l'age avec validation."""
        if isinstance(age, int) and age >= 0:
            self.__age = age
        else:
            raise ValueError(f"L'age doit etre un entier positif. Recu : {age}")

    # --- Methodes ---
    def parler(self):
        """Methode polymorphe : chaque animal parle differemment."""
        return f"{self.__nom} fait un son generique..."

    def se_presenter(self):
        """Retourne une description de l'animal."""
        return (
            f"Je suis {self.__nom}, un(e) {self.espece} "
            f"age(e) de {self.__age} an(s)."
        )

    def est_adulte(self):
        """Retourne True si l'animal a plus de 2 ans."""
        return self.__age > 2

    def __str__(self):
        """Representation textuelle de l'objet."""
        return f"Animal({self.__nom}, {self.espece}, {self.__age} ans)"

    def to_dict(self):
        """Convertit l'objet en dictionnaire pour les templates Django."""
        return {
            'nom':    self.__nom,
            'age':    self.__age,
            'espece': self.espece,
            'adulte': self.est_adulte(),
            'parole': self.parler(),
            'classe': self.__class__.__name__,
        }


class Chien(Animal):
    """
    Classe Chien - herite de Animal.

    Ajoute :
        - attribut race
        - redefinition de parler() (polymorphisme)
        - methode rapporter()
    """

    def __init__(self, nom, age, race):
        """Constructeur : appelle super().__init__ puis ajoute race."""
        super().__init__(nom, age, espece='Chien')
        self.race = race

    def parler(self):
        """POLYMORPHISME : un chien aboie."""
        return f"{self.get_nom()} dit : Wouf ! Wouf !"

    def rapporter(self):
        """Methode specifique au Chien."""
        return f"{self.get_nom()} ({self.race}) rapporte la balle !"

    def to_dict(self):
        """Etend to_dict() du parent."""
        data = super().to_dict()
        data['race']   = self.race
        data['action'] = self.rapporter()
        return data


class Chat(Animal):
    """
    Classe Chat - herite de Animal.

    Ajoute :
        - attribut couleur
        - redefinition de parler() (polymorphisme)
        - methode ronronner()
    """

    def __init__(self, nom, age, couleur):
        """Constructeur : appelle super().__init__ puis ajoute couleur."""
        super().__init__(nom, age, espece='Chat')
        self.couleur = couleur

    def parler(self):
        """POLYMORPHISME : un chat miaule."""
        return f"{self.get_nom()} dit : Miaou !"

    def ronronner(self):
        """Methode specifique au Chat."""
        return f"{self.get_nom()} ({self.couleur}) ronronne : Rrrrr..."

    def to_dict(self):
        """Etend to_dict() du parent."""
        data = super().to_dict()
        data['couleur'] = self.couleur
        data['action']  = self.ronronner()
        return data


if __name__ == '__main__':
    print("=" * 55)
    print("   DEMONSTRATION POO - Animal, Chien, Chat")
    print("=" * 55)

    chien1 = Chien("Rex",   4, "Labrador")
    chien2 = Chien("Buddy", 1, "Berger allemand")
    chat1  = Chat("Mimi",   3, "blanche")
    chat2  = Chat("Felix",  7, "noir")

    print("\n--- Polymorphisme : parler() ---")
    for animal in [chien1, chien2, chat1, chat2]:
        print(f"  {animal.parler()}")

    print("\n--- Heritage : se_presenter() ---")
    for animal in [chien1, chien2, chat1, chat2]:
        print(f"  {animal.se_presenter()}")

    print("\n--- Encapsulation : getters ---")
    print(f"  Nom de chien1 : {chien1.get_nom()}")
    print(f"  Age de chat1  : {chat1.get_age()}")

    print(f"\n--- Attribut de classe ---")
    print(f"  Nombre d'animaux crees : {Animal.nb_animaux}")
    print("=" * 55)
