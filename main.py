import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
import sys

def main():
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    drawables = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()   
    shots = pygame.sprite.Group()

    Player.containers = (drawables, updatables)
    Asteroid.containers = (asteroids, drawables, updatables)
    AsteroidField.containers = updatables
    Shot.containers = (shots, drawables, updatables)
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(pygame.Color("black"))
        dt = clock.tick()/1000

        for drawable in drawables:
            drawable.draw(screen)

        updatables.update(dt)

        for asteroid in asteroids:
            if asteroid.collide(player):
                sys.exit("Game over!")
            for bullet in shots:
                if asteroid.collide(bullet):
                    pygame.sprite.Sprite.kill(bullet)
                    pygame.sprite.Sprite.kill(asteroid)


        
        clock.tick(60)
        pygame.display.flip()



if __name__ == "__main__":
    main()
