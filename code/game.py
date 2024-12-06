import pygame

from code.const import SCREEN_WIDTH, SCREEN_HEIGHT
from code.menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()