import pygame
import time

pygame.init()

mickey_image = pygame.image.load('C:/Users/user/Downloads/mickey_hands.png')
right_hand = pygame.image.load('C:/Users/user/Downloads/right_hand.png')
left_hand = pygame.image.load('C:/Users/user/Downloads/left_hand.png')

mickey_image = pygame.transform.scale(mickey_image, (1000, 900))  
right_hand = pygame.transform.scale(right_hand, (1800, 300))  
left_hand = pygame.transform.scale(left_hand, (500, 100)) 

# Создание окна
screen = pygame.display.set_mode((1000, 600))

# Настройка таймера
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Получаем текущее время
    seconds = int(time.time()) % 60  
    minutes = (int(time.time()) // 60) % 60  

    second_angle = 6 * seconds  # 360 градусов за 60 секунд
    minute_angle = 6 * minutes  # 360 градусов за 60 минут

    screen.fill((255, 255, 255))

    screen.blit(mickey_image, (400 - mickey_image.get_width() // 2, 300 - mickey_image.get_height() // 2))  # Центрируем Микки

    # Вращаем стрелки
    rotated_right_hand = pygame.transform.rotate(right_hand, -minute_angle)
    rotated_left_hand = pygame.transform.rotate(left_hand, -second_angle)

    right_hand_rect = rotated_right_hand.get_rect(center=(400, 300))  # Центр для правой руки
    left_hand_rect = rotated_left_hand.get_rect(center=(400, 300))  # Центр для левой руки

    # Отображаем стрелки
    screen.blit(rotated_right_hand, right_hand_rect)  # Минутная стрелка
    screen.blit(rotated_left_hand, left_hand_rect)  # Секундная стрелка

    pygame.display.flip()  # Обнова экрана

    clock.tick(60)  # FPS 60
