import pygame 
from Window import Window
import sys
import pickle 
import copy
window = Window()
screen_width = 800
screen_height = 800
pygame.init()
window.CreateWindow(screen_height, screen_width)
pygame.display.init()

from Entity import Entity
from Entity import Enemy
from Camera import Camera
import Map as maps

player = Entity(0, 0, 'guy2.png')
 
cam = Camera(0, 0, screen_width, screen_height)


maps.loadMap()
maps.level.loadNextMap()
maps.new_blocks = maps.load()
 
maps.all_block_types = maps.getAllBlockTypes(maps.new_blocks)


start = None
block = None

for block in maps.new_blocks:    
    if block.ID == 2:
        start = block
    if block.ID == 3:
        end = block
    





#cam.rect.x = start.rect.x - 400 
#cam.rect.y = start.rect.y - 400
player.rect.x = start.rect.x
player.rect.y = start.rect.y


from Finding import Finding
from Editor import Editor

edit = Editor()



"""
find = Finding(start, end, maps.new_blocks)

while not find.found_end:
    find.getNeighbors()
    find.beginSearch()
    
print find.path
"""


clock = pygame.time.Clock()
entities = []


total_screen_height = maps.level.current_map * 50
total_screen_width = maps.level.current_map[0] * 50
