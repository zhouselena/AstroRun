"""
Astro Runner
2D platformer game written in Python with PyGame.

Selena Zhou, May 2022
"""

import pygame
from sys import exit
from random import randint, choice

"""GLOBAL VARS"""

WINDOW_W = 1280
WINDOW_H = 720
FLOOR_Y = 540

"""INITIALIZE GAME"""

pygame.init()
screen = pygame.display.set_mode((WINDOW_W, WINDOW_H))
pygame.display.set_caption("Astro Runner")


"""MAIN FUNCTION"""

if __name__ == '__main__':

    print("Hi, this is Astro Run!")
