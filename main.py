import pygame
from random import randint

from creatures import *

pygame.init()

pygame.display.set_caption("Sticking Out")
WINDOW_SIZE = (1280, 720)
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()

player = Player("Assets/PlayerL1.png", 100)
spawn_enemy(5, "Assets/BottleL1.png")

speed = 5
gravity = 0.5

def jump(thing):
    thing.speed_y += gravity
    thing.y += thing.speed_y

def movement(keys):
    player.movement(keys)
    for enemy in enemies:
        if keys[pygame.K_w] and enemy.ground_collision:
            enemy.speed_y = -enemy.jump_height
        if keys[pygame.K_a]:
            enemy.x += speed
        if keys[pygame.K_d]:
            enemy.x -= speed
    for tile in tiles:
        if keys[pygame.K_w] and tile.ground_collision:
            tile.speed_y = 0 - tile.jump_height
        if keys[pygame.K_a]:
            tile.x += speed
        if keys[pygame.K_d]:
            tile.x -= speed

tiles = []
walls = {"Top" : [], 
         "Bottom" : [], 
         "Left" : [], 
         "Right": []
         }

def level_rect(amt_x, amt_y, x, y):
    walls["Top"].append(pygame.Rect(x, y, int(100*amt_x), 1))
    for _ in range(amt_x):
        tiles.append(Tile("Assets/Tile_down.png", x, y))
        x -= 100


running = True
state = "playing"
level_rect(100, 1, 320, 450)
while running:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if state == "playing":
        screen.fill((0, 0, 0))
        keys = pygame.key.get_pressed()
        movement(keys)
        player.draw(screen)
        for enemy in enemies:
            hitbox = pygame.Rect(enemy.x, enemy.y, 50, 100)
            for base in walls["Top"]:
                enemy.ground_collision = hitbox.colliderect(base)
            jump(enemy)
            enemy.draw(screen)
        for tile in tiles:
            jump(tile)
            tile.draw(screen)
        # for _, value in walls.items():
            
    pygame.display.update()
pygame.quit()