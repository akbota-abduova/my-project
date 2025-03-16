import pygame
import time

pygame.init()

# Загружаем фотки
mickey_image = pygame.image.load('C:/Users/user/Downloads/mickey_hands.png')
right_hand = pygame.image.load('C:/Users/user/Downloads/right_hand.png')
left_hand = pygame.image.load('C:/Users/user/Downloads/left_hand.png')


# Создаем окно
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()  # Настроим таймер

while True:
    screen.fill((255, 255, 255))  #фон
    
    # Получаем текущее время
    seconds = int(time.time()) % 60  # Сек
    minutes = (int(time.time()) // 60) % 60  # Мин
    
    # углы 
    second_angle = 6 * seconds  # 360 градусов за 60 секунд
    minute_angle = 6 * minutes  # 360 градусов за 60 минут

    # Вращаем руки
    rotated_right_hand = pygame.transform.rotate(right_hand, minute_angle)
    rotated_left_hand = pygame.transform.rotate(left_hand, second_angle)
    
    # Рисуем изображения 
    screen.blit(mickey_image, (400, 300)) 
    screen.blit(rotated_right_hand, (400, 300))  
    screen.blit(rotated_left_hand, (400, 300))  

    pygame.display.flip()  # Обнова экранф
    clock.tick(60)  # FPS до 60
