import pygame
import random

# screen size
WIDTH, HEIGHT = 800, 600

# paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 80
PADDLE_SPEED = 2

# ball settings
BALL_DIAMETER = 15
BALL_SPEED = 2

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# initialize pygame
pygame.init()

# set up display
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# set up assets
paddle = pygame.Rect(WIDTH // 2, HEIGHT - 50, PADDLE_WIDTH, PADDLE_HEIGHT)
balls = [pygame.Rect(random.randint(0, WIDTH), random.randint(0, HEIGHT // 2), BALL_DIAMETER, BALL_DIAMETER) for _ in range(5)]
lives = 3

def draw_screen():
    SCREEN.fill(BLACK)
    pygame.draw.rect(SCREEN, WHITE, paddle)
    for ball in balls:
        pygame.draw.ellipse(SCREEN, WHITE, ball)
    pygame.display.update()

def move_paddle():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-PADDLE_SPEED, 0)
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.move_ip(PADDLE_SPEED, 0)

def move_balls():
    global lives
    for ball in balls:
        ball.move_ip(BALL_SPEED, BALL_SPEED)
        if ball.colliderect(paddle):
            ball.y -= BALL_SPEED
        elif ball.bottom > HEIGHT:
            balls.remove(ball)
            lives -= 1

def check_game_over():
    if lives <= 0:
        print("Game Over!")
        pygame.quit()

def main():
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        draw_screen()
        move_paddle()
        move_balls()
        check_game_over()

        clock.tick(60)

if __name__ == "__main__":
    main()
