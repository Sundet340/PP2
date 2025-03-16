import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Red Ball")
clock = pygame.time.Clock()
r = 25
x = WIDTH//2
y = HEIGHT//2
d = 20

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if y - r - d >= 0:
                    y -= d
            elif event.key == pygame.K_DOWN:
                if y + r + d <= HEIGHT:
                    y += d
            elif event.key == pygame.K_LEFT:
                if x - r - d >= 0:
                    x -= d
            elif event.key == pygame.K_RIGHT:
                if x + r + d <= WIDTH:
                    x += d
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), r)
    pygame.display.flip()
    clock.tick(30)
