import pygame
import sys

display = pygame.display.set_mode((1920,1080),pygame.FULLSCREEN)
donkerblauw = 0,0,64
rood = 255,0,0
rechthoekhoogte = 540
rechthoekhoogte2 = 540
rechthoekhoogtesnelheid = 0
rechthoekhoogtesnelheid2 = 0
balx = 1000
baly = 500

class Balsnelheid:
    def __init__(self,x,y):
        self.x = x
        self.y = y
balsnelheid = Balsnelheid(0.5,0)

while True:
    display.fill(donkerblauw)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            if event.key == pygame.K_s:
                rechthoekhoogtesnelheid = 0.5
            if event.key == pygame.K_w:
                rechthoekhoogtesnelheid = -0.5 
    if balsnelheid.y > 0:
        rechthoekhoogtesnelheid2 = 3
    if balsnelheid.y < 0:
        rechthoekhoogtesnelheid2 = -3
    rechthoekhoogte = rechthoekhoogte + rechthoekhoogtesnelheid
    rechthoekhoogte2 = rechthoekhoogte2 + rechthoekhoogtesnelheid2
    rechthoek = pygame.Rect(0,rechthoekhoogte,20,100)
    rechthoek2 = pygame.Rect(1900,rechthoekhoogte2,20,100)
    balx = balx + balsnelheid.x
    baly = baly + balsnelheid.y
    bal = pygame.Rect(balx,baly,10,10)
    pygame.draw.rect(display,rood,rechthoek)
    pygame.draw.rect(display,rood,rechthoek2)
    pygame.draw.rect(display,rood,bal)

    pygame.display.flip()
