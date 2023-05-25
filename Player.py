"""
Astro Runner: Player sprite class

Selena Zhou, May 2023
"""

import pygame
from random import choice


"""GLOBAL VARS"""

WINDOW_W = 1280
WINDOW_H = 720
FLOOR_Y = 580


"""HELPER FUNCTIONS"""


def make_surf(filename):
    initial_surf = pygame.image.load(filename).convert_alpha()
    scaled_surf = pygame.transform.scale_by(initial_surf, 3)
    return scaled_surf


"""PLAYER CLASS"""


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.player_frames = [make_surf("graphics/player/player_1.png"), make_surf("graphics/player/player_2.png"),
                              make_surf("graphics/player/player_3.png"), make_surf("graphics/player/player_4.png"),
                              make_surf("graphics/player/player_5.png"), make_surf("graphics/player/player_6.png"),
                              make_surf("graphics/player/player_7.png"), make_surf("graphics/player/player_8.png"),
                              make_surf("graphics/player/player_9.png"), make_surf("graphics/player/player_10.png"),
                              make_surf("graphics/player/player_11.png"), make_surf("graphics/player/player_12.png"),
                              make_surf("graphics/player/player_13.png"), make_surf("graphics/player/player_14.png")]
        self.player_jump_frame = make_surf("graphics/player/player_jump.png") # update to animate this
        self.player_frame_index = 0

        self.image = self.player_frames[self.player_frame_index]
        self.rect = self.image.get_rect(midbottom=(175, FLOOR_Y)).inflate(-30, -10)
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound("audio/jump.mp3")
        self.jump_sound.set_volume(0.5)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= FLOOR_Y:
            self.gravity = -25
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= FLOOR_Y:
            self.rect.bottom = FLOOR_Y

    def animate_frames(self):
        if self.rect.bottom < FLOOR_Y-10:
            self.image = self.player_jump_frame
            self.player_frame_index = choice([0, 0, 0, 10])
        else:
            self.player_frame_index += 0.1
            if self.player_frame_index >= len(self.player_frames):
                self.player_frame_index = 0
            self.image = self.player_frames[int(self.player_frame_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animate_frames()
