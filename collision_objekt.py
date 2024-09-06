import pygame as pg
from typing import Final, TypeVar

Game = TypeVar("Game")

class CollisionRect:
    def __init__(self, game: Game, position: tuple[int], size: tuple[int]) -> None:
        """
        Initialize a collision rectangle.
        Args:
        game: The game object.
        position (tuple(int, int)): The position of the rectangle.
        size (tuple(int, int)): The size of the collision rectangle
        """
        self.game: Game = game
        self.position: Final[tuple[int]] = position
        self.size: Final[tuple[int]] = size
