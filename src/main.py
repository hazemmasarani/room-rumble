import pygame
from settings import Settings
from game import Game

def run_game():
    pygame.init()
    settings = Settings()
    game = Game(settings)
    game.run()

if __name__ == "__main__":
    run_game()