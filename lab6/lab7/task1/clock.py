import pygame
import time

pygame.init()

# Загружаем изображение Микки и рук
mickey_image = pygame.image.load('mickey_hands.png') 
right_hand = pygame.image.load('right_hand.png') 
left_hand = pygame.image.load('left_hand.png')  

screen = pygame.display.set_mode((800, 600))  # Создаем окно
clock = pygame.time.Clock()  # Настроим таймер
