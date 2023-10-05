import keyboard
import pygame

naytto = pygame.display.set_mode((640, 400))
pygame.display.set_caption("Minun Python Pelini.")
print("Testi")
x = 20
y = 20

def main():
    while True:
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break

        naytto.fill((0, 0, 0))
        hahmo = pygame.image.load("pelihahmo.png").convert()
        naytto.blit(hahmo, (x, y))
        pygame.display.flip()
        if keyboard.is_pressed("W"):
            x = x + 5

main()