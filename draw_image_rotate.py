import sys
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((400, 300))
FPSCLOCK = pygame.time.Clock()

def main():
    logo = pygame.image.load("images/pythonlogo.jpg")
    theta = 0

    while True:
        for event in pygame.event.get(QUIT):
            pygame.quit()
            sys.exit()

        theta += 1
        SURFACE.fill((225, 225, 225))

        # rotate logo
        rotated_logo = pygame.transform.rotate(logo, theta)
        rect = rotated_logo.get_rect()
        rect.center = (200, 150)
        SURFACE.blit(rotated_logo, rect)

        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == '__main__':
    main()
