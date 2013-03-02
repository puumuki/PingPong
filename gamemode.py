
MODE_PAUSE = 0
MODE_PLAY = 1

class GameMode:
    __game_mode = MODE_PLAY
    
    def __init__(self, mode):
        self.__game_mode = mode
    
    def get_mode(self):
        return self.__game_mode
    
    def set_mode(self, mode):
        self.__game_mode = mode
        
    def toggle_mode(self):
        if self.__game_mode == MODE_PAUSE:
            self.__game_mode = MODE_PLAY
        else:
            self.__game_mode = MODE_PAUSE

            