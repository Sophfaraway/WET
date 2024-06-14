import pygame
from sys import exit
from settings import *
from utility import get_image
from player import Player1
from player import Player2

# from player import Player2
from monster import Monster
from level import Level

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
player2 = pygame.sprite.GroupSingle()
# player.add(Player())

monsters = pygame.sprite.Group()
# monster = Monster()
# monsters.add(monster)

desk_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
powerup_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
# desk_group.draw(screen)

sprite_groups = {
    "all": all_sprites,
    "player_group": player,
    "player2_group": player2,
    "monsters_group": monsters,
    "desk_group": desk_group,
    "coin_group": coin_group,
    "powerup_group": powerup_group,
}

level = Level("tiled/ucebna-final.tmx", screen, sprite_groups)


# game loop
while True:
    level.draw_backround()
    # checks what happens in the game
    for event in pygame.event.get():
        # turns it off
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if game_over == False:
        # screen.fill((100, 0, 100))
        level.draw_backround()

        monsters.update()
        # player.draw(screen)
        player.update()
        player2.update()

        # monster.draw(screen)
        # monster.update()
        # monster.animation()

        all_sprites.draw(screen)

        player.sprite.invul_time += clock.get_time()

        player1_text = font.render("Player 1:", False, "#FFFFFF")
        lives1 = font.render(f"Lives: {player.sprite.lives}", False, "#FFFFFF")
        score1 = font.render(f"Score: {player.sprite.score}", False, "#FFFFFF")
        screen.blit(lives1, (15, 45))
        screen.blit(score1, (15, 30))
        screen.blit(player1_text, (15, 15))

        player2_text = font.render("Player 2:", False, "#FFFFFF")
        lives2 = font.render(f"Lives: {player2.sprite.lives}", False, "#FFFFFF")
        score2 = font.render(f"Score: {player2.sprite.score}", False, "#FFFFFF")
        screen.blit(lives2, (1190, 45))
        screen.blit(score2, (1190, 30))
        screen.blit(player2_text, (1190, 15))

        if player.sprite.lives <= 0:
            game_over = True

    else:
        screen.fill((0, 0, 0))
        font2 = pygame.font.Font(None, 100)
        text2 = font2.render(f"Game over", False, "#FFFFFF")
        screen.blit(text2, (450, 340))

    pygame.display.update()
    clock.tick(60)
