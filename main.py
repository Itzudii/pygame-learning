import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Color:
    BLACK = (0,0,0)
    RED = (255,0,0)
    YELLOW = (255,255,0)
    BLUE = (0,0,255)

class Rect():
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.left = self.x
        self.right = self.x+self.w
        self.top = self.y
        self.bottom = self.y+self.h

    def update(self):
        self.left = self.x
        self.right = self.x+self.w
        self.top = self.y
        self.bottom = self.y+self.h


rect1 = Rect(150,100,50,50)
rect2 = Rect(100,100,50,50)
color = Color.RED
# game loop
running = True
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(screen,Color.YELLOW,(rect2.x,rect2.y,rect2.w,rect2.h))
    pygame.draw.rect(screen,color,(rect1.x,rect1.y,rect1.w,rect1.h))
    rect1.update()
    rect2.update()

    # logic 
    mouse = pygame.mouse.get_pos()
    rect1.x = mouse[0]
    rect1.y = mouse[1]

    if rect2.right > rect1.left and rect2.left < rect1.right and rect1.top < rect2.bottom and rect1.bottom > rect2.top:
        color = (0,255,0)
    else:
        color = Color.RED
    
    pygame.display.update()



pygame.quit()