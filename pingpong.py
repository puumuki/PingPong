

#Module Imports
from entities.racket import Racket
from entities.ball import Ball
from options import OPTIONS
from pygame.locals import *
from vector import Vector2
from entitymanager import EntityManager


LOCALIZATION = {'TITLE': 'new Pingpong(2013)'}

class PingPong():

    def __init__(self, pygame):

        self.__player_1_scores = 0
        self.__player_2_scores = 0

        self.__entity_manager = EntityManager()

        self.__pygame = pygame
        self.__background_color = Color(0,0,0)

        #Initialize Everything
        self.__pygame.init()

        self.__fullscreen = OPTIONS['FULLSCREEN']

        screen_mode =  (RESIZABLE | DOUBLEBUF | FULLSCREEN) if OPTIONS['FULLSCREEN'] else (RESIZABLE | DOUBLEBUF)

        self.__screen = pygame.display.set_mode((OPTIONS['SCREEN_WIDTH'],
                                                 OPTIONS['SCREEN_HEIGHT']),
                                                 screen_mode)

        #pygame.display.set_icon(surface)
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

        ball = Ball(self.__pygame, {'X':self.__screen.get_width()/2,
                                    'Y':self.__screen.get_height()/2})

        ball.rand_velocity()

        left_racket = Racket(self.__pygame, {'X':20,'Y':20, 'side':'left','ball':ball})
        right_racket = Racket(self.__pygame, {'X': self.__screen.get_width() - 20*2,
                                              'Y':20,'side':'right', 'ball':ball})

        self.__entity_manager.add('leftracket',left_racket)
        self.__entity_manager.add('rightracket',right_racket)


        self.__entity_manager.add('ball',ball)

    def toggle_fullscreen(self):
        self.__pygame.display.set_mode()

    def tick(self):
        self.delta = self.__clock.tick(OPTIONS['TARGET_FPS'])

    def update(self):

        ball = self.__entity_manager.get('ball')

        for gameobject in self.__entity_manager.as_list():
            gameobject.update(self.delta)

        if ball.outside() == 'right':
            self.__player_1_scores += 1


        if ball.outside() == 'left':
            self.__player_2_scores += 1

        if ball.outside():
            ball.reset().rand_velocity()

    def render(self):
        self.__screen.blit(self.__background, (0, 0))
        self.__background.fill((50, 50, 5))

        score_player_one = self.__font.render( str(self.__player_1_scores), 1, (250, 250, 250))
        score_player_two = self.__font.render( str(self.__player_2_scores), 1, (250, 250, 250))

        textpos = score_player_one.get_rect(centerx=20)
        self.__background.blit(score_player_one, textpos)

        textpos = score_player_two.get_rect(centerx=OPTIONS['SCREEN_WIDTH']-20)
        self.__background.blit(score_player_two, textpos)

        for gameobject in self.__entity_manager.as_list():
            gameobject.render(self.__background)

        self.__pygame.display.flip()
