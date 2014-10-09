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
         
new_blocks = []
def RenderMap():

    x = 0
    y = 0
    tile_x = 0
    tile_y = 0
    walls = []
    for row in level.current_map:
        for block in row:
          
           if block == '.':
                block = Blocks(0, x, y, 'sand.png',  False)
                
                
           
           if block == '#':
                block = Blocks(1, x, y, 'wall.png', True)
                                      
           if block == 'S':
                block = Blocks(2, x, y, 'stairsBroken.png', 
                    False)
                                           
           if block == "s":
                block = Blocks(3, x, y, 'stairsDown.png', 
                    False)                                         
           
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
    def __init__(self, ID, x, y, pic, wall):
        self.ID = ID
        self.is_wall = wall
        self.image = self.GetImage(pic)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.onScreen = True
        self.parent = (0,0)
        self.gx = 0
        self.hx = 0
        self.fx = self.gx + self.hx
        self.location = (self.rect.x / 50 ,self.rect.y / 50)
        self.tile_x = self.location[0]
        self.tile_y = self.location[1]
        
    
    
    
    def GetImage(self, pic):
    
        self.pic = pic
        if not type(pic) is int: 
            img_file = os.path.join('img', self.pic)
            self.image = gb.pygame.image.load(img_file).convert()
            return self.image
                

def cycleBlock(selected):
    

    for loc, blocks in enumerate(all_block_types):
        if selected.ID == blocks.ID:
            whereIs = loc
            end = len(all_block_types) - 1
            if whereIs != end:
                selected = all_block_types[whereIs + 1]
            
            
            if whereIs == end:
                selected = all_block_types[0]
                
            break    
            #selected = all_block_types[0]
    
    
    return selected



def inherent(selected, x, y):
    block = Blocks(selected.ID, x, y,selected.pic, selected.is_wall)
    return block


def loadMap():
    global level
    level = Level() 
    level.load_file("level")
    RenderMap()
        

def unloadBlocks(new_blocks):
    i = 0 
    for blocks in new_blocks:
        
        stored = [blocks.ID, blocks.rect.x, blocks.rect.y,
            blocks.pic, blocks.is_wall]
        new_blocks[i] = stored 
        i += 1
    return new_blocks
        



def save():
    global new_blocks
    with open(os.getcwd() + '/saves/' + gb.mapName, 'w') as f:
        new_blocks = unloadBlocks(new_blocks)
        gb.pickle.dump(new_blocks, f)


def load():
    with open(os.getcwd() + '/saves/' + gb.mapName, 'r') as f:
        new_blocks = gb.pickle.load(f)
        i = 0
        for block in new_blocks:
            
            block = Blocks(block[0], block[1], block[2], block[3], block[4])
            new_blocks[i] = block

            i += 1
            
        return new_blocks 



def getAllBlockTypes(new_blocks):
    gotten = []
    for block in new_blocks:
        if block.ID not in gotten:
            all_block_types.append(block)
            gotten.append(block.ID)


            
            
    
    return all_block_types
 
    

all_block_types = []





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
