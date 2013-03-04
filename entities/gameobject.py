import Polygon
import Polygon.Utils

class GameObject(object):

    def __init__(self):

        self.pos_x = 0
        self.pos_y = 0

        self.vel_x = 0
        self.vel_y = 0

        self.initial_x =0
        self.initial_y =0

        self.width = 0
        self.height = 0

        self.rotation = 0
        self.rotation_speed = 0

    def reset(self):
        self.pos_x = self.initial_x
        self.pos_y = self.initial_y
        self.create_hitbox()
        return self

    def create_hitbox(self):
        top_left = (self.pos_x, self.pos_y)
        top_right = (self.pos_x + self.width, self.pos_y)
        bottom_left = (self.pos_x, self.pos_y + self.height)
        bottom_right = (self.pos_x + self.width, self.pos_y + self.height)
        self.polygon = Polygon.Polygon((top_left, top_right, bottom_right, bottom_left))
