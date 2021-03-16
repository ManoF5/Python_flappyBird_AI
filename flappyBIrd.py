import pygame
import os
import random

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800

IMAGE_PIPE = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
IMAGE_FLOOR = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
IMAGE_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))
IMAGES_BIRD = [
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))
]

pygame.font.init()
SCORE = pygame.font.SysFont("arial", 50) 


class Bird:
    IMGS = IMAGES_BIRD
    # rotation animation
    ROTATION_MAX = 25
    ROTATION_SPEED = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = 0
        self.height = self.y
        self.time = 0
        self.image_count = 0
        self.image = IMGS[0]

    def pular(self):
        self.speed = -10.5
        self.time = 0
        self.height = self.y

    def move(self):
    # calculate the displacement
        self.time += 1
        displacement = 1.5 * (self.time**2) + self.speed * self.time

    # restrict the displacement
        if displacement > 16:
            displacement = 16
        elif displacement < 0:
            displacement -= 2

        self.y += displacement

    # bird's angle
        if displacement < 0 or self.y < (self.height + 50):
            if self.angle < self.ROTATION_MAX:
                self.angle = self.ROTATION_MAX
        else:
            if self.angle > -90:
                self.angle -= self.ROTATION_SPEED
    
    # PROJECT CHECKPOINT


class Pipe:
    pass


class Floor:
    pass
