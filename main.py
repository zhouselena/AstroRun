"""
Astro Runner
2D platformer game written in Python with PyGame.

Selena Zhou, May 2022
"""

import pygame
from sys import exit
from random import choice
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


def intro_screen():
    global rising

    screen.blit(title_screen, (0, 0))
    screen.blit(title_button, title_button_rect)
    screen.blit(title_player, title_player_rect)

    if title_player_rect.centery > 450 and rising:
        title_player_rect.centery -= 1
        if title_player_rect.centery == 450:
            rising = False
    else:
        title_player_rect.centery += 1
        if title_player_rect.centery == 550:
            rising = True

    if pygame.MOUSEBUTTONDOWN and title_button_rect.collidepoint(pygame.mouse.get_pos()):
        screen.blit(title_button_pressed, title_button_rect)


def end_screen():

    screen.blit(bg_surface, (0, 0))
    screen.blit(title_button, title_button_rect)

    if pygame.MOUSEBUTTONDOWN and title_button_rect.collidepoint(pygame.mouse.get_pos()):
        screen.blit(title_button_pressed, title_button_rect)

    score_message = font.render(f'Your score: {score}', False, (203, 195, 227))
    score_message_rect = score_message.get_rect(center=(WINDOW_W/2, 350))
    screen.blit(score_message, score_message_rect)

    game_over_font = pygame.font.Font("font/Pixeltype.ttf", 200)
    game_over_msg = game_over_font.render("GAME OVER", False, (0, 0, 0))
    game_over_msg_rect = game_over_msg.get_rect(center=(WINDOW_W/2, 200))
    screen.blit(game_over_msg, game_over_msg_rect)

    player.draw(screen)


def calculate_collisions():
    global screen_number
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        screen_number = 2
        return False
    else:
        return True


def display_score():
    score_surface = font.render(f'Score: {score}', False, (203, 195, 227))
    score_rect = score_surface.get_rect(center=(WINDOW_W/2, 100))
    screen.blit(score_surface, score_rect)
    return score


"""***************** INITIALIZE GAME *****************"""

pygame.init()
screen = pygame.display.set_mode((WINDOW_W, WINDOW_H))
pygame.display.set_caption("Astro Runner")

clock = pygame.time.Clock()
score = 0
font = pygame.font.Font("font/Pixeltype.ttf", 70)

game_active = False
screen_number = 0  # 0: intro screen | 1: game OR paused game | 2: end screen

"""Sprites"""

# Buttons
pause_button = pygame.image.load("graphics/buttons/pause_button.png").convert_alpha()
play_button = pygame.image.load("graphics/buttons/play_button.png").convert_alpha()
button_rect = pause_button.get_rect(topright=(WINDOW_W-10, 20))

home_button = pygame.image.load("graphics/buttons/home_button.png").convert_alpha()
home_button_rect = pause_button.get_rect(topleft=(10, 20))

# Player
player = pygame.sprite.GroupSingle()
player.add(Player.Player())

# Obstacles
obstacle_group = pygame.sprite.Group()

"""Surfaces"""
bg_rect_list = [pygame.image.load("graphics/background.png").convert().get_rect(topleft=(0, 0)),
                        pygame.image.load("graphics/background.png").convert().get_rect(topleft=(1280, 0))]
bg_surface = pygame.image.load("graphics/background.png").convert()

# Intro Screen
title_button = pygame.transform.scale_by(pygame.image.load("graphics/intro_screen/play_button.png").convert_alpha(), 1.5)
title_button_pressed = pygame.transform.scale_by(pygame.image.load("graphics/intro_screen/play_button_pressed.png").convert_alpha(), 1.5)
title_button_rect = title_button.get_rect(midbottom=(WINDOW_W / 2, 600))

title_screen = pygame.transform.scale_by(pygame.image.load("graphics/intro_screen/title_screen.png").convert(), 2)
title_player = pygame.transform.scale_by(pygame.image.load("graphics/player/player_jump.png").convert_alpha(), 4)
title_player_rect = title_player.get_rect(center=(200, 500))
rising = True

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
                    score += 1

            else:
                if event.type == pygame.MOUSEBUTTONDOWN and title_button_rect.collidepoint(pygame.mouse.get_pos()):
                    player.sprite.kill()
                    player.add(Player.Player())
                    obstacle_group.empty()
                    score = 0
                    game_active = True
                    screen_number = 1

            # Play or Pause
            if screen_number == 1:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        game_active = not game_active
                    if home_button_rect.collidepoint(event.pos):
                        game_active = False
                        screen_number = 0

        """Game"""

        # Intro screen
        if screen_number == 0:
            intro_screen()

        # Game
        elif screen_number == 1:

            if game_active:
                animate_background()
                screen.blit(pause_button, button_rect)
                screen.blit(home_button, home_button_rect)
                score = display_score()

                player.draw(screen)
                player.update()

                obstacle_group.draw(screen)
                obstacle_group.update()

                game_active = calculate_collisions()

            else:
                animate_background()
                score = display_score()
                screen.blit(play_button, button_rect)
                screen.blit(home_button, home_button_rect)
                player.draw(screen)
                obstacle_group.draw(screen)

        # End screen
        else:
            end_screen()

        """Draws all elements, updates everything"""
        pygame.display.update()
        clock.tick(60)
