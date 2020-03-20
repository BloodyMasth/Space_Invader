# Importer le module pygame
import pygame
# Importer la class game
from Game import Game
# Initialiser le module
pygame.init()


# générer la fenètre
# Titre
pygame.display.set_caption("Space Invader")
# Taille
gamediplay = pygame.display.set_mode((1080, 720))

# chargement du fond de fenètre
background = pygame.image.load("Image/space_bg.gif")

# chargement de la bande blanche
grande_bande_haut = pygame.image.load("Image/bande blanche.png")
grande_bande_haut = pygame.transform.scale(grande_bande_haut, (1080, 10))

# chargement du jeu
game = Game()

# initialisation de la variable boucle du jeu
running = True

# boucle du jeu
while running:
    # print(game.pressed, game.player.all_projectile)
    # afficher le fond de la fenètre
    gamediplay.blit(background, (0, 0))

    # afficher la bande blanche
    gamediplay.blit(grande_bande_haut, (0, 100))

    # afficher l'image du joueur
    gamediplay.blit(game.player.player_img, game.player.rect)

    # Réaliser les déplacement du joueur
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < 1080:
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > -10:
        game.player.move_left()

    # recuperation des projectiles pour les faire bouger
    for projectile in game.player.all_projectile:
        projectile.move()

    # afficher tout les projectile du groupe
    game.player.all_projectile.draw(gamediplay)

    # affiche un seul monstre
    gamediplay.blit(game.monstre.monstre_img, game.monstre.rect)

    # Réaliser les déplacements du monstre
    game.monstre.move()


    # mise à jour de l'affichage
    pygame.display.flip()


    for event in pygame.event.get():
        # pour fermer la fenètre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            # Si la touche espace est appuyé
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
                #print("ici")
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
