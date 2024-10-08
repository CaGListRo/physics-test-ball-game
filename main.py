from cannon import Cannon
from collision_objekt import CollisionRect

import pygame as pg
from time import time
from random import randint
from typing import Final, TypeVar



class PhysicsTestGame:
    WINDOW_WIDTH: Final[int] = 1600
    WINDOW_HEIGHT: Final[int] = 900

    def __init__(self) -> None:
        """ The initializer of the main game class. """
        pg.init()
        self.screen = pg.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.fps: int = 0
        self.run: bool = True
        self.cannon = Cannon(self, x=200, y=self.WINDOW_HEIGHT * 0.6, width=100, height=20)
        self.balls: list = []
        self.rects: list = []
        self.create_rects()
    
    def create_rects(self) -> None:
        """ Creates a list of rectangles. """

        # "backwall"
        # rect = CollisionRect(game=self, position=(self.WINDOW_WIDTH -20, 0), size=(10, self.WINDOW_HEIGHT))
        self.rects.append(CollisionRect(game=self, position=(self.WINDOW_WIDTH -20, 0), size=(10, self.WINDOW_HEIGHT)))
        # middle wall
        # rect = CollisionRect(game=self, position=(self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2), size=(10, self.WINDOW_HEIGHT / 2))
        self.rects.append(CollisionRect(game=self, position=(self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2), size=(10, self.WINDOW_HEIGHT / 2)))
        # other walls
        # rect = CollisionRect(game=self, position=(self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2), size=(self.WINDOW_WIDTH / 3, 10))
        self.rects.append(CollisionRect(game=self, position=(self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2), size=(self.WINDOW_WIDTH / 3, 10)))
        # rect = CollisionRect(game=self, position=(self.WINDOW_WIDTH / 2 + self.WINDOW_WIDTH / 3, self.WINDOW_HEIGHT / 2), size=(10, self.WINDOW_HEIGHT / 4))
        self.rects.append(CollisionRect(game=self, position=(self.WINDOW_WIDTH / 2 + self.WINDOW_WIDTH / 3, self.WINDOW_HEIGHT / 2), size=(10, self.WINDOW_HEIGHT / 4)))

    def handle_events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.run = False

    def draw_window(self) -> None:
        pg.display.set_caption(f"    Physics Test Game     FPS:{self.fps}")
        self.screen.fill((130, 130, 255))
        pg.draw.rect(self.screen, (32, 200, 32), (0, self.WINDOW_HEIGHT / 3 * 2, self.WINDOW_WIDTH, self.WINDOW_HEIGHT / 3))
        if len(self.balls) > 0:
            for ball in self.balls:
                ball.draw(self.screen)
                # print(ball.speed, ball.pos)
        self.cannon.draw(self.screen)
        for rect in self.rects:
            rect.draw(self.screen)
        
        pg.display.flip()

    def main(self) -> None:
        old_time = time()
        frame_counter: int = 0
        frame_timer: float = 0
        while self.run:
            
            # calculating delta time
            dt = time() - old_time
            old_time = time()

            # counting frames per second
            frame_counter += 1
            frame_timer += dt
            if frame_timer >= 1:
                self.fps = frame_counter
                frame_counter = 0
                frame_timer = 0

            self.handle_events()
            self.cannon.update()
            if len(self.balls) > 0:
                for ball in self.balls:
                    ball.update(dt)
                    # print(ball.pos)

            self.draw_window()          


pg.quit()


if __name__ == "__main__":
    game = PhysicsTestGame()
    game.main()