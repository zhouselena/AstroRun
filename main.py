"""
Astro Runner
2D platformer game written in Python with PyGame.

Selena Zhou, May 2022
"""

import pygame
from sys import exit
from random import randint, choice
import Player
import Obstacle

"""***************** GLOBAL VARS *****************"""

WINDOW_W = 1280
WINDOW_H = 720
FLOOR_Y = 580

"""***************** FUNCTIONS *****************"""


def animate_background():

    for bg_rect in bg_rect_list: # update to animate stars
        bg_rect.x -= 2
        screen.blit(bg_surface, bg_rect)
        if bg_rect.x <= -1280:
            bg_rect.x = 1280


"""***************** INITIALIZE GAME *****************"""

pygame.init()
screen = pygame.display.set_mode((WINDOW_W, WINDOW_H))
pygame.display.set_caption("Astro Runner")

clock = pygame.time.Clock()
font = pygame.font.Font("font/Pixeltype.ttf", 50)

game_active = False
screen_number = 0  # 0: intro screen | 1: game OR paused game | 2: end screen

"""Sprites"""

# Player
player = pygame.sprite.GroupSingle()
player.add(Player.Player())

# Obstacles
obstacle_group = pygame.sprite.Group()

"""Surfaces"""
bg_rect_list = [pygame.image.load("graphics/background.png").convert().get_rect(topleft=(0, 0)),
                        pygame.image.load("graphics/background.png").convert().get_rect(topleft=(1280, 0))]
bg_surface = pygame.image.load("graphics/background.png").convert()

"""Timers"""
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

"""***************** MAIN *****************"""

if __name__ == '__main__':

    while True:

        """Events"""

        for event in pygame.event.get():
            # Exit upon close
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # Toggle game active
            if game_active:

                if event.type == obstacle_timer:
                    obstacle_group.add(Obstacle.Obstacle(choice(['obstacle1', 'obstacle1', 'obstacle1', 'obstacle1', 'obstacle2', 'obstacle2', 'obstacle3'])))

            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_active = True
                    screen_number = 1

        """Game"""

        # Intro screen
        if screen_number == 0:
            screen.blit(bg_surface, (0, 0))

        # Game
        if screen_number == 1:
            animate_background()

            player.draw(screen)
            player.update()

            obstacle_group.draw(screen)
            obstacle_group.update()

        # End screen
        if screen_number == 2:
            screen.blit(bg_surface, (0, 0))

        """Draws all elements, updates everything"""
        pygame.display.update()
        clock.tick(60)
