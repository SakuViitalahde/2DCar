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
        if keystate[273]: ## Up
            car.accelerate()
            print("acc")
        if keystate[274]: ## Down

            print("brake")
            car.brake()
        if keystate[276]: ## Left
            car.rotate_left()
        if keystate[275]: ## Right
            car.rotate_right()

        clock.tick(60)
        print(car.speed)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()