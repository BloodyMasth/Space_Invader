import pygame
import random

class Monstre(pygame.sprite.Sprite):
    """
    La classe générant les monstres
    """
    def __init__(self):
        super().__init__()
        self.vitesse = 1
        self.monstre_img = pygame.image.load("Image/monstre1.png")
        self.rect = self.monstre_img.get_rect()
        self.rect.x = 200
        self.rect.y = 300
        self.droite_ou_gauche = 0
        self.droite_ou_gauche = random.choice([0, 1])

    def move(self):
        if self.droite_ou_gauche == 0:
            self.rect.x = self.rect.x + self.vitesse
            self.changer_sens()
        else:
            self.rect.x = self.rect.x - self.vitesse
            self.changer_sens()

    def changer_sens(self):
        if self.rect.x + self.rect.width > 1080:
            self.vitesse = self.vitesse * -1
        if self.rect.x < 0:
            self.vitesse = self.vitesse * -1
