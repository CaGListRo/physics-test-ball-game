import pygame as pg
from typing import Final, TypeVar
from math import sqrt

Game = TypeVar("Game")


class Ball:
    def __init__(self, game: Game, cannon_x: int, cannon_y: int, radius: int, color: str, speed: tuple[float], rebounce: float) -> None:
        """
        Initializes an ball object.
        Args:
        game (Game): The game object.
        cannon_x (int): The x-coordinate of the cannon.
        cannon_y (int): The y-coordinate of the cannon.
        radius (int): The radius of the ball.
        color (str): The color of the ball.
        speed (tuple[float]): The speed of the ball.
        rebounce (float): The rebounce of the ball.
        """
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
        # calculating the length of one side of the rect(square): a = side length, c = hypotenuse
        # c = sqrt(a² + a²) = sqrt(2a²) = a * sqrt(2)  =>  a = c / sqrt(2)
        self.rect_length: int = int(self.radius * 2 / sqrt(2))
        self.ball_rect: pg.Rect = pg.Rect(self.pos.x - self.rect_length / 2, self.pos.y - self.rect_length / 2, self.rect_length, self.rect_length)

    def check_collision_with_rects(self) -> None:
        """ Checks if the ball collides with any of the game's rectangles. """
        for rect in self.game.rects:
            if self.ball_rect.colliderect(rect.rect):
                if self.speed.x > 0:
                    # delta_x is the overlap of the self rect and the collision rect in x direction
                    delta_x = self.ball_rect.right - rect.rect.left
                    # self.pos.x = rect.rect.left - self.radius
                    self.ball_rect.right = rect.rect.left - 1
                elif self.speed.x < 0:
                    delta_x = rect.rect.right - self.ball_rect.left
                    # self.pos.x = rect.rect.right + self.radius
                    self.ball_rect.left = rect.rect.right + 1
                    
                if self.speed.y > 0:
                    # delta_y is the overlap of the self rect and the collision rect in y direction
                    delta_y = self.ball_rect.bottom - rect.rect.top
                    # self.pos.y = rect.rect.top - self.radius
                    self.ball_rect.bottom = rect.rect.top - 1
                elif self.speed.y < 0:
                    delta_y = rect.rect.bottom - self.ball_rect.top
                    # self.pos.y = rect.rect.bottom + self.radius
                    self.ball_rect.top = rect.rect.bottom + 1

                
                
                if abs(delta_x - delta_y) < 5:
                    self.speed.x = -self.speed.x * self.rebounce
                    self.speed.y = -self.speed.y * self.rebounce
                
                elif delta_x > delta_y:
                    self.speed.y = -self.speed.y * self.rebounce
                elif delta_y > delta_x:
                    self.speed.x = -self.speed.x * self.rebounce
                
                # self.ball_rect.centerx = self.pos.x
                # self.ball_rect.centery = self.pos.y

    def check_collision_with_ground(self) -> None:
        """ Checks if the ball collides with the ground. """
        if self.ball_rect.bottom >= 800 and self.speed.y > 0:
            self.ball_rect.bottom = 800 - 1
            self.speed.y = -self.speed.y * self.rebounce

    def update(self, dt: float) -> None:
        """
        Updates the ball position.
        Args:
        dt (float): The time difference between to frames
        """
        self.pos.x += self.speed.x * dt
        self.pos.y += self.speed.y * dt
        self.ball_rect.centerx = self.pos.x
        self.ball_rect.centery = self.pos.y

        if not self.airborne:
            if abs(sqrt((self.pos.x - self.cannon_x)**2 + (self.pos.y - self.cannon_y)**2)) + self.radius > self.game.cannon.width / 2:
                self.airborne = True
        else:
            self.speed.y += self.gravity

        if self.pos.x < 0 - self.radius or self.pos.x > self.game.WINDOW_WIDTH + self.radius:
            self.game.balls.remove(self)

        self.check_collision_with_ground()
        self.check_collision_with_rects()

    def draw(self, surf: pg.Surface) -> None:
        """
        Draws the ball on the given surface.
        Args:
        surf (pg.Surface): The surface to draw on.
        """
        pg.draw.circle(surf, self.color, self.pos, self.radius)