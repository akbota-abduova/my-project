import pygame
import time

pygame.init()

# Загружаем фотки
mickey_image = pygame.image.load('mickey_hands.png') 
right_hand = pygame.image.load('right_hand.png') 
left_hand = pygame.image.load('left_hand.png')  

# Создаем окно
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()  # Настроим таймер

while True:
    screen.fill((255, 255, 255))  # фон
    
    # Получаем текущее время
    seconds = int(time.time()) % 60  # Сек
    minutes = (int(time.time()) // 60) % 60  # Мин
    
    # Рассчитываем углы для вращения стрелок
    second_angle = 6 * seconds  #сек
    minute_angle = 6 * minutes  #мин

    # Вращаем руки
    rotated_right_hand = pygame.transform.rotate(right_hand, minute_angle)
    rotated_left_hand = pygame.transform.rotate(left_hand, second_angle)
    
    # Рисуем 
    screen.blit(mickey_image, (400, 300)) 
    screen.blit(rotated_right_hand, (400, 300))  
    screen.blit(rotated_left_hand, (400, 300))  

    pygame.display.flip()  # Обнова экрана
    clock.tick(60)  # скорость FPS до 60
