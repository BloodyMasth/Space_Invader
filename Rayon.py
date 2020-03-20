import pygame


class Rayon(pygame.sprite.Sprite):
    """
    La class qui gére les projectiles lancer par notre personnage
    """
    def __init__(self, player):
        # appel de la super class
        super().__init__()
        self.vitesse_proj = 1
        self.player = player
        self.image = pygame.image.load("Image/tire vaisseaux.png")
        self.image = pygame.transform.scale(self.image, (5, 30))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 28
        self.rect.y = player.rect.y - 20

    def remove(self):
        # supprimer le projectile qui se trouve en dehors de l'écran
        self.player.all_projectile.remove(self)
        # print("proj supp")

    def move(self):
        self.rect.y = self.rect.y - self.vitesse_proj
        # verifier les collision avec les bordures
        if self.rect.y < 110:
            self.remove()

