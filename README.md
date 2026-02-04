# Projet 1 — Gestion d’une Librairie  
**Réalisé par : Damien Lebas, Cristian Carp et Oscar Stemmelin**

## Description du projet  
Ce projet propose une application Python permettant de **gérer une librairie** à l’aide d’une petite base de données locale au format JSON.  
L’utilisateur peut consulter, ajouter, supprimer ou emprunter des livres, gérer les utilisateurs, et afficher des statistiques descriptives.

Le dépôt contient également les tests unitaires, les consignes du projet et les dépendances nécessaires.

---

## Structure du dépôt  

```
M1EcoStats-GroupProject/
├── Code/
│   ├── main.py
│   ├── librairie.py
│   ├── modeles.py
│   ├── tests.py
│   └── data.json
├── requirements.txt
├── consignes.md
└── README.md
```

### Détails des fichiers du dossier `Code/`
- **main.py** : Point d’entrée du programme, interface utilisateur.  
- **librairie.py** : Contient la classe `Librairie` et l’ensemble des méthodes de gestion.  
- **modeles.py** : Définit les deux dataclasses `Livre` et `Utilisateur`.  
- **tests.py** : Ensemble des tests unitaires.  
- **data.json** : Base de données contenant deux tableaux : `Livres` et `Utilisateurs`.

### Fichiers à la racine
- **requirements.txt** : Liste des dépendances Python.  
- **consignes.md** : Copie de la consigne du projet.  
- **README.md** : Documentation du projet.

---

## Fonctionnalités  
Le programme permet de :

-  **Afficher la liste des livres**  
-  **Ajouter** un livre ou un utilisateur  
-  **Rechercher** un livre  
-  **Supprimer** un livre ou un utilisateur  
-  **Emprunter** un livre  
-  **Retourner** un livre  
-  **Afficher des statistiques descriptives** sur la base de données  

---

## Outils utilisés (non vus en cours)

### **JSON**
Utilisé comme base de données légère et modifiable.  
Il permet de **sauvegarder l’état de la librairie** même après fermeture du programme.

### **uuid**
La bibliothèque standard `uuid` permet d’attribuer automatiquement un **identifiant unique** à chaque livre.

### **try / except**
Initialement, les erreurs étaient gérées via `raise ValueError`, ce qui arrêtait le programme.  
Le passage à `try/except` permet :
- d’afficher l’erreur à l’utilisateur  
- de **ne pas interrompre l’exécution**  
- de conserver les modifications déjà effectuées  

### **capsys (pytest)**
Utilisé dans les tests unitaires pour **capturer et masquer les sorties console**, uniquement pour des raisons d’esthétique.
