import pygame
from random import randint

enemies = []
enemy_num = 0
enemy_speed = 4

class Player:
    def __init__(self, img, hp):
        self.x = 100
        self.y = 100
        self.speed = 5
        self.hp = hp
        self.img = pygame.image.load(img).convert_alpha()
        self.img = pygame.transform.scale(self.img, (100, 100))
    
    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))
    
    def movement(self, keys):
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_d]:
            self.x += self.speed

class Enemy:
    def __init__(self, img, hp):
        self.x = randint(100, 300)
        self.y = randint(100, 300)
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