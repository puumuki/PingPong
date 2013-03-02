from pygame.locals import *
from vector import Vector2
from options import OPTIONS
import random


class Ball :

    __pos_x = 50
    __pos_y = 50        
    
    __vel_x = 0
    __vel_y = 0          
    
    def reset(self):
        self.__pos_x = self.__initial_x
        self.__pos_y = self.__initial_y
        return self

    def rand_velocity(self):        
        vals = [-1,1]        
        vel_x = random.uniform(0.2, 0.4) * vals[ random.randint(0, len(vals)-1)]
        vel_y = random.uniform(0.2, 0.4) * vals[ random.randint(0, len(vals)-1)]
        self.__vel = Vector2( vel_x, vel_y)
        return self
    
    def __init__(self, pygame, options):
        self.__diameter = 10
        self.__pygame = pygame
        self.__color = Color(255,255,255,255)
        self.__pos_x = self.__initial_x = options['X']
        self.__pos_y = self.__initial_y = options['Y']
        self.hitbox = Rect(self.__pos_x, self.__pos_y, self.__diameter, self.__diameter)
    
    def outside(self):
        if self.__pos_x < 0:
            return 'left'
            
        if self.__pos_x + self.__diameter > OPTIONS['SCREEN_WIDTH']:
            return 'right'
    
        return False
    
    def reflect(self, vector):
        self.__vel = self.__vel.reflect(vector)
        
    def update(self, delta):
        self.__pos_y += self.__vel.y * delta
        self.__pos_x += self.__vel.x * delta
        
        if self.__pos_y < 0 :
            self.__vel = self.__vel.reflect(Vector2(1,0))
        
        if self.__pos_y >  OPTIONS['SCREEN_HEIGHT']:
            self.reflect(Vector2(1,0))
            
        if self.__pygame.key.get_pressed()[K_p]:
            self.reset()
            self.rand_velocity()
                        
        self.hitbox.left = self.__pos_x
        self.hitbox.top = self.__pos_y        
           
    def render(self, surface):
        self.__pygame.draw.rect( surface, self.__color, Rect( self.__pos_x, self.__pos_y, self.__diameter, self.__diameter))        
    