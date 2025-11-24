from Librairie import Librairie


def main():
    lib = Librairie()

    lib.lien_fichiers("Data.json")

    while True:
        action = input("Que voulez-vous faire ? (Lister, Ajouter, Chercher, Supprimer, Emprunt, Retour, Statistiques, Sauvegarder, Quitter)").lower()
        match action:
            case "lister":
                print("====Liste des livres====")
                for livre in lib.liste_des_livres():
                    print(f" [{livre.id[:7]}] | {livre.titre} - {livre.auteur} ({livre.status})")
                print("")
                print("====Liste des utilisateurs====")
                for utilisateur in lib.liste_des_utilisateurs():
                    print(f" [{utilisateur.id[:8]}] | {utilisateur.nom} - emprunts: {utilisateur.livres_empruntes}")
                print("")
            case "ajouter":
                # Le lower() nous permet d'écrire en majuscule ou en miniscule sans provoquer d'erreur
                choix = input("Que voulez-vous ajouter ? (Livre, Utilisateur)").lower()
                match choix:
                    case "livre":
                        titre = input("Titre: ")
                        auteur = input("Auteur: ")
                        lib.ajouter_livre(titre, auteur)
                    case "utilisateur":
                        nom = input("Nom: ")
                        lib.ajouter_utilisateur(nom)
                    case _:
                        # Selon le cours, nous aurions dû mettre un raise ValueError("truc"), mais cela stoppait notre
                        # programme à chaque faute de frappe. On a donc choisi le print.
                        print(f"Choix invalide: {choix}")

            case "chercher":
                mot = input("Entrez un mot clé: ")
                resultats = lib.chercher_livre(mot)
                if not resultats:
                    print("Aucun livre trouvé")
                else:
                    print("Les livres correspondant à vos recherches: ")
                    for livre in resultats:
                        print(f" [{livre.id[:8]}] | {livre.titre} - {livre.auteur} ({livre.status})")

            case "supprimer":
                condamner = input("Que souhaitez-vous supprimer de la liste ? (Livre, Utilisateur)").lower()
                match condamner:
                    case "livre":
                        id_livre = input("ID de livre: ")
                        # On a tout de même mis des raise ValueError dans notre classe librairie, on a trouvé cette
                        # mèthode qui nous permet de ne pas faire planter le programme à chaque fois qu'on fait une
                        # erreur de frappe.
                        try:
                            lib.supprimer_livre(id_livre)
                        except ValueError as e:
                            print(e)
                    case "utilisateur":
                        id_utilisateur = input("ID de utilisateur: ")
                        try:
                            lib.supprimer_utilisateur(id_utilisateur)
                        except ValueError as e:
                            print(e)
                    case _:
                        print("Choix invalide (taper livre ou utilisateur)")

            case "emprunt":
                id_livre = input("ID du livre: ")
                id_utilisateur = input("ID de l'emprunteur: ")
                try:
                    lib.emprunt_livre(id_livre, id_utilisateur)
                except ValueError as e:
                    print(e)

            case "retour":
                choix = input("Connaissez vous l'ID de l'emprunteur ? (Oui ou Non)").lower()
                match choix:
                    case "oui":
                        id_livre = input("ID du livre: ")
                        id_utilisateur = input("ID de l'emprunteur: ")
                        try:
                            lib.retour_livre(id_livre, id_utilisateur)
                        except ValueError as e:
                            print(e)
                    case "non":
                        id_livre = input("ID du livre: ")
                        try:
                            lib.retour_anonyme(id_livre)
                        except ValueError as e:
                            print(e)
                    case _:
                        print("Choix invalide (taper Oui ou Non)")

            case "statistiques":
                lib.stats()

            case "sauvegarder":
                lib.sauvegarde("Data.json")

            case "quitter":
                lib.sauvegarde("Data.json")
                break

            case _:
                print(f"Opération inconnue: {action}")




if __name__ == '__main__':

    main()
