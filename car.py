import sys
import pygame
import pygame.math
import math

BLACK = (0, 0, 0)
MAX_SPEED = 250
DELTA = 1/60

class Car:
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load('car.png').convert()
        self.speed = 0
        self.wheel_base = 30
        self.engine_power = 2700
        self.acceleration = 0
        self.velocity = pygame.math.Vector2(0,0)
        self.movement_vector = pygame.math.Vector2(0,0)
        self.steering_angle = 0
        self.back_wheel =  pygame.math.Vector2(100,100)
        self.front_wheel = pygame.math.Vector2(130,100)
        self.position = (self.back_wheel + self.front_wheel) / 2 # X vaaka y pysty
        self.angle = math.atan2(self.front_wheel[1] - self.back_wheel[1], self.front_wheel[0] - self.back_wheel[0])
        self.acceleration_change = 0
        self.slip_speed = 500
        self.traction_fast = 0.3
        self.traction_mid = 0.5
        self.traction_slow = 0.8

    def rotate_left(self):
        if self.steering_angle < 0:
             self.steering_angle = 0    
        if self.steering_angle < 90:
            self.steering_angle += 9
        print(self.steering_angle)

    def rotate_right(self):
        if self.steering_angle > 0:
             self.steering_angle = 0    
        if self.steering_angle > -90:
            self.steering_angle -= 9
        print(self.steering_angle)

    def refresh(self):
        image = pygame.transform.rotate(self.image, 360 - math.degrees(self.angle))
        image_rect = image.get_rect(center=self.position)

        self.screen.fill(BLACK)
        self.screen.blit(image, image_rect)

        self.calculate_movement()

        pygame.draw.circle(self.screen, (255,0,0), self.back_wheel, 3)
        pygame.draw.circle(self.screen, (255,0,0), self.front_wheel, 3)

        pygame.display.flip()
        self.steering_angle = self.steering_angle * 0.9

    def accelerate(self):
        if self.acceleration_change < 2:
            self.acceleration_change += 0.005

    def brake(self):
        if self.acceleration_change > -0.5:
            self.acceleration_change += -0.02

    def calculate_movement(self):
        self.acceleration = (self.movement_vector.length() + self.acceleration_change) * self.engine_power
        self.speed = self.acceleration * DELTA
        print(self.speed)
        self.angle = math.atan2(self.front_wheel[1] - self.back_wheel[1], self.front_wheel[0] - self.back_wheel[0])
        original_back_wheel = pygame.math.Vector2(self.back_wheel)
        
        front_wheel_no_turn = self.front_wheel + self.speed * DELTA * pygame.math.Vector2(math.cos(self.angle) , math.sin(self.angle))
        back_wheel_no_turn = self.back_wheel + self.speed * DELTA * pygame.math.Vector2(math.cos(self.angle) , math.sin(self.angle))

        self.front_wheel += self.speed * DELTA * pygame.math.Vector2(math.cos(self.angle + math.radians(self.steering_angle)) , math.sin(self.angle + math.radians(self.steering_angle)))
        self.back_wheel += self.speed * DELTA * pygame.math.Vector2(math.cos(self.angle) , math.sin(self.angle))

        back_wheel_movement_vector = (original_back_wheel - self.back_wheel) / 10
 
        if self.speed > 0:
            while self.back_wheel.distance_to(self.front_wheel) < self.wheel_base:
                self.back_wheel += back_wheel_movement_vector
        elif self.speed < 0:
            while self.back_wheel.distance_to(self.front_wheel) > self.wheel_base:
                self.back_wheel += back_wheel_movement_vector
        
        traction = 0.5 - self.speed / 1000 
            
        #print(front_wheel_no_turn + ((front_wheel_no_turn - self.front_wheel) * traction))

        self.front_wheel = front_wheel_no_turn - ((front_wheel_no_turn - self.front_wheel) * traction)
        #self.back_wheel = back_wheel_no_turn + ((back_wheel_no_turn - self.back_wheel) * traction) 
        
        self.movement_vector = (self.position - ((self.back_wheel + self.front_wheel) / 2))
        self.position = (self.back_wheel + self.front_wheel) / 2