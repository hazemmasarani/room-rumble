class Settings:

    def __init__(self, screen_width, screen_height):
        # Screen settings
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.window_caption = "Room Rumble"
        self.bg_color = (0, 0, 0)
        self.fps = 60
        self.grid_width = 100
        self.grid_height = 50
        self.block_size = 13
        self.origin_x = 0
        self.origin_y = 0

        # rooms setting (dimenssions are with block size)
        self.rooms_min_count = 9
        self.rooms_max_count = 16
        self.room_min_width = 4
        self.room_max_width = 8
        self.room_min_height = 4
        self.room_max_height = 8
        self.room_default_color = (90, 90, 90)

