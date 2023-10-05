import pygame

naytto = pygame.display.set_mode((640, 400))
pygame.display.set_caption("Minun Python Pelini.")
print("Testi")

def main():
    while True:
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break

        naytto.fill((0, 0, 0))
        pygame.draw.line(naytto, (0, 0, 255), (100, 50), (400, 370))
        pygame.display.flip()

main()