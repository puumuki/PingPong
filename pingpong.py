from racket import Racket
from ball import Ball
from options import OPTIONS
from pygame.locals import *
import random
from vector import Vector2

LOCALIZATION = {'TITLE': 'new Pingpong(2013)'}

class PingPong():
    
    __player_1_scores = 0
    __player_2_scores = 0
    
    __gameobjects = []
    
    def __init__(self, pygame):
        
        self.__pygame = pygame        
        self.__background_color = Color(0,0,0)
        
        #Initialize Everything
        self.__pygame.init()                                   
        self.__screen = pygame.display.set_mode((OPTIONS['SCREEN_WIDTH'], OPTIONS['SCREEN_HEIGHT']), OPTIONS['SCREENMODE'])
        
        pygame.display.set_caption(LOCALIZATION['TITLE'])
        pygame.mouse.set_visible(0)
    
        #Create The Backgound
        self.__background = pygame.Surface(self.__screen.get_size())
        self.__background = self.__background.convert()
        self.__background.fill((0, 0, 0))
        
        #Put Text On The Background, Centered
        if pygame.font:
            self.__font = pygame.font.Font(None, 36)            
    
        #Display The Background
        self.__screen.blit(self.__background, (0, 0))
        pygame.display.flip()
        
        #Prepare Game Objects
        self.__clock = pygame.time.Clock()        
        
        self.init_gameobjects()        
    
    def init_gameobjects(self):        
        self.__gameobjects.append(Racket(self.__pygame, {'X':20,'Y':20, 'side':'left'}))
        self.__gameobjects.append(Racket(self.__pygame, {'X': self.__screen.get_width() - 20*2,'Y':20,'side':'right'}))
        
        ball = Ball(self.__pygame, {'X':self.__screen.get_width()/2, 
                                    'Y':self.__screen.get_height()/2})        

        ball.rand_velocity()        
        self.__gameobjects.append(ball)
        self.__ball = ball                  
        
    def tick(self):
        self.delta = self.__clock.tick(OPTIONS['TARGET_FPS'])
        
    def update(self):
        
        for gameobject in self.__gameobjects:
            gameobject.update(self.delta)
            
            if isinstance(gameobject, Racket) and gameobject.hitracket(self.__ball):
                self.__ball.reflect(Vector2(0,1))
            
        if self.__ball.outside() == 'right':
            self.__player_1_scores += 1
         
            
        if self.__ball.outside() == 'left':
            self.__player_2_scores += 1   
        
        if self.__ball.outside():
            self.__ball.reset().rand_velocity()                                    
        
    def render(self):        
        self.__screen.blit(self.__background, (0, 0))                
        self.__background.fill((0, 0, 0))
        
        score_player_one = self.__font.render( str(self.__player_1_scores), 1, (250, 250, 250))
        score_player_two = self.__font.render( str(self.__player_2_scores), 1, (250, 250, 250))
        
        textpos = score_player_one.get_rect(centerx=20)
        self.__background.blit(score_player_one, textpos)
        
        textpos = score_player_two.get_rect(centerx=OPTIONS['SCREEN_WIDTH']-20)        
        self.__background.blit(score_player_two, textpos)        
        
        for gameobject in self.__gameobjects:
            gameobject.render(self.__background)
                                   
        self.__pygame.display.flip()   