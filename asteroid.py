import pygame
import random
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_velocity = 1.2
        vector1 = self.velocity.rotate(random_angle) * new_velocity
        vector2 = self.velocity.rotate(-random_angle) * new_velocity
        Asteroid(self.position.x, self.position.y, new_radius).velocity = vector1
        Asteroid(self.position.x, self.position.y, new_radius).velocity = vector2
    