import pygame
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        pygame.Surface.fill(screen, (0,0,0))
        
        pygame.display.flip()
    
    
    
    
if __name__ == "__main__":
    main()