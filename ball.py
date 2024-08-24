import pygame as pg
from typing import Final, TypeVar


class Ball:
    def __init__(self, x: int, y: int, radius: int, color: str, direction: tuple[int], speed: float) -> None:
        self.x: int = x
        self.y: int = y
        self.radius: int = radius
        self.color: str = color
        self.direction: pg.Vector2 = pg.Vector2(direction)
        self.speed: float = speed