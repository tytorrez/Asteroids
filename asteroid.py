import pygame
from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,
                           pygame.Color("white"),
                            self.position,
                            self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity*dt

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            split_angle = random.uniform(20,50)

            new_direction1 = self.velocity.rotate(split_angle)
            new_direction2 = self.velocity.rotate(split_angle*-1)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            
            asteroid1.velocity = new_direction1* 1.5
            asteroid2.velocity = new_direction2* 1.5
