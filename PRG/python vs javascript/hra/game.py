import pygame
from sys import exit
from settings import *
from utility import get_image
from player import Player
from monster import Monster

# from level import Level

# inicializes the game - starts it
pygame.init()

clock = pygame.time.Clock()

# creates screen
screen = pygame.display.set_mode((screen_width, screen_height))

font = pygame.font.Font(None, 25)

game_over = False

elapsed_time = 0

invul = True

lives = 3

player = pygame.sprite.GroupSingle()
player.add(Player())

monsters = pygame.sprite.Group()
monster = Monster()
monsters.add(monster)

# game loop
while True:
    # checks what happens in the game
    for event in pygame.event.get():
        # turns it off
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if game_over == False:
        # colors backround black
        screen.fill((100, 0, 100))

        player.draw(screen)
        player.update(monsters)

        monster.draw(screen)
        monster.update()
        monster.animation()

        player.sprite.invul_time += clock.get_time()

        text = font.render(f"Lives: {player.sprite.lives}", False, "#FFFFFF")
        screen.blit(text, (1200, 10))

        if player.sprite.lives <= 0:
            game_over = True

    else:
        screen.fill((0, 0, 0))
        font2 = pygame.font.Font(None, 100)
        text2 = font2.render(f"Game over", False, "#FFFFFF")
        screen.blit(text2, (450, 340))

    pygame.display.update()
    clock.tick(60)
