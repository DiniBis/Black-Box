import pygame
import sys

pygame.init()

largeur_fenetre = 800
hauteur_fenetre = 600

fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

pygame.display.set_caption("Black Box")

blanc = (255, 255, 255)
noir = (0, 0, 0)
gris_clair = (200, 200, 200)

police_titre = pygame.font.Font(None, 74)
police_bouton = pygame.font.Font(None, 50)

texte_titre = police_titre.render("Black Box", True, noir)
rect_texte_titre = texte_titre.get_rect()
rect_texte_titre.center = (largeur_fenetre // 2, hauteur_fenetre // 6)

def afficher_boutons(boutons):
    for bouton in boutons:
        pygame.draw.rect(fenetre, gris_clair, bouton["rect"])
        texte_bouton = police_bouton.render(bouton["label"], True, noir)
        rect_texte_bouton = texte_bouton.get_rect(center=bouton["rect"].center)
        fenetre.blit(texte_bouton, rect_texte_bouton)

def Menu():
    n = 8  # Taille par défaut du plateau
    p = 5  # Nombre de balles par défaut
    contre_ordi = False  # Par défaut, jouer contre un autre joueur

    boutons_principal = [
        {"label": "Jouer", "rect": pygame.Rect(largeur_fenetre // 2 - 100, hauteur_fenetre // 2 - 60, 200, 50)},
        {"label": "Options", "rect": pygame.Rect(largeur_fenetre // 2 - 100, hauteur_fenetre // 2, 200, 50)},
        {"label": "Quitter", "rect": pygame.Rect(largeur_fenetre // 2 - 100, hauteur_fenetre // 2 + 60, 200, 50)},
    ]

    boutons_jouer = [
        {"label": "Commencer", "rect": pygame.Rect(largeur_fenetre // 2 - 100, hauteur_fenetre // 2 - 30, 200, 50)},
        {"label": "Retour", "rect": pygame.Rect(largeur_fenetre // 2 - 100, hauteur_fenetre // 2 + 30, 200, 50)},
    ]

    boutons_options = [
        {"label": f"Taille du plateau: {n}", "rect": pygame.Rect(largeur_fenetre // 2 - 150, hauteur_fenetre // 2 - 90, 300, 50)},
        {"label": f"Nombre de balles: {p}", "rect": pygame.Rect(largeur_fenetre // 2 - 150, hauteur_fenetre // 2 - 30, 300, 50)},
        {"label": f"Contre ordi: {'oui' if contre_ordi else 'non'}", "rect": pygame.Rect(largeur_fenetre // 2 - 150, hauteur_fenetre // 2 + 30, 300, 50)},
        {"label": "Retour", "rect": pygame.Rect(largeur_fenetre // 2 - 100, hauteur_fenetre // 2 + 90, 200, 50)},
    ]

    menu_actuel = "principal"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos_souris = pygame.mouse.get_pos()
                if menu_actuel == "principal":
                    for bouton in boutons_principal:
                        if bouton["rect"].collidepoint(pos_souris):
                            if bouton["label"] == "Jouer":
                                menu_actuel = "jouer"
                            elif bouton["label"] == "Options":
                                menu_actuel = "options"
                            elif bouton["label"] == "Quitter":
                                pygame.quit()
                                sys.exit()
                elif menu_actuel == "jouer":
                    for bouton in boutons_jouer:
                        if bouton["rect"].collidepoint(pos_souris):
                            if bouton["label"] == "Commencer":
                                return contre_ordi, n, p 
                            elif bouton["label"] == "Retour":
                                menu_actuel = "principal"
                elif menu_actuel == "options":
                    for bouton in boutons_options:
                        if bouton["rect"].collidepoint(pos_souris):
                            if bouton["label"].startswith("Taille du plateau"):
                                n = n + 1 if n < 12 else 4  # Cycle entre 4 et 12
                                bouton["label"] = f"Taille du plateau: {n}"
                            elif bouton["label"].startswith("Nombre de balles"):
                                p = p + 1 if p < 10 else 1  # Cycle entre 1 et 10
                                bouton["label"] = f"Nombre de balles: {p}"
                            elif bouton["label"].startswith("Contre ordi"):
                                contre_ordi = not contre_ordi
                                bouton["label"] = f"Contre ordi: {'oui' if contre_ordi else 'non'}"
                            elif bouton["label"] == "Retour":
                                menu_actuel = "principal"

        fenetre.fill(blanc)

        if menu_actuel == "principal":
            fenetre.blit(texte_titre, rect_texte_titre)
            afficher_boutons(boutons_principal)
        elif menu_actuel == "jouer":
            afficher_boutons(boutons_jouer)
        elif menu_actuel == "options":
            afficher_boutons(boutons_options)

        pygame.display.flip()