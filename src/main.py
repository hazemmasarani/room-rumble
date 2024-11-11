import pygame
from settings import Settings
from game import Game

def run_game():


    ########################################
    ########### set game setting ###########
    ########################################
    # initialize pygame
    pygame.init()

    # Get screen size
    display_info = pygame.display.Info()
    screen_width, screen_height = display_info.current_w, display_info.current_h
    # Adjust screen size setting
    settings = Settings(screen_width, screen_height)

    ########################################
    ############ initialize game ###########
    ########################################

    game = Game(settings)

    ########################################
    ############### Run game ###############
    ########################################

    game.run()

if __name__ == "__main__":
    run_game()
