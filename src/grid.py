import pygame

class Grid:
    def __init__(self, width, height, block_size):
        self.width = width
        self.height = height
        self.block_size = block_size
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def draw(self, surface):
        # Draw grid lines
        for x in range(0, self.width * self.block_size, self.block_size):
            for y in range(0, self.height * self.block_size, self.block_size):
                pygame.draw.rect(surface, (50, 50, 50), (x, y, self.block_size, self.block_size), 1)

        # Draw rooms
        for room in self.rooms:
            room.draw(surface)
