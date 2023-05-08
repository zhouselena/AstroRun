"""
Astro Runner: Player sprite class

Selena Zhou, May 2022
"""

import pygame


"""GLOBAL VARS"""

WINDOW_W = 1280
WINDOW_H = 720
FLOOR_Y = 540


"""HELPER FUNCTIONS"""


def make_surf(filename):
    return pygame.image.load(filename).convert_alpha()


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
        self.player_jump_frame = make_surf("graphics/player/player_jump.png")
        self.player_frame_index = 0

        self.image = self.player_frames[self.player_frame_index]
        self.rect = self.image.get_rect(midbottom=(200, FLOOR_Y))
