import pygame

from constants import ASTEROID_KINDS
from constants import ASTEROID_MAX_RADIUS
from constants import ASTEROID_MIN_RADIUS
from constants import ASTEROID_SPAWN_RATE
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt: float = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()
