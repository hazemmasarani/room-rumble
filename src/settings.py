class Settings:

    def __init__(self, screen_width, screen_height):
        # Screen settings
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.window_caption = "Room Rumble"
        self.bg_color = (0, 0, 0)
        self.fps = 60

    def reset_settings(self, screen_width = None, screen_height = None):
        """
            Method to reset settings to their initial state if needed.
        """
        self.window_caption = "Room Rumble"
        self.bg_color = (0, 0, 0) 
        self.fps = 60
        if screen_width:
            self.screen_width = screen_width
        if screen_height:
            self.screen_height = screen_height
