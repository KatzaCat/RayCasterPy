import pygame

from settings import *

pygame.init()

class RayCaster:
    def __init__(self):
        self.window = pygame.display.set_mode(WINDOW_SIZE)
        self.quit = False

        self.time = pygame.time.Clock()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
                quit()

    def update(self):
        fps = str(int(self.time.get_fps()))
        pygame.display.set_caption(WINDOW_TITLE + " FPS:" + fps)
        self.window.fill(WINDOW_BACKGROUND_COLOR)
        pygame.display.flip()
        self.time.tick(FPS_CAP)

    def loop(self):
        while not self.quit:
            self.event()
            self.update()

def main():
    app = RayCaster()
    app.loop()

    # print("hello world")

if __name__ == "__main__":
    main()