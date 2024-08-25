
import pygame as pg
from typing import Final, TypeVar
import math


class PullBall:
    def __init__(self, x: int, y: int, radius: int, max_pull_length: int) -> None:
        self.pos: pg.Vector2 = pg.Vector2(x=x, y=y)
        self.radius: int = radius 
        self.max_pull_length: int = max_pull_length
        self.selected: bool = False
        self.pullball_image: pg.Surface = pg.image.load("pullball image.png").convert_alpha()
        new_image_width_height = self.pullball_image.get_width() / 2
        self.pullball_image = pg.transform.scale(self.pullball_image, (new_image_width_height, new_image_width_height))
        self.pullball_rect: pg.Rect = self.pullball_image.get_rect(center=self.pos)

    def check_pullball_action(self, cannon_x, cannon_y) -> None:
        """check if the pull ball is within the cannon's bounds"""
        mouse_pos = pg.mouse.get_pos()
        if self.pullball_rect.collidepoint(mouse_pos) and pg.mouse.get_pressed()[0]:
            self.pos.x = mouse_pos[0]
            self.pos.y = mouse_pos[1]
            self.pullball_rect.centerx = self.pos.x
            self.pullball_rect.centery = self.pos.y
        
        x_dist = cannon_x - mouse_pos[0]
        y_dist = cannon_y - mouse_pos[1]
        if math.sqrt(x_dist**2 + y_dist**2) <= self.max_pull_length:
            self.pos.x = mouse_pos[0]

    def draw(self, surf: pg.Surface) -> None:
        """draw the pullball on the screen"""
        # draw pullball
        surf.blit(self.pullball_image, self.pullball_rect)


