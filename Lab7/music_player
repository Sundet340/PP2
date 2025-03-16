import pygame
import sys

pygame.init()
pygame.mixer.init()
WIDTH, HEIGHT = 400, 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")
clock = pygame.time.Clock()
music_files = ["song1.mp3","song2.mp3","song3.mp3"]
i = 0

def play_track(idx):
    pygame.mixer.music.load(music_files[idx])
    pygame.mixer.music.play()

play_track(i)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pygame.mixer.music.unpause()
                if not pygame.mixer.music.get_busy():
                    play_track(i)
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
            elif event.key == pygame.K_n:
                i = (i + 1) % len(music_files)
                play_track(i)
            elif event.key == pygame.K_b:
                i = (i - 1) % len(music_files)
                play_track(i)
    screen.fill((200, 200, 200))
    pygame.display.flip()
    clock.tick(30)
