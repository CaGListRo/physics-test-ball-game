from cannon import Cannon

import pygame as pg
from time import time
from typing import Final, TypeVar



class PhysicsTestGame:
    def __init__(self) -> None:
        pg.init()
        self.window_width: int = 1600
        self.window_height: int = 900
        self.screen = pg.display.set_mode((self.window_width, self.window_height))
        self.fps: int = 0
        self.run: bool = True
        self.cannon = Cannon(self, x=200, y=self.window_height * 0.6, width=100, height=20)
        self.ball = None

    def handle_events(self, dt) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.run = False

    def draw_window(self) -> None:
        pg.display.set_caption(f"    Physics Test Game     FPS:{self.fps}")
        self.screen.fill((130, 130, 255))
        pg.draw.rect(self.screen, (32, 200, 32), (0, self.window_height / 3 * 2, self.window_width, self.window_height / 3))
        self.cannon.draw(self.screen)
        if self.ball:
            self.ball.draw(self.screen)

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

            self.handle_events(dt)
            self.cannon.update()
            if self.ball:
                self.ball.update(dt)
            self.draw_window()                


pg.quit()


if __name__ == "__main__":
    game = PhysicsTestGame()
    game.main()