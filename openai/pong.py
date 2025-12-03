

# Generated Code:

# Creating a simple Pong game in Python can be accomplished using the `pygame` library, which is suited for game development. Below is a basic implementation of the Pong game. Make sure to install the `pygame` library if you haven't already:

# ```bash
# pip install pygame
# ```

# Then you can use the following script to create a simple Pong game:

# ```python
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BALL_SPEED_X = 5
BALL_SPEED_Y = 5
PADDLE_SPEED = 7

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Define the ball and paddles
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
paddle1 = pygame.Rect(30, HEIGHT // 2 - 60, 10, 120)
paddle2 = pygame.Rect(WIDTH - 40, HEIGHT // 2 - 60, 10, 120)

# Ball movement variables
ball_speed_x = BALL_SPEED_X
ball_speed_y = BALL_SPEED_Y

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
        paddle1.y += PADDLE_SPEED
    if keys[pygame.K_UP] and paddle2.top > 0:
        paddle2.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle2.bottom < HEIGHT:
        paddle2.y += PADDLE_SPEED

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with top and bottom walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y = -ball_speed_y

    # Ball collision with paddles
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x = -ball_speed_x

    # Reset the ball if it goes out of bounds
    if ball.left <= 0 or ball.right >= WIDTH:
        ball.x = WIDTH // 2 - 15
        ball.y = HEIGHT // 2 - 15
        ball_speed_x = -ball_speed_x  # Change direction

    # Drawing everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    pygame.display.flip()
    pygame.time.Clock().tick(60)
# ```

# ### How to Run the Game:
# 1. Ensure you have Python and `pygame` installed.
# 2. Copy the script into a Python file, e.g., `pong.py`.
# 3. Run the script using `python pong.py`.

# ### Controls:
# - Player 1 (Left Paddle): Use `W` to move up, `S` to move down.
# - Player 2 (Right Paddle): Use the `UP` arrow key to move up, `DOWN` arrow key to move down.

# This code provides a simple Pong game that you can build upon for more features, such as scoring, sound effects, or improved graphics. Enjoy coding!