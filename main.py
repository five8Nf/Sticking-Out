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

running = True
state = "playing"
while running:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if state == "menu":
    # show menu screen
        screen.fill((135, 206, 235))

    elif state == "playing":
        screen.fill((30, 80, 30))
        keys = pygame.key.get_pressed()
        movement(keys)
        player.draw(screen)
        # spawn_timer = 2
        # spawn_timer -= dt
        # if spawn_timer <= 0:
        #     spawn_enemy(randint(1, 5), "Assets/BottleL1.png")
        #     spawn_timer = 2
        for enemy in enemies:
        #     # dx = player.x - enemy.x
        #     # dy = player.y - enemy.y

        #     # if dx > 0:
        #     #     enemy.x += enemy_speed
        #     # if dx < 0:
        #     #     enemy.x -= enemy_speed
        #     # if dy > 0:
        #     #     enemy.y += enemy_speed
        #     # if dy < 0:
        #     #     enemy.y -= enemy_speed
        #     player_rect = pygame.Rect(player.x, player.y, 50, 50)
        #     enemy_rect = pygame.Rect(enemy.x, enemy.y, 50, 50)
        #     if player_rect.colliderect(enemy_rect):
        #         player.hp -= 1
        #         enemy.hp -= 1
        #         print(player.hp)
        #         if player.hp < 1:
        #             state = "game over"
        #         if enemy.hp < 1:
        #             enemies.remove(enemy)
            enemy.draw(screen)
    elif state == "game over":
    # show game over screen
        screen.fill((80, 30, 30))
    pygame.display.update()
pygame.quit()