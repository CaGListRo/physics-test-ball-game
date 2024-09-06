import pygame as pg
from typing import Final, TypeVar
from math import sqrt


class Ball:
    def __init__(self, game, cannon_x: int, cannon_y: int, radius: int, color: str, speed: tuple[float], rebounce: float) -> None:
        self.game = game
        self.cannon_x: int = cannon_x
        self.cannon_y: int = cannon_y
        self.pos: pg.Vector2 = pg.Vector2(self.cannon_x, self.cannon_y)
        self.radius: int = radius
        self.color: str = color
        self.speed: pg.Vector2 = pg.Vector2(speed)
        self.rebounce: float = rebounce
        self.airborne: bool = False
        self.gravity: float = 0.9

    def update(self, dt) -> None:
        if not self.airborne:
            if abs(sqrt((self.pos.x - self.cannon_x)**2 + (self.pos.y - self.cannon_y)**2)) + self.radius > self.game.cannon.width / 2:
                self.airborne = True
        else:
            self.speed.y += self.gravity
        self.pos.x += self.speed.x * dt
        self.pos.y += self.speed.y * dt

        if self.pos.x < 0 - self.radius or self.pos.x > self.game.WINDOW_WIDTH + self.radius:
            self.game.balls.remove(self)

        if self.pos.y + self.radius >= 800 and self.speed.y > 0:
            self.speed.y = -self.speed.y * self.rebounce



    def draw(self, surf) -> None:
        pg.draw.circle(surf, self.color, self.pos, self.radius)