import pygame
import sys
pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
green = [0, 250, 0]
dark_green = [0, 100, 0]
white = [250, 250, 250]
black = [0, 0, 0]
red=(255, 0, 0)
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
    text = font.render(ath, True, white)
    text_rect = text.get_rect(center=(400, 50))
    window.blit(text, text_rect)

def afficher_score(joueurs):
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
    n = len(plateau)  # Nombre de cases dans la grille
    case_width = plateau_width // n
    case_height = plateau_height // n
    case_x = plateau_x + x * case_width
    case_y = plateau_y + y * case_height
    pygame.draw.rect(window, red, (case_x, case_y, case_width, case_height))
    pygame.display.update()

def grille_to_window_coords(plateau):
    n=len(plateau)
    case_width = plateau_width // n
    case_height = plateau_height // n
    x = plateau_x + n * case_width + case_width // 2
    y = plateau_y + n * case_height + case_height // 2
    return x, y

def clic(n):
    x, y = 0, 0
    for event in pygame.event.get():
        pygame.event.clear(eventtype= pygame.MOUSEBUTTONDOWN)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                case_width = plateau_width // n
                case_height = plateau_height // n
                x = (mouse_x - plateau_x) // case_width
                y = (mouse_y - plateau_y) // case_height
    return x, y
