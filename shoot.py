import pygame

from circleshape import CircleShape
from constants import PLAYER_SHOOT_SPEEED
from constants import SHOOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOOT_RADIUS)
    
    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="red", center=self.position, radius=self.radius, width=2)
    
    def update(self, dt):
        self.position += (self.velocity * PLAYER_SHOOT_SPEEED * dt)
