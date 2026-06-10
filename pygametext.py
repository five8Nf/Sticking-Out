import pygame
from random import randint
pygame.init()

WINDOW_SIZE = (400, 400)
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()

class Enemy:
    def __init__(self, img, hp):
        self.x = randint(100, 300)
        self.y = randint(100, 300)
        self.hp = hp
        self.img = pygame.image.load(img).convert_alpha()
        self.img = pygame.transform.scale(self.img, (100, 100))
    
    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))

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

enemies = []
enemy_num = 0
enemy_speed = 4

def spawn_enemy(num):
    global enemy_num
    for _ in range(num):
        enemies.append(Enemy("Enemy.png", 10))
        enemy_num += 1

player = Player("Sword.png", 100)
spawn_enemy(5)

running = True
state = "playing"
while running:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if state == "menu":
    # show menu screen
        screen.fill((30, 30, 80))

    elif state == "playing":
        screen.fill((30, 80, 30))
        keys = pygame.key.get_pressed()
        player.movement(keys)
        player.draw(screen)
        spawn_timer = 2
        spawn_timer -= dt
        if spawn_timer <= 0:
            spawn_enemy(randint(1, 5))
            spawn_timer = 2
        for enemy in enemies:
            dx = player.x - enemy.x
            dy = player.y - enemy.y

            if dx > 0:
                enemy.x += enemy_speed
            if dx < 0:
                enemy.x -= enemy_speed
            if dy > 0:
                enemy.y += enemy_speed
            if dy < 0:
                enemy.y -= enemy_speed
            player_rect = pygame.Rect(player.x, player.y, 50, 50)
            enemy_rect = pygame.Rect(enemy.x, enemy.y, 50, 50)
            if player_rect.colliderect(enemy_rect):
                player.hp -= 1
                enemy.hp -= 1
                print(player.hp)
                if player.hp < 1:
                    state = "game over"
                if enemy.hp < 1:
                    enemies.remove(enemy)
            enemy.draw(screen)
    elif state == "game over":
    # show game over screen
        screen.fill((80, 30, 30))
    pygame.display.update()
pygame.quit()