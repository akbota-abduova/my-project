import pygame, sys
from pygame.locals import *
import random, time
import os

pygame.init()

# частота обновления экрана
FPS = 60
clock = pygame.time.Clock()

# основные цвета
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Размеры окна
W, H = 400, 600
SPEED = 5  # Начальная скорость
SCORE = 0  
COINS = 0  

# путь к шрифту
downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
font_path = os.path.join(downloads_folder, 'font_user (1).ttf')  

# Загружаем шрифт для текста
font = pygame.font.Font(font_path, 60)
font_small = pygame.font.Font(font_path, 20)
game_over = font.render("Game Over", True, BLACK)

# Загружаем изображения для монеты, фона, игрока и врага 
coin_icon = pygame.image.load(os.path.join(downloads_folder, 'coin.png'))
coin_icon = pygame.transform.scale(coin_icon, (coin_icon.get_width() // 20, coin_icon.get_height() // 20))
bg = pygame.image.load(os.path.join(downloads_folder, 'AnimatedStreet.png'))

# Создаем окно 
SC = pygame.display.set_mode((W, H))
SC.fill(WHITE)  # Заливаем экран белым
pygame.display.set_caption("My game")  # Заголовок окна


# Класс врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(downloads_folder, 'Enemy.png'))
        self.rect = self.image.get_rect() 
        self.rect.center = (random.randint(40, W - 40), 0)  # Инициализация врага с случайной позиции сверху

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)  # Двигаем врага вниз
        if self.rect.top > 600:  # Если враг выходит за нижнюю границу экрана
            SCORE += 1  # Увеличиваем счёт
            self.rect.top = 0  # Перемещаем врага обратно в верхнюю часть экрана
            self.rect.center = (random.randint(40, W - 40), 0)  # Задаем случайную позицию

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(downloads_folder, 'Player.png'))
        self.rect = self.image.get_rect()  # Получаем прямоугольник для управления положением
        self.rect.center = (160, 520)  # Устанавливаем начальную позицию игрока

    def move(self):
        pressed_key = pygame.key.get_pressed()  # Получаем информацию о нажатых клавишах
        if self.rect.left > 1:
            if pressed_key[K_LEFT]:  # Если нажата стрелка влево
                self.rect.move_ip(-5, 0)  # Двигаем игрока влево
            if pressed_key[K_RIGHT]:  # Если нажата стрелка вправо
                self.rect.move_ip(5, 0)  # Двигаем игрока вправо

# Класс монеты
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(downloads_folder, 'coin.png'))
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 12, self.image.get_height() // 12))  # Масштабируем монету
        self.rect = self.image.get_rect()  # Получаем прямоугольник вокруг монеты
        self.rect.center = (random.randint(40, W - 40), 0)  # Инициализация монеты в случайной позиции сверху

    def move(self):
        self.rect.move_ip(0, 5)  # Двигаем монету вниз
        if self.rect.top > 600:  # Если монета выходит за нижнюю границу экрана
            self.rect.top = 0  # Перемещаем её обратно в верхнюю часть экрана
            self.rect.center = (random.randint(40, W - 40), 0)  # Устанавливаем случайную позицию

# Создаем экземпляры объектов
P1 = Player()  
E1 = Enemy() 
C1 = Coin() 

# Создаем группы для спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)
coins_group = pygame.sprite.Group()
coins_group.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Таймер для увеличения скорости врагов
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 4000)

# Главный цикл
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 1  # Увеличиваем скорость врагов по таймеру
        
        if event.type == QUIT:
            pygame.quit()  # Закрываем игру при выходе
            exit()

    # Отображаем фон и монеты
    SC.blit(bg, (0, 0))
    SC.blit(coin_icon, (10, 35))
    coins_v = font_small.render(f"X{str(COINS)}", True, BLACK)  # Отображаем количество монет
    SC.blit(coins_v, (50, 50))

    # Отображаем все объекты на экране и обновляем их состояние
    for entity in all_sprites:
        SC.blit(entity.image, entity.rect)  # Отображаем объект
        entity.move()  # Обновляем положение объекта
    
    # Проверка на столкновение игрока с врагом
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound(os.path.join(downloads_folder, 'crash.wav')).play()  # Звук столкновения
        time.sleep(0.5)

        SC.fill(RED)  # Заливаем экран красным
        SC.blit(game_over, (30, 250))  # Отображаем текст "Game Over"
        result = font_small.render(f"Your result: {COINS}", True, BLACK)  # Показываем результат
        SC.blit(result, (120, 350))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()  # Удаляем все спрайты

        time.sleep(2)
        pygame.quit()
        sys.exit()  # Закрытие игры после смерти игрока
    
    # Проверка на сбор монеты
    if pygame.sprite.spritecollideany(P1, coins_group):
        COINS += 1  # Увеличиваем количество монет
        for i in coins_group:
            i.rect.top = 0  # Перемещаем монету обратно вверх
            i.rect.center = (random.randint(40, W - 40), 0)  # Задаем случайную позицию

    pygame.display.update()  # Обновляем экран
    clock.tick(FPS)  # Задержка
