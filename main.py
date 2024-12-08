import time

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import ASTEROID_KINDS
from constants import ASTEROID_MAX_RADIUS
from constants import ASTEROID_MIN_RADIUS
from constants import ASTEROID_SPAWN_RATE
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
from player import Player
from shoot import Shot



def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt: float = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable, )
    Shot.containers = (shots, updatable, drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player1 = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        for element in updatable:
            element.update(dt)
        for asteroid in asteroids:
            if asteroid.collisions(player1):
                print("Game over!")
                raise SystemExit("Game has finished!")
            for bullet in shots:
                if asteroid.collisions(bullet):
                    asteroid.split()
                    bullet.kill()

        player1.move(dt=dt)
        for element in drawable:
            element.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()
