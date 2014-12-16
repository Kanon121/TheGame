import pygame
from Window import Window
window = Window()
screen_width = 800
screen_height = 800
pygame.init()
window.CreateWindow(screen_height, screen_width)
pygame.display.init()
clock = pygame.time.Clock()

while True:
    gb.pygame.display.flip()
    gb.window.RenderWindow('black')