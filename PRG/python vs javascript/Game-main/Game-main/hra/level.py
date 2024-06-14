import pygame
from pytmx.util_pygame import load_pygame
from items import Desk, Coin, PowerUp
from monster import Monster
from player import Player1
from player import Player2


class Level:
    def __init__(self, level_data, screen, sprite_groups):
        self.data = load_pygame(level_data)
        self.ground = self.data.get_layer_by_name("ground")
        self.sprite_groups = sprite_groups
        self.screen = screen

        for layer in self.data.visible_layers:
            setattr(self, layer.name, self.data.get_layer_by_name(layer.name))

        for key, group in sprite_groups.items():
            setattr(self, key, group)

        self.background = pygame.Surface(
            (
                self.data.width * self.data.tilewidth,
                self.data.height * self.data.tileheight,
            )
        )

        self.init_items()

        # self.draw_backround()

    def draw_backround(self):
        for x, y, image in self.ground.tiles():
            self.background.blit(
                image, (x * self.data.tilewidth, y * self.data.tileheight)
            )
        self.screen.blit(self.background, (0, 0))

    def init_items(self):
        self.create_items(self.furniture, Desk, self.desk_group)
        self.create_items(self.spawn_coins, Coin, self.coin_group)
        self.create_items(self.spawn_powerups, PowerUp, self.powerup_group)
        self.create_monsters(self.spawn_enemies_h, self.monsters_group)
        self.create_player(self.spawn_player, self.player_group)
        self.create_player2(self.spawn_player, self.player2_group)

    def create_items(self, layer, item_class, group):
        for item in layer:
            new_item = item_class(item.image, item.width, item.height, (item.x, item.y))
            group.add(new_item)
            self.all.add(new_item)

    def create_monsters(self, layer, group):
        for monster in layer:
            new_monster = Monster((monster.x, monster.y))
            group.add(new_monster)
            self.all.add(new_monster)

    def create_player(self, layer, group):
        for player in layer:
            new_player = Player1((player.x, player.y), self.sprite_groups)
            group.add(new_player)
            self.all.add(new_player)

    def create_player2(self, layer, group):
        for player in layer:
            new_player2 = Player2((player.x, player.y), self.sprite_groups)
            group.add(new_player2)
            self.all.add(new_player2)


# path = "../assets/tiled/ucebna2.tmx"
# level = Level(path)
