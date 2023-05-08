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
import Button

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


def calculate_collisions():
    global screen_number
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        screen_number = 2
        return False
    else:
        return True


"""***************** INITIALIZE GAME *****************"""

pygame.init()
screen = pygame.display.set_mode((WINDOW_W, WINDOW_H))
pygame.display.set_caption("Astro Runner")

clock = pygame.time.Clock()
font = pygame.font.Font("font/Pixeltype.ttf", 50)

game_active = False
screen_number = 0  # 0: intro screen | 1: game OR paused game | 2: end screen

"""Sprites"""

# Buttons
pause_button = pygame.sprite.GroupSingle()
pause_button.add(Button.Button("graphics/buttons/pause_button.png"))
play_button = pygame.sprite.GroupSingle()
play_button.add(Button.Button("graphics/buttons/play_button.png"))
button_rect = pause_button.sprite.rect

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
                # Continually generate obstacles
                if event.type == obstacle_timer:
                    obstacle_group.add(Obstacle.Obstacle(choice(['obstacle1', 'obstacle1', 'obstacle1', 'obstacle1', 'obstacle2', 'obstacle2', 'obstacle3'])))

            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_active = True
                    screen_number = 1

            # Play or Pause
            if screen_number == 1:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        game_active = not game_active

        """Game"""

        # Intro screen
        if screen_number == 0:
            screen.blit(bg_surface, (0, 0))

        # Game
        elif screen_number == 1:

            if game_active:
                animate_background()
                pause_button.draw(screen)

                player.draw(screen)
                player.update()

                obstacle_group.draw(screen)
                obstacle_group.update()

                game_active = calculate_collisions()

            else:
                animate_background()
                play_button.draw(screen)
                player.draw(screen)
                obstacle_group.draw(screen)

        # End screen
        else:
            player_surf = pygame.image.load("graphics/player/player_1.png").convert_alpha()
            screen.blit(bg_surface, (0, 0))
            screen.blit(player_surf, player_surf.get_rect())

        """Draws all elements, updates everything"""
        pygame.display.update()
        clock.tick(60)
