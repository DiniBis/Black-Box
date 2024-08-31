import random

class Joueur:
    def __init__(self,numero):
        self.score=0
        self.numero=numero

def augementer_score(joueurs,numero,points):
    """
        IN : La liste des joueurs, le numéro du joueur et le nombre de points à ajouter
        OUT : None
        Fontion qui augmente le score d'un joueur
    """
    for joueur in joueurs:
        if joueur.numero==numero:
            joueur.score+=points

class Ball:
    def __init__(self,joueur):
        self._joueur=joueur

    def getJoueur(self):
        return self._joueur

class Grille:
    def __init__(self,n=8):
        """ -1: hors plateau / 1: bord / 0: case libre"""
        self._plateau = []
        for ligne in range(n):
            #bords verticaux
            if ligne==0 or ligne==n-1:
                n_ligne=[]
                for colonne in range(n):
                    if colonne!=0 and colonne!=n-1:
                        n_ligne.append(1)
                    else:
                        n_ligne.append(-1)
                self._plateau.append(n_ligne)
            #bords horizontaux
            else:
                n_ligne=[]
                for colonne in range(n):
                    if colonne==0 or colonne==n-1:
                        n_ligne.append(1)
                    else:
                        n_ligne.append(0)
                self._plateau.append(n_ligne)      

    def placerBalle(self,joueur,x,y):
        """
            IN : Les coordonnées d'une balle
            OUT : False si l'emplacement n'est pas valide
            Effectue le placement d'une balle si l'emplacement choisi est valide
        """
        #Si les coordonnées sont valides:
        if self._plateau[x][y]==0:
            #Placer la balle
            self._plateau[x][y]=Ball(joueur)
        #Sinon, tant que les coordonnées ne sont pas valides:
        else:
            #préviens si le placement n'a pas été fait pour que la balle soit placé ailleurs
            return False
        
    def trajectoire_faisceau(self, x, y, n):
        """
            IN : Les coordonnées d'un point d'origine de faisceaux et la taille de la grille
            OUT : Les coordonnées de sortie du faisceau et son etat
            Fonction qui calcule la trajectoire d'un faisceau
        """
        if x==0: #haut
            direction=[1,0] #vers le bas
        elif x==n-1: #bas
            direction=[-1,0] #vers le haut
        elif y==0: #gauche
            direction=[0,1] #vers la droite
        else: #droite
            direction=[0,-1] #vers la gauche
        etat=""
        x+=direction[0]
        y+=direction[1]
        #tant que le faisceau n'est pas sorti du plateau
        while x+direction[0]!=0 and x+direction[0]!=n and y+direction[1]!=0 and y+direction[1]!=n:
            n_direction=self.changerDirection(x, y, direction)
            if n_direction=="H": #si la direction est "Hit"
                return None,None,"H" #une balle a été touchée, pas de sortie de laser
            elif n_direction!=direction: #si la direction a changé
                direction=n_direction
                etat="R" #etat R pour "Reflection"
            x+=direction[0]
            y+=direction[1]
        return x,y,etat
    
    def changerDirection(self, x, y, direction):
        """
            IN : La direction d'un rayon
            OUT : Sa nouvelle direction après avoir croisé les balles
        """
        x_dir=direction[0]
        y_dir=direction[1]
        #Si la direction est horizontale (y=0):
        if y_dir==0:
            #Si ses 2 diagonales sont occupées par des balles
            if isinstance(self._plateau[x+x_dir][y-1],Ball) and isinstance(self._plateau[x+x_dir][y+1],Ball):
                #Direction -> son opposée
                return [-x_dir,y_dir]
            #Si la diagonale haute est occupée par une balle
            elif isinstance(self._plateau[x+x_dir][y-1],Ball):
                #Direction -> bas
                return [0,1]
            #Si la diagonale basse est occupée par une balle
            elif isinstance(self._plateau[x+x_dir][y+1],Ball):
                #Direction -> haut
                return [0,-1]
            #Si la prochaine case est occupée par une balle
            elif isinstance(self._plateau[x+x_dir][y],Ball):
                #Direction -> Hit
                return "H"
            else:
                return direction
        #Si la direction est verticale (x=0):
        if x_dir==0:
            if isinstance(self._plateau[x-1][y+y_dir],Ball) and isinstance(self._plateau[x+1][y+y_dir],Ball):
                return [x_dir,-y_dir]
            #Si la diagonale gauche est occupée par une balle
            elif isinstance(self._plateau[x-1][y+y_dir],Ball):
                #Direction -> droite
                return [1,0]
            #Si la diagonale gauche est occupée par une balle
            elif isinstance(self._plateau[x+1][y+y_dir],Ball):
                #Direction -> gauche
                return [-1,0]
            #Si la prochaine case est occupée par une balle
            elif isinstance(self._plateau[x][y+y_dir],Ball):
                #Direction -> Hit
                return "H"
            else:
                return direction

def origine_faisceaux(x, y, n):
    """
        IN : Les coordonnées d'un point d'origine de faisceaux et la taille de la grille
        OUT : True si les coordonnées sont un bord, mais pas un coin
        Fonction qui vérifie si les coordonnées sont un bord, mais pas un coin
    """
    if (x==0 or x==n-1) and (y!=0 and y!=n-1):
        return True
    elif (y==0 or y==n-1) and (x!=0 and x!=n-1):
        return True
    else:
        return False
    
def victoire():
    return False

def coordonnee_alea(n):
    """
        Prends en entrée la taille du plateau, renvoie des coordonnées aléatoires pour le bot
    """
    x = random.randint(1, n - 1)
    y = random.randint(0, n - 1)
    return x, y