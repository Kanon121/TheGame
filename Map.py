import Globals as gb
import ConfigParser
import os



class Level(object):
    def load_file(self, filename="level.map"):
        self.current_map = []
        self.key = {}
        parser = ConfigParser.ConfigParser()
        parser.read(filename)
        self.current_map = parser.get("level", "map").split("\n")
        for section in parser.sections():
            if len(section) == 1:
                desc = dict(parser.items(section))
                self.key[section] = desc
        self.width = len(self.current_map[0])
        self.height = len(self.current_map)




                   
level = Level() 
level.load_file()

class Blocks(object):
    def __init__(self):
        self.ID = 0
        self.is_wall = False
        self.pic = 'sand.png'
        self.img_file = os.path.join('img', self.pic)
        self.image = gb.pygame.image.load(self.img_file)
        self.image = gb.pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.remembered = False
        self.trans = False



new_blocks = []
x = 0
y = 0
for row in level.current_map:
    for block in row:
        if block == '.':
            block = Blocks()
            block.pic = 'sand.png'
            block.rect.x = x
            block.rect.y = y
            x += 50
            new_blocks.append(block)
        if block == '#':
            block = Blocks()
            block.ID = 1
            block.pic = 'wall.png'
            block.is_wall = True
            block.img_file = os.path.join('img', block.pic)
            block.image = gb.pygame.image.load(block.img_file)
            block.image = gb.pygame.transform.scale(block.image, (50, 50))
            block.rect.x = x
            block.rect.y = y
            x += 50
            new_blocks.append(block)
        if x == gb.screen_width:
            y += 50
            x = 0


    
def newImage(block, location, picture):
    block.pic = picture
    block.img_file = os.path.join(location, block.pic)
    block.image = gb.pygame.image.load(block.img_file)
    block.image = gb.pygame.transform.scale(block.image, (50, 50))



def render(cam):
    for block in new_blocks:
        if block.rect.colliderect(cam):
            block.remembered = True
            if block.ID == 0:
                if block.trans == True:
                    newImage(block, 'img', 'sand.png')
                    block.trans = False
                gb.window.screen.blit(block.image, block.rect)
            if block.ID == 1:
                if block.trans == True:
                    newImage(block, 'img', 'wall.png')
                    block.trans = False
                gb.window.screen.blit(block.image, block.rect)

       
        if not block.rect.colliderect(cam):
            if block.remembered == True:
                if block.trans == False:
                    if block.ID == 0:
                        newImage(block, 'img', 'sand_trans.png')
                        block.trans = True
                    if block.ID == 1:
                        newImage(block, 'img', 'wall_trans.png')
                        block.trans = True
                gb.window.screen.blit(block.image, block.rect)
               
               
