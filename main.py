import sys
import pygame
from car import Car
from track import Track

BLACK = (0, 0, 0)


def main():
    pygame.init()
    size = [1000, 1000]
    screen = pygame.display.set_mode(size)
    background = pygame.image.load('tausta.png').convert()

    clock = pygame.time.Clock()
    done = False

    car = Car(screen)
    track = Track(screen)
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
        screen.fill(BLACK)
        screen.blit(background, [0, 0])
        track.draw_track()
        car.refresh()
        pygame.display.flip()
        track.check_collision(car.wheel_collision)
        
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()