import pygame

# Инициализация Pygame
pygame.init()

# Загрузка изображений
mickey_image = pygame.image.load('mickey_hands.png')
right_hand = pygame.image.load('right_hand.png')
left_hand = pygame.image.load('left_hand.png')

# Уменьшаем размер изображений для лучшего отображения
mickey_image = pygame.transform.scale(mickey_image, (200, 200))  # Изменение размера изображения Микки
right_hand = pygame.transform.scale(right_hand, (50, 50))  # Изменение размера правой руки
left_hand = pygame.transform.scale(left_hand, (50, 50))  # Изменение размера левой руки

# Создание окна
screen = pygame.display.set_mode((800, 600))

# Настройка таймера
clock = pygame.time.Clock()

# Главный цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Отображаем фон и изображения
    screen.fill((255, 255, 255))  # Белый фон
    screen.blit(mickey_image, (100, 100))  # Рисуем Микки
    screen.blit(right_hand, (300, 300))  # Минутная стрелка
    screen.blit(left_hand, (400, 400))  # Секундная стрелка

    pygame.display.flip()  # Обновление экрана

    clock.tick(60)  # Ограничиваем FPS до 60
