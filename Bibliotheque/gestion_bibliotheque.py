#Classe livres
#Les livres sont initialisés avec un titre, un auteur et un ISBN. Le statut du livre est fixé sur dispo par défaut
#Il y a une fonction __str__ qui permet d'afficher les informations du livre à l'aide d'un print

class Livre:
    def __init__(self, titre, auteur, ISBN):
        self.titre = titre
        self.auteur = auteur
        self.ISBN = ISBN
        self.dispo = True

    def __str__(self):
        if self.dispo:
            return f"Titre : {self.titre} \nAuteur : {self.auteur} \nISBN : {self.ISBN} \nLe livre est disponible"
        else:
            return f"Titre : {self.titre} \nAuteur : {self.auteur} \nISBN : {self.ISBN} \nLe livre est indisponible"


#Classe Membre
#Dans cette classe il y a un compteur de membres qui est utilisé comme id pour les membres
#Les membres sont initialisés avec un nom, l'id correspondant à leur ordre d'arrivé et avec une liste vide qui contiendra les livres empruntés
#Il y a une fonction __str__ qui permet d'afficher les informations du membre

class Membre:
    nb_membres = 0
    def __init__(self, nom):
        self.nom = nom
        self.id_membre = Membre.nb_membres
        self.livres_empruntes = []
        Membre.nb_membres += 1


    def __str__(self):
        if len(self.livres_empruntes) == 0:
            return f"Nom : {self.nom} \nID : {self.id_membre} \nCe membre n'a aucun livre emprunté en ce moment."
        elif len(self.livres_empruntes) == 1:
            return f"Nom : {self.nom} \nID : {self.id_membre} \nCe membre a emprunté {self.livres_empruntes[0]}"
        else:
            return f"Nom : {self.nom} \nID : {self.id_membre} \nListe des livres empruntés : {self.livres_empruntes}"


#Classe bibliothèque
#La bibliotheque est initialisée avec une liste de membres et un dictionnaire contenant la liste des livres dispos et celle des livres non dispos
#Une fonction __str__ permet d'afficher les informations générales de la bibliotheque comme le nombre de membre et de livres dispos et non dispos

