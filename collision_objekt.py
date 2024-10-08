import pygame as pg
from typing import Final, TypeVar

Game = TypeVar("Game")

class CollisionRect:
    def __init__(self, game: Game, position: tuple[int], size: tuple[int]) -> None:
        """
        Initialize a collision rectangle.
        Args:
        game: The game object.
        position (tuple(int, int)): The position of the top left corner of the rectangle.
        size (tuple(int, int)): The size of the collision rectangle
        """
        self.game: Game = game
        self.position: Final[tuple[int]] = position
        self.size: Final[tuple[int]] = size
        self.rect: Final[pg.Rect] = pg.Rect(self.position, self.size)

    def draw(self, surf: pg.Surface) -> None:
        """
        Draw the collision rectangle on the given surface.
        Args:
        surf (pg.Surface): The surface to draw on.
        """
        pg.draw.rect(surf, (50, 50, 50), self.rect)
