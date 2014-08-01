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
        self.grid_x = 0
        self.grid_y = 0
        self.grid_light_x = 0
        self.grid_light_y = 0
        self.is_wall = False
        self.pic = 'sand.png'
        self.img_file = os.path.join('img', self.pic)
        self.image = gb.pygame.image.load(self.img_file)
        self.image = gb.pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.remembered = False
        self.trans = False
        self.in_cam = False
        self.touched = False
        self.on_x = False
        self.on_y = False

def newImage(block, location, picture):
    block.pic = picture
    block.img_file = os.path.join(location, block.pic)
    block.image = gb.pygame.image.load(block.img_file)
    block.image = gb.pygame.transform.scale(block.image, (50, 50))

    

    
new_blocks = []
x = 0
y = 0
grid_x = 0
grid_y = 0
walls = []
for row in level.current_map:
    for block in row:
        if block == '.':
            block = Blocks()
            block.pic = 'sand.png'
            block.rect.x = x
            block.rect.y = y
            block.grid_x = grid_x
            block.grid_y = grid_y
            x += 50
            grid_x += 1
            new_blocks.append(block)
        if block == "T":
            block = Blocks()
            block.rect.x = x
            block.ID = 3
            block.rect.y = y
            block.grid_x = grid_x
            block.grid_y = grid_y
            x += 50
            grid_x += 1
            new_blocks.append(block)
            block.grid_light_x = block.grid_x
            block.grid_light_y = block.grid_y
        if block == '#':
            block = Blocks()
            block.ID = 1
            block.is_wall = True
            newImage(block, 'img', 'wall.png')
            block.rect.x = x
            block.rect.y = y
            block.grid_x = grid_x
            block.grid_y = grid_y
            block.grid_light_x = block.grid_x
            block.grid_light_y = block.grid_y
            walls.append(block)
            x += 50
            grid_x += 1
            new_blocks.append(block)
        if x == gb.screen_width:
            y += 50
            x = 0
            grid_x = 0
            grid_y += 1


light = gb.pygame.Rect(10, 10, 50, 50)
def render(cam, player):
    for block in new_blocks:
        

        if block.rect.colliderect(cam):
            block.in_cam = True
        if block.ID == 3:
            print "trying!"
            if block.grid_light_x == player.on_tile_x:
                block.on_x = True
            if block.grid_light_y == player.on_tile_y:
                block.on_y = True
            if not block.on_x:
                if block.grid_light_x >= player.on_tile_x:
                    block.grid_light_x -= 1
                if block.grid_light_x <= player.on_tile_x:
                    block.grid_light_x += 1
            if not block.on_y:
                if block.grid_light_y >= player.on_tile_y:
                    block.grid_light_y -= 1
                if block.grid_light_y <= player.on_tile_y:
                    block.grid_light_y += 1
            if block.on_x and block.on_y:
                block.on_x = False
                block.on_y = False
                block.grid_light_y = block.grid_y
                block.grid_light_x = block.grid_x

            
            light.x = block.grid_light_x * 50
            light.y = block.grid_light_y * 50           
            gb.pygame.draw.rect(gb.window.screen, (255, 255, 255), light)
        gb.window.screen.blit(block.image, block.rect)

'''
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
'''               
               
