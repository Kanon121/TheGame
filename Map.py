import Globals as gb
import ConfigParser
import os



class Level(object):
    def __init__(self):
        self.onLevel = ["level", 0]
        self.mapCount = 0
        self.levels = ["a", "b", "c", "d" , "e", "f", "g"]
    def optionxform(self):
        pass
    def load_file(self, level, filename="level.map"):
        self.current_map = []
        self.key = {}
        parser = ConfigParser.ConfigParser()
        parser.read(filename)
        self.current_map = parser.get("level", level).split("\n")
    def loadNextMap(self):
        new_blocks = []
        self.mapCount += 1
        self.onLevel[1] = self.mapCount
        self.onLevel = self.onLevel[0] + str(self.levels[self.mapCount])
        self.load_file(self.onLevel)
        RenderMap()
        self.onLevel = ["level", self.mapCount]
         
def applyTile(block, tile_x, tile_y):
    block.tile_x = tile_x
    block.tile_y = tile_y
    block.location = (block.tile_x, block.tile_y)

def RenderMap():
    global new_blocks
    new_blocks = []
    x = 0
    y = 0
    tile_x = 0
    tile_y = 0
    walls = []
    for row in level.current_map:
        for block in row:
          
           if block == '.':
                block = Blocks()
                block.pic = 'sand.png'
                applyTile(block, tile_x, tile_y)
                
                
           
           elif block == '#':
                block = Blocks()
                block.ID = 1
                block.is_wall = True
                newImage(block, 'img', 'wall.png')
                applyTile(block, tile_x, tile_y)
                                      
           elif block == 'S':
                block = Blocks()
                block.ID = 2
                newImage(block, 'img', 'stairsDown.png')
                applyTile(block, tile_x, tile_y)
                                           
           if block == "s":
                block = Blocks()
                block.ID = 3
                newImage(block, 'img', 'stairsBroken.png')
                block.rect.x = x
                block.rect.y = y
                gb.player.rect.x = block.rect.x
                gb.player.rect.y = block.rect.y
                gb.player.save_x = block.rect.x
                gb.player.save_y = block.rect.y
                applyTile(block, tile_x, tile_y)
                                         
           
           if block != "-":
                block.rect.x = x
                block.rect.y = y
                x += 50
                new_blocks.append(block)
                tile_x += 1 
                
           
           if block == "-":
                x += 50 
                block = Blocks()
                block.pic = ''
                applyTile(block, tile_x, tile_y)
                tile_x += 1
                       
           
           if x == len(level.current_map[0])*50:
                y += 50
                x = 0
                tile_y += 1
                tile_x = 0
class Blocks(object):
    def __init__(self):
        self.tile_x = 0
        self.tile_y = 0
        self.ID = 0
        self.is_wall = False
        self.pic = 'sand.png'
        self.img_file = os.path.join('img', self.pic)
        self.image = gb.pygame.image.load(self.img_file).convert()
        self.rect = self.image.get_rect()
        self.onScreen = True
        self.parent = (0,0)
        self.location = self.tile_x, self.tile_y
        self.parent = None 
        self.gx = 0
        self.hx = 0
        self.fx = self.gx + self.hx
    
def newImage(block, location, picture):
    block.pic = picture
    block.img_file = os.path.join(location, block.pic)
    block.image = gb.pygame.image.load(block.img_file)


def loadMap():
    global level
    level = Level() 
    level.load_file("level")
    RenderMap()
        
loadMap()



def render(fov, cam):
    for block in new_blocks:
     
        screenposX = (block.rect.x - cam.rect.x) / 50
        screenposY = (block.rect.y - cam.rect.y) / 50
        if screenposX > 800 / 50:
            block.onScreen = False
        elif screenposX < -50:
            block.onScreen = False
        elif screenposY > 800 / 50:
            block.onScreen = False
        elif screenposY < -50:
            block.onScreen = False
            
        else:
            block.onScreen = True


        if block.onScreen == True:                 
           
            gb.window.screen.blit(block.image, (block.rect.x - cam.rect.x,
                block.rect.y - cam.rect.y))
""" 
        if block.onScreen:
            if block.rect.colliderect(fov):
                block.remembered = True
                if block.ID == 0:
                    if block.trans == True:
                        newImage(block, 'img', 'sand.png')
                        block.trans = False
                if block.ID == 1:
                    if block.trans == True:
                        newImage(block, 'img', 'wall.png')
                        block.trans = False
                gb.window.screen.blit(block.image, (block.rect.x - cam.rect.x,
                    block.rect.y - cam.rect.y))
        

           
            if not block.rect.colliderect(fov):

                if block.remembered == True:
                    if block.trans == False:
                        if block.ID == 0:
                            newImage(block, 'img', 'sand_trans.png')
                            block.trans = True
                        if block.ID == 1:
                            newImage(block, 'img', 'wall_trans.png')
                            block.trans = True
                    gb.window.screen.blit(block.image, (block.rect.x - cam.rect.x,
            block.rect.y - cam.rect.y))
"""
       
