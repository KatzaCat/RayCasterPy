import pygame

from settings import *

from level import Level

pygame.init()

WALL = pygame.Surface(TILE_SIZE)      # 1
WALLRED = pygame.Surface(TILE_SIZE)   # 2
WALLGREEN = pygame.Surface(TILE_SIZE) # 3
WALLBLUE = pygame.Surface(TILE_SIZE)  # 4

WALL.fill((255, 255, 255))
WALLRED.fill((255, 0, 0))
WALLGREEN.fill((0, 255, 0))
WALLBLUE.fill((0, 0, 255))

class RayCaster:
    def __init__(self):
        self.window = pygame.display.set_mode(WINDOW_SIZE)
        self.quit = False

        self.time = pygame.time.Clock()

        self.level = Level("level.txt", 10, 10)

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True

    def draw(self):
        self.window.fill(WINDOW_BACKGROUND_COLOR)

        # draws map
        for y in range(self.level.size_y):
            for x in range(self.level.size_x):
                if self.level.level[y * self.level.size_x + x] == "1":
                    self.window.blit(WALL, (x * TILE_WIDTH, y * TILE_HEIGHT))
                elif self.level.level[y * self.level.size_x + x] == "2":
                    self.window.blit(WALLRED, (x * TILE_WIDTH, y * TILE_HEIGHT))
                elif self.level.level[y * self.level.size_x + x] == "3":
                    self.window.blit(WALLGREEN, (x * TILE_WIDTH, y * TILE_HEIGHT))
                elif self.level.level[y * self.level.size_x + x] == "4":
                    self.window.blit(WALLBLUE, (x * TILE_WIDTH, y * TILE_HEIGHT))

        pygame.display.flip()

    def update(self):
        fps = str(int(self.time.get_fps()))
        pygame.display.set_caption(WINDOW_TITLE + " FPS:" + fps)
        self.draw()
        self.time.tick(FPS_CAP)

    def loop(self):
        while not self.quit:
            self.event()
            self.update()

def main():
    app = RayCaster()
    app.loop()

if __name__ == "__main__":
    main()