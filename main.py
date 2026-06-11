import pygame
from Entities import *

pygame.init()
pygame.display.set_caption("Sticking Out")
WINDOW_SIZE = (1280, 720)
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()

player = Player("Assets/PlayerL1.png", 100)

speed = 5
gravity = 0.5
tiles = []
walls = {"nofall": [], "Bottom": [], "Left": [], "Right": []}

def level_rect(amt_x, amt_y, x, y):
    start_x = x - (amt_x - 1) * 100
    platform_rect = pygame.Rect(start_x, y, amt_x * 100, 1)
    walls["nofall"].append(platform_rect)
    
    for _ in range(amt_x):
        tiles.append(Tile("Assets/Tile_down.png", x, y))
        x -= 100
        
    spawn_enemy(5, "Assets/BottleL1.png")
    
    for enemy in enemies:
        if platform_rect.left <= enemy.x <= platform_rect.right:
            enemy.y = platform_rect.top - 100
            enemy.speed_y = 0
            enemy.ground_collision = True

def update_physics():
    if not player.ground_collision:
        player.speed_y += gravity

    if player.speed_y != 0:
        for tile in tiles: tile.y -= player.speed_y
        for wall_list in walls.values():
            for rect in wall_list: rect.y -= player.speed_y
        for enemy in enemies:
            if not enemy.ground_collision:
                enemy.y -= player.speed_y

    player_hitbox = pygame.Rect(player.x, player.y, 100, 100)
    player_sensor = pygame.Rect(player.x, player.y + 100, 100, 2)
    player.ground_collision = False

    if player.speed_y >= 0:
        for base in walls["nofall"]:
            if player_sensor.colliderect(base) or player_hitbox.colliderect(base):
                correction = player_hitbox.bottom - base.top
                for tile in tiles: tile.y += correction
                for wall_list in walls.values():
                    for rect in wall_list: rect.y += correction
                for enemy in enemies:
                    if not enemy.ground_collision:
                        enemy.y += correction
                player.speed_y = 0
                player.ground_collision = True
                break


    for i, base in enumerate(walls["nofall"]):
        base.y = int(tiles[i * (len(tiles) // len(walls["nofall"]))].y)

    for enemy in enemies:
        on_ground = False
        enemy_bottom = enemy.y + 100

        for base in walls["nofall"]:
            if enemy.x + 100 > base.left and enemy.x < base.right:
                if enemy_bottom >= base.top:
                    enemy.y = base.top - 100
                    enemy.speed_y = 0
                    enemy.ground_collision = True
                    on_ground = True
                    break

        if not on_ground:
            enemy.ground_collision = False
            enemy.speed_y += gravity
            enemy.y += enemy.speed_y

def movement(keys):
    player.movement(keys)
    
    if keys[pygame.K_w] and player.ground_collision:
        player.speed_y = -12
        player.ground_collision = False

    if keys[pygame.K_a]:
        for enemy in enemies: 
            enemy.x += speed
        for tile in tiles: 
            tile.x += speed
        for wall_list in walls.values():
            for rect in wall_list: rect.x += speed
            
    if keys[pygame.K_d]:
        for enemy in enemies: enemy.x -= speed
        for tile in tiles: tile.x -= speed
        for wall_list in walls.values():
            for rect in wall_list: rect.x -= speed

running = True
state = "playing"

level_rect(100, 1, 320, 450)

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    if state == "playing":
        screen.fill((0, 0, 0))
        
        keys = pygame.key.get_pressed()
        movement(keys)
        update_physics()
        
        player.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)
        for tile in tiles:
            tile.draw(screen)
            
        pygame.display.update()

pygame.quit()