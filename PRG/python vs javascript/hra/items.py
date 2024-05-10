import pygame

# from pygame.sprite import _Group


class Item(pygame.sprite.Sprite):
    def __init__(self, image, width, height, position):
        super().__init__()
        self.image = image
        self.width = width
        self.height = height
        self.position = position
        self.scale = 1
        self.scale_item()
        self.rect = self.image.get_rect(topleft=self.position)

    def scale_item(self):
        scaled_size = (self.width * self.scale, self.height * self.scale)
        self.image = pygame.transform.scale(self.image, scaled_size)


class Coin(Item):
    pass


class Desk(Item):
    pass


class PowerUp(Item):
    pass
