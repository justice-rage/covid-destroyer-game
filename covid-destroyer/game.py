# 3rd Party Imports:
import pygame

# Internal Imports:
from models import GameObject
from utils import load_sprite


class COVID:
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite("green", False)
        self.plague_doctor = GameObject(
            (400, 300), load_sprite("plague_doctor"), (0, 0)
        )
        self.covid = GameObject(
            (400, 300), load_sprite("covid"), (1, 0)
        )

    def main_loop(self):
        while True:
            self._handle_input()
            self._process_game_logic()
            self._draw()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("COVID Destroyer")

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                quit()

    def _process_game_logic(self):
        self.plague_doctor.move()
        self.covid.move()

    def _draw(self):
        self.screen.blit(self.background, (0, 0))
        self.plague_doctor.draw(self.screen)
        self.covid.draw(self.screen)
        pygame.display.flip()