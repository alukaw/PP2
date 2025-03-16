import pygame
import os

pygame.init()
pygame.mixer.init()


WIDTH, HEIGHT = 500, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLUE = (70, 130, 180)


font = pygame.font.Font(None, 30)


playlist = [
    "music/ambient-128950.mp3",
    "music/desolate-150576.mp3",
    "music/energetic-background-for-happy-moments-30s-248827.mp3"
]

current_track = 0
paused = False


def play_music():
    global paused
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()
    paused = False 

def stop_music():
    pygame.mixer.music.stop()

def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    play_music()

def previous_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    play_music()

def toggle_pause():
    global paused
    if pygame.mixer.music.get_busy():  
        if paused:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()
        paused = not paused
    else:
        play_music()  



buttons = {
    "Play/Pause": pygame.Rect(50, 200, 110, 50),
    "Stop": pygame.Rect(160, 200, 100, 50),
    "Next": pygame.Rect(270, 200, 100, 50),
    "Previous": pygame.Rect(380, 200, 100, 50)
}


running = True
while running:
    screen.fill(WHITE)

  
    track_text = font.render(f"Now Playing: {os.path.basename(playlist[current_track])}", True, BLUE)
    screen.blit(track_text, (50, 50))

    
    for text, rect in buttons.items():
        pygame.draw.rect(screen, GRAY, rect, border_radius=10)
        label = font.render(text, True, BLUE)
        screen.blit(label, (rect.x + 10, rect.y + 15))

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if buttons["Play/Pause"].collidepoint(event.pos):
                toggle_pause()
            elif buttons["Stop"].collidepoint(event.pos):
                stop_music()
            elif buttons["Next"].collidepoint(event.pos):
                next_track()
            elif buttons["Previous"].collidepoint(event.pos):
                previous_track()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                toggle_pause()
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_b:
                previous_track()

    pygame.display.flip()

pygame.quit()
