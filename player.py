import pygame

from circleshape import CircleShape
from shoot import Shot
from constants import PLAYER_RADIUS
from constants import PLAYER_SPEED
from constants import PLAYER_SHOOT_SPEEED
from constants import PLAYER_TURN_SPEED

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
    
        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(surface=screen, color="white", points=self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate((-1)*dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE]:
            self.shot(dt)

    def shot(self, dt):
        new_shot = Shot(self.position.x, self.position.y)
        new_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation)

    def move(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            self.position += forward * PLAYER_SPEED * dt    
        if keys[pygame.K_s]:
            backwards = pygame.Vector2(0, 1).rotate(self.rotation) * (-1)
            self.position += backwards * PLAYER_SPEED * dt    
        