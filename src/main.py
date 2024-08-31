from MainMenu import *#import des fonctions du MainMenu différent pour éviter les erreurs
from back import * #import de toutes les fonctions en back
from front import * #import de toutes les fonctions d'affichage

#récupérer les infos des menus (nombre de joueurs, taille de la grille, nombre de balles)
contre_ordi, n, p = Menu()


#Pour 2 joueurs sur une même machine
def boucle_de_jeu(n, p):
    #création des 2 joueurs
    joueurs = [Joueur(1), Joueur(2)]
    #Pour une durée de 5 manches:
    for tour in range(5):
        tour_joueur= 1 if tour%2!=0 else 2
        tour_joueur2= 2 if tour%2!=0 else 1
        #création de la grille
        plateau=Grille(n)

        #le premier joueur pose ses balles (par défaut p=4)
        afficher_plateau(plateau._plateau, joueurs, "Reste à placer "+str(p)+" balles")
        for i in range(p):
            x,y = clic(n)
            est_place=plateau.placerBalle(tour_joueur,x,y)
            afficher_plateau(plateau._plateau, joueurs, "Reste à placer "+str(p-i)+" balles")
            while est_place==False:
                #afficher message erreur: emplacement invalide
                x,y = clic(n)
                est_place=plateau.placerBalle(tour_joueur,x,y)
        afficher_plateau(plateau._plateau, joueurs, "Changemet de joueur")

        bouton=False #bouton permet de sortir de la boucle si le joueur 2 a fini de jouer
        while bouton==False:
            #le deuxième joueur clique sur des points d'origine de faisceaux 
            x,y = clic(n)
            #Si les coordonnées cliquées sont celles d'un bord:
            if origine_faisceaux(x, y, n)==True:
                augementer_score(joueurs,tour_joueur2,1)
                #calculer la trajectoire du faisceau et renvoyer sa sortie
                sortie_x,sortie_y,etat=plateau.trajectoire_faisceau(x, y, n)
                if etat!="H" or (sortie_x==x and sortie_y==y): #Si le faisceau n'est pas absorbé, 1 point supplémentaire
                    augementer_score(joueurs,tour_joueur2,1)
                    afficher_plateau(plateau._plateau, joueurs, etat)
                    sortie(sortie_x, sortie_y, plateau._plateau)
                elif etat=="H":
                    afficher_plateau(plateau._plateau, joueurs, "HIT")
                
                #afficher la sortie du faisceau / etat
            
            afficher_score(joueurs)
            x,y = 0,0

        #le joueur 2 devine la position des balles à partir des résultats précédents
        for essai in range(n):
            essais=[]
            x,y = clic(n)
            while (x,y) in essais:
                #afficher message erreur: emplacement déjà testé
                x,y = clic()
            essais.append((x,y))
            if isinstance(plateau._plateau[x][y],Ball):
                #afficher message: balle trouvée
                pass
            else:
                #afficher message: mauvais emplacement
                augementer_score(joueurs,tour_joueur2,5)

# Pour affronter un bot
def mode_solo(n,p):
    #Le bot pose 4 balles aléatoirement
    #Le joueur essaie de retrouver les balles
    joueurs = [Joueur(1), Joueur(2)]

if contre_ordi:
    mode_solo(n,p)    
else:
    boucle_de_jeu(n,p)