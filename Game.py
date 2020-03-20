import pygame
from Vaisseau import Vaisseau
from Monstre import Monstre


class Game:
    """
    La class game permetant d'appeler la class joueur
    """
    def __init__(self):
        # créer un joueur
        self.player = Vaisseau()
        self.pressed = {}
        for i in range(8):
            self.monstre = Monstre()