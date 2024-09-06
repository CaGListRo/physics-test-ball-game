from ball import Ball
import pygame as pg
from typing import Final, TypeVar
import math

Game = TypeVar("Game")

class PullBall:
    def __init__(self, game: Game, x: int, y: int, radius: int, max_pull_length: int, cannon_length: int) -> None:
        """
        Initialize a pullball object.
        Args:
        game (Game): The game object.
        x (int): The x-coordinate of the pullball.
        y (int): The y-coordinate of the pullball.
        radius (int): The radius of the pullball.
        max_pull_length (int): The maximum length of the pull.
        cannon_length (int): The length of the cannon.
        """
        self.game: Game = game
        self.pos: pg.Vector2 = pg.Vector2(x=x, y=y)
        self.radius: int = radius 
        self.max_pull_length: int = max_pull_length + cannon_length / 2
        self.cannon_length: int = cannon_length
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
            # calculating the speed vector for the bacll(projectile)
            pull_ball_pulled_length: float = (math.sqrt((cannon_x - self.pos.x)**2 + (cannon_y - self.pos.y)**2) - self.cannon_length / 2)*10
            #calculating the x and y speed out of the speed vector
            x_speed: float = 1 * math.cos(math.radians(self.angle_alpha)) * pull_ball_pulled_length
            y_speed: float = 1 * math.sin(math.radians(self.angle_alpha)) * pull_ball_pulled_length
            speed: tuple[float] = (x_speed, y_speed)
            self.game.balls.append(Ball(self.game, cannon_x=cannon_x, cannon_y=cannon_y, radius=self.radius, color="blue", speed=speed, rebounce=0.8))
            self.selected = False
            self.pos.x = int(cannon_x - (self.cannon_length / 2 + self.radius) * math.cos(math.radians(self.angle_alpha)))
            self.pos.y = int(cannon_y - (self.cannon_length / 2 + self.radius) * math.sin(math.radians(self.angle_alpha)))
            self.pullball_rect.centerx = self.pos.x
            self.pullball_rect.centery = self.pos.y
            
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
        return -self.angle_alpha

    def draw(self, surf: pg.Surface) -> None:
        """draw the pullball on the screen"""
        # draw pullball
        surf.blit(self.pullball_image, self.pullball_rect)


