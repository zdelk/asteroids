import pygame
from constants import *

def main():
    # Initilizing the game
    pygame.init()
    print("Starting Asteroids!")
    # Screen Parameters
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    game_clock = pygame.time.Clock()
    
    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, (0,0,0))
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000
    
    
    
if __name__ == "__main__":
    main()