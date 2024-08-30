from ball import Ball
import pygame as pg
from typing import Final, TypeVar
import math


class PullBall:
    def __init__(self, game, x: int, y: int, radius: int, max_pull_length: int, cannon_lenght: int) -> None:
        self.game = game
        self.pos: pg.Vector2 = pg.Vector2(x=x, y=y)
        self.radius: int = radius 
        self.max_pull_length: int = max_pull_length + cannon_lenght / 2
        self.cannon_lenght: int = cannon_lenght
        self.selected: bool = False
        self.pullball_image: pg.Surface = pg.image.load("pullball image.png").convert_alpha()
        new_image_width_height = self.pullball_image.get_width() / 2
        self.pullball_image = pg.transform.scale(self.pullball_image, (new_image_width_height, new_image_width_height))
        self.pullball_rect: pg.Rect = self.pullball_image.get_rect(center=self.pos)
        self.angle_alpha: float = 0.0

    def check_pullball_action(self, cannon_x, cannon_y) -> float:
        """check if the pull ball is within the cannon's bounds"""
        mouse_pos = pg.mouse.get_pos()

        if self.pullball_rect.collidepoint(mouse_pos) and pg.mouse.get_pressed()[0]:
            self.selected = True
        elif not pg.mouse.get_pressed()[0] and self.selected:
            speed = (math.sqrt((cannon_x - self.pos.x)**2 + (cannon_y - self.pos.y)**2) - self.cannon_lenght / 2) * 10
            x_direction = 1 * math.cos(math.radians(self.angle_alpha))
            y_direction = 1 * math.sin(math.radians(self.angle_alpha))
            direction = (x_direction, y_direction)
            self.game.ball = Ball(x=cannon_x, y=cannon_y, radius=self.radius, color="blue", direction=direction, speed=speed)
            self.selected = False
            print(speed)
            
        if self.selected:
            mouse_pull_x = cannon_x - mouse_pos[0]  # distance between the point of reference (turning point of the cannon)
            mouse_pull_y = cannon_y - mouse_pos[1]  # to the mouse cursor x and y
            mouse_pull_vector = math.sqrt(mouse_pull_x**2 + mouse_pull_y**2)  # calculating the mouse_pull_vector

            self.angle_alpha = math.degrees(math.atan2(mouse_pull_y, mouse_pull_x))  # calculating the angle of the cannon (angle alpha)
            if mouse_pull_vector <= self.max_pull_length:
                self.pos.x = mouse_pos[0]
                self.pos.y = mouse_pos[1]           
            else:
                self.pos.x = int(cannon_x - self.max_pull_length * math.cos(math.radians(self.angle_alpha)))
                self.pos.y = int(cannon_y - self.max_pull_length * math.sin(math.radians(self.angle_alpha)))
                
            self.pullball_rect.centerx = self.pos.x
            self.pullball_rect.centery = self.pos.y
        print(self.angle_alpha)
        return -self.angle_alpha

    def draw(self, surf: pg.Surface) -> None:
        """draw the pullball on the screen"""
        # draw pullball
        surf.blit(self.pullball_image, self.pullball_rect)


