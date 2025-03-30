import pygame

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))
base_layer.fill((255, 255, 255))

# Colors
colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorGREEN = (0, 255, 0)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)

draw_color = colorRED
clock = pygame.time.Clock()

# Mouse and drawing settings
LMBpressed = False
THICKNESS = 5
prevX = prevY = currX = currY = 0

draw_mode = "rectangle"  # Modes: rectangle, circle, square, right_triangle, equilateral_triangle, rhombus, eraser

# Functions to calculate shapes
def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def calculate_circle(x1, y1, x2, y2):
    radius = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 / 2)
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    return center_x, center_y, radius

def calculate_square(x1, y1, x2, y2):
    side = min(abs(x2 - x1), abs(y2 - y1))
    return pygame.Rect(x1, y1, side, side)

def calculate_right_triangle(x1, y1, x2, y2):
    return [(x1, y1), (x1, y2), (x2, y2)]

def calculate_equilateral_triangle(x1, y1, x2, y2):
    side = abs(x2 - x1)
    height = int((side * (3 ** 0.5)) / 2)
    return [(x1, y2), (x2, y2), ((x1 + x2) // 2, y2 - height)]

def calculate_rhombus(x1, y1, x2, y2):
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    return [(center_x, y1), (x2, center_y), (center_x, y2), (x1, center_y)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            prevX, prevY = event.pos
        
        if event.type == pygame.MOUSEMOTION and LMBpressed:
            currX, currY = event.pos
            screen.blit(base_layer, (0, 0))
            
            if draw_mode == "rectangle":
                pygame.draw.rect(screen, draw_color, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
            elif draw_mode == "circle":
                cx, cy, r = calculate_circle(prevX, prevY, currX, currY)
                pygame.draw.circle(screen, draw_color, (cx, cy), r, THICKNESS)
            elif draw_mode == "square":
                pygame.draw.rect(screen, draw_color, calculate_square(prevX, prevY, currX, currY), THICKNESS)
            elif draw_mode == "right_triangle":
                pygame.draw.polygon(screen, draw_color, calculate_right_triangle(prevX, prevY, currX, currY), THICKNESS)
            elif draw_mode == "equilateral_triangle":
                pygame.draw.polygon(screen, draw_color, calculate_equilateral_triangle(prevX, prevY, currX, currY), THICKNESS)
            elif draw_mode == "rhombus":
                pygame.draw.polygon(screen, draw_color, calculate_rhombus(prevX, prevY, currX, currY), THICKNESS)
            elif draw_mode == "eraser":
                pygame.draw.line(base_layer, colorWHITE, (prevX, prevY), (currX, currY), THICKNESS)
                prevX, prevY = currX, currY
        
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False
            currX, currY = event.pos
            
            if draw_mode == "rectangle":
                pygame.draw.rect(base_layer, draw_color, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
            elif draw_mode == "circle":
                cx, cy, r = calculate_circle(prevX, prevY, currX, currY)
                pygame.draw.circle(base_layer, draw_color, (cx, cy), r, THICKNESS)
            elif draw_mode == "square":
                pygame.draw.rect(base_layer, draw_color, calculate_square(prevX, prevY, currX, currY), THICKNESS)
            elif draw_mode == "right_triangle":
                pygame.draw.polygon(base_layer, draw_color, calculate_right_triangle(prevX, prevY, currX, currY), THICKNESS)
            elif draw_mode == "equilateral_triangle":
                pygame.draw.polygon(base_layer, draw_color, calculate_equilateral_triangle(prevX, prevY, currX, currY), THICKNESS)
            elif draw_mode == "rhombus":
                pygame.draw.polygon(base_layer, draw_color, calculate_rhombus(prevX, prevY, currX, currY), THICKNESS)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_EQUALS:
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                THICKNESS = max(1, THICKNESS - 1)
            if event.key == pygame.K_r:
                draw_color = colorRED
            if event.key == pygame.K_g:
                draw_color = colorGREEN
            if event.key == pygame.K_b:
                draw_color = colorBLUE
            if event.key == pygame.K_e:
                draw_mode = "eraser"
            if event.key == pygame.K_c:
                draw_mode = "circle"
            if event.key == pygame.K_s:
                draw_mode = "rectangle"
            if event.key == pygame.K_q:
                draw_mode = "square"
            if event.key == pygame.K_t:
                draw_mode = "right_triangle"
            if event.key == pygame.K_y:
                draw_mode = "equilateral_triangle"
            if event.key == pygame.K_h:
                draw_mode = "rhombus"
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
