import pygame
from sys import exit
from settings import *
from utility import get_image
from player import Player
from monster import Monster

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

player = Player()
monster = Monster()
# game loop
while True:
    # checks what happens in the game
    for event in pygame.event.get():
        # turns it off
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    elapsed_time += clock.get_time()
    if elapsed_time > 2000:
        invul = False

    if game_over == False:
        # colors backround black
        screen.fill((100, 0, 100))

        player.draw(screen)
        player.update()
        monster.draw(screen)
        monster.update()
        monster.animation()

        text = font.render(f"Lives: {lives}", False, "#FFFFFF")
        screen.blit(text, (700, 10))

        if player.rect.colliderect(monster.rect):
            if not invul:
                lives -= 1
                invul = True
                elapsed_time = 0

        if lives <= 0:
            game_over = True

    else:
        screen.fill((0, 0, 0))
        font2 = pygame.font.Font(None, 100)
        text2 = font2.render(f"Game over", False, "#FFFFFF")
        screen.blit(text2, (220, 265))

    pygame.display.update()
    clock.tick(60)
