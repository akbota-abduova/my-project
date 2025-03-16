import pygame
import os

pygame.init()

# Параметры окна
W, H = 800, 600
screen = pygame.display.set_mode((W, H))

# путь к Downloads
download_folder = 'C:/Users/user/Downloads/'  

songs = [os.path.join(download_folder, "song1.mp3"), 
         os.path.join(download_folder, "song2.mp3")]

current_song_index = 0

pygame.mixer.init()

def play_music():
    pygame.mixer.music.load(songs[current_song_index])
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(songs)
    play_music()

def previous_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(songs)
    play_music()

running = True
play_music()  # музыка играет сразу
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # клавы
    keys = pygame.key.get_pressed()

    if keys[pygame.K_p]:  # Play/Pause
        if pygame.mixer.music.get_busy():  # Если музыка играет, приостановить
            pygame.mixer.music.pause()
        else:
            play_music()

    if keys[pygame.K_s]:  # Stop
        stop_music()

    if keys[pygame.K_n]:  # Next
        next_song()

    if keys[pygame.K_b]:  # back
        previous_song()

    # Обновф экрана
    screen.fill((255, 255, 255)) 
    pygame.display.flip()

    pygame.time.Clock().tick(30)  # FPS

pygame.quit()
