import pygame
from sys import exit

# inicializes the game - starts it
pygame.init()

clock = pygame.time.Clock()

screen_height = 600
screen_width = 800
# creates screen
screen = pygame.display.set_mode((screen_width, screen_height))

player_x = 100
player_y = 200
# creates player - x,y,width,height
player_surf = pygame.image.load("bunny.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(player_x, player_y))
# convert alpha - transparency


monster_surf = pygame.image.load("monster.png").convert_alpha()
monster_rect = monster_surf.get_rect(midbottom=(300, 600))


lives = 3
font = pygame.font.Font(None, 25)

monster_direction = "Left"

monster_y = 400
monster_x = 600

game_over = False

# game loop
while True:
    # checks what happens in the game
    for event in pygame.event.get():
        # turns it off
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if game_over == False:
        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            # player.move_ip(-10, 0)
            player_rect.left -= 10
        if key[pygame.K_d]:
            player_rect.right += 10
        if key[pygame.K_s]:
            player_rect.bottom += 10
        if key[pygame.K_w]:
            player_rect.top -= 10
        # colors backround black
        screen.fill((0, 0, 0))

        if monster_rect.x <= 0:
            monster_direction = "Right"
        elif monster_rect.x >= screen_width - 50:
            monster_direction = "Left"

        if monster_direction == "Left":
            monster_rect.x -= 5
        if monster_direction == "Right":
            monster_rect.x += 5

        # if monster_rect.x <= 0 or monster_rect.x >= screen_width - 50:
        #     speed = -speed
        # monster_rect += speed

        text = font.render(f"Lives: {lives}", False, "#FFFFFF")
        screen.blit(text, (700, 10))
        # draws player on screen, where
        screen.blit(player_surf, player_rect)
        screen.blit(monster_surf, monster_rect)
        # updates everything

        if player_rect.colliderect(monster_rect):
            lives -= 1

        if lives <= 0:
            game_over = True

    else:
        screen.fill((0, 0, 0))
        font2 = pygame.font.Font(None, 100)
        text2 = font2.render(f"Game over", False, "#FFFFFF")
        screen.blit(text2, (220, 265))

    pygame.display.update()
    clock.tick(60)
