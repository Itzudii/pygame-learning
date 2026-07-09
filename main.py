import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True

# way1
rect1 = [100,100,50,50]


# way2
rect1_x = 100
rect1_y = 100
rect1_w = 50
rect1_h = 50

# way 3
class Rect():
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

rect1 = Rect(100,100,50,50)

# game loop
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    mouse = pygame.mouse.get_pos()
    pygame.draw.rect(screen,(255,255,0),(mouse[0],mouse[1],50,50))
    
    pygame.display.update()



pygame.quit()