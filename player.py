import math

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

        self.angle = 0.000000000000001

        self.delta_x = 0
        self.delta_y = 0

        # movement
        self.pressed_forward  = False
        self.pressed_backward = False
        self.pressed_left     = False
        self.pressed_right    = False

        self.turn_left = False
        self.turn_right = False

        # ray from player

    def player_event(self, event):
        # moving around
        # gotta be a better way to do this...
        if event.type == pygame.KEYDOWN:
            # move in xy plain
            if event.key == pygame.K_w:
                self.pressed_forward = True
            if event.key == pygame.K_s:
                self.pressed_backward = True
            #if event.key == pygame.K_a:
            #    self.pressed_left = True
            #if event.key == pygame.K_d:
            #    self.pressed_right = True

            #turning
            if event.key == pygame.K_LEFT:
                self.turn_left = True
            if event.key == pygame.K_RIGHT:
                self.turn_right = True

        if event.type == pygame.KEYUP:
            # move in xy plain
            if event.key == pygame.K_w:
                self.pressed_forward = False
            if event.key == pygame.K_s:
                self.pressed_backward = False
            #if event.key == pygame.K_a:
            #    self.pressed_left = False
            #if event.key == pygame.K_d:
            #    self.pressed_right = False

            #turning
            if event.key == pygame.K_LEFT:
                self.turn_left = False
            if event.key == pygame.K_RIGHT:
                self.turn_right = False

    def player_update(self):
        if self.pressed_forward:
            self.x += self.delta_x * PLAYER_SPEED
            self.y += self.delta_y * PLAYER_SPEED
        if self.pressed_backward:
            self.x -= self.delta_x * PLAYER_SPEED
            self.y -= self.delta_y * PLAYER_SPEED
        #if self.pressed_left:
        #    self.x -= (PI/self.delta_x) * 0.001
        #    self.y -= (PI/self.delta_y) * 0.001
        #if self.pressed_right:
        #    self.x += (PI/self.delta_x) * 0.001
        #    self.y += (PI/self.delta_y) * 0.001

        if self.turn_left:
            self.angle -= 0.003
            if (self.angle < 0):
                self.angle += 2*PI
            self.delta_x = math.cos(self.angle)
            self.delta_y = math.sin(self.angle)
        if self.turn_right:
            self.angle += 0.003
            if (self.angle > 2*PI):
                self.angle -= 2*PI
            self.delta_x = math.cos(self.angle)
            self.delta_y = math.sin(self.angle)

    def player_draw(self):
        pygame.draw.circle(self.app.window, PINK, (self.x, self.y), PLAYER_SIZE)
