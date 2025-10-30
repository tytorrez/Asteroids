import pygame
from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0
        self.model = self.triangle()

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, 
                            pygame.Color("white"),
                            self.triangle(), 2)
        
    def rotate(self):
        pygame.transform.rotate(self.model, self.rotation)

    def update(self, dt):

        mouse_pos = pygame.mouse.get_pos()
        direction = pygame.math.Vector2(mouse_pos) - self.position

        if direction.length_squared() > 0:
            self.rotation = -direction.angle_to(pygame.math.Vector2(0,1))

        keys = pygame.key.get_pressed()

        if self.shot_timer > 0:
            self.shot_timer -= dt

        if keys[pygame.K_a]:
            self.strafe(dt*-1)
        if keys[pygame.K_d]:
            self.strafe(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt*-1)
        if pygame.mouse.get_pressed()[0]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1)
        self.position += forward * PLAYER_SPEED * -dt
    
    def strafe(self, dt):
        right = pygame.Vector2(1,0)
        self.position += right * PLAYER_SPEED * dt

    def shoot(self):

        if self.shot_timer <= 0:
            self.shot_timer = PLAYER_SHOOT_COOLDOWN
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            direction = pygame.Vector2(0, 1).rotate(self.rotation)
            shot.velocity = direction * PLAYER_SHOT_SPEED

    def respawn(self, screen):

        width, height = screen.get_size()
        self.position = pygame.math.Vector2(width//2, height//2)



    

