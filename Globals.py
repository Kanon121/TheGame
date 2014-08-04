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
import Map as maps



player = Entity(100, 100, 'guy2.png')

clock = pygame.time.Clock()
entities = []


total_screen_height = maps.level.current_map * 50
total_screen_width = maps.level.current_map[0] * 50
