import pygame

pygame.init()

# screen setup
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))
base_layer.fill((255, 255, 255))

# colors
colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorGREEN = (0, 255, 0)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)

draw_color = colorRED

clock = pygame.time.Clock()

# checks if left button is pressed
LMBpressed = False
THICKNESS = 5

currX = 0
currY = 0
prevX = 0
prevY = 0

draw_mode = "rectangle"  # modes: "rectangle", "circle", "eraser"

#functions to calculate shapes
def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def calculate_circle(x1, y1, x2, y2):
    radius = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 / 2)
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    return center_x, center_y, radius

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            prevX, prevY = event.pos
        
        # drawing shapes
        if event.type == pygame.MOUSEMOTION:
            if LMBpressed:
                currX, currY = event.pos
                screen.blit(base_layer, (0, 0))
                
                if draw_mode == "rectangle":
                    pygame.draw.rect(screen, draw_color, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                elif draw_mode == "circle":
                    cx, cy, r = calculate_circle(prevX, prevY, currX, currY)
                    pygame.draw.circle(screen, draw_color, (cx, cy), r, THICKNESS)
                elif draw_mode == "eraser":
                    pygame.draw.line(base_layer, colorWHITE, (prevX, prevY), (currX, currY), THICKNESS)
                    prevX, prevY = currX, currY
        
        # mouse button is released
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False
            currX, currY = event.pos
            
            if draw_mode == "rectangle":
                pygame.draw.rect(base_layer, draw_color, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
            elif draw_mode == "circle":
                cx, cy, r = calculate_circle(prevX, prevY, currX, currY)
                pygame.draw.circle(base_layer, draw_color, (cx, cy), r, THICKNESS)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_EQUALS: #changing thickness
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                THICKNESS = max(1, THICKNESS - 1)
            if event.key == pygame.K_r:
                draw_color = colorRED # changing clors 
            if event.key == pygame.K_g:
                draw_color = colorGREEN
            if event.key == pygame.K_b:
                draw_color = colorBLUE
            if event.key == pygame.K_e: # changind modes
                draw_mode = "eraser"
            if event.key == pygame.K_c:
                draw_mode = "circle"
            if event.key == pygame.K_s:
                draw_mode = "rectangle"
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
