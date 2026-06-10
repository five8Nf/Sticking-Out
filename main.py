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

tiles = []

def level_rect(amt_x, amt_y, x, y):
    temp_var = Tile("Assets/Grass.png", x, y)
    for _ in range(amt_x):
        temp_var.draw(screen)
        tiles.append(temp_var)
        x += 100


running = True
state = "playing"
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
    pygame.display.update()
pygame.quit()