import pygame
import random

pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bricks Breaker")

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

# панель
paddle_width = 100
paddle_height = 10
paddle_x = (screen_width - paddle_width) // 2
paddle_y = screen_height - paddle_height - 10

# мячик и его размеры
ball_radius = 10
ball_x = random.randint(ball_radius, screen_width - ball_radius)
ball_y = screen_height // 2
ball_dx = random.choice([-2, 2])
ball_dy = -2

# размеры блоков
brick_width = 75
brick_height = 20
brick_gap = 10
brick_rows = 5
brick_cols = screen_width // (brick_width + brick_gap)

# Блоки
bricks = []
for row in range(brick_rows):
    for col in range(brick_cols):
        brick_x = col * (brick_width + brick_gap)
        brick_y = row * (brick_height + brick_gap)
        bricks.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))


score = 0
game_over = False
paused = False

F1 = pygame.font.Font(None, 40)
pause_text = F1.render('Пауза', True, white)


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            screen.blit(pause_text, (400, 300))
            if event.key == pygame.K_SPACE:
              paused = not paused
              screen.blit(pause_text, (400, 300)) #Не могу понять как вставить текст при паузе.
    
    
    if not paused:
        # Управление мышью
        paddle_x = pygame.mouse.get_pos()[0] - paddle_width // 2

        # Движение мячика
        ball_x += ball_dx /2
        ball_y += ball_dy /2

        # границы панели
        if ball_y + ball_radius >= paddle_y and ball_x >= paddle_x and ball_x <= paddle_x + paddle_width:
            ball_dy = -ball_dy

        # границы блоков
        for brick in bricks:
            if brick.colliderect(pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)):
                bricks.remove(brick)
                ball_dy = -ball_dy
                score += 1

        # границы экрана
        if ball_x - ball_radius <= 0 or ball_x + ball_radius >= screen_width:
            ball_dx = -ball_dx
        if ball_y - ball_radius <= 0 or ball_y + ball_radius >= screen_height:
            ball_dy = -ball_dy    
        if ball_y - ball_radius <= 0:
            ball_dy = -ball_dy

    
    screen.fill(black)

    
    pygame.draw.rect(screen, white, (paddle_x, paddle_y, paddle_width, paddle_height))

    
    pygame.draw.circle(screen, red, (ball_x, ball_y), ball_radius)

    
    for brick in bricks:
        pygame.draw.rect(screen, blue, brick)

    # Счет
    font = pygame.font.Font(None, 36)
    score_text = font.render("Счет: " + str(score), True, green)
    screen.blit(score_text, (10, 10))

   
    pygame.display.flip()


pygame.quit()
