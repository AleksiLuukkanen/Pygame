import pygame
import time
import sys

pygame.init()

naytto = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Vihollis peli.")

x = 20
y = 60

x2 = 20
y2 = 60
def main():
    global x, y

    while True:
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        
        background = pygame.image.load("Maailma.png").convert()
        naytto.blit(background, (0, 0))

        hahmo = pygame.image.load("vihollinen.png").convert_alpha()
        hahmo.set_colorkey((0, 0, 0))
        naytto.blit(hahmo, (x2, y2))

        hahmo = pygame.image.load("pelihahmo.png").convert_alpha()
        hahmo.set_colorkey((0, 0, 0))
        naytto.blit(hahmo, (x, y))

        pygame.display.flip()

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            y = y - 1.5
        elif pygame.key.get_pressed()[pygame.K_d]:
            x = x + 1.5
        elif pygame.key.get_pressed()[pygame.K_a]:
            x = x - 1.5
main()