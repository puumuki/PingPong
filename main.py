#!/usr/bin/env python
"""
Simple Ping Pong Game
"""

#Import Modules
import os, pygame
import sys
from pygame.locals import *
from pingpong import *
from gamemode import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'



def input(events, current_game_mode): 
    for event in events: 
        if event.type == QUIT: 
            sys.exit(0) 
        elif event.type == KEYDOWN and event.key == K_ESCAPE:            
            sys.exit(0)
        elif event.type == KEYDOWN and event.key == K_PAUSE: 
            current_game_mode.toggle_mode()
                   
                
def main():    
    current_game_mode = GameMode(MODE_PLAY)    
    
    pingpong = PingPong(pygame)
        
    #Main Game Loop
    while 1:
        
        input(pygame.event.get(), current_game_mode)
        pressed_keys = pygame.key.get_pressed()                                             
         
        pingpong.tick()         
         
        if current_game_mode.get_mode() == MODE_PLAY:                    
            pingpong.update()        
            pingpong.render()                
        
#this calls the 'main' function when this script is executed
if __name__ == '__main__': main()