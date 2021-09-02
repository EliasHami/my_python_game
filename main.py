"""
this is the main entry of the game
"""
import pygame 

def main():
    """main function
    """

    pygame.init()
    screen = pygame.display.set_mode((240,180))
    rect =  pygame.Rect(100,100,10,10)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    # map arrow keys to motion vector
    dir = {
        pygame.K_LEFT : (-5,0),
        pygame.K_RIGHT : (5,0),
        pygame.K_UP : (0,-5),
        pygame.K_DOWN : (0,5),
    }
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key in dir:
                    v = dir[event.key]
                    rect.move_ip(v)
                    print(v)
        screen.fill(WHITE)
        pygame.draw.rect(screen, RED , rect)
        pygame.display.flip()
if __name__ == "__main__":
    main()
