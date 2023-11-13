import pygame , sys
from settings import *
from level import Level


pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
screen_rect = screen.get_rect()
clock = pygame.time.Clock()

level = Level(level_map, screen)



running = True 

while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    

    
    screen.fill('black')
    clock.tick(60)        
    pygame.display.update()

