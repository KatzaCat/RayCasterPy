import pygame

from settings import *

from player import Player

from level import Level

pygame.init()

class RayCaster:
    def __init__(self):
        self.window = pygame.display.set_mode(WINDOW_SIZE)
        self.quit = False

        self.time = pygame.time.Clock()

        self.player = Player(self)

        self.level = Level(self, "level.txt", 20, 20)

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            self.player.player_event(event)

    def draw(self):
        self.window.fill(WINDOW_BACKGROUND_COLOR)
        self.player.player_draw()
        self.level.level_draw()
        pygame.display.flip()

    def update(self):
        fps = str(int(self.time.get_fps()))
        pygame.display.set_caption(WINDOW_TITLE + " FPS:" + fps)
        self.player.player_update()
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
