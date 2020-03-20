import pygame
from Rayon import Rayon


class Vaisseau(pygame.sprite.Sprite):
    """
    La classe générant le joueur
    """
    def __init__(self):
        super().__init__()
        self.attack = 10
        self.vitesse = 1
        self.all_projectile = pygame.sprite.Group()
        self.player_img = pygame.image.load("Image/vaisseauxj1.png")
        self.rect = self.player_img.get_rect()
        self.rect.x = 500
        self.rect.y = 650

    def launch_projectile(self):
        # creer un nouvelle instace de la class projectile
        self.all_projectile.add(Rayon(self))

    def move_right(self):
        self.rect.x = self.rect.x + self.vitesse

    def move_left(self):
        self.rect.x = self.rect.x - self.vitesse