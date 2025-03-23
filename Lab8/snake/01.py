import pygame
import random
from color_palette import *

pygame.init()

# get sizes 
WIDTH = 600
HEIGHT = 600
CELL = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# font for displaying score and level
font = pygame.font.Font(None, 36)

# function to draw the grid
def draw_grid():
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

# point class to store x and y positions
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0
        self.grow = False  # checks whether the snake should grow on eating food

    def move(self): #moves a snake
        if self.grow:
            self.body.append(Point(self.body[-1].x, self.body[-1].y))
            self.grow = False

        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self): # draws a snake
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food): # whether snake ate the food or not
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            print("Got food!")
            self.grow = True
            food.generate_food(self)  # generate a new food location

    def check_wall_collision(self): # checks collision with wall
        head = self.body[0]
        return head.x < 0 or head.x >= WIDTH // CELL or head.y < 0 or head.y >= HEIGHT // CELL

    def check_self_collision(self): # checks collision with itself
        head = self.body[0]
        return any(segment.x == head.x and segment.y == head.y for segment in self.body[1:])

class Food:
    def __init__(self):
        self.pos = Point(9, 9)

    def generate_food(self, snake):
        while True:
            x = random.randint(0, WIDTH // CELL - 1)
            y = random.randint(0, HEIGHT // CELL - 1)
            if not any(segment.x == x and segment.y == y for segment in snake.body):
                self.pos = Point(x, y)
                break

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))


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
    
    if snake.body[0].x == food.pos.x and snake.body[0].y == food.pos.y:
        score += 1
        food.generate_food(snake)
        snake.grow = True

        # increasing level og the game
        if score % 4 == 0:
            level += 1
            FPS += 2  # increasing gsme

    if snake.check_wall_collision() or snake.check_self_collision():
        print("Game Over!")
        running = False

    
    snake.draw()
    food.draw()

    # display score and level
    score_text = font.render(f"Score: {score}", True, colorWHITE)
    level_text = font.render(f"Level: {level}", True, colorWHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
