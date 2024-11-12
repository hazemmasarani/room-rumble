import pygame

class Room:

    def __init__(self, x, y, width, height, setting, color=None):
        self.setting = setting
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.block_size = setting.block_size
        if not color:
            color = setting.room_default_color
        self.color = color

    def overlaps(self, other):
        return (
                (
                    (other.x <= self.x + self.width <= other.x + other.width)
                    or
                    (self.x <= other.x + other.width <= self.x + self.width)
                ) 
                and
                (
                    (other.y <= self.y + self.height <= other.y + other.height)
                    or
                    (self.y <= other.y + other.height <= self.y + self.height)
                )
            )

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x*self.block_size + self.setting.origin_x, self.y*self.block_size + self.setting.origin_y, self.width*self.block_size, self.height*self.block_size))
