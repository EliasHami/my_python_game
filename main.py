"""
this is the main entry of the game
"""
import pygame 
import time

def main():
    """main function
    """

    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    pygame.init()
    # screen
    screen = pygame.display.set_mode((240,180))
    screen.fill(WHITE)
    # spaceship rectangle
    spaceship =  pygame.Rect(100,100,10,10)
    pygame.draw.rect(screen, RED, spaceship)
    # missile rectangle
    missile =  pygame.Rect(50,50,5,5)
    
    pygame.display.flip()

    # map arrow keys to motion vector
    arrow_dir = {
        pygame.K_LEFT : (-5,0),
        pygame.K_RIGHT : (5,0),
        pygame.K_UP : (0,-5),
        pygame.K_DOWN : (0,5),
    }

    # missile motion vector
    missile_vector = (-5, 0)

    def move_space_ship(key_pressed):
        """move the space ship

        Args:
            key_pressed (integer): arrow key pressed
        """
        if key_pressed in arrow_dir:
            v = arrow_dir[key_pressed]
            spaceship.move_ip(v)
            screen.fill(WHITE)
            pygame.draw.rect(screen, RED, spaceship)
            pygame.display.flip()
        
    def shoot(key_pressed):
        """shoot a missile 

        Args:
            key_pressed (integer): arrow key pressed
        """
        if key_pressed == pygame.K_SPACE:
            screen.fill(WHITE)
            pygame.draw.rect(screen, RED, spaceship)
            missile.update(spaceship.left -5, spaceship.top+2, 5, 5)
            pygame.draw.rect(screen, RED, missile)
            pygame.display.flip()
            while missile.x > 0:
                screen.fill(WHITE)
                pygame.draw.rect(screen, RED, spaceship)
                missile.move_ip(missile_vector)
                pygame.draw.rect(screen, RED, missile)
                pygame.display.flip()
                time.sleep(0.1)
        screen.fill(WHITE)
        pygame.draw.rect(screen, RED, spaceship)   
        pygame.display.flip() 

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                move_space_ship(event.key)
                shoot(event.key)
        
if __name__ == "__main__":
    main()
