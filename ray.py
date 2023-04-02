import math

import pygame

from settings import *
from color import *

class Rays:
    def __init__(self, app, amount):
        self.app = app

        self.y = 0
        self.x = 0

        self.y_offset = 0
        self.x_offset = 0

        self.distance = 0

        #depth of feald
        self.dof = 0

        self.angle = 0
        self.amount = amount

        self.map_x = 0
        self.map_y = 0
        self.map_pos = 0
        self.v_map_value = ""
        self.h_map_value = ""

        self.color = 0

    def get_distance(self, ax, ay, bx, by, anges):
        return (math.sqrt((bx - ax) * (bx - ax) + (by - ay) * (by - ay)))

    def rays_draw(self, player):
        self.angle = player.angle - DAGREE * 25
        if self.angle < 0:
            self.angle += 2*PI
        if self.angle > 2*PI:
            self.angle -= 2*PI

        for index in range(self.amount):
            
            # HORIZONTAL LINES
            self.dof = 0
            h_max_distance = 1000000000
            hx = player.x
            hy = player.y
            atan = -1 / math.tan(self.angle)
            if self.angle > PI:  #looking up
                self.y = ((int(player.y) // self.app.level.size) * self.app.level.size) - 0.0000001
                self.x = (player.y - self.y) * atan + player.x
                self.y_offset = -self.app.level.size
                self.x_offset = -self.y_offset * atan
            if self.angle < PI:  #looking down
                self.y = ((int(player.y) // self.app.level.size) * self.app.level.size) + self.app.level.size
                self.x = (player.y - self.y) * atan + player.x
                self.y_offset = self.app.level.size
                self.x_offset = -self.y_offset * atan
            if self.angle == 0 or self.angle == PI: # looking side to side
                self.x = player.x
                self.y = player.y
                self.dof = RAY_MAX_DOF
            
            while self.dof < RAY_MAX_DOF:
                self.map_x = int(self.x) // self.app.level.size
                self.map_y = int(self.y) // self.app.level.size
                self.map_pos = self.map_y * self.app.level.size_x + self.map_x
                if self.map_pos > 0 and self.map_pos < self.app.level.size_x * self.app.level.size_y and self.app.level.level[self.map_pos] != ".":
                    self.h_map_value = self.app.level.level[self.map_pos]
                    hx = self.x
                    hy = self.y
                    h_max_distance = self.get_distance(player.x, player.y, hx, hy, self.angle)
                    self.dof = RAY_MAX_DOF
                else:
                    self.x += self.x_offset
                    self.y += self.y_offset
                    self.dof += 1

            # VERTICAL LINES
            self.dof = 0
            v_max_distance = 1000000000
            vx = player.x
            vy = player.y
            ntan = -math.tan(self.angle)
            if self.angle > PI2 and self.angle < PI3:  #looking left
                self.x = ((int(player.x) // self.app.level.size) * self.app.level.size) - 0.0000001
                self.y = (player.x - self.x) * ntan + player.y
                self.x_offset = -self.app.level.size
                self.y_offset = -self.x_offset * ntan
            if self.angle < PI2 or self.angle > PI3:  #looking right
                self.x = ((int(player.x) // self.app.level.size) * self.app.level.size) + self.app.level.size
                self.y = (player.x - self.x) * ntan + player.y
                self.x_offset = self.app.level.size
                self.y_offset = -self.x_offset * ntan
            if self.angle == 0 or self.angle == PI: # looking up or down
                self.x = player.x
                self.y = player.y
                self.dof = RAY_MAX_DOF
            
            while self.dof < RAY_MAX_DOF:
                self.map_x = int(self.x) // self.app.level.size
                self.map_y = int(self.y) // self.app.level.size
                self.map_pos = self.map_y * self.app.level.size_x + self.map_x
                if self.map_pos > 0 and self.map_pos < self.app.level.size_x * self.app.level.size_y and self.app.level.level[self.map_pos] != ".":
                    self.v_map_value = self.app.level.level[self.map_pos]
                    vx = self.x
                    vy = self.y
                    v_max_distance = self.get_distance(player.x, player.y, vx, vy, self.angle)
                    self.dof = RAY_MAX_DOF
                else:
                    self.x += self.x_offset
                    self.y += self.y_offset
                    self.dof += 1

            if v_max_distance < h_max_distance:
                self.x = vx
                self.y = vy
                self.distance = v_max_distance
                if self.v_map_value == "w":
                    self.color = WHITE
                if self.v_map_value == "r":
                    self.color = RED
                if self.v_map_value == "g":
                    self.color = GREEN
                if self.v_map_value == "b":
                    self.color = BLUE
            else:
                self.x = hx
                self.y = hy
                self.distance = h_max_distance
                if self.h_map_value == "w":
                    self.color = WHITE
                if self.h_map_value == "r":
                    self.color = RED
                if self.h_map_value == "g":
                    self.color = GREEN
                if self.h_map_value == "b":
                    self.color = BLUE

            pygame.draw.line(self.app.window, YELLOW, (player.x, player.y), (self.x, self.y), 3)

            # 3d walls
            cos_angle = player.angle - self.angle
            if cos_angle < 0:
                cos_angle += 2*PI
            if cos_angle > 2*PI:
                cos_angle -= 2*PI
            self.distance = self.distance * math.cos(cos_angle)

            lineh = (TILE_HEIGHT * 360) / self.distance
            if lineh > 360:
                lineh = 360

            lineo = 360 - lineh/2

            pygame.draw.line(self.app.window, self.color, (index * 8 + 210, lineo), (index * 8 + 210, lineh + lineo), 8)

            self.angle += DAGREE/2
            if self.angle < 0:
                self.angle += 2*PI
            if self.angle > 2*PI:
                self.angle -= 2*PI
