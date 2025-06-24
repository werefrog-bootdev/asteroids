import pygame

from constants import *


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        # Exit the game if the window is closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Fill the screen with black color
        screen.fill("black")
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
