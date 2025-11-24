from Librairie import Librairie
from Modèles import Livre, Utilisateur

# Les tests vérifiant le bon fonctionnement des fonctions

# ------------------ Tests pour les fonctions concernant les livres ----------------------

def test_liste_des_livres():
    lib = Librairie()
    livre = Livre(
        id="Test",
        titre="Test",
        auteur="Moi",
        status="Disponible"
    )
    lib.Livres[livre.id] = livre
    # Vérification : OK si la fonction affiche le livre, AssertError sinon
    assert livre in lib.liste_des_livres()
    print("Test liste_des_livres : OK ")

def test_ajouter_livre(capsys):
    lib = Librairie()
    id_livre = lib.ajouter_livre("Test", "Moi")
    capsys.readouterr()
    # Vérification : OK si l'ID généré par uuid dont les paramètres sont entre parentheses vérifient ces conditions, AssertError sinon
    assert id_livre in lib.Livres
    assert lib.Livres[id_livre].titre == "Test"
    assert lib.Livres[id_livre].auteur == "Moi"
    assert lib.Livres[id_livre].status == "Disponible"
    print("Test ajouter_livre : OK ")


def test_chercher_livre():
    lib = Librairie()
    # On donne quelques livres exemples car sinon la fonction va chercher dans le vide. En effet, l'assemblage Librairie - Dictionnaires se fait seulement à l'étape main
    livre1 = Livre(id="1", titre="Les Misérables", auteur="Victor Hugo", status="Disponible")
    livre2 = Livre(id="2", titre="Madame Bovary", auteur="Gustave Flaubert", status="Disponible")
    lib.Livres[livre1.id] = livre1
    lib.Livres[livre2.id] = livre2
    mot = "hugo"
    resultats = lib.chercher_livre(mot)
    # Vérification : OK si la recherche donne qu'une seele réponse et que l'auteur trouvé dans le premier livre est Victor Hugo, AssertError sinon
    assert len(resultats) == 1
    assert resultats[0].auteur == "Victor Hugo"
    print("Test chercher_livre : OK ")


def test_supprimer_livre(capsys):
    lib = Librairie()
    livre = Livre(
        id="Test",
        titre="Test",
        auteur="Moi",
        status="Disponible"
    )
    lib.Livres[livre.id] = livre
    lib.supprimer_livre(livre.id)
    capsys.readouterr()
    # Vérification : OK si le livre test n'existe plus dans la liste, AssertError sinon
    assert livre.id not in lib.Livres
    print("Test supprimer_livre : OK ")


# ----------------------- Tests concernant les fonctions des utilisateurs ------------------------

def test_liste_des_utilisateurs():
    lib = Librairie()
    utilisateur = Utilisateur(
        id="Test",
        nom="Moi",
        livres_empruntes=[]
    )
    lib.Utilisateurs[utilisateur.id] = utilisateur
    # Vérification : OK si l'utilisateur test est affiché, AssertError sinon
    assert utilisateur in lib.liste_des_utilisateurs()
    print("Test liste_des_utilisateurs : OK ")


def test_ajouter_utilisateur(capsys):
    lib = Librairie()
    id_utilisateur = lib.ajouter_utilisateur("Moi")
    capsys.readouterr()
    # Vérification : OK si l'ID généré par uuid dont le nom est "Moi" font partie du dictionnaire
    assert id_utilisateur in lib.Utilisateurs
    assert lib.Utilisateurs[id_utilisateur].nom == "Moi"
    print("Test ajouter_utilisateur : OK ")


def test_supprimer_utilisateur(capsys):
    lib = Librairie()
    utilisateur = Utilisateur(
        id="Test",
        nom="Moi",
        livres_empruntes=[]
    )
    lib.Utilisateurs[utilisateur.id] = utilisateur
    lib.supprimer_utilisateur(utilisateur.id)
    capsys.readouterr()
    # Vérification : OK si l'utilisateur ne fait plus partie de la liste des utilisateurs de la librairie
    assert utilisateur.id not in lib.Utilisateurs
    print("Test supprimer_utilisateur : OK ")


# -------------------------- Tests concernant les emprunts et les retours ----------------------------

def test_emprunt_livres(capsys):
    lib = Librairie()
    livre = Livre(
        id="Test",
        titre="Test",
        auteur="Moi",
        status="Disponible"
    )
    utilisateur = Utilisateur(
        id="Test",
        nom="Toi",
        livres_empruntes=[]
    )
    lib.Livres[livre.id] = livre
    lib.Utilisateurs[utilisateur.id] = utilisateur
    lib.emprunt_livre(utilisateur.id, livre.id)
    capsys.readouterr()
    # Vérification : OK si le status du livré change et qu'il est désormais dans la liste de livres empruntés de l'utilisateur
    assert lib.Livres[livre.id].status == "Emprunté"
    assert livre.id in lib.Utilisateurs[utilisateur.id].livres_empruntes
    print("Test emprunt_livres : OK ")


def test_retour_livre(capsys):
    lib = Librairie()
    livre = Livre(
        id="Test",
        titre="Test",
        auteur="Moi",
        status="Emprunté"
    )
    utilisateur = Utilisateur(
        id="Test",
        nom="Toi",
        livres_empruntes=[livre.id]
    )
    lib.Livres[livre.id] = livre
    lib.Utilisateurs[utilisateur.id] = utilisateur
    lib.retour_livre(utilisateur.id, livre.id)
    capsys.readouterr()
    # Vérification : OK si le retour change le status du livre et qu'il ne fait plus partie des livres empruntés de l'utilisateur
    assert lib.Livres[livre.id].status == "Disponible"
    assert livre.id not in lib.Utilisateurs[utilisateur.id].livres_empruntes
    print("Test retour_livre : OK ")

def test_retour_anonyme(capsys):
    lib = Librairie()
    livre = Livre(
        id="Test",
        titre="Test",
        auteur="Moi",
        status="Emprunté"
    )
    utilisateur = Utilisateur(
        id="Test",
        nom="Toi",
        livres_empruntes=[livre.id]
    )
    lib.Livres[livre.id] = livre
    lib.Utilisateurs[utilisateur.id] = utilisateur
    lib.retour_anonyme(livre.id)
    capsys.readouterr()
    # Vérification : OK si le retour change le status du livre et qu'il ne fait plus partie des livres empruntés de l'utilisateur
    assert lib.Livres[livre.id].status == "Disponible"
    assert livre.id not in lib.Utilisateurs[utilisateur.id].livres_empruntes
    print("Test retour_livre : OK ")


# ---------------------------------- Test pour les statistiques ---------------------------------

def test_statistiques(capsys):
    lib = Librairie()
    lib.Livres = {
        "L1": Livre("L1", "A", "X", "Disponible"),
        "L2": Livre("L2", "B", "Y", "Disponible"),
        "L3": Livre("L3", "C", "Z", "Emprunté"),
    }
    lib.Utilisateurs = {
        "U1": Utilisateur("U1", "Alice", ["L3"]),
        "U2": Utilisateur("U2", "Bob", []),
    }
    resultats = lib.stats(show=False)
    capsys.readouterr()
    assert resultats["total_livres"] == 3
    assert resultats["total_utilisateurs"] == 2
    assert resultats["noms"] == ["Alice", "Bob"]
    assert resultats["emprunts"] == [1, 0]
    print("Test statistiques : OK ")
