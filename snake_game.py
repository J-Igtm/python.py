# =========================================
# FULL WORKING SNAKE GAME
# =========================================
# Install pygame:
# pip install pygame

import pygame
import random

# Initialize pygame
pygame.init()

# Screen size
WIDTH = 800
HEIGHT = 600

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 180, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Snake settings
BLOCK = 20
SPEED = 10

# Fonts
font = pygame.font.SysFont("Arial", 30)
big_font = pygame.font.SysFont("Arial", 60)

# Clock
clock = pygame.time.Clock()


# =========================================
# Draw Snake
# =========================================
def draw_snake(snake_body):

    # Body
    for block in snake_body[:-1]:
        pygame.draw.rect(
            screen,
            DARK_GREEN,
            (block[0], block[1], BLOCK, BLOCK)
        )

    # Head
    head = snake_body[-1]

    pygame.draw.rect(
        screen,
        GREEN,
        (head[0], head[1], BLOCK, BLOCK)
    )

    # Eyes
    pygame.draw.circle(screen, WHITE, (head[0] + 5, head[1] + 6), 2)
    pygame.draw.circle(screen, WHITE, (head[0] + 15, head[1] + 6), 2)


# =========================================
# Draw Text
# =========================================
def draw_text(text, color, x, y, big=False):

    if big:
        msg = big_font.render(text, True, color)
    else:
        msg = font.render(text, True, color)

    screen.blit(msg, (x, y))


# =========================================
# Main Game
# =========================================
def game():

    game_over = False

    # Snake start position
    x = WIDTH // 2
    y = HEIGHT // 2

    # Movement
    x_change = BLOCK
    y_change = 0

    # Snake body
    snake_body = [
        [x - 80, y],
        [x - 60, y],
        [x - 40, y],
        [x - 20, y],
        [x, y]
    ]

    snake_length = 5

    # Food position
    food_x = random.randrange(0, WIDTH - BLOCK, BLOCK)
    food_y = random.randrange(0, HEIGHT - BLOCK, BLOCK)

    # Score
    score = 0

    # =========================================
    # Game Loop
    # =========================================
    while not game_over:

        # =====================================
        # Events
        # =====================================
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:

                # LEFT
                if event.key == pygame.K_LEFT:
                    x_change = -BLOCK
                    y_change = 0

                # RIGHT
                elif event.key == pygame.K_RIGHT:
                    x_change = BLOCK
                    y_change = 0

                # UP
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -BLOCK

                # DOWN
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = BLOCK

        # =====================================
        # Move Snake
        # =====================================
        x += x_change
        y += y_change

        # =====================================
        # Border Collision
        # =====================================
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            game_over = True

        # =====================================
        # Background
        # =====================================
        screen.fill(BLACK)

        # =====================================
        # Draw Food
        # =====================================
        pygame.draw.rect(
            screen,
            RED,
            (food_x, food_y, BLOCK, BLOCK)
        )

        # =====================================
        # Snake Head
        # =====================================
        snake_head = [x, y]
        snake_body.append(snake_head)

        # Remove extra body parts
        if len(snake_body) > snake_length:
            del snake_body[0]

        # =====================================
        # Self Collision
        # =====================================
        for block in snake_body[:-1]:
            if block == snake_head:
                game_over = True

        # =====================================
        # Draw Snake
        # =====================================
        draw_snake(snake_body)

        # =====================================
        # Score
        # =====================================
        draw_text(f"Score: {score}", YELLOW, 10, 10)

        # =====================================
        # Update Screen
        # =====================================
        pygame.display.update()

        # =====================================
        # Eat Food
        # =====================================
        if x == food_x and y == food_y:

            food_x = random.randrange(0, WIDTH - BLOCK, BLOCK)
            food_y = random.randrange(0, HEIGHT - BLOCK, BLOCK)

            snake_length += 1
            score += 1

        # Speed
        clock.tick(SPEED)

    # =========================================
    # Game Over Screen
    # =========================================
    screen.fill(BLACK)

    draw_text("GAME OVER", RED, 240, 220, True)
    draw_text(f"Final Score: {score}", WHITE, 300, 320)

    pygame.display.update()

    pygame.time.wait(3000)

    pygame.quit()


# Start Game
game()