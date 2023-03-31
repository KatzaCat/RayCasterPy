import pygame

from settings import *
from color import *

class Level:
    def __init__(self, app, file, size_x, size_y):
        self.app = app
        
        self.file = file
        
        self.level = self.init_level()
        self.size_x = size_x
        self.size_y = size_y

        # blocks
        self.WALL      = pygame.Surface(TILE_SIZE) # 1
        self.WALLRED   = pygame.Surface(TILE_SIZE) # 2
        self.WALLGREEN = pygame.Surface(TILE_SIZE) # 3
        self.WALLBLUE  = pygame.Surface(TILE_SIZE) # 4

        self.WALL.fill(WHITE)
        self.WALLRED.fill(RED)
        self.WALLGREEN.fill(GREEN)
        self.WALLBLUE.fill(BLUE)

    def init_level(self):
        rv = []
        with open(self.file, "r") as file:
            rv = file.read()
            rv = rv.replace(" ", "")
            rv = rv.replace("\n", "")

        return rv
    
    def level_draw(self):
        # draws map
        for y in range(self.size_y):
            for x in range(self.size_x):
                if self.level[y * self.size_x + x] == "1":
                    self.app.window.blit(self.WALL, (x * TILE_WIDTH, y * TILE_HEIGHT))
                elif self.level[y * self.size_x + x] == "2":
                    self.app.window.blit(self.WALLRED, (x * TILE_WIDTH, y * TILE_HEIGHT))
                elif self.level[y * self.size_x + x] == "3":
                    self.app.window.blit(self.WALLGREEN, (x * TILE_WIDTH, y * TILE_HEIGHT))
                elif self.level[y * self.size_x + x] == "4":
                    self.app.window.blit(self.WALLBLUE, (x * TILE_WIDTH, y * TILE_HEIGHT))