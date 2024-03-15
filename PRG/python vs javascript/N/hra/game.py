import pygame
from sys import exit

# inicializes the game - starts it
pygame.init()

clock = pygame.time.Clock()

screen_height = 600
screen_width = 800
# creates screen
screen = pygame.display.set_mode((screen_width, screen_height))


def player_animation(direction):
    global p_index, player_surf
    frame_count = 4

    p_index += 0.1
    if p_index >= frame_count:
        p_index = 0

    player_surf = get_image(player_spritesheet, int(p_index), direction, 15, 16, 3)


def monster_animation():
    global monster_surf, monster_index
    monster_index += 0.1
    if monster_index > len(monster_walk):
        monster_index = 0
    monster_surf = monster_walk[int(monster_index)]


def get_image(sheet, frame_x, frame_y, width, height, scale):
    img = pygame.Surface((width, height)).convert_alpha()
    img.blit(sheet, (0, 0), ((frame_x * width), (frame_y * height), width, height))
    img = pygame.transform.scale(img, (width * scale, height * scale))
    img.set_colorkey((0, 0, 0))
    return img


player_x = 100
player_y = 200
p_index = 0

# convert alpha - transparency
player_spritesheet = pygame.image.load("man_brownhair_run.png").convert_alpha()
# creates player - x,y,width,height
player_surf = get_image(player_spritesheet, 0, 4, 15, 16, 3)
player_rect = player_surf.get_rect(midbottom=(player_x, player_y))


monster_walk_1 = pygame.image.load("monster.png").convert_alpha()
monster_walk_2 = pygame.image.load("monster_walk.png").convert_alpha()
monster_walk = [monster_walk_1, monster_walk_2]
monster_index = 0
monster_surf = monster_walk[monster_index]

monster_y = 500
monster_x = 750

monster_rect = monster_surf.get_rect(midbottom=(monster_x, monster_y))


lives = 3
font = pygame.font.Font(None, 25)

monster_direction = "Left"

game_over = False

elapsed_time = 0

invul = True

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
    print(elapsed_time)

    if game_over == False:
        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            # player.move_ip(-10, 0)
            player_rect.left -= 10
            player_animation(2)
        if key[pygame.K_d]:
            player_rect.right += 10
            player_animation(3)
        if key[pygame.K_s]:
            player_rect.bottom += 10
            player_animation(0)
        if key[pygame.K_w]:
            player_rect.top -= 10
            player_animation(1)
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
        monster_animation()
        text = font.render(f"Lives: {lives}", False, "#FFFFFF")
        screen.blit(text, (700, 10))
        # draws player on screen, where
        screen.blit(player_surf, player_rect)
        screen.blit(monster_surf, monster_rect)
        # updates everything

        if player_rect.colliderect(monster_rect):
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
