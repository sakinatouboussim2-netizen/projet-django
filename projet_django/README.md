# Projet Django - Universite

Projet Django 4.2.7 contenant trois applications pedagogiques :
- **des_app** : Simulation de des (Exercice 7)
- **exceptions_app** : Gestion des exceptions Python
- **poo_app** : Programmation Orientee Objet (classes Animal, Chien, Chat)

---

## Mise en place

### 1. Creer et activer l'environnement virtuel

**Windows (PowerShell) :**
```
python -m venv venv
venv\Scripts\activate
```

**Mac / Linux :**
```
python3 -m venv venv
source venv/bin/activate
```

### 2. Installer les dependances

```
python -m pip install -r requirements.txt
```

### 3. Appliquer les migrations

```
python manage.py migrate
```

### 4. Lancer le serveur

```
python manage.py runserver
```

Ouvrir dans le navigateur : http://127.0.0.1:8000/

---

## Structure du projet

```
projet_django/
    manage.py
    generateur.py          <- Module Exercice 7 (independant)
    requirements.txt
    config/
        settings.py
        urls.py
        wsgi.py
    des_app/
        views.py
        urls.py
    exceptions_app/
        views.py
        urls.py
    poo_app/
        modeles_poo.py     <- Classes Animal, Chien, Chat
        views.py
        urls.py
    templates/
        base.html
        accueil.html
        des_app/
        exceptions_app/
        poo_app/
```

---

## URLs

| URL | Description |
|---|---|
| / | Page d'accueil |
| /des/ | Accueil simulation des |
| /des/lancer/?nb=10 | Lancer n des |
| /des/probabilites/ | Calcul des probabilites |
| /exceptions/ | Accueil exceptions |
| /exceptions/division/ | Demo ZeroDivisionError |
| /exceptions/conversion/ | Demo ValueError |
| /exceptions/liste/ | Demo IndexError |
| /poo/ | Accueil POO |
| /poo/animaux/ | Creation d'objets |
| /poo/heritage/ | Heritage et isinstance() |
| /poo/polymorphisme/ | Polymorphisme |

---

## Pousser sur GitHub

```
git init
git add .
git commit -m "Projet Django initial"
git remote add origin https://github.com/VOTRE_NOM/projet_django.git
git branch -M main
git push -u origin main
```
