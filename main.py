import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 10
BASKET_X, BASKET_Y = 400, 50

# Set up some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Create the game screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a ball
ball_pos = [WIDTH // 2, HEIGHT - 100]
ball_vel = [1, -2]

# Create a basket
basket_pos = [BASKET_X, BASKET_Y]

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the background with white
    screen.fill(WHITE)

    # Draw the ball
    pygame.draw.circle(screen, RED, ball_pos, BALL_RADIUS)

    # Draw the basket
    pygame.draw.rect(screen, BLACK, pygame.Rect(basket_pos[0], basket_pos[1], 50, 50))

    # Move the ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # Check for collision with the basket
    if abs(ball_pos[0] - basket_pos[0]) < BALL_RADIUS and abs(ball_pos[1] - basket_pos[1]) < BALL_RADIUS:
        print("Score!")

    # Flip the display
    pygame.display.flip()
