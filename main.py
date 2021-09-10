"""
this is the main entry of the game
"""
import pygame 
import time
import threading
from math import isclose
from random import randrange

def main():
    """main function
    """

    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    pygame.init()
    # screen
    screen = pygame.display.set_mode((240,180))
    screen.fill(WHITE)
    # spaceship
    spaceship = { 
        "rect" : pygame.Rect(100,100,10,10),
        "color" : RED,
        "is_displayed" : True
    }
    # missile rectangle
    missile =  { 
        "rect" : pygame.Rect(50,50,5,5),
        "color" : RED,
        "is_displayed" : False
    }
    
    # extraterrestrial monsters
    et_monster = { 
        "rect" : pygame.Rect(5, 100, 10, 10),
        "color" : BLACK,
        "is_displayed" : False
    }
    
    # map arrow keys to motion vector
    arrow_dir = {
        pygame.K_LEFT : (-5,0),
        pygame.K_RIGHT : (5,0),
        pygame.K_UP : (0,-5),
        pygame.K_DOWN : (0,5),
    }

    # missile motion vector
    missile_vector = (-5, 0)

    def redraw():
        """redraw objects
        """
        screen.fill(WHITE)
        for object in [spaceship, et_monster, missile]:
            if object["is_displayed"]: 
                pygame.draw.rect(screen, object["color"], object["rect"])
        pygame.display.flip()
    
    def move_space_ship(key_pressed):
        """move the space ship

        Args:
            key_pressed (integer): arrow key pressed
        """
        if key_pressed in arrow_dir:
            v = arrow_dir[key_pressed]
            spaceship["rect"].move_ip(v)
            redraw()
        
    def shoot(key_pressed):
        """shoot a missile 

        Args:
            key_pressed (integer): arrow key pressed
        """
        if key_pressed == pygame.K_SPACE:
            missile["rect"].update(spaceship["rect"].left -5, spaceship["rect"].top+2, 5, 5)
            missile["is_displayed"] = True
            redraw()
            while missile["rect"].x > 0:
                missile["rect"].move_ip(missile_vector) 
                redraw()
                time.sleep(0.01)
                if isclose(missile["rect"].x, et_monster["rect"].x, abs_tol=5) and isclose(missile["rect"].y, et_monster["rect"].y, abs_tol=5):
                    et_monster["is_displayed"] = False
            missile["is_displayed"] = False
            redraw()

    running = True

    def pop_monsters():
        """pop monsters at random place
        """
        while running:
            if not(et_monster["is_displayed"]):
                et_monster["rect"].update(5, randrange(0, 180, 5), 10, 10)
                et_monster["is_displayed"] = True
                redraw()
            time.sleep(1)

    t1 = threading.Thread(target=pop_monsters)
    t1.daemon = True
    t1.start()
    
    redraw()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                move_space_ship(event.key)
                shoot(event.key)
        # pop_monsters()
    t1.join()

if __name__ == "__main__":
    main()
