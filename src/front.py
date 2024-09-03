import pygame
import sys
pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
black = [0, 0, 0]
red=[255, 0, 0]
white = [250, 250, 250]
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Black Box')

plateau_image = pygame.image.load('board.png')
nouvelle_largeur = int(plateau_image.get_width() * 0.7)
nouvelle_hauteur = int(plateau_image.get_height() * 0.7)
plateau_image = pygame.transform.scale(plateau_image, (nouvelle_largeur, nouvelle_hauteur))
plateau_width, plateau_height = plateau_image.get_size()
plateau_x = (WINDOW_WIDTH - plateau_width) // 2
plateau_y = (WINDOW_HEIGHT - plateau_height) // 2

font = pygame.font.SysFont(None, 55)
placement = 0

def afficher_plateau(plateau, joueurs, ath):
    """
        IN : La grille, les joueurs et le texte à afficher
        OUT : None
        Affiche la grille et le texte à l'écran
    """
    window.fill(black)
    afficher_ath(ath)
    afficher_score(joueurs)
    window.blit(plateau_image, (plateau_x, plateau_y))
    n=len(plateau)
    case_width = plateau_width // n
    case_height = plateau_height // n
    # Dessiner les lignes horizontales de la grille
    for i in range(n+1):
        pygame.draw.line(window, white, (plateau_x, plateau_y + i * case_height), (plateau_x + plateau_width, plateau_y + i * case_height))
    # Dessiner les lignes verticales de la grille
    for j in range(n+1):
        pygame.draw.line(window, white, (plateau_x + j * case_width, plateau_y), (plateau_x + j * case_width, plateau_y + plateau_height))
    pygame.display.update()

def afficher_ath(ath):
    """
        IN : Le texte à afficher
        OUT : None
        Affiche le texte en haut de l'écran
    """
    text = font.render(ath, True, white)
    text_rect = text.get_rect(center=(400, 50))
    window.blit(text, text_rect)

def afficher_score(joueurs):
    """
        IN : Les joueurs
        OUT : None
        Affiche le score des joueurs
    """
    for joueur in joueurs:
        if joueur.numero==1: 
            text = font.render("J1:"+str(joueur.score), True, white)
            text_rect = text.get_rect(center=(200, 550))
            window.blit(text, text_rect)
        elif joueur.numero==2:
            text = font.render("J2:"+str(joueur.score), True, white)
            text_rect = text.get_rect(center=(600, 550))
            window.blit(text, text_rect)

def sortie(x, y, plateau):
    """
        IN : Les coordonnées de sortie du faisceau
        OUT : None
        Dessine un carré rouge à la sortie du faisceau
    """
    n = len(plateau)  # Nombre de cases dans la grille
    case_width = plateau_width // n
    case_height = plateau_height // n
    case_x = plateau_x + x * case_width
    case_y = plateau_y + y * case_height
    pygame.draw.rect(window, red, (case_x, case_y, case_width, case_height))
    pygame.display.update()

# Dimensions du bouton
bouton_largeur = 150
bouton_hauteur = 50
bouton_x = WINDOW_WIDTH - bouton_largeur - 30
bouton_y = 10 

def afficher_bouton():
    pygame.draw.rect(window, red, (bouton_x, bouton_y, bouton_largeur, bouton_hauteur))
    texte = font.render("PASSER", True, white)
    text_rect = texte.get_rect(center=(bouton_x + bouton_largeur // 2, bouton_y + bouton_hauteur // 2))
    window.blit(texte, text_rect)
    pygame.display.update()

def clic(n, bouton):
    x, y = 0, 0
    for event in pygame.event.get():
        pygame.event.clear(eventtype= pygame.MOUSEBUTTONDOWN)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                if bouton==True: #Si le bouton est sensé être affiché
                    if bouton_x <=mouse_x<= bouton_x+bouton_largeur and bouton_y <=mouse_y<= bouton_y+bouton_hauteur:
                        return True, True #a et b prennent la valeur True pour signifier que le bouton a été cliqué
                case_width = plateau_width // n
                case_height = plateau_height // n
                x = (mouse_x - plateau_x) // case_width
                y = (mouse_y - plateau_y) // case_height           
    return x, y
