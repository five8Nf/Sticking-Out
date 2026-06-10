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
def movement(keys):
    player.movement(keys)
    for enemy in enemies:
        if keys[pygame.K_w]:
            enemy.y += speed
        if keys[pygame.K_a]:
            enemy.x += speed
        if keys[pygame.K_s]:
            enemy.y -= speed
        if keys[pygame.K_d]:
            enemy.x -= speed
    for tile in tiles:
        if keys[pygame.K_w]:
            tile.y += speed
        if keys[pygame.K_a]:
            tile.x += speed
        if keys[pygame.K_s]:
            tile.y -= speed
        if keys[pygame.K_d]:
            tile.x -= speed

tiles = []
walls = {"Top" : [], 
         "Bottom" : [], 
         "Left" : [], 
         "Right": []
         }

def level_rect(amt_x, amt_y, x, y):
    for _ in range(amt_x):
        tiles.append(Tile("Assets/Grass.png", x, y))
        x += 100


running = True
state = "playing"
level_rect(100, 1, 100, 100)
while running:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if state == "playing":
        screen.fill((30, 80, 30))
        keys = pygame.key.get_pressed()
        movement(keys)
        player.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)
        for tile in tiles:
            tile.draw(screen)
    pygame.display.update()
pygame.quit()