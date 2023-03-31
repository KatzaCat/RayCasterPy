import pygame

from color import *

class Rays:
    def __init__(self, app):
        self.app = app

    def rays_draw(self, player_x, player_y):
        pygame.draw.line(self.app.window, YELLOW, (player_x, player_y), (player_x, player_y - 20), 1)