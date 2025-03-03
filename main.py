import pygame
import sys
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    # Initilizing the game
    pygame.init()
    print("Starting Asteroids!")
    # Screen Parameters
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    game_clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (drawable, updatable)
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    
    shots = pygame.sprite.Group()
    Shot.containers = (shots, drawable, updatable)
    
    
    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
           
        
        screen.fill("black")
        
        updatable.update(dt)
        
        for asteroid in asteroids:
            if player.collision_detection(asteroid) == True:
                sys.exit("Game over!")
                
        for item in drawable:
            item.draw(screen)
        
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000
    
    
    
if __name__ == "__main__":
    main()