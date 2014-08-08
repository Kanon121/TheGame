import pygame 
from Window import Window
window = Window()
screen_width = 800
screen_height = 800
pygame.init()
window.CreateWindow(screen_height, screen_width)
pygame.display.init()

from Entity import Entity
from Entity import Enemy
player = Entity(50, 50, 'guy2.png')

from Camera import Camera


cam = Camera(0, 0, screen_width, screen_height)
import Map as maps




clock = pygame.time.Clock()
entities = []


total_screen_height = maps.level.current_map * 50
total_screen_width = maps.level.current_map[0] * 50
