import pygame
from pygame.locals import *

pygame.init()
screen_info = pygame.display.Info()

# set the width and height to the size of the screen
size = (width, height) = (screen_info.current_w, screen_info.current_h)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (26, 255, 255)

ball_image = pygame.image.load("ball-6x6.png")
ball_image = pygame.transform.smoothscale(ball_image, (30, 30))
ball_rect = ball_image.get_rect()


def main():
    while True:
        # program will never run at more than 60 frames/sec
        clock.tick(60)
        screen.fill(color)
        screen.blit(ball_image, ball_rect)
        # update the full display to the screen
        pygame.display.flip()


if __name__ == '__main__':
    main()
