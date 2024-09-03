import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Snake properties
snake_block = 20
snake_speed = 15

# Initialize the snake
snake_list = []
snake_length = 1
snake_x = width // 2
snake_y = height // 2

# Initialize movement direction
direction_x = 0
direction_y = 0

# Initialize food
food_x = round(random.randrange(0, width - snake_block) / snake_block) * snake_block
food_y = round(random.randrange(0, height - snake_block) / snake_block) * snake_block

# Set up the game clock
clock = pygame.time.Clock()

# Game loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction_x = -snake_block
                direction_y = 0
            elif event.key == pygame.K_RIGHT:
                direction_x = snake_block
                direction_y = 0
            elif event.key == pygame.K_UP:
                direction_y = -snake_block
                direction_x = 0
            elif event.key == pygame.K_DOWN:
                direction_y = snake_block
                direction_x = 0

    # Move the snake
    snake_x += direction_x
    snake_y += direction_y

    # Check for collision with walls
    if snake_x >= width or snake_x < 0 or snake_y >= height or snake_y < 0:
        game_over = True

    # Draw the game objects
    window.fill(BLACK)
    pygame.draw.rect(window, GREEN, [food_x, food_y, snake_block, snake_block])
    
    snake_head = [snake_x, snake_y]
    snake_list.append(snake_head)
    
    if len(snake_list) > snake_length:
        del snake_list[0]

    for segment in snake_list[:-1]:
        if segment == snake_head:
            game_over = True

    for segment in snake_list:
        pygame.draw.rect(window, WHITE, [segment[0], segment[1], snake_block, snake_block])

    pygame.display.update()

    # Check if snake has eaten the food
    if snake_x == food_x and snake_y == food_y:
        food_x = round(random.randrange(0, width - snake_block) / snake_block) * snake_block
        food_y = round(random.randrange(0, height - snake_block) / snake_block) * snake_block
        snake_length += 1

    # Control game speed
    clock.tick(snake_speed)

# Quit the game
pygame.quit()
