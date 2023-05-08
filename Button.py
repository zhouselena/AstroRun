"""
Astro Runner: Button sprite class

Selena Zhou, May 2022
"""

import pygame


"""GLOBAL VARS"""

WINDOW_W = 1280
WINDOW_H = 720
FLOOR_Y = 580


"""HELPER FUNCTIONS"""


def make_surf(filename):
    initial_surf = pygame.image.load(filename).convert_alpha()
    scaled_surf = pygame.transform.scale_by(initial_surf, 1.5)
    return scaled_surf


"""BUTTON CLASS"""


class Button(pygame.sprite.Sprite):

    def __init__(self, filename):
        super().__init__()

        self.image = make_surf(filename)
        self.rect = self.image.get_rect(topright=(WINDOW_W-10, 20))



