import pygame
from circleshape import *
from weapon import *
import random

class WeaponSpawn(CircleShape):
    def __init__(self, x, y, type):
        super().__init__(x, y, 15)
        self.type = type
        self.color = self.choose_color(self.type)

    def choose_color(self, type):
        if type == "Shotgun":
            return pygame.Color("Blue")
        if type == "Force Field":
            return pygame.Color("Yellow")
        if type == "Boulder":
            return pygame.Color("Red")
        if type == "SMG":
            return pygame.Color("Green")
        if type == "Rifle":
            return pygame.Color("Orange")
        
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)

    def create(self, player):
        if self.type == "Shotgun":
            shotgun = Weapon(self.type, 2, 500, 20)
            player.weapon_list.append(shotgun)
        if self.type == "Force Field":
            force_field = Weapon(self.type, 10, 1500, 5)
            player.weapon_list.append(force_field)
        if self.type == "Boulder":
            boulder = Weapon(self.type, 5, 500, 100)
            player.weapon_list.append(boulder)
        if self.type == "SMG":
            smg = Weapon(self.type, 0.1, 1500, 5)
            player.weapon_list.append(smg)
        if self.type == "Rifle":
            rifle = Weapon(self.type, 0.001, 1500, 20)
            player.weapon_list.append(rifle)
    
    def kill(self):
        pygame.sprite.Sprite.kill(self)


