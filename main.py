import sys

import pygame

from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    updatetable = pygame.sprite.Group()
    drawtable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = updatetable, drawtable
    Asteroid.containers = (asteroids, updatetable, drawtable)
    AsteroidField.containers = updatetable
    Shot.containers = (shots, updatetable, drawtable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    asteroidfield = AsteroidField( )

    while True:
        # Exit the game if the window is closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        updatetable.update(dt)

        for asteroid in asteroids:
            # Check if asteroid is shot
            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.kill()
                    shot.kill()
                    
            # Check if player collides with asteroid
            if asteroid.check_collision(player):
                print("Game over!")
                sys.exit()
        
        for item in drawtable:
            item.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
