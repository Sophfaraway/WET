import pygame
from pytmx.util_pygame import load_pygame


class Level:
    def __init__(self, path):
        self.path = path
        self.data = load_pygame(self.path)
        self.ground = self.data.get_layer_by_name("ground")

    def draw_backround(self):
        for tile in self.ground.tiles():
            print(tile)


level = Level("../assets/tiled/ucebna2.tmx")
level.draw_backround()
