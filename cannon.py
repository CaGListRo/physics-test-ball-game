from pullball import PullBall

import pygame as pg
from typing import Final, TypeVar


class Cannon:
    def __init__(self, game, x: int, y: int, width: int, height: int) -> None:
        self.game = game
        self.x: int = x
        self.y: int = y
        # cannon settings
        self.width: int = width
        self.height: int = height
        self.cannon_topleft: tuple[int] = (self.x - self.width / 2, self.y - self.height / 2)
        self.cannon_image: pg.Surface = pg.image.load("silly cannon image.png").convert_alpha()
        self.cannon_image = pg.transform.scale(self.cannon_image, (self.width, self.height))
        self.cannon_rect:pg.Rect = self.cannon_image.get_rect(center=(self.x, self.y))
        self.angle: float = 0.0
        # turret settings
        turret_width: int = int(self.height / 2)
        turret_height: int = int(self.width * 1.5)
        self.turret: pg.Rect = pg.Rect(self.x - turret_width / 2, self.y - turret_width / 2, turret_width, turret_height)
        # pullball settings
        self.pullball_radius: int = int(self.height * 0.45)
        self.pullball = PullBall(self.game, x=(self.x - self.width / 2 - self.pullball_radius), y=self.y, radius=int(self.height * 0.45), max_pull_length=int(self.width * 0.8), cannon_length=self.width)
        self.max_pull_length: int = int(width * 0.8)

    def update(self) -> None:
        self.angle = self.pullball.check_pullball_action(cannon_x=self.x, cannon_y=self.y)

    def draw(self, surf: pg.Surface) -> None:
        """draw the cannon on the screen"""
        self.pullball.draw(surf)
        # rotate the cannon
        self.rotated_cannon_image = pg.transform.rotate(surface=self.cannon_image, angle=self.angle)
        #create new "rotated" rect of the rotated cannon image
        self.rotated_cannon_rect = self.rotated_cannon_image.get_rect(center=(self.x, self.y))
        # draw cannon on the given surface
        surf.blit(source=self.rotated_cannon_image, dest=self.rotated_cannon_rect)
        # draw the turret rect
        pg.draw.rect(surf, (100, 100, 100), self.turret)


