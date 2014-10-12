import Globals as gb
import ConfigParser
import os

class AddBlockType(object):
    def __init__(self):
        self.load_file()
    def load_file(self, filename="level.map"):
        self.all_types = []
        self.key = {}
        parser = ConfigParser.ConfigParser()
        parser.read(filename)
        self.all_types = parser.get("level", "level").split("\n")

        


new_blocks = []
def RenderMap():
    x = 0
    y = 0
    tile_x = 0
    tile_y = 0
    walls = []
    for row in gotTypes.all_types:
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
           
           if block == "t":
                block = Blocks(4, x, y, 'torch.png', False)
           
           if block == "!":
                block = Blocks(5, x, y, 'door_open1.png', False)
           if block == "@":
                block = Blocks(6, x, y, 'door_open2.png', False)
           if block == "%":
                block = Blocks(7, x, y, 'door_closed1.png', True)
           if block == "$":
                block = Blocks(8, x, y, 'door_closed2.png', True)
           if block != "-":
                block.rect.x = x
                block.rect.y = y
                x += 50
                allTypes.append(block)
                tile_x += 1 
                
           
           if block == "-":
                x += 50 
                tile_x += 1
                       
           
           if x == len(gotTypes.all_types[0])*50:
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
            self.image = gb.pygame.image.load(img_file).convert_alpha()
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
        charInfo = [gb.player.rect]
        new_blocks.append(charInfo)
        gb.pickle.dump(new_blocks, f)
        
        

def load():
    with open(os.getcwd() + '/saves/' + gb.mapName, 'r') as f:
        new_blocks = gb.pickle.load(f)
        i = 0
        for block in new_blocks:
            if type(block[0]) == int:
                if block[0] == 2:
                    gb.player.rect.x, gb.player.rect.y = block[1], block[2]                
                block = Blocks(block[0], block[1], block[2], block[3], block[4])
                new_blocks[i] = block

            else:
                gb.player.rect = block[0]
                new_blocks.remove(block)
            i += 1
            
        return [new_blocks, gb.player.rect] 


"""
def getAllBlockTypes(new_blocks):
    gotten = []
    for block in new_blocks:
        if block.ID not in gotten:
            all_block_types.append(block)
            gotten.append(block.ID)
    return all_block_types
 """
# Simplified this in AddBlockType. Also much faster
            
def getLights():
    for block in new_blocks:
        if block.ID == 4:
            lights.append(block)
    return lights

class RenderLight():
    def __init__(self, x, y, alpha):
        self.surface = gb.pygame.Surface((50,50), gb.pygame.SRCALPHA)  
        self.surface.fill((255,255,255, alpha))
        self.x = x
        self.y = y
        self.location = x / 50, y / 50


def getAdjacents(list):
    notWall = []
    for light in list:
        for (i, j) in ADJACENTS:
            check = (light.location[0]+i, light.location[1]+j)
            for block in new_blocks:
                if check == block.location:
                    check = block       
                    if not check.is_wall:
                        if not check in notWall:
                            if not check.ID == 4:
                                notWall.append(check)        
    return notWall
        
def renderLight():
    alpha = 65
    notWall = getAdjacents(lights)
    masterLights = []
    for block in notWall:
        light = RenderLight(block.rect.x, block.rect.y, alpha)
        rendered.append(light)
    #alpha -= 10
    notWall = getAdjacents(rendered)
"""
    for block in notWall:
        light = RenderLight(block.rect.x, block.rect.y, alpha)
        rendered.append(light)
"""
  

def lighting(cam):
    darkness = gb.pygame.Surface((1000, 1000), gb.pygame.SRCALPHA)
    darkness.fill((0,0,0, 100))
    gb.window.screen.blit(darkness, (0, 0))
    for light in lights:
        s = gb.pygame.Surface((50,50), gb.pygame.SRCALPHA)   
        s.fill((255,255,255, 90))         
        gb.window.screen.blit(s, (light.rect.x - cam.rect.x, light.rect.y - cam.rect.y))
    for light in rendered:
        gb.window.screen.blit(light.surface, (light.x - cam.rect.x, light.y - cam.rect.y))

                    
                

                
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


ADJACENTS = ((1,0), (-1,0), (0,1), (0,-1), (1,1), (1, -1), (-1, 1), (-1, -1))    
masterLights = []
rendered = []
lights = []
gotTypes = AddBlockType()       
allTypes = []
RenderMap()


