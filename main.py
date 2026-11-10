import pygame
from logger import log_state, log_event
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from AsteroidField import AsteroidField
from circleshape import CircleShape
import sys
from shot import Shot


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, drawable, updatable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for obj in asteroids:
            if CircleShape.collides_with(player, obj) is True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        screen.fill("black")
        for i in drawable:
            i.draw(screen)
        for obj in asteroids:
            for shot in shots:
                if CircleShape.collides_with(shot, obj) is True:
                    log_event("asteroid_shot")
                    obj.kill()
                    shot.kill()
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
