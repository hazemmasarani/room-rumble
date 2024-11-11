import pygame

class Grid:

    def __init__(self, screen_w, screen_h):
        self.width = 100
        self.height = 50
        self.block_size = min(screen_w/self.width, screen_h/self.height)
        self.origin_x = (screen_w - (self.block_size * self.width) ) // 2
        self.origin_y = (screen_h - (self.block_size * self.height) ) // 2
        self.bg_color = (50, 40, 30)
        self.grid_lines_color = (80, 70, 60)
        self.matrix = []

    def draw(self, screen):

        # Draw the whole grid
        pygame.draw.rect(screen, self.bg_color, (self.origin_x, self.origin_y, self.width * self.block_size, self.height * self.block_size))
        
        # Draw grid lines one pixl line every block
        # vertical lines
        x = 0
        while x <= self.width * self.block_size:
            xi = int(x)
            start_x = xi + self.origin_x
            start_y = self.origin_y
            end_x = xi + self.origin_x
            end_y = self.height * self.block_size + self.origin_y
            pygame.draw.line(screen, self.grid_lines_color, (start_x, start_y), (end_x, end_y), 1)
            x += self.block_size

        # Horizontal lines
        y = 0
        while y <= self.height * self.block_size:
            yi = int(y)
            start_x = self.origin_x
            start_y = yi + self.origin_y
            end_x = self.width * self.block_size + self.origin_x
            end_y = yi + self.origin_y
            pygame.draw.line(screen, self.grid_lines_color, (start_x, start_y), (end_x, end_y), 1)
            y += self.block_size



