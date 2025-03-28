import pygame
from circleshape import CircleShape
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", 
                           self.position, 
                           self.radius, width=2)
        
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        # if small asteroid, it disappears 
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # if not, 2 smaller asteroids appear

        # randomize the angle for the 2 new asteroids
        new_angle = random.uniform(20, 50)        
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # initialize the 2 new asteroids
        asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_a.velocity = self.velocity.rotate(-new_angle) * 1.2
        asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_b.velocity = self.velocity.rotate(new_angle) * 1.2
