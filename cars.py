import sys
import pygame

BLACK = (0, 0, 0)


def main():
    pygame.init()
    size = [1000, 1000]
    screen = pygame.display.set_mode(size)
    position = (200, 200)

    clock = pygame.time.Clock()
    car_image = pygame.image.load('car.png').convert()

    angle = 0
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        image = pygame.transform.rotate(car_image, angle)
        image_rect = image.get_rect(center=position)
        screen.fill(BLACK)
        screen.blit(image, image_rect)
        pygame.display.flip()
        clock.tick(60)
        angle += -1

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()