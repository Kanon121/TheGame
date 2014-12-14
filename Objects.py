import Globals as gb
import os
import ConfigParser
all_objects = []
all_object_types = []
class AddObjectType(object):
    def __init__(self):
        self.load_file()
    def load_file(self, filename="level.map"):
        self.all_types = []
        self.key = {}
        parser = ConfigParser.ConfigParser()
        parser.read(filename)
        self.all_types = parser.get("objects", "objects").split("\n")
class Objects():
    def __init__(self, ID, image,  x, y, direction=None): 
        self.setup(image) 
        self.ID = ID
        self.pic = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = direction
      
   
    def setup(self, image):
        img_file = os.path.join('img', image)
        self.image = gb.pygame.image.load(img_file)




def inherent(selected, x, y):
    obj = Objects(selected.ID, selected.pic, x, y)
    if obj.ID == 102:
        obj.direction = "up"
    if obj.ID == 103:
        obj.direction = "left"
    return obj

# WORK ON THIS
def turretDetect(obj):

    if obj.direction == "left":
        if gb.player.rect.x < obj.rect.x:   
            if gb.player.rect.y < (obj.rect.y + 20) and gb.player.rect.y > (obj.rect.y - 20):
                pass
            

    if obj.direction == "right":
        pass
    if obj.direction == "up":
        pass
    if obj.direction =="down":
        pass
        
    

def UpdateObjects():
    for obj in gb.objects.all_objects:
        if not gb.edit.editing:
            speed = 3
        else:
            if not gb.edit.pauseMoving:
                speed = 0
            else:
                speed = 1
        gb.window.screen.blit(obj.image, (obj.rect.x - gb.cam.rect.x,
            obj.rect.y - gb.cam.rect.y))       
       
        if obj.ID == 102 or obj.ID == 103:
            if obj.direction == "up":
                obj.rect.y -= speed
            elif obj.direction == "down":
                obj.rect.y += speed
            elif obj.direction == "right":
                obj.rect.x += speed
            elif obj.direction == "left":
                obj.rect.x -= speed
        
            for block in gb.maps.new_blocks:
                if block.is_wall:
                    if obj.rect.colliderect(block):
                        if obj.direction == "up":
                            obj.direction = "down"
                        elif obj.direction == "down":
                            obj.direction = "up"
                        elif obj.direction == "left":
                            obj.direction = "right"
                        elif obj.direction == "right":
                            obj.direction = "left" 

        if obj.ID >= 104  and obj.ID <= 107:
            turretDetect(obj)
            

        
def GetTypes():
    for row in ObjTypes.all_types:
        for obj in row:
            if obj == "C": 
                chest = Objects(100, 'chest.png', 100, 100)
                all_object_types.append(chest)
                all_objects.append(chest)
                
            if obj == "c":
                crate = Objects(101, 'crate.png', 100, 100)
                all_object_types.append(crate)
            
            if obj == "<":
                spikeY = Objects(102, 'spikeblock.png', 100, 100, direction="up")
                all_object_types.append(spikeY)

            if obj == "^":
                spikeX = Objects(103, 'spikeblock.png', 100, 100, direction="left")
                all_object_types.append(spikeX)
            
            if obj == "L":
                turretLeft = Objects(104, 'turretleft.png', 100, 100, direction="left")
                all_object_types.append(turretLeft)
                
ObjTypes = AddObjectType()
GetTypes()

class Items(Objects):
    pass
    
