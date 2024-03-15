import pygame
from settings import *
from utility import get_image


class Monster(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 750
        self.y = 500
        # self.walk1 = pygame.image.load("assets/monster/monster.png").convert_alpha()
        # self.walk2 = pygame.image.load("assets/monster/monster_walk.png").convert_alpha()
        self.spritesheet = pygame.image.load(
            "assets/monster/monster_sprites.png"
        ).convert_alpha()
        self.image = get_image(self.spritesheet, 0, 4, 16, 16, 3)
        self.index = 0
        self.rect = self.image.get_rect(midbottom=(self.x, self.y))
        self.direction = "Left"

    def animation(self):
        frame_count = 2
        self.index += 0.1
        if self.index >= frame_count:
            self.index = 0
        self.image = get_image(self.spritesheet, int(self.index), 1, 16, 16, 5)

    def update(self):

        if self.rect.x <= 0:
            self.direction = "Right"
        elif self.rect.x >= screen_width - 50:
            self.direction = "Left"

        if self.direction == "Left":
            self.rect.x -= 5
        if self.direction == "Right":
            self.rect.x += 5

    def draw(self, screen):
        screen.blit(self.image, self.rect)
