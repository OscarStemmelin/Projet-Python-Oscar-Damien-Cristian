Projet 1 -- Gestion d'une librairie

Réalisé par: Damien Lebas, Cristian Carp et Oscar Stemmelin



Notre projet contient un dossier "code" dans lequel y apparait tous les fichiers python et un fichier json ayant le rôle de base de données. On expliquera son utilité plus tard. Nous trouverons aussi un fichier consignes.txt (copie exacte de la consigne), un requirements.txt qui contient les dépendances nécéssaires au projet, et le README que vous lisez actuellement.

Le dossier code contient :
    - main.py : Programme principal que l'utilisateur doit lancer
    - librairie.py : Contient la classe Librairie, et contient toutes ses méthodes
    - modeles.py : Contient les deux dataclasses : livre et utilisateur
    - tests.py : Contient l'ensemble des tests des fonctions et méthodes
    - data.json : Représente la base de données contenant deux tableaux : Livres et Utilisateurs

Le reste du projet contient : 
    requirements.txt : Contient les dépendances
    consignes.md : Copie de la consigne
    README.md : Page d'explication


Structure :

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


Contenu :

Ce programme gère une librairie, nous pouvons :
    - Afficher la liste des livres
    - Ajouter un livre et/ou utilisateur
    - Chercher un livre
    - Supprimer un livre et/ou utilisateur
    - Emprunter un livre
    - Retourner un livre
    - Afficher les statistiques descriptives de la base de données



Outils non vus en cours :

json : ce type de fichier nous permet d'utiliser une base de données modifiable. Nous avons choisi le json car il nous fallait pouvoir sauvegarder les différentes taches ci-dessus même lorsque le programme s'arrête.

uuid : Nous avons utilisé la classe de la bibliothèque standart de python 'uuid', qui nous permet facilement d'attribuer un identifiant à chaque livre de manière aléatoire.

try, except : Comme indiqué dans le cours, nous avons initialement utilisé des raise ValueError, cependant, dès que l'utilisateur faisait une faute de frappe, le programme s'arrêtait sans sauvegarder les modifications effectuées. Ainsi le try except permet à l'utilisateur de print l'erreur sans arrêter le programme.

capsys : Utiliser dans les tests, capsys nous permet de masquer ce que print une fonction. Il s'agit seulement d'esthetisme.







