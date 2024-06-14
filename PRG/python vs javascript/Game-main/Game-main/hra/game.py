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
def main():
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

    scenario = 0

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
            player2.sprite.invul_time += clock.get_time()

            player1_text = font.render("Player 1:", False, "#1520A6")
            lives1 = font.render(f"Lives: {player.sprite.lives}", False, "#FFFFFF")
            score1 = font.render(f"Score: {player.sprite.score}", False, "#FFFFFF")
            screen.blit(lives1, (180, 15))
            screen.blit(score1, (100, 15))
            screen.blit(player1_text, (15, 15))

            player2_text = font.render("Player 2:", False, "#800000")
            lives2 = font.render(f"Lives: {player2.sprite.lives}", False, "#FFFFFF")
            score2 = font.render(f"Score: {player2.sprite.score}", False, "#FFFFFF")
            screen.blit(lives2, (1190, 15))
            screen.blit(score2, (1110, 15))
            screen.blit(player2_text, (1025, 15))

            if player.sprite.lives <= 0:
                game_over = True
                scenario = 1
            if player2.sprite.lives <= 0:
                game_over = True
                scenario = 2
            if player.sprite.score + player2.sprite.score == 19 and player.sprite.score < player2.sprite.score :
                game_over = True
                scenario = 3
            if player.sprite.score + player2.sprite.score == 19 and player.sprite.score > player2.sprite.score :
                game_over = True
                scenario = 4

        elif scenario == 1 :
            screen.fill(("#800000"))
            font1 = pygame.font.Font(None, 60)
            font2 = pygame.font.Font(None, 100)
            winner = font2.render(f"Player 2 wins!", False, "#FFFFFF")
            text_score = font1.render(f"Player 1 died", False, "#FFFFFF")
            play_again = font1.render(f"Press SPACE to play again", False, "#FFFFFF")
            exit_game = font1.render(f"Press X to exit", False, "#FFFFFF")

            screen.blit(winner, (410, 340))
            screen.blit(text_score, (525, 420))
            screen.blit(play_again, (385, 520))
            screen.blit(exit_game, (495, 600))

            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                main()
            if key[pygame.K_x]:
                exit()
        
        elif scenario == 2 :
            screen.fill(("#1520A6"))
            font1 = pygame.font.Font(None, 60)
            font2 = pygame.font.Font(None, 100)
            winner = font2.render(f"Player 1 wins!", False, "#FFFFFF")
            text_score = font1.render(f"Player 2 died", False, "#FFFFFF")
            play_again = font1.render(f"Press SPACE to play again", False, "#FFFFFF")
            exit_game = font1.render(f"Press X to exit", False, "#FFFFFF")
            screen.blit(winner, (410, 340))
            screen.blit(text_score, (525, 420))
            screen.blit(play_again, (385, 520))
            screen.blit(exit_game, (495, 600))

            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                main()
            if key[pygame.K_x]:
                exit()


        elif scenario == 3 :
            screen.fill(("#800000"))
            font1 = pygame.font.Font(None, 60)
            font2 = pygame.font.Font(None, 100)
            winner = font2.render(f"Player 2 wins!", False, "#FFFFFF")
            text_score = font1.render(f"{player.sprite.score} : {player2.sprite.score}", False, "#FFFFFF")
            play_again = font1.render(f"Press SPACE to play again", False, "#FFFFFF")
            exit_game = font1.render(f"Press X to exit", False, "#FFFFFF")

            screen.blit(winner, (410, 340))
            screen.blit(text_score, (600, 420))
            screen.blit(text_score, (600, 420))
            screen.blit(play_again, (385, 520))
            screen.blit(exit_game, (495, 600))

            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                main()
            if key[pygame.K_x]:
                exit()
            
                

        elif scenario == 4 :
            screen.fill(("#1520A6"))
            font1 = pygame.font.Font(None, 60)
            font2 = pygame.font.Font(None, 100)
            winner = font2.render(f"Player 1 wins!", False, "#FFFFFF")
            text_score = font1.render(f"{player.sprite.score} : {player2.sprite.score}", False, "#FFFFFF")
            play_again = font1.render(f"Press SPACE to play again", False, "#FFFFFF")
            exit_game = font1.render(f"Press X to exit", False, "#FFFFFF")
            screen.blit(winner, (410, 340))
            screen.blit(text_score, (600, 420))
            screen.blit(play_again, (385, 520))
            screen.blit(exit_game, (495, 600))

            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                main()
            if key[pygame.K_x]:
                exit()

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()