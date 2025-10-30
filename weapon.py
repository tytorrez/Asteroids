import pygame
from constants import *

class Weapon():
    def __init__(self, type, cooldown, speed, shot_radius):
        self.type = type
        self.cooldown = cooldown
        self.speed = speed
        self.shot_radius = shot_radius
    
    def get_type(self):
        return self.type
    
    def get_cooldown(self):
        return self.cooldown
    
    def get_speed(self):
        return self.speed

    def get_shot_radius(self):
        return self.shot_radius