import pygame
from utility import get_image
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 100
        self.y = 200
        self.index = 0
        self.spritesheet = pygame.image.load("assets/player/man.png").convert_alpha()
        self.image = get_image(self.spritesheet, 0, 4, 15, 16, 3)
        self.rect = self.image.get_rect(midbottom=(self.x, self.y))
        self.lives = 3
        self.invul = False
        self.invul_time = 0

    def animation(self, direction):
        frame_count = 4

        self.index += 0.1
        if self.index >= frame_count:
            self.index = 0

        self.image = get_image(self.spritesheet, int(self.index), direction, 15, 16, 3)

    def update(self, monsters):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.rect.left -= 10
            self.animation(2)
        if key[pygame.K_d]:
            self.rect.right += 10
            self.animation(3)
        if key[pygame.K_s]:
            self.rect.bottom += 10
            self.animation(0)
        if key[pygame.K_w]:
            self.rect.top -= 10
            self.animation(1)

        if self.rect.x > screen_width:
            self.rect.x = 10
        elif self.rect.x < 0:
            self.rect.x = screen_width - 10

        if self.rect.y > screen_height:
            self.rect.y = 10
        elif self.rect.y < 0:
            self.rect.y = screen_height - 10

        if pygame.sprite.spritecollide(self, monsters, False):
            if not self.invul:
                self.lives -= 1
                self.invul = True
                self.invul_time = 0

        if self.invul_time > 2000:
            self.invul = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
