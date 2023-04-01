import pygame

from settings import *
from color import *

class Level:
    def __init__(self, app, file, size_x, size_y):
        self.app = app
        
        self.file = file
        
        # level stuff
        self.level = self.init_level()
        self.size_x = size_x
        self.size_y = size_y

        # blocks
        self.size = TILE_WIDTH

        self.WALL      = pygame.Surface(TILE_SIZE_S) # 1
        self.WALLRED   = pygame.Surface(TILE_SIZE_S) # 2
        self.WALLGREEN = pygame.Surface(TILE_SIZE_S) # 3
        self.WALLBLUE  = pygame.Surface(TILE_SIZE_S) # 4

        self.FLOR = pygame.Surface(TILE_SIZE_S) # 0

        self.WALL.fill(WHITE)
        self.WALLRED.fill(RED)
        self.WALLGREEN.fill(GREEN)
        self.WALLBLUE.fill(BLUE)

        self.FLOR.fill(GREAY)

    def init_level(self):
        rv = []
        with open(self.file, "r") as file:
            rv = file.read()

            # realize that i could just not include spaces, but 
            # spaces make it look better whaen wrting it out
            rv = rv.replace(" ", "")
            rv = rv.replace("\n", "")

        return rv
    
    def level_draw(self):
        # draws map
        for y in range(self.size_y):
            for x in range(self.size_x):
                # sure there is a better way to do this...
                # well we'll find out later
                if self.level[y * self.size_x + x] == ".":
                    self.app.window.blit(self.FLOR, (x * TILE_WIDTH, y * TILE_HEIGHT))
                elif self.level[y * self.size_x + x] == "w":
                    self.app.window.blit(self.WALL, (x * TILE_WIDTH, y * TILE_HEIGHT))
                elif self.level[y * self.size_x + x] == "r":
                    self.app.window.blit(self.WALLRED, (x * TILE_WIDTH, y * TILE_HEIGHT))
                elif self.level[y * self.size_x + x] == "g":
                    self.app.window.blit(self.WALLGREEN, (x * TILE_WIDTH, y * TILE_HEIGHT))
                elif self.level[y * self.size_x + x] == "b":
                    self.app.window.blit(self.WALLBLUE, (x * TILE_WIDTH, y * TILE_HEIGHT))
