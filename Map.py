import Globals as gb
import ConfigParser
import os



class Level(object):
    def __init__(self):
        self.onLevel = ["level", 0]
        self.mapCount = 0
        self.levels = ["a", "b", "c", "d" , "e", "f", "g"]
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
                block = Blocks(0, x, y, tile_x, tile_y, 'sand.png',  False)
                
                
           
           elif block == '#':
                block = Blocks(1, x, y, tile_x, tile_y, 'wall.png', True)
                                      
           elif block == 'S':
                block = Blocks(2, x, y, tile_x, tile_y, 'stairsBroken.png', 
                    False)
                                           
           if block == "s":
                block = Blocks(3, x, y, tile_x, tile_y, 'stairsDown.png', 
                    False)
                gb.player.save_x = block.rect.x
                gb.player.save_y = block.rect.y
                                         
           
           if block != "-":
                block.rect.x = x
                block.rect.y = y
                x += 50
                new_blocks.append(block)
                tile_x += 1 
                
           
           if block == "-":
                x += 50 
                #Block = Blocks(-1, x, y, tile_x, tile_y, '',  False)
                tile_x += 1
                       
           
           if x == len(level.current_map[0])*50:
                y += 50
                x = 0
                tile_y += 1
                tile_x = 0

class Blocks(object):
    def __init__(self, ID, x, y, tile_x, tile_y, pic, wall):
        self.tile_x = tile_x
        self.tile_y = tile_y
        self.location = (tile_x, tile_y)
        self.ID = ID
        self.is_wall = wall
        self.image = self.GetImage(pic)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.onScreen = True
        self.parent = (0,0)
        self.location = self.tile_x, self.tile_y
        self.parent = None
        self.gx = 0
        self.hx = 0
        self.fx = self.gx + self.hx

    def GetImage(self, pic):
        self.pic = pic
        img_file = os.path.join('img', pic)
        self.image = gb.pygame.image.load(img_file).convert()
        return self.image
        



def inherent(selected, x, y):
    block = Blocks(selected.ID, x, y, 
        selected.tile_x,selected.tile_y, selected.pic, selected.is_wall)
    return block


def loadMap():
    global level
    level = Level() 
    level.load_file("level")
    RenderMap()
        

def save():
    with open('save.save', 'w') as f:
        for blocks in new_blocks:   
            stored = (blocks.ID, blocks.rect.x, blocks.rect.y, blocks.tile_x,
                blocks.tile_y, blocks.pic, blocks.is_wall)
            blocks = stored 
       
            print str(type(blocks))
            

        gb.pickle.dump(new_blocks, f)
        exit()

def load():
    with open('save.save', 'r') as f:
        new_blocks = gb.pickle.load(f)
        for block in new_blocks:
            print block            
        
        
        
        
        """    
            if block.ID == 0:
                pic = 'sand.png'
            elif block.ID == 1:
                pic = 'wall.png'
            elif block.ID == 2:
                pic = 'stairsDown.png'
            elif block.ID == 3:
                pic = 'stairsBroken.png'
            img_file = os.path.join('img', pic)
            block.image = gb.pygame.image.load(img_file).convert()
        
        
        
        return new_blocks
"""

loadMap()
#new_blocks = load()
    


def render(cam):
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
           
            gb.window.screen.blit(block.image,(block.rect.x - cam.rect.x, 
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
       
