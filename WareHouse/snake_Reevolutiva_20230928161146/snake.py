import pygame
class Snake:
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.size = 20
        self.position = [(window_width // 2, window_height // 2)]
        self.direction = "RIGHT"
    def update(self):
        # Update the snake's position based on the current direction
        head_x, head_y = self.position[0]
        if self.direction == "UP":
            head_y -= self.size
        elif self.direction == "DOWN":
            head_y += self.size
        elif self.direction == "LEFT":
            head_x -= self.size
        elif self.direction == "RIGHT":
            head_x += self.size
        # Add a new head position in the direction of movement
        self.position.insert(0, (head_x, head_y))
        # Remove the tail position to maintain the snake's length
        self.position.pop()
    def check_collision(self, food):
        # Check if the snake's head collides with the food
        if self.position[0] == food.position:
            # Increase the snake's length
            self.position.append((0, 0))  # Add a dummy position
            # Generate new food position
            food.position = food.generate_position()
    def draw(self, window):
        # Draw the snake on the game window
        for segment in self.position:
            pygame.draw.rect(window, (0, 255, 0), (segment[0], segment[1], self.size, self.size))
    def change_direction(self, new_direction):
        # Change the snake's direction based on user input
        if new_direction == pygame.K_UP and self.direction != "DOWN":
            self.direction = "UP"
        elif new_direction == pygame.K_DOWN and self.direction != "UP":
            self.direction = "DOWN"
        elif new_direction == pygame.K_LEFT and self.direction != "RIGHT":
            self.direction = "LEFT"
        elif new_direction == pygame.K_RIGHT and self.direction != "LEFT":
            self.direction = "RIGHT"