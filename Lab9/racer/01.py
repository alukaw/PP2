import pygame
import random
import time

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load('resources/AnimatedStreet.png')

running = True
score = 0

clock = pygame.time.Clock()
FPS = 60

player_img = pygame.image.load('resources/Player.png')
enemy_img = pygame.image.load('resources/Enemy.png')
coin_img = pygame.image.load('resources/coin.png')

pygame.mixer.music.load('resources/background.wav')
crash_sound = pygame.mixer.Sound('resources/crash.wav')

font = pygame.font.SysFont("Verdana", 60)
score_font = pygame.font.SysFont("Verdana", 20)
coin_font = pygame.font.SysFont("Verdana", 20, bold=True)
game_over = font.render("Game Over", True, "black")

pygame.mixer.music.play(-1)

PLAYER_SPEED = 5
ENEMY_SPEED = 10
COIN_SPEED = 7
COIN_THRESHOLD = 5  # Increase speed every 5 coins

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 50))
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-PLAYER_SPEED, 0)
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.move_ip(PLAYER_SPEED, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.generate_random_rect()
    
    def move(self):
        global ENEMY_SPEED
        self.rect.move_ip(0, ENEMY_SPEED)
        if self.rect.top > HEIGHT:
            self.generate_random_rect()
    
    def generate_random_rect(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.w)
        self.rect.y = random.randint(-100, -40)

class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.generate_random_coin()

    def move(self):
        self.rect.move_ip(0, COIN_SPEED)
        if self.rect.top > HEIGHT:
            self.generate_random_coin()

    def generate_random_coin(self):
        self.weight = random.randint(1, 5)  # Random weight between 1 and 5
        size = 20 + (self.weight * 6)  # Ensure size matches weight
        self.image = pygame.transform.scale(coin_img, (size, size))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.w)
        self.rect.y = random.randint(-100, -40)
        
        # Draw weight number on coin
        coin_surface = self.image.copy()
        text = coin_font.render(str(self.weight), True, "black")
        text_rect = text.get_rect(center=(size // 2, size // 2))
        coin_surface.blit(text, text_rect)
        self.image = coin_surface

player = Player()
enemy = Enemy()
coin = Coins()

all_sprites = pygame.sprite.Group(player, enemy, coin)
enemy_sprites = pygame.sprite.Group(enemy)
coin_sprites = pygame.sprite.Group(coin)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(background, (0, 0))

    player.move()
    enemy.move()
    coin.move()

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
    
    if pygame.sprite.spritecollideany(player, enemy_sprites):
        crash_sound.play()
        time.sleep(1)
        screen.fill("red")
        screen.blit(game_over, game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
        pygame.display.flip()
        time.sleep(2)
        running = False
    
    if pygame.sprite.spritecollideany(player, coin_sprites):
        score += coin.weight  # Increase score by coin weight
        coin.generate_random_coin()
        
        if score % COIN_THRESHOLD == 0:
            ENEMY_SPEED += 1  # Increase enemy speed every threshold
    
    score_text = score_font.render(f"Coins: {score}", True, "white")
    screen.blit(score_text, (WIDTH - 100, 10))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
