import pygame
import sys
import time
import random
import threading

pygame.init()

naytto = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Vihollis peli.")
x = 20
y = 60

x2 = 700
y2 = 60

game_over_font = pygame.font.Font(None, 74)

def move_vihollinen():
    global x2
    while True:
        x2 += random.randint(-90, 90)
        x2 = max(1, min(700, x2))
        time.sleep(2)

def peli_ohi():
    peli_ohi_teksti = game_over_font.render("HÄVISIT", True, (255, 0, 0))
    naytto.blit(peli_ohi_teksti, (300, 250))
    pygame.display.flip()
    time.sleep(10)
    pygame.quit()
    sys.exit()

def main():
    global x, y

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        background = pygame.image.load("Maailma.png").convert()
        naytto.blit(background, (0, 0))

        viholliset = pygame.image.load("vihollinen.png").convert_alpha()
        viholliset.set_colorkey((0, 0, 0))
        naytto.blit(viholliset, (x2, y2))

        hahmot = pygame.image.load("pelihahmo.png").convert_alpha()
        hahmot.set_colorkey((0, 0, 0))
        naytto.blit(hahmot, (x, y))

        hahmo_rect = hahmot.get_rect(x=x + 100, y=y + 100, width=hahmot.get_width() - 200, height=hahmot.get_height() - 200)
        vihollinen_rect = viholliset.get_rect(x=x2 + 100, y=y2 + 100, width=viholliset.get_width() - 200, height=viholliset.get_height() - 200)
        if hahmo_rect.colliderect(vihollinen_rect):
            peli_ohi()

        pygame.display.flip()

        if pygame.key.get_pressed()[pygame.K_w]:
            y = y - 1.5
        elif pygame.key.get_pressed()[pygame.K_d]:
            x = x + 1.5
        elif pygame.key.get_pressed()[pygame.K_a]:
            x = x - 1.5
        elif pygame.key.get_pressed()[pygame.K_s]:
            y = y + 1.5

vihollinen_liikkuu = threading.Thread(target=move_vihollinen)
vihollinen_liikkuu.start()

main()
