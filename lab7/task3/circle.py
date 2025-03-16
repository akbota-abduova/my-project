import pygame

pygame.init()

# Устанавливаем размер окна
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Начальные координаты и размер мяча
x, y = WIDTH // 2, HEIGHT // 2  # Центр экрана
radius = 25 
speed = 20  # Сколько пикселей двигается мяч за раз

# Создаем мячик
ball = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)

running = True
while running:
    #события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #клавы
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        if ball.top > 0:  # Проверка, чтобы мяч не вышел за верхнюю границу
            ball.y -= speed
    if keys[pygame.K_DOWN]:
        if ball.bottom < HEIGHT: 
            ball.y += speed
    if keys[pygame.K_LEFT]:
        if ball.left > 0:  
            ball.x -= speed
    if keys[pygame.K_RIGHT]:
        if ball.right < WIDTH:  
            ball.x += speed

    screen.fill(WHITE)
    
    pygame.draw.circle(screen, RED, ball.center, radius)
    
    pygame.display.flip()

    #  FPS 
    pygame.time.Clock().tick(60)
    
# Закрытие Pygame
pygame.quit()
