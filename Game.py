import pygame
import random
from Vaisseau import Vaisseau
from Monstre import Monstre



class Game:
    """
    La class game permetant d'appeler la class joueur
    """
    def __init__(self, image):
        # créer un joueur
        self.player_groupe = pygame.sprite.Group
        self.player = Vaisseau()

        # capturer les touches appuyées
        self.pressed = {}

        # initialiser le premier groupe de monstre
        self.monstre_ligne_1 = pygame.sprite.Group()
        self.monstre_pos = []

        # initialisation des position de départ des monstres
        monstre_start_x = 20
        monstre_start_y = 400

        # initialisation de la direction de déplacement des monstres
        droite_ou_gauche = random.choice([0, 1])

        # creation des monstres
        for i in range(8):
            self.monstre = Monstre(image, monstre_start_x + 80 * i, monstre_start_y, droite_ou_gauche)
            self.monstre_ligne_1.add(self.monstre)
            self.monstre_pos.append(self.monstre)
            # print(monstre_start_x + 70 * i, self.monstre, self.monstre_ligne_1, self.monstre_pos)

