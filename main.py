import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# game loop
running = True
while running:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255,0,0))
    pygame.display.update()
    screen.fill((255,255,0))

pygame.quit()