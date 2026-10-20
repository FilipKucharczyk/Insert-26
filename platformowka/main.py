import pygame
pygame.init()

#USTWAIENIA GRY
SZEROKOSC = 800
WYSOKOSC = 600
FPS = 60

#Ustawienia gracza
ROZMIAR = 40
X = 150
Y = 150
KROK = 20

#Kolory RGB
BIALY = (255, 255, 255)
GRACZOWY = (163, 219, 90)
TLO = (220, 163, 61)

#Zegar
zegar = pygame.time.Clock()

ekran = pygame.display.set_mode((SZEROKOSC,WYSOKOSC))
pygame.display.set_caption("Geomtryczny skok!!!")

#Tworzenie gracza 
#gracz = pygame.Surface((ROZMIAR, ROZMIAR))
#gracz.fill(GRACZOWY)
#Sciezka wzgledna
gracz = pygame.image.load("./platformowka/assets/cube.png")
#Sciezka bezwzgledna
#gracz = pygame.image.load("C:/Users/clientadmin/Documents/Filip Insert wtorek/platformowka/assets/cube.png")
gracz = pygame.transform.scale(gracz, (ROZMIAR, ROZMIAR))

gra_dziala = True
while gra_dziala:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gra_dziala = False    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                X += KROK
            elif event.key == pygame.K_LEFT:
                X -= KROK 
            elif event.key == pygame.K_DOWN:
                Y += KROK
            elif event.key == pygame.K_UP:
                Y -= KROK
    #Ograniczenia
    if X < 0 :      #Lewa
        X = 0
    if X > SZEROKOSC - ROZMIAR: #Prawa
        X = SZEROKOSC - ROZMIAR
    if Y < 0:  #Góra
        Y = 0
    if Y > WYSOKOSC - ROZMIAR: #Dół
        Y = WYSOKOSC - ROZMIAR
        
    
    #Grawitacja  
    Y += 2
         
    ekran.fill(TLO)
    
    ekran.blit(gracz,(X,Y))
    
    pygame.display.update()
    zegar.tick(FPS)