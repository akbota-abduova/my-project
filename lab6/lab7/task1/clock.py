import pygame
import time

pygame.init()

# Загружаем изображение Микки и рук
mickey_image = pygame.image.load('mickey_hands.png')  # Путь к изображению
right_hand = pygame.image.load('right_hand.png') 
left_hand = pygame.image.load('left_hand.png')  

screen = pygame.display.set_mode((800, 600))  # Создаем окно
clock = pygame.time.Clock()  # Настроим таймер

while True:
    screen.fill((255, 255, 255))  # фон
    
    # текущее время
    seconds = int(time.time()) % 60  # Сек
    minutes = (int(time.time()) // 60) % 60  # Мин
    
    # углы для вращения
    second_angle = 6 * seconds  # 360 градусов за 60 секунд
    minute_angle = 6 * minutes  # 360 градусов за 60 минут

    # Вращаем руки
    rotated_right_hand = pygame.transform.rotate(right_hand, minute_angle)
    rotated_left_hand = pygame.transform.rotate(left_hand, second_angle)
    
    screen.blit(mickey_image, (400, 300))  # Рисуем Микки
    screen.blit(rotated_right_hand, (400, 300))  # Минутная стрелка
    screen.blit(rotated_left_hand, (400, 300))  # Секундная стрелка

    pygame.display.flip()  # Обнова экрана
    clock.tick(60)  # скорость FPS до 60
