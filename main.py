import sys
import pygame
from car import Car

BLACK = (0, 0, 0)


def main():
    pygame.init()
    size = [1000, 1000]
    screen = pygame.display.set_mode(size)

    clock = pygame.time.Clock()
    done = False

    car = Car(screen)
    car.refresh()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        keystate = pygame.key.get_pressed()
        if keystate[105]: ## Up
            car.accelerate()
        if keystate[107]: ## Down
            car.brake()
        if keystate[108]: ## Left
            car.rotate_left()
        if keystate[106]: ## Right
            car.rotate_right()

        clock.tick(60)
        car.refresh()
        
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()