import pygame
import time

pygame.init()

# Загружаем изображение Микки и рук
mickey_image = pygame.image.load('mickey_hands.png')  # Путь к изображению
right_hand = pygame.image.load('right_hand.png')  # Путь к руке для минут
left_hand = pygame.image.load('left_hand.png')  # Путь к руке для секунд

# Создаем окно
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()  # Настроим таймер

while True:
    screen.fill((255, 255, 255))  # Белый фон
    
    # Получаем текущее время (секунды и минуты)
    seconds = int(time.time()) % 60  # Секунды
    minutes = (int(time.time()) // 60) % 60  # Минуты
    
    # Рассчитываем углы для вращения стрелок
    second_angle = 6 * seconds  # 360 градусов за 60 секунд
    minute_angle = 6 * minutes  # 360 градусов за 60 минут

    # Вращаем руки
    rotated_right_hand = pygame.transform.rotate(right_hand, minute_angle)
    rotated_left_hand = pygame.transform.rotate(left_hand, second_angle)
    
    # Рисуем изображения (Микки и его руки)
    screen.blit(mickey_image, (400, 300))  # Рисуем Микки
    screen.blit(rotated_right_hand, (400, 300))  # Минутная стрелка
    screen.blit(rotated_left_hand, (400, 300))  # Секундная стрелка

    pygame.display.flip()  # Обновляем экран
    clock.tick(60)  # Ограничиваем FPS до 60
