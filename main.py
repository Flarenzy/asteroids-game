import pygame

from constants import ASTEROID_KINDS
from constants import ASTEROID_MAX_RADIUS
from constants import ASTEROID_MIN_RADIUS
from constants import ASTEROID_SPAWN_RATE
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
from player import Player
from asteroid import Asteroid


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
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player1 = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        for element in updatable:
            element.update(dt)
        player1.move(dt=dt)
        for element in drawable:
            element.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()
