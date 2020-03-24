import pygame


class Monstre(pygame.sprite.Sprite):
    """
    La classe générant les monstres
    """
    def __init__(self, image, monstre_start_x, monstre_start_y, droite_ou_gauche):
        super().__init__()
        self.vitesse = 1
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = monstre_start_x
        self.rect.y = monstre_start_y
        self.droite_ou_gauche = droite_ou_gauche
        self.swap = False

    def move(self):
        if self.droite_ou_gauche == 0:
            self.rect.x = self.rect.x + self.vitesse
            # self.changer_sens()
        else:
            self.rect.x = self.rect.x - self.vitesse
            # self.changer_sens()

    def changer_sens(self):
        self.vitesse = self.vitesse * -1
        #self.rect.y = self.rect.y + self.rect.height

