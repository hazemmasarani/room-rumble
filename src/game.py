import pygame
import sys
from grid import Grid

class Game:

    def __init__(self, settings):

        # Set game screen size in the game to full size
        self.settings = settings
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        # Set game screen caption
        pygame.display.set_caption(self.settings.window_caption)

        # Create clock to use in frame rate
        self.clock = pygame.time.Clock()

        # create game grid
        self.grid = Grid(self.settings)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:  # Check if a key was pressed
                    if event.key == pygame.K_q:  # If the "q" key is pressed
                        running = False 

            self.update()
            self.draw()
            pygame.display.flip()  # Update the display

            # Limit frames per second
            self.clock.tick(self.settings.fps)
        
        pygame.quit()
        sys.exit()

    def update(self):
        pass

    def draw(self):
        self.screen.fill(self.settings.bg_color)
        self.grid.draw(self.screen)

