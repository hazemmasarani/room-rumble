import pygame
from random import randint

from room import Room

class Grid:

    def __init__(self, setting):
        self.setting = setting
        self.width = setting.grid_width
        self.height = setting.grid_height
        self.block_size = min(self.setting.screen_width/self.width, self.setting.screen_height/self.height)
        self.setting.block_size = self.block_size
        self.origin_x = (self.setting.screen_width - (self.block_size * self.width) ) // 2
        self.origin_y = (self.setting.screen_height - (self.block_size * self.height) ) // 2
        setting.origin_x = self.origin_x
        setting.origin_y = self.origin_y
        self.bg_color = (50, 40, 30)
        self.grid_lines_color = (80, 70, 60)

        self.map = []
        for _ in range(self.height):
            self.map.append([])
            for __ in range(self.width):
                self.map[-1].append("")

        self.rooms = []
        self.create_random_rooms()

    def draw(self, screen):

        # Draw the whole grid
        pygame.draw.rect(screen, self.bg_color, (self.origin_x, self.origin_y, self.width * self.block_size, self.height * self.block_size))
        
        # Draw Rooms
        for room in self.rooms:
            room.draw(screen)

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

    def create_random_rooms(self):
        
        self.rooms_cnt = randint(self.setting.rooms_min_count, self.setting.rooms_max_count) 

        i = 0
        while i < self.rooms_cnt:

            room_w = randint(self.setting.room_min_width, self.setting.room_max_width)
            room_h = randint(self.setting.room_min_height, self.setting.room_max_height)

            room_x = randint(0, self.width - room_w)
            room_y = randint(0, self.height - room_h)

            new_room = Room(room_x, room_y, room_w, room_h, self.setting)

            overlap_flag = False
            for room in self.rooms:
                if new_room.overlaps(room):
                    overlap_flag = True
                    break
            
            if not overlap_flag:
                self.rooms.append(new_room)
                i += 1

        # for room in self.rooms:
        #     x = room.x
        #     y = room.y
        #     for i in range(room.width):
        #         for j in range(room.height):
        #             self.map[x + i][y + j] = "r"
    