class Bibliotheque:
    def __init__(self):
        self.livres = {
            "Dispo" : [],
            "Non Dispo" : []
        }
        self.membres = []

    #Fonction permettant d'ajouter un livre en faisant appel à la fonction d'initialisation de la classe livre
    #Il faut renseigner le titre, l'auteur et l'ISBN
    #Le livre initialisé est ajouté dans la liste des livres disponibles de la classe bibliotheque
    def ajouter_livre(self, titre, auteur, ISBN):
        nouveau_livre = Livre(titre, auteur, ISBN)
        self.livres["Dispo"].append(nouveau_livre)

    #La fonction vérifie que le livre renseigné est présent dans la bibliotheque (en emprunt ou non) et le supprime de la bibliotheque
    #Un message d'erreur est renvoyé dans le cas où l'objet renseigné n'est pas un livre
    def supp_livre(self, livre):
        try:
            if livre in self.livres["Dispo"]:
                self.livres["Dispo"].remove(livre)
                print("Le livre a été supprimé de la liste des disponibles.")
            elif livre in self.livres["Non Dispo"]:
                self.livres["Non Dispo"].remove(livre)
                print("Le livre a été supprimé de la liste des non disponibles.")
            else:
                print("Le livre n'existe pas dans la bibliothèque.")

        except AttributeError:
            print("Erreur : le livre fourni n'est pas valide.")

    #Fait appel à la fonction d'initialisation de la classe membre pour ajouter un membre
    #Il faut renseigner le nom du membre
    #Le membre est ajouté à la liste de membres
    def ajouter_membre(self, nom):
        nouveau_membre = Membre(nom)
        self.membres.append(nouveau_membre)


    #Vérifie si le membre est correct et que le livre est disponible et permet l'emprunt d'un livre
    #Le statut du livre change, il est ajouté à la liste des livres empruntés par le membre et est supprimé de la liste dispo pour être ajouté à la liste non dispo
    #un message est affiché pour confirmer l'emprunt
    def emprunt(self, livre, membre):
        if livre.dispo and isinstance(membre, Membre):
            membre.livres_empruntes.append(livre.titre)
            livre.dispo = False
            self.livres["Dispo"].remove(livre)
            self.livres["Non Dispo"].append(livre)
            print(f'{membre.nom} a emprunté "{livre.titre}"')
        else:
            print("Le titre saisi n'est pas disponible.")

    #Fonction qui permet de retourner un livre à la bibliotheque
    #La fonction vérifie si le livre a bien été emprunté par le membre et le retire de sa liste d'emprunt, change son statut et supprime de la liste non dispo pour l'ajouter dans la liste dispo
    #Un message est affiché pour confirmer le retour
    def retour(self, livre, membre):
        if livre.titre in membre.livres_empruntes:
            membre.livres_empruntes.remove(livre.titre)
            livre.dispo = True
            self.livres["Non Dispo"].remove(livre)
            self.livres["Dispo"].append(livre)
        else:
            print("Il n'y a pas de livre à rendre.")

    #Permet, s'il y en a, d'afficher les livres disponibles à la bibliotheque
    def afficher_livres_dispos(self):
        if not self.livres["Dispo"]:
            print("Aucun livre disponible.")
        else:
            for livre in self.livres["Dispo"]:
                print(f"{livre}\n")
    
    #Permet, si le membre a emprunté des livres, de les afficher
    def afficher_livres_membre(self, membre):
        if len(membre.livres_empruntes) == 0:
            print(f"{membre.nom} n'a aucun livre emprunté en ce moment.")
        elif len(membre.livres_empruntes) > 0:
            print(f"Voici les livres empruntés par {membre.nom} :")
            for titre_livre in membre.livres_empruntes:
                print(titre_livre)

    #La fonction permet de chercher les titres correspondant à une chaine de caracteres parmis les livres de la bibliotheque
    #La variable livres_complet qui contient la concaténation des listes de livres dispo ou non permet de faire cette recherche parmis l'ensemble des livres
    def recherche_titre(self, titre):
        
        def check_title(titre_teste):
            if titre in titre_teste.titre:
                return True
            else:
                return False
        
        livres_complet = self.livres["Dispo"] + self.livres["Non Dispo"]

        livre_recherche = list(filter(check_title, livres_complet))

        if len(livre_recherche) == 0:
            print(f"Le livre {titre} n'a pas été trouvé")
        elif len(livre_recherche) > 0:
            for recherche in livre_recherche:
                print(recherche)

    #La fonction permet de chercher les livres dont l'auteur correspond à une chaine de caracteres parmis les livres de la bibliotheque
    #La variable livres_complet qui contient la concaténation des listes de livres dispo ou non permet de faire cette recherche parmis l'ensemble des livres
    def recherche_auteur(self, auteur):
           
        def check_autor(auteur_teste):
            if auteur in auteur_teste.auteur:
                return True
            else:
                return False
        
        livres_complet = self.livres["Dispo"] + self.livres["Non Dispo"]

        livre_recherche = list(filter(check_autor, livres_complet))

        if len(livre_recherche) == 0:
            print(f"L'auteur {auteur} n'a pas de livre dans la bibliothèque")
        elif len(livre_recherche) > 0:
            for recherche in livre_recherche:
                print(recherche)


    def __str__(self):
        nb_dispo = len(self.livres["Dispo"])
        nb_non_dispo = len(self.livres["Non Dispo"])
        nb_membres = len(self.membres)
        
        return (
            f"Bibliothèque :\n"
            f"- Nombre de livres disponibles : {nb_dispo}\n"
            f"- Nombre de livres empruntés : {nb_non_dispo}\n"
            f"- Nombre de membres : {nb_membres}"
        )
