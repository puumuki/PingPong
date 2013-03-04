# -*- coding: utf-8 *-*

#Import Modules
import sys, pygame
from pygame.locals import *
from pingpong import *
from gamemode import *

#Check that all resources can be loaded
if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

class Application:

    def __init__(self):
        self.pygame = pygame
        self.current_game_mode = GameMode(MODE_PLAY)
        self.pingpong = PingPong(pygame)

    def handle_input(self,events):
        for event in events:
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == K_PAUSE:
                self.current_game_mode.toggle_mode()
            elif event.type == KEYDOWN and event.key == K_F11:
                self.pingpong.toggle_fullscreen()

    def start(self):
        while 1:
            self.pingpong.tick()#Make Pong Tick

            self.handle_input(self.pygame.event.get())

            if self.current_game_mode.get_mode() == MODE_PLAY:
                self.pingpong.update()
                self.pingpong.render()
