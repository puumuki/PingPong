from pygame.locals import *
from vector import Vector2
from options import OPTIONS
from gameobject import GameObject
import random
import Polygon


class Ball(GameObject):

    def __init__(self, pygame, options):
        super(Ball,self).__init__()
        self.__diameter = 10
        self.__pygame = pygame
        self.__color = Color(255,255,255,255)
        self.pos_x = self.initial_x = options['X']
        self.pos_y = self.initial_y = options['Y']
        self.width = self.__diameter
        self.height = self.__diameter
        self.create_hitbox()

    def rand_velocity(self):
        #vals = [-1, 1]
        #vel_x = random.uniform(0.2, 0.4) * vals[random.randint(0, len(vals) - 1)]
        #vel_y = random.uniform(0.2, 0.4) * vals[random.randint(0, len(vals) - 1)]
        #self.velocity = Vector2( vel_x, vel_y)
        self.velocity = Vector2( 0.4, 0)
        return self

    def outside(self):
        if self.pos_x < 0:
            return 'left'

        if self.pos_x + self.__diameter > OPTIONS['SCREEN_WIDTH']:
            return 'right'

        return False

    def reflect(self, vector):
        self.velocity = self.velocity.reflect(vector)

    def update(self, delta):

        movement_x = self.velocity.x * delta
        movement_y = self.velocity.y * delta

        self.pos_y += movement_y
        self.pos_x += movement_x

        if self.pos_y < 0:
            self.velocity = self.velocity.reflect(Vector2(1,0))

        if self.pos_y >  OPTIONS['SCREEN_HEIGHT']:
            self.reflect(Vector2(1,0))

        if self.__pygame.key.get_pressed()[K_p]:
            self.reset()
            self.rand_velocity()

        self.polygon.shift( movement_x, movement_y )

    def render(self, surface):
        rectangle = Rect( self.pos_x, self.pos_y, self.__diameter, self.__diameter)
        self.__pygame.draw.rect( surface, self.__color, rectangle)
        points = Polygon.Utils.pointList(self.polygon)
        self.__pygame.draw.polygon(surface, (255, 0, 0), points ,1)
