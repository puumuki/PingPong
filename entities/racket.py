"""
Class Racket
"""

#Import Modules
import math
from pygame.locals import *
from options import OPTIONS
from gameobject import GameObject
from vector import Vector2
import Polygon
import Polygon.Utils

#Tracket vertical speed, the maxmimun speed is VERTICAL_SPEED * FRICTION
VERTICAL_SPEED = 0.5

#Tracket friction, 1 no friction at all or 0.90 very much friction
FRICTION = 0.95

ROTATION_SPEED = 0.01

class Racket(GameObject):

    __tracket_side = 'left'

    __joystick_id = 0
    __joystick =  False

    def __init__(self, pygame, options):
        super(Racket,self).__init__()
        self.__pygame = pygame

        #Tracket color
        self.__color = Color(255,255,255,0)

        self.__hitbox_color = Color(255,0,0,0)

        self.__tracket_side = options['side']
        self.__racketsurface = pygame.Surface((OPTIONS['SCREEN_WIDTH'], OPTIONS['SCREEN_HEIGHT']))

        #Position & Dimensions
        self.pos_x = options['X']
        self.pos_y = options['Y']
        self.height = OPTIONS['TRACKET_HEIGHT']
        self.width =  OPTIONS['TRACKET_WIDTH']
        self.rotation = 0
        self.rotation_speed = 0.0

        #Reference to ball object
        self.__ball = options['ball']

        #Initialize Joysticks
        self.__joystick_id = 0 if options['side'] == 'left' else 1

        if pygame.joystick.get_count() > 0 and self.__joystick_id == 0:
            self.__joystick = pygame.joystick.Joystick(self.__joystick_id)
            self.__joystick.init()

        elif pygame.joystick.get_count() > 1 and self.__joystick_id == 1:
            self.__joystick = pygame.joystick.Joystick(self.__joystick_id)
            self.__joystick.init()

        self.create_hitbox()

    def handle_joystick_input(self):

        rotation_value = self.__joystick.get_axis(2)

        if math.fabs(rotation_value) > OPTIONS['JOYSTICK_DEAD_ZONE']:
            self.rotation_speed -= ROTATION_SPEED * rotation_value

        rotation_value = self.__joystick.get_axis(4)

        if math.fabs(rotation_value) > OPTIONS['JOYSTICK_DEAD_ZONE']:
            self.rotation_speed += ROTATION_SPEED * rotation_value

        value = self.__joystick.get_axis(1)

        if math.fabs(value) > OPTIONS['JOYSTICK_DEAD_ZONE']:
            self.vel_y += VERTICAL_SPEED * value

    def update(self, delta):

        #Handle Keyboard Inputs
        pressed_keys = self.__pygame.key.get_pressed()

        if(pressed_keys[K_UP] and self.__tracket_side == 'right'):
            self.vel_y -= VERTICAL_SPEED

        if(pressed_keys[K_DOWN] and self.__tracket_side == 'right'):
            self.vel_y += VERTICAL_SPEED

        if(pressed_keys[K_w] and self.__tracket_side == 'left'):
            self.vel_y -= VERTICAL_SPEED

        if(pressed_keys[K_s] and self.__tracket_side == 'left'):
            self.vel_y += VERTICAL_SPEED

        if pressed_keys[K_LEFT] and self.__tracket_side == 'right':
            self.rotation_speed += 0.001

        if pressed_keys[K_RIGHT] and self.__tracket_side == 'right':
            self.rotation_speed -= 0.001

        self.rotation_speed *= 0.95;

        #Handle Game Controller (Xbox Controller)
        if self.__joystick: self.handle_joystick_input()

        #Check is ball hitting the racket
        if self.polygon.overlaps(self.__ball.polygon):
            x = math.cos( self.rotation - math.pi /2 )
            y = math.sin( self.rotation - math.pi /2 )
            reflect_vector = Vector2( x, y )
            self.__ball.reflect(reflect_vector)

        self.vel_y *= FRICTION

        #Prevent tracket go outside of screen
        if self.pos_y + self.height > OPTIONS['SCREEN_HEIGHT'] or self.pos_y < 0:
            self.vel_y *= -1

        #Move Tracket
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y
        self.rotation += self.rotation_speed

        self.polygon.shift(self.vel_x, self.vel_y)
        self.polygon.rotate(self.rotation_speed)

    def render(self, surface):
        points = Polygon.Utils.pointList(self.polygon)
        self.__pygame.draw.polygon(surface, (255, 255, 255), points)

