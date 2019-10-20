import sys
import pygame

BLACK = (0, 0, 0)
MAX_SPEED = 50

class Car:
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load('car.png').convert()
        self.position = (200, 200)
        self.speed = 0
        self.angle = 0

    def rotate_left(self):
        image = pygame.transform.rotate(self.image, self.angle)
        image_rect = image.get_rect(center=self.position)
        self.screen.fill(BLACK)
        self.screen.blit(image, image_rect)
        pygame.display.flip()
        self.angle += -1

    def rotate_right(self):
        image = pygame.transform.rotate(self.image, self.angle)
        image_rect = image.get_rect(center=self.position)
        self.screen.fill(BLACK)
        self.screen.blit(image, image_rect)
        pygame.display.flip()
        self.angle += 1

    def refresh(self):
        image = pygame.transform.rotate(self.image, self.angle)
        image_rect = image.get_rect(center=self.position)
        self.screen.fill(BLACK)
        self.screen.blit(image, image_rect)
        pygame.display.flip()

    def accelerate(self):
        if self.speed < MAX_SPEED:
            self.speed = self.speed + 1

    def brake(self):
        if self.speed > 0:
            self.speed = self.speed - 1