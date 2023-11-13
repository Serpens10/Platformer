import pygame
import sys


pygame.init()
screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
screen_rect = screen.get_rect()
clock = pygame.time.Clock()



running = True 

while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    

    screen.fill('black')
    clock.tick(60)        
    pygame.display.update()

