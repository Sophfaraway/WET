import pygame
from sys import exit

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 1. způsob
# x = 250
# y = 300

# 2. způspb
# square = pygame.Rect(250, 300, 70, 70)

# 3. způsob - vytvořit surface a z něho rectangle
square_surface = pygame.Surface((70, 70))
square_surface.fill((0, 255, 0))


square = square_surface.get_rect(topleft=(250, 300))

ninja_surf = pygame.image.load("ninja.png").convert_alpha()
ninja_rect = ninja_surf.get_rect(topleft=(450, 200))



clock = pygame.time.Clock()



running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()


    key = pygame.key.get_pressed()

    if key[pygame.K_w]:
        square.y -= 5
    if key[pygame.K_a]:
        square.x -= 5
    if key[pygame.K_s]:
        square.y += 5
    if key[pygame.K_d]:
        square.x += 5

    screen.fill((255,255,255))

    # 1. způsob vykreslení
    # pygame.draw.rect(screen, (0,255,0), (x, y, 70, 70))

    # 2. způsob vykreslení
    # pygame.draw.rect(screen, (0,255,0), square)

    # 3. způsob vykreslení
    screen.blit(square_surface, square)

    screen.blit(ninja_surf, ninja_rect)

    if square.colliderect(ninja_rect):
        print("Kolize!!!")

    pygame.display.update()

    clock.tick(60)
pygame.quit()
