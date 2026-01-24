import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Game variables
gravity = 0.5
bird_movement = 0
game_active = True
score = 0
high_score = 0
speed = 3

# Bird
bird = pygame.Rect(50, SCREEN_HEIGHT//2, 30, 30)

# Pipes
pipe_width = 70
pipe_height = random.randint(150, 450)
pipe_gap = 150
pipe_x = SCREEN_WIDTH
pipe_top = pygame.Rect(pipe_x, 0, pipe_width, pipe_height)
pipe_bottom = pygame.Rect(pipe_x, pipe_height + pipe_gap, pipe_width, SCREEN_HEIGHT - pipe_height - pipe_gap)

# Font
font = pygame.font.SysFont(None, 40)

# Clock
clock = pygame.time.Clock()

# Function to reset pipes
def reset_pipes():
    global pipe_height, pipe_top, pipe_bottom, pipe_x
    pipe_x = SCREEN_WIDTH
    pipe_height = random.randint(150, 450)
    pipe_top = pygame.Rect(pipe_x, 0, pipe_width, pipe_height)
    pipe_bottom = pygame.Rect(pipe_x, pipe_height + pipe_gap, pipe_width, SCREEN_HEIGHT - pipe_height - pipe_gap)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = -10
            if event.key == pygame.K_SPACE and not game_active:
                game_active = True
                bird.center = (50, SCREEN_HEIGHT//2)
                bird_movement = 0
                score = 0
                reset_pipes()
    
    if game_active:
        # Bird
        bird_movement += gravity
        bird.y += int(bird_movement)
        
        # Pipes
        pipe_x -= speed
        pipe_top.x = pipe_x
        pipe_bottom.x = pipe_x
        
        if pipe_x < -pipe_width:
            reset_pipes()
            score += 1
            if score > high_score:
                high_score = score
        
        # Collision
        if bird.top <= 0 or bird.bottom >= SCREEN_HEIGHT:
            game_active = False
        if bird.colliderect(pipe_top) or bird.colliderect(pipe_bottom):
            game_active = False

    # Draw
    screen.fill(BLUE)
    pygame.draw.rect(screen, GREEN, bird)
    pygame.draw.rect(screen, BLACK, pipe_top)
    pygame.draw.rect(screen, BLACK, pipe_bottom)
    
    # Score
    score_surface = font.render(f'Score: {score}  High Score: {high_score}', True, WHITE)
    screen.blit(score_surface, (10, 10))
    
    pygame.display.update()
    clock.tick(60)

