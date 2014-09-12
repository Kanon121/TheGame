import pygame 
from Window import Window
import sys
window = Window()
screen_width = 800
screen_height = 800
pygame.init()
window.CreateWindow(screen_height, screen_width)
pygame.display.init()

from Entity import Entity
from Entity import Enemy
player = Entity(52, 52, 'guy2.png')

from Camera import Camera

cam = Camera(0, 0, screen_width, screen_height)

import Map as maps
from Finding import Finding

find = Finding(maps.new_blocks[105], maps.new_blocks[302], maps.new_blocks)
clock = pygame.time.Clock()
entities = []


total_screen_height = maps.level.current_map * 50
total_screen_width = maps.level.current_map[0] * 50
