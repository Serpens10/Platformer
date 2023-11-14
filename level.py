import pygame
from tiles import Tile
from settings import TILESIZE

class Level :
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
            
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                if cell == 'X' :
                    x = col_index * TILESIZE
                    y = row_index * TILESIZE
                    tile = Tile((x, y), TILESIZE)
                    self.tiles.add(tile)


    def run(self):
        self.tiles.draw(self.display_surface)   