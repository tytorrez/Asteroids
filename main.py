import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
from weaponspawn import *
import sys

def main():
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background = pygame.image.load("background.png")
    pygame.display.set_caption("Ultra Asteroids")
    font = pygame.font.SysFont(None, 36)

    clock = pygame.time.Clock()
    dt = 0

    drawables = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()   
    shots = pygame.sprite.Group()
    weapons = pygame.sprite.Group()

    Player.containers = (drawables, updatables)
    Asteroid.containers = (asteroids, drawables, updatables)
    AsteroidField.containers = updatables
    Shot.containers = (shots, drawables, updatables)
    WeaponSpawn.containers = (drawables, weapons)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    score = 0
    current_lives = PLAYER_LIVES

    last_hit = 0
    last_update = pygame.time.get_ticks()

    pickup_list = []
    show_list = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.blit(background, (0,0))
        current_time = pygame.time.get_ticks()

        if random.random() < 0.005:
            position = [random.randint(50, SCREEN_WIDTH-50), random.randint(50, SCREEN_HEIGHT-50)]
            type = random.choice(["Shotgun", "Boulder", "Force Field", "SMG", "Rifle"])
                                 
            if type not in show_list:
                show_list.append(type)
                WeaponSpawn(position[0], position[1], type)

        for drawable in drawables:
            drawable.draw(screen)

        updatables.update(dt)

        for asteroid in asteroids:
            if asteroid.collide(player) and current_time - last_hit >= PLAYER_INVULNERABILITY:
                if current_lives == 0:
                    sys.exit("Game over!")
                else:
                    current_lives -= 1
                    last_hit = pygame.time.get_ticks()
                    player.respawn(screen)
                    
            for bullet in shots:
                if asteroid.collide(bullet):
                    bullet.kill()
                    asteroid.split()
                    score += 1000

        for weapon in weapons:
            if weapon.collide(player):
                weapon.create(player)
                weapon.kill()
                pickup_list.append(weapon.type)

        if current_time - last_update >= 1000:
            last_update = current_time
            score += 100

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    player.previous_weapon()
                if event.key == pygame.K_e:
                    player.next_weapon()

        lives_text = font.render(f"Lives: {current_lives}", True, (255,255,255))
        score_text = font.render(f"Score: {score}", True, (255,255,255))
        weapon_list_text = font.render(f"Weapons: {player.get_weapon_list()}", True, (255,255,255))
        current_weapon_text = font.render(f"Current Weapon: {player.get_current_weapon()}", True, (255,255,255))
        screen.blit(current_weapon_text, (20,110))
        screen.blit(weapon_list_text, (20,80))
        screen.blit(score_text, (20,20))
        screen.blit(lives_text, (20,50))

        dt = clock.tick(60)/1000
        pygame.display.flip()


if __name__ == "__main__":
    main()
