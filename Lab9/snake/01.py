import pygame
import random
from color_palette import *

pygame.init()

# Constants for game dimensions
WIDTH = 600
HEIGHT = 600
CELL = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Font for displaying score, level, and food weight
font = pygame.font.Font(None, 36)
food_font = pygame.font.Font(None, 24)

# Function to draw the grid
def draw_grid():
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

# Point class to store x and y positions
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0
        self.grow = False

    def move(self):
        if self.grow:
            self.body.append(Point(self.body[-1].x, self.body[-1].y))
            self.grow = False

        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        head = self.body[0]
        return head.x == food.pos.x and head.y == food.pos.y

    def check_wall_collision(self):
        head = self.body[0]
        return head.x < 0 or head.x >= WIDTH // CELL or head.y < 0 or head.y >= HEIGHT // CELL

    def check_self_collision(self):
        head = self.body[0]
        return any(segment.x == head.x and segment.y == head.y for segment in self.body[1:])

class Food:
    def __init__(self):
        self.pos = Point(9, 9)
        self.weight = random.randint(1, 3)  # Random weight for food
        self.timer = 50 # Timer before food disappears

    def generate_food(self, snake):
        while True:
            x = random.randint(0, WIDTH // CELL - 1)
            y = random.randint(0, HEIGHT // CELL - 1)
            if not any(segment.x == x and segment.y == y for segment in snake.body):
                self.pos = Point(x, y)
                self.weight = random.randint(1, 3)  # Random weight for new food
                self.timer = 100  # Reset timer
                break

    def update_timer(self):
        self.timer -= 1
        return self.timer <= 0  # Returns True if the timer runs out

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))
        weight_text = food_font.render(str(self.weight), True, colorBLACK)
        screen.blit(weight_text, (self.pos.x * CELL + CELL // 3, self.pos.y * CELL + CELL // 4))

FPS = 5
clock = pygame.time.Clock()
food = Food()
snake = Snake()
score = 0
level = 1
running = True

while running:
    screen.fill(colorBLACK)
    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP and snake.dy == 0:
                snake.dx = 0
                snake.dy = -1

    snake.move()
    
    if snake.check_collision(food):
        score += food.weight  # Increase score by food weight
        food.generate_food(snake)
        snake.grow = True

        if score % 4 == 0:
            level += 1
            FPS += 2  # Increase game speed

    if food.update_timer():  # Check if food disappears
        food.generate_food(snake)

    if snake.check_wall_collision() or snake.check_self_collision():
        print("Game Over!")
        running = False

    snake.draw()
    food.draw()

    score_text = font.render(f"Score: {score}", True, colorWHITE)
    level_text = font.render(f"Level: {level}", True, colorWHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()