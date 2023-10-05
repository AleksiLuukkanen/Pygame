import pygame

naytto = pygame.display.set_mode((640, 400))
pygame.display.set_caption("Minun Python Pelini.")
print("Testi")
x = 400
y = 400

def main():
    while True:
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break

        naytto.fill((0, 0, 0))
        hahmo = pygame.image.load("pelihahmo.png").convert()
        naytto.blit(hahmo, (x, y))
        pygame.display.flip()

main()