# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 12:45:39 2022

@author: gen
"""
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1000, 800))
r = pygame.Rect(50, 50, 100, 200)
pygame.draw.rect(screen, (255, 0, 0), r, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()