import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        # size: x and y. identical because square.
        self.image.fill('grey')
        self.rect = self.image.get_rect(topleft = position)
