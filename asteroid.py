from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity *dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        positive_angle = self.rotate(random_angle)
        negative_angle = self.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        pos_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
        
        neg_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
        
        pos_asteroid.velocity = self.velocity.rotate(positive_angle) * 1.2
        neg_asteroid.velocity = self.velocity.rotate(negative_angle) * 1.2
        