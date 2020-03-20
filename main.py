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
# redimensionnement du fond de la fenètre
background = pygame.image.load("Image/space_bg.gif")
background = pygame.transform.scale(background, (1080, 720))

# chargement du premier monstre
image = pygame.image.load("Image/monstre1.png")

# chargement de la bande blanche
# redimensionnement de la bande blanche
grande_bande_haut = pygame.image.load("Image/bande blanche.png")
grande_bande_haut = pygame.transform.scale(grande_bande_haut, (1080, 10))

# chargement du jeu
game = Game(image)

# initialisation du score
score = 0

# initialisation de la variable boucle du jeu
running = True

# boucle du jeu
while running:
    # print(game.pressed, game.player.all_projectile)
    # gamediplay.fill((0, 0, 0, 0))
    # afficher le fond de la fenètre
    gamediplay.blit(background, (0, 0))

    # initialisation du nombre maximum de projectile
    max_projectile = 3

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
    # print(game.player.all_projectile)

    # affiche les monstres d'un groupe
    game.monstre_ligne_1.draw(gamediplay)

    # Réaliser les déplacements des monstres
    for monstre_1_pos in game.monstre_ligne_1:
        monstre_1_pos.move()
        #print(monstre_1_pos.rect.x, game.monstre_ligne_1, game.monstre_pos)
        #print(type(game.monstre_pos))
        # monstre_1_pos.changer_sens()

        if game.monstre_pos[0].rect.x < 0:
            monstre_1_pos.changer_sens()
        elif game.monstre_pos[-1].rect.x + game.monstre_pos[-1].rect.width > 1080:
            monstre_1_pos.changer_sens()
            #print(type(game.monstre_ligne_1))

    # Collision Rayon/ALien
    for projectile in game.player.all_projectile:
        collision = pygame.sprite.groupcollide(game.monstre_ligne_1, game.player.all_projectile, True, True)
        #print(collision)
        if collision:
            #game.player.all_projectile.remove(projectile)
            #print(game.monstre_pos, projectile)
            score = score + 20
            print(score)

    # mise à jour de l'affichage
    pygame.display.flip()

    # gestion des différent événements
    for event in pygame.event.get():
        # pour fermer la fenètre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # lorsqu'une touche est appuyé
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            # Si la touche espace est appuyé
            if event.key == pygame.K_SPACE:
                if len(game.player.all_projectile) < max_projectile:
                    game.player.launch_projectile()
                    # print("ici")
        # lorsqu'une touche est relaché
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
