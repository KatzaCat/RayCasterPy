import pygame

from settings import *
from color import *

from ray import *

class Player:
    def __init__(self, app):
        self.app = app
        
        # player info
        self.x = 5 * TILE_WIDTH
        self.y = 5 * TILE_HEIGHT

        # movement
        self.pressed_up    = False
        self.pressed_down  = False
        self.pressed_left  = False
        self.pressed_right = False

        # ray from player
        self.rays = Rays(app)

    def player_event(self, event):
        # moving around
        # gotta be a better way to do this...
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.pressed_up = True
            if event.key == pygame.K_s:
                self.pressed_down = True
            if event.key == pygame.K_a:
                self.pressed_left = True
            if event.key == pygame.K_d:
                self.pressed_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.pressed_up = False
            if event.key == pygame.K_s:
                self.pressed_down = False
            if event.key == pygame.K_a:
                self.pressed_left = False
            if event.key == pygame.K_d:
                self.pressed_right = False

    def player_update(self):
        if self.pressed_up:
            self.y -= PLAYER_SPEED
        if self.pressed_down:
            self.y += PLAYER_SPEED
        if self.pressed_left:
            self.x -= PLAYER_SPEED
        if self.pressed_right:
            self.x += PLAYER_SPEED

    def player_draw(self):
        pygame.draw.circle(self.app.window, PINK, (self.x, self.y), PLAYER_SIZE)
        self.rays.rays_draw(self.x, self.y)
