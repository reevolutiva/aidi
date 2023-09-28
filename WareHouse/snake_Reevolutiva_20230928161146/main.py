'''
This is the main file that runs the snake game.
'''
import pygame
import sys
from snake import Snake
from food import Food
# Initialize pygame
pygame.init()
# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")
# Set up game objects
snake = Snake(window_width, window_height)
food = Food(window_width, window_height)
# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Update game objects
    snake.update()
    snake.check_collision(food)
    # Draw game objects
    window.fill((0, 0, 0))
    snake.draw(window)
    food.draw(window)
    pygame.display.update()
    # Set game speed
    pygame.time.Clock().tick(10)