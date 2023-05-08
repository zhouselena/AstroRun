"""
Astro Runner: Obstacle sprite class

Selena Zhou, May 2022
"""

import pygame
from random import randint, choice


"""GLOBAL VARS"""

WINDOW_W = 1280
WINDOW_H = 720
FLOOR_Y = 580


"""HELPER FUNCTIONS"""


def make_surf(filename):
    initial_surf = pygame.image.load(filename).convert_alpha()
    scaled_surf = pygame.transform.scale_by(initial_surf, 2)
    return scaled_surf


"""OBSTACLE CLASS"""

class Obstacle(pygame.sprite.Sprite):

    def __init__(self, type):
        super().__init__()

        if type == "obstacle1":
            self.frames = [make_surf("graphics/obstacles/obstacle1_1.png"), make_surf("graphics/obstacles/obstacle1_2.png")]
            y_pos = FLOOR_Y
        elif type == "obstacle2":
            self.frames = [make_surf("graphics/obstacles/obstacle2_1.png"), make_surf("graphics/obstacles/obstacle2_2.png")]
            y_pos = FLOOR_Y
        elif type == "obstacle3":
            self.frames = [make_surf("graphics/obstacles/obstacle3_1.png"), make_surf("graphics/obstacles/obstacle3_2.png")]
            y_pos = FLOOR_Y - 275

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(1300, 1500), y_pos))

    def animate_frames(self):
        self.animation_index += 0.05
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def destroy(self):
        if self.rect.x <= -300:
            self.kill()

    def update(self):
        self.animate_frames()
        self.rect.x -= 9
        self.destroy()
