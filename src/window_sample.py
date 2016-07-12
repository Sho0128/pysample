#coding:utf-8
'''
Created on 2016/07/13

@author: Shohei
'''

import pygame
from pygame.locals import *
import sys

SCREEN_SIZE = (640, 480)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("ウィンドウの作成")

while True:
    screen.fill((0,0,255))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    