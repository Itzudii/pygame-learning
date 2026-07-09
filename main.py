import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))


class Rect():
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

rect1 = Rect(150,100,50,50)
rect2 = Rect(100,100,50,50)

# game loop
running = True
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(screen,(255,0,0),(rect1.x,rect1.y,rect1.w,rect1.h))
    pygame.draw.rect(screen,(255,255,0),(rect2.x,rect2.y,rect2.w,rect2.h))


    # logic
    mouse = pygame.mouse.get_pos()
    rect1.x = mouse[0]
    rect1.y = mouse[1]
    
    pygame.display.update()



pygame.quit()