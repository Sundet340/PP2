import pygame
import sys
import datetime

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()

clock_face = pygame.image.load("mickeyclock.jpeg").convert_alpha()
hand_right = pygame.image.load("right hand.png").convert_alpha() 
hand_left = pygame.image.load("left hand.png").convert_alpha()   

center_x = WIDTH // 2
center_y = HEIGHT // 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second

    second_angle = -(seconds / 60.0) * 360 + 90
    minute_angle = -(minutes / 60.0) * 360 + 90

    rotated_right_hand = pygame.transform.rotate(hand_right, minute_angle)
    rotated_left_hand = pygame.transform.rotate(hand_left, second_angle)

    right_rect = rotated_right_hand.get_rect(center=(center_x, center_y))
    left_rect = rotated_left_hand.get_rect(center=(center_x, center_y))

    screen.fill((255, 255, 255)) 
    screen.blit(clock_face, clock_face.get_rect(center=(center_x, center_y)))
    screen.blit(rotated_right_hand, right_rect)
    screen.blit(rotated_left_hand, left_rect)

    pygame.display.flip()
    clock.tick(30) 
