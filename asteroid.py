import pygame
from circleshape import *
from constants import *
import random
import math

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, vertices=12):
        super().__init__(x, y, radius)
        self.vertices = vertices
        self.points = self.generate_points()

    def draw(self, screen):

        polygon_points = [self.position + p for p in self.points]
        pygame.draw.polygon(screen,
                           pygame.Color("white"),
                            polygon_points, 2)
        
    def update(self, dt):
        self.position += self.velocity*dt

    def generate_points(self):
        
        points = []
        for i in range(self.vertices):
            angle = i * (360 / self.vertices)
            offset = random.uniform(self.radius*0.9, self.radius*1.2)
            x = math.cos(math.radians(angle)) * offset
            y = math.sin(math.radians(angle)) * offset
            points.append(pygame.math.Vector2(x,y))

        return points


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
