import pygame
from random import randint
from math import floor

enemies = []
enemy_num = 0
enemy_speed = 4

class Tile():
    def __init__(self, img, x, y):
        self.x = x
        self.y = y
        self.speed_y
        self.ground_collision = False
        self.img = pygame.image.load(img).convert_alpha()
        self.img = pygame.transform.scale(self.img, (100, 100))
    
    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))

class Player:
    def __init__(self, img, hp):
        self.x = 320
        self.y = 350
        self.hp = hp
        self.frame = 1
        self.img = pygame.image.load(img).convert_alpha()
        self.img = pygame.transform.scale(self.img, (100, 100))
    
    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))
    
    def movement(self, keys):
        if not (keys[pygame.K_a] and keys[pygame.K_d]):
            if keys[pygame.K_a]:
                self.img = pygame.image.load(f"Assets/PlayerL{floor(self.frame)%4}.png").convert_alpha()
                self.img = pygame.transform.scale(self.img, (100, 100))
                self.frame += 0.5
            if keys[pygame.K_d]:
                self.img = pygame.image.load(f"Assets/PlayerR{floor(self.frame)%4}.png").convert_alpha()
                self.img = pygame.transform.scale(self.img, (100, 100))
                self.frame += 0.5
        

class Enemy:
    def __init__(self, img, hp):
        self.x = randint(0, 640)
        self.y = randint(0, 400)
        self.speed_y = 0
        self.ground_collision = False
        self.hp = hp
        self.img = pygame.image.load(img).convert_alpha()
        self.img = pygame.transform.scale(self.img, (100, 100))
    
    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))

def spawn_enemy(num, img):
    global enemy_num
    for _ in range(num):
        enemies.append(Enemy(img, 10))
        enemy_num += 1