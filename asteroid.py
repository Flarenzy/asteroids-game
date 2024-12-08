import random
import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="green", center=self.position,radius=self.radius, width=2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        asteroid1_velocity = self.velocity.rotate(angle)
        asteroid2_velocity = self.velocity.rotate(-angle)
        asteroid1_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid2_radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, asteroid1_radius)
        a2 = Asteroid(self.position.x, self.position.y, asteroid2_radius)
        a1.velocity = asteroid1_velocity * 1.2
        a2.velocity = asteroid2_velocity 