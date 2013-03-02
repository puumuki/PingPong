from pygame.locals import *
from options import OPTIONS

#Tracket vertical speed
VERTICAL_SPEED = 0.5

#Tracket friction 
FRICTION = 0.95

class Racket():
        
    __pos_x = 50
    __pos_y = 50        
    __vel_x = 0
    __vel_y = 0        
        
    __tracket_height = OPTIONS['TRACKET_HEIGHT']
    __tracket_width =  OPTIONS['TRACKET_WIDTH']    
   
    __tracket_side = 'left'   
        
    def __init__(self, pygame, options):                       
        self.__pygame = pygame
        self.__pos_x = options['X']
        self.__pos_y = options['Y']
        self.__color = Color(255,255,255,0)
        self.__tracket_side = options['side']
        self.__racketsurface = pygame.Surface((OPTIONS['SCREEN_WIDTH'], OPTIONS['SCREEN_HEIGHT']))                               
        self.hitbox = Rect(self.__pos_x, self.__pos_y, self.__tracket_width, self.__tracket_height)
        
    def hitracket(self,ball):
        return self.hitbox.colliderect(ball.hitbox)
    
    def render(self, surface):                
        self.__pygame.draw.rect( surface, self.__color, Rect( self.__pos_x, self.__pos_y, self.__tracket_width, self.__tracket_height))
    
    def update(self, delta):
        
        pressed_keys = self.__pygame.key.get_pressed()
                           
        if(pressed_keys[K_UP] and self.__tracket_side == 'right'):
            self.__vel_y -= VERTICAL_SPEED
                        
        if(pressed_keys[K_DOWN] and self.__tracket_side == 'right'):
            self.__vel_y += VERTICAL_SPEED        
    
        if(pressed_keys[K_w] and self.__tracket_side == 'left'):
            self.__vel_y -= VERTICAL_SPEED
                                
        if(pressed_keys[K_s] and self.__tracket_side == 'left'):
            self.__vel_y += VERTICAL_SPEED                   
    
        self.__pos_y += self.__vel_y
        self.__pos_x += self.__vel_x
        
        self.__vel_y *= FRICTION
                
        if self.__pos_y + self.__tracket_height > OPTIONS['SCREEN_HEIGHT'] or self.__pos_y < 0:
            self.__vel_y *= -1
        
        if self.__pos_y + self.__tracket_height > OPTIONS['SCREEN_HEIGHT']:
            self.__pos_y -= VERTICAL_SPEED
        
        if self.__pos_y < 0:
            self.__pos_y += VERTICAL_SPEED
    
        self.hitbox.left = self.__pos_x
        self.hitbox.top = self.__pos_y
        