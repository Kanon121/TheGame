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
    def __init__(self, image, ID, x, y): 
        self.setup(image) 
        self.ID = ID
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
       
      
   
    def setup(self, image):
        img_file = os.path.join('img', image)
        self.image = gb.pygame.image.load(img_file)

def GetTypes():
    for row in ObjTypes.all_types:
        for obj in row:
            if obj == "C":
                chest = Objects('chest.png', 1, 100, 100)
                all_object_types.append(chest)


ObjTypes = AddObjectType()
GetTypes()

def render():
    for objs in all_objects: 
        gb.window.screen.blit(objs.image,(objs.rect.x - gb.cam.rect.x, 
            objs.rect.y - gb.cam.rect.y))         
