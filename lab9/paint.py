import pygame
import random

# Основные цвета для рисования
white = (255, 255, 255)
eraser = (0, 0, 0)  # Цвет ластика (стирание)
green = (34, 139, 34)  
blue = (0, 0, 255)  
red = (255, 0, 0)  
yellow = (255, 255, 0)  

pygame.display.set_caption("Paint")  # Устанавливаем название окна

def main():
    pygame.init()  # Инициализация библиотеки Pygame
    screen = pygame.display.set_mode((640, 480))  # Создаем окно с размерами 640x480
    clock = pygame.time.Clock()  # Таймер для контроля FPS (частоты кадров)
    
    radius = 15  # Радиус кисти для рисования линий
    mode = white  # Текущий выбранный цвет (по умолчанию белый)
    last_pos = None  # Переменная для хранения последней позиции мыши при рисовании линий
    
    # Основной цикл приложения
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return  # Завершаем приложение при закрытии окна или нажатии Esc
                
            # Цвета при нажатии клавиш
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    mode = red  # Меняем цвет на красный
                elif event.key == pygame.K_g:
                    mode = green  
                elif event.key == pygame.K_b:
                    mode = blue  
                elif event.key == pygame.K_y:
                    mode = yellow  
                elif event.key == pygame.K_BACKSPACE:
                    mode = eraser  # Включаем ластик для стирания
                elif event.key == pygame.K_x:
                    # Случайный цвет при нажатии клавиши x
                    mode = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    
                # При нажатии клавиш w, t, p, e рисуются прямоугольник, треугольник, квадрат и ромб
                elif event.key == pygame.K_w:
                    drawRectangle(screen, pygame.mouse.get_pos(), 200, 100, mode)  # Рисуем прямоугольник
                elif event.key == pygame.K_t:
                    drawRightTriangle(screen, pygame.mouse.get_pos(), 150, 100, mode)  # Рисуем прямоугольный треугольник
                elif event.key == pygame.K_p:
                    drawSquare(screen, pygame.mouse.get_pos(), 100, mode)  # Рисуем квадрат
                elif event.key == pygame.K_e:
                    drawRhombus(screen, pygame.mouse.get_pos(), 150, 100, mode)  # Рисуем ромб
                    
            # При нажатии и перемещении мыши рисуется линия между последней позицией и текущей позицией курсора.
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                last_pos = pygame.mouse.get_pos()  # Запоминаем позицию мыши при первом нажатии
            
            if event.type == pygame.MOUSEMOTION and event.buttons[0] and last_pos:
                drawLineBetween(screen, last_pos, pygame.mouse.get_pos(), radius, mode)  # Рисуем линию
                last_pos = pygame.mouse.get_pos()  # Обновляем последнюю позицию мыши
                
        pygame.display.flip()  # Обновляем экран
        clock.tick(60)  # Ограничиваем FPS до 60 кадров в секунду
        
# Функция для рисования линии между двумя точками
def drawLineBetween(screen, start, end, width, color_mode):
    color = color_mode  # Выбираем цвет для линии
    
    # Рассчитываем горизонтальное (dx) и вертикальное (dy) расстояние между начальной и конечной точками
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    
    # Определяем количество итераций (шагов) на основе максимального из абсолютных значений dx и dy
    # Это гарантирует плавность линии, независимо от наклона
    iterations = max(abs(dx), abs(dy))

    # В цикле для каждой итерации вычисляется прогрессивная позиция между начальной и конечной точками
    # И на каждом шаге рисуется круг, в результате чего образуется плавная линия
    for i in range(iterations):
        progress = 1.0 * i / iterations  # Прогресс на текущем шаге
        aprogress = 1 - progress  # Обратный прогресс для плавного перехода
        x = int(aprogress * start[0] + progress * end[0])  # Вычисляем X-координату точки
        y = int(aprogress * start[1] + progress * end[1])  # Вычисляем Y-координату точки
        pygame.draw.circle(screen, color, (x, y), width)  # Рисуем маленький круг для создания линии

# Функция для рисования прямоугольника
def drawRectangle(screen, mouse_pos, w, h, color):
    x = mouse_pos[0]  # Получаем координату X курсора
    y = mouse_pos[1]  # Получаем координату Y курсора
    rect = pygame.Rect(x, y, w, h)  # Создаем прямоугольник с координатами и размерами
    pygame.draw.rect(screen, color, rect, 3)  # Рисуем прямоугольник с рамкой толщиной 3 пикселя

# Функция для рисования квадрата
def drawSquare(screen, mouse_pos, side, color):
    x = mouse_pos[0]  # Получаем координату X курсора
    y = mouse_pos[1]  # Получаем координату Y курсора
    pygame.draw.rect(screen, color, (x, y, side, side), 3)  # Рисуем квадрат с шириной и высотой side

# Функция для рисования прямоугольного треугольника
def drawRightTriangle(screen, mouse_pos, base, height, color):
    x = mouse_pos[0]  # Получаем координату X курсора
    y = mouse_pos[1]  # Получаем координату Y курсора
    points = [(x, y), (x + base, y), (x, y - height)]  # Точки треугольника
    pygame.draw.polygon(screen, color, points)  # Рисуем треугольник с помощью этих точек

# Функция для рисования ромба
def drawRhombus(screen, mouse_pos, diagonal1, diagonal2, color):
    x = mouse_pos[0]  # Получаем координату X курсора
    y = mouse_pos[1]  # Получаем координату Y курсора
    half_diag1 = diagonal1 / 2  # Половина первой диагонали
    half_diag2 = diagonal2 / 2  # Половина второй диагонали
    points = [(x, y - half_diag2),  # Верхняя точка ромба
              (x - half_diag1, y),  # Левая точка ромба
              (x, y + half_diag2),  # Нижняя точка ромба
              (x + half_diag1, y)]  # Правая точка ромба
    pygame.draw.polygon(screen, color, points)  # Рисуем ромб с помощью этих точек

# Запуск программы
main()
