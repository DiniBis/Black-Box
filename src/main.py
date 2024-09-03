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
    tour=0
    scoreJ1=0
    scoreJ2=0
    for tour in range(10):
        tour_joueur= 1 if tour%2!=0 else 2
        tour_joueur2= 2 if tour%2!=0 else 1
        #création de la grille
        plateau=Grille(n)

        #le premier joueur pose ses balles (par défaut p=4)
        afficher_plateau(plateau._plateau, joueurs, "Reste à placer "+str(p)+" balles")
        for i in range(p):
            x,y = clic(n,False)
            est_place=plateau.placerBalle(tour_joueur,x,y)
            afficher_plateau(plateau._plateau, joueurs, "Reste à placer "+str(p-i)+" balles")
            while est_place==False:
                x,y = clic(n,False)
                est_place=plateau.placerBalle(tour_joueur,x,y)   
        afficher_plateau(plateau._plateau, joueurs, "Changemet de joueur")

        bouton=False #bouton permet de sortir de la boucle si le joueur 2 a fini de jouer
        afficher_bouton()
        while bouton==False:
            afficher_bouton()
            #le deuxième joueur clique sur des points d'origine de faisceaux 
            x,y = clic(n,True) #True pour prendre en compte le bouton
            if x==True and y==True:
                bouton=True
                break
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
            #màj de l'affichage du score
            afficher_score(joueurs)
        afficher_plateau(plateau._plateau, joueurs, "Trouve l'emplacement des "+str(p)+" balles")
        #le joueur 2 devine la position des balles à partir des résultats précédents
        essais=[]
        for i in range(p):        
            x,y = clic(n,False)
            essai=[x,y]
            while (essai in essais) or (x==0 and y==0):
                x,y = clic(n,False)
                essai=[x,y]
            if isinstance(plateau._plateau[x][y],Ball):
                afficher_plateau(plateau._plateau, joueurs, str(i+1)+":    Balle trouvée")
                essais.append(essai) #pour empêcher de cliquer sur la même case valide
            else:
                afficher_plateau(plateau._plateau, joueurs, str(i+1)+":    Raté")
                augementer_score(joueurs,tour_joueur2,5)
            afficher_score(joueurs)
        
        #Chaque joueur a fait une manche
        if tour%2!=0:
            if joueurs[0].score<joueurs[1].score:
                scoreJ1+=1
                afficher_plateau(plateau._plateau, joueurs, "Joueur 1 a gagné "+str(scoreJ1)+" manche(s)")
            elif joueurs[0].score>joueurs[1].score:
                scoreJ2+=1
                afficher_plateau(plateau._plateau, joueurs, "Joueur 2 a gagné "+str(scoreJ2)+" manche(s)")
            else:
                scoreJ1+=1
                scoreJ2+=1
            bouton=False
            afficher_bouton()
            while bouton==False:
                if tour+1==10:
                    afficher_plateau(plateau._plateau, joueurs, "Joueur 1: "+str(scoreJ1)+"  Joueur 2: "+str(scoreJ2))
                x,y = clic(n,True) #True pour prendre en compte le bouton
                afficher_bouton()
                if x==True and y==True:
                    bouton=True
                    #bouton continuer -> remettre les scores de la manche à 0
                    joueurs[0].score,joueurs[1].score=0,0
                    if tour+1==10:
                        boucle_de_jeu(n,p)


# Pour affronter un bot
def mode_solo(n,p):
    """
        Fonction qui permet de jouer contre un bot
        Le bot pose "p" balles aléatoirement, le joueur doit les retrouver avec le meilleur score possible
    """
    joueurs = [Joueur(1), Joueur(2)]
    plateau=Grille(n)
    afficher_plateau(plateau._plateau, joueurs, "Reste à placer "+str(p)+" balles")
    for i in range(p):
        x,y = coordonnee_alea(n)
        est_place=plateau.placerBalle(1,x,y)
        afficher_plateau(plateau._plateau, joueurs, "Reste à placer "+str(p-i)+" balles")
        while est_place==False:
            x,y = coordonnee_alea(n)
            est_place=plateau.placerBalle(1,x,y)   
    afficher_plateau(plateau._plateau, joueurs, "à toi de retrouver les "+str(p)+" balles")

    bouton=False
    afficher_bouton()
    while bouton==False:
        afficher_bouton()
        x,y = clic(n,True)
        if x==True and y==True:
            bouton=True
            break
        if origine_faisceaux(x, y, n)==True:
            augementer_score(joueurs,2,1)
            sortie_x,sortie_y,etat=plateau.trajectoire_faisceau(x, y, n)
            if etat!="H" or (sortie_x==x and sortie_y==y):
                augementer_score(joueurs,2,1)
                afficher_plateau(plateau._plateau, joueurs, etat)
                sortie(sortie_x, sortie_y, plateau._plateau)
            elif etat=="H":
                afficher_plateau(plateau._plateau, joueurs, "HIT")
        afficher_score(joueurs)
    afficher_plateau(plateau._plateau, joueurs, "Trouve l'emplacement des "+str(p)+" balles")

    essais=[]
    for i in range(p):        
        x,y = clic(n,False)
        essai=[x,y]
        while (essai in essais) or (x==0 and y==0):
            x,y = clic(n,False)
            essai=[x,y]
        if isinstance(plateau._plateau[x][y],Ball):
            afficher_plateau(plateau._plateau, joueurs, str(i+1)+":    Balle trouvée")
            essais.append(essai) #pour empêcher de cliquer sur la même case valide
        else:
            afficher_plateau(plateau._plateau, joueurs, str(i+1)+":    Raté")
            augementer_score(joueurs,2,5)
        afficher_score(joueurs)

    bouton=False
    afficher_plateau(plateau._plateau, joueurs, "Continuer ?")
    afficher_bouton()
    while bouton==False:
        x,y = clic(n,True) #True pour prendre en compte le bouton
        if x==True and y==True:
            bouton=True
            mode_solo(n,p)

if contre_ordi:
    mode_solo(n,p)    
else:
    boucle_de_jeu(n,p)