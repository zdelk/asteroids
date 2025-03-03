import pygame
from constants import *
from player import Player

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
    

    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
           
        
        screen.fill("black")
        updatable.update(dt)
        
        for item in drawable:
            item.draw(screen)
        
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000
    
    
    
if __name__ == "__main__":
    main()