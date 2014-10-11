import pygame 
from Window import Window
import sys
import os
playing = True
editing = False
reloadGame = False
try: 
    arg = sys.argv[1]
    if arg == "-edit":
        editing = True
        playing = False

    if arg == "-reload":
        reloadGame = True
except IndexError:
    pass

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

cam = Camera(0, 0, screen_width, screen_height)

player = Entity(0, 0, 'guy2.png')

mapName = "level1.level"
onLevel = 1
def LoadGame():
    maps.loadMap()
    if not reloadGame:
        loadHolder = maps.load() 
        maps.new_blocks = loadHolder[0]
        player.rect = loadHolder[1]

LoadGame()
def MovePlayer():
    for block in maps.new_blocks:
        if block.ID == 2:
            start = block.rect.x, block.rect.y

    player.rect.x, player.rect.y = start
MovePlayer()
maps.all_block_types = maps.getAllBlockTypes(maps.new_blocks)

from Editor import Editor
edit = Editor()
if editing == True:
    edit.editing = True



clock = pygame.time.Clock()

entities = []

