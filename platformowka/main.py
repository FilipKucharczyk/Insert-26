import pygame
pygame.init()

FPS = 60
BIALY = (255, 255, 255)
#Zegar
zegar = pygame.time.Clock()

ekran = pygame.display.set_mode((800,600))

gra_dziala = True
while gra_dziala:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            gra_dziala = False           
    
    ekran.fill(BIALY)
    
    pygame.display.update()
    zegar.tick(FPS)