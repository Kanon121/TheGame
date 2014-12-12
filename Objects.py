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
    def __init__(self, ID, image,  x, y): 
        self.setup(image) 
        self.ID = ID
        self.pic = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = None
      
   
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
                spikeY = Objects(102, 'spikeblock.png', 100, 100)

                all_object_types.append(spikeY)

            if obj == "^":
                spikeX = Objects(103, 'spikeblock.png', 100, 100)
                all_object_types.append(spikeX)

ObjTypes = AddObjectType()
GetTypes()

class Items(Objects):
    pass
    
