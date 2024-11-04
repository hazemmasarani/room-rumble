import pygame

class Game:
    def __init__(self, settings):
        pass
        # self.settings = settings
        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # pygame.display.set_caption("My Game")
        # self.player = Player()
        # self.enemies = [Enemy() for _ in range(5)]

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.update()
            self.draw()
        pygame.quit()

    def update(self):
        self.player.update()
        for enemy in self.enemies:
            enemy.update()

    def draw(self):
        self.screen.fill(self.settings.bg_color)
        self.player.draw(self.screen)
        for enemy in self.enemies:
            enemy.draw(self.screen)
        pygame.display.flip()