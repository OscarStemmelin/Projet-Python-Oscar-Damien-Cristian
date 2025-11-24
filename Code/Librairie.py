from Modèles import Livre, Utilisateur
import uuid
import matplotlib.pyplot as plt
import json

# La structure interne de la librairie.
class Librairie :

    def __init__(self) -> None:
        self.Livres = {}
        self.Utilisateurs = {}

    ### Fonction : rattacher le fichier des données de base
    def lien_fichiers(self, chemin_fichier: str) -> None:
        """
        Cette fonction a pour objectif de faire le lien entre les dictionnaires vides de la
        class Librairie et les données du fichier "Data". Ce lien consiste dans le fait que
        les objets livre et utilisateur sont créés et ensuite stockés dans la class Librairie.
        """
        with open(chemin_fichier, "r", encoding="utf-8") as f:
            data = json.load(f)
        dict_livres = data.get("livres", {})
        dict_utilisateurs = data.get("utilisateurs", {})

        # Transformation en dictionnaire
        dict_livres = {l["id"]: l for l in dict_livres}
        dict_utilisateurs = {u["id"]: u for u in dict_utilisateurs}

        # Création des livres
        self.Livres = {}  # On réinitialise
        for id_livre, data in dict_livres.items():
            self.Livres[id_livre] = Livre(
                id=data["id"],
                titre=data["titre"],
                auteur=data["auteur"],
                status=data["status"]
            )

        # Création des utilisateurs
        self.Utilisateurs = {}
        for id_utilisateur, data in dict_utilisateurs.items():
            self.Utilisateurs[id_utilisateur] = Utilisateur(
                id=data["id"],
                nom=data["nom"],
                livres_empruntes=data["livres_empruntes"]
            )

    ### Fonction : sauvegarde les modification dans le fichier json
    def sauvegarde(self, chemin_fichier: str) -> None:
        # Transformation des objets Livre et Utilisateur en dictionnaires simples
        livres_export = [
            {
                "id": livre.id,
                "titre": livre.titre,
                "auteur": livre.auteur,
                "status": livre.status
            }
            for livre in self.Livres.values()
        ]
        utilisateurs_export = [
            {
                "id": u.id,
                "nom": u.nom,
                "livres_empruntes": list(u.livres_empruntes)
            }
            for u in self.Utilisateurs.values()
        ]
        # Fusion des livres et utilisateurs en une base de données
        data = {
            "livres": livres_export,
            "utilisateurs": utilisateurs_export
        }
        with open(chemin_fichier, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print("Les données ont bien été sauvegardés")


# =======================================================================================================
# ===================================== Les fonctionnalités =============================================
# =======================================================================================================


# ------------------------------------------ Les livres -------------------------------------------------
    ### Fonction : affichage
    def liste_des_livres(self) -> list:
        return list(self.Livres.values())

    ### Fonction : ajouter un nouveau livre
    def ajouter_livre(self, titre: str, auteur: str) -> str:
        id_livre = str(uuid.uuid4())
        nouveau_livre = Livre(
            id = id_livre,
            titre = titre,
            auteur = auteur,
            status = "Disponible",
        )
        self.Livres[id_livre] = nouveau_livre
        print(f"Livre ajouté - {titre} de {auteur} [id:{id_livre}]")
        return id_livre

    ### Fonction : chercher un livre
    def chercher_livre(self, mot: str) -> list:
        mot = mot.lower()
        resultats = []

        for livre in self.Livres.values():
            if mot in livre.titre.lower() or mot in livre.auteur.lower():
                resultats.append(livre)
        return resultats

    ### Fonction : supprimer un livre
    def supprimer_livre(self, id_livre: str) -> None:
        livre = self.Livres.get(id_livre)
        if not livre:
            raise ValueError(f"Livre introuvable : {id_livre}")
        if livre.status != "Disponible":
            raise ValueError("Impossible de supprimer un livre emprunté")
        del self.Livres[id_livre]
        print("Livre supprimé de la liste.")

    ### Fonction : emprunter un livre
    def emprunt_livre(self, id_livre: str, id_utilisateur: str) -> None:
        livre = self.Livres.get(id_livre)
        utilisateur = self.Utilisateurs.get(id_utilisateur)
        if not livre:
            raise ValueError(f"Livre introuvable : {id_livre}")
        if not utilisateur:
            raise ValueError(f"Utilisateur introuvable : {id_utilisateur}")
        if livre.status != "Disponible":
            raise ValueError("Livre déjà emprunté: {id_livre}")
        livre.status = "Emprunté"
        utilisateur.livres_empruntes.append(livre.id)
        print(f"{utilisateur.nom} a bien emprunté {livre.titre}")

    ### Fonction : rendre un livre
    def retour_livre(self, id_livre: str, id_utilisateur: str) -> None:
        livre = self.Livres.get(id_livre)
        utilisateur = self.Utilisateurs.get(id_utilisateur)
        if not livre:
            raise ValueError(f"Livre introuvable : {id_livre}")
        if not utilisateur:
            raise ValueError(f"Utilisateur introuvable : {id_utilisateur}")
        if livre.status != "Emprunté":
            raise ValueError("Livre non emprunté: {id_livre}")
        livre.status = "Disponible"
        utilisateur.livres_empruntes.remove(livre.id)
        print(f"{utilisateur.nom} a bien rendu {livre.titre}")

    ### Fonction : retour d'un livre sans connaitre l'ID de l'utilisateur
    def retour_anonyme(self, id_livre: str) -> None:
        livre = self.Livres.get(id_livre)
        if not livre:
            raise ValueError(f"Livre introuvable : {id_livre}")
        if livre.status != "Emprunté":
            raise ValueError(f"Livre non emprunté: {id_livre}")
        utilisateur_trouve = None
        for utilisateur in self.Utilisateurs.values():
            if id_livre in utilisateur.livres_empruntes:
                utilisateur_trouve = utilisateur
        if not utilisateur_trouve:
            raise ValueError("Aucun utilisateur ne possède ce livre (erreur dans la base de données).")
        livre.status = "Disponible"
        utilisateur_trouve.livres_empruntes.remove(id_livre)
        print(f"Retour anonyme : {utilisateur_trouve.nom} a rendu '{livre.titre}'")

    # --------------------------------------- Les utilisateurs ----------------------------------------------
    ### Fonction : affichage
    def liste_des_utilisateurs(self) -> list:
        return list(self.Utilisateurs.values())

    ### Fonction : ajouter un nouvel utilisateur
    def ajouter_utilisateur(self, nom: str) -> str:
        id_utilisateur = str(uuid.uuid4())
        nouveau_utilisateur = Utilisateur(
            id = id_utilisateur,
            nom = nom,
            livres_empruntes = []
        )
        self.Utilisateurs[id_utilisateur] = nouveau_utilisateur
        print(f"Utilisateur ajouté - {nom} [id:{id_utilisateur}]")
        return id_utilisateur

    ### Fonction : supprimer un utilisateur
    def supprimer_utilisateur(self, id_utilisateur: str) -> None:
        utilisateur = self.Utilisateurs.get(id_utilisateur)
        if not utilisateur:
            raise ValueError(f"Utilisateur introuvable : {id_utilisateur}")
        if utilisateur.livres_empruntes:
            raise ValueError("Cet utilisateur détiens un livre non rendu. Veuillez attendre le retour des livres avant de le supprimer")
        del self.Utilisateurs[id_utilisateur]
        print("L'utilisateur a été supprimé avec succès")

    ### Fonction : statistiques élémentaires de la base de données
    def stats(self, show=True) -> dict:
        total_livres = len(self.Livres)
        total_utilisateurs = len(self.Utilisateurs)
        print(f"{total_livres} livres")
        print(f"{total_utilisateurs} utilisateurs")
        # Tri des utilisateurs par ordre décroissant d'emprunts
        utilisateurs_sorted = sorted(self.Utilisateurs.values(), key=lambda u: len(u.livres_empruntes), reverse=True)
        noms = [u.nom for u in utilisateurs_sorted]
        emprunts = [len(u.livres_empruntes) for u in utilisateurs_sorted]
        # Création du graphique
        plt.figure(figsize=(12, 6))
        plt.bar(noms, emprunts)
        plt.title("Nombre de livres empruntés par utilisateur")
        plt.xlabel("Utilisateurs")
        plt.ylabel("Livres empruntés")
        if show:
            plt.show()
        return {
            "total_livres": total_livres,
            "total_utilisateurs": total_utilisateurs,
            "noms": noms,
            "emprunts": emprunts

        }

