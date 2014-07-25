import Globals as gb
import os
class Entity(object):
    def __init__(self, x, y, image):
        self.setup(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.movingR = False
        self.movingL = False
        self.movingU = False
        self.movingD = False
        self.flipped = False
        self.flippedImage = gb.pygame.transform.flip(self.image, True, False)


    def setup(self, image):
        img_file = os.path.join('img', image)
        self.image = gb.pygame.image.load(img_file)
    def render(self):
        if self.flipped == True:
            gb.window.screen.blit(self.flippedImage, self.rect)
        else:
            gb.window.screen.blit(self.image, self.rect)

        
    def update(self, e):
        if self.movingR == True:
            if self.flipped == False:
                self.flipped = True  
            self.rect.x += 3
        if self.movingL == True:
            self.flipped = False
            self.rect.x -= 3
        if self.movingD == True:
            self.rect.y += 3
        if self.movingU == True:
            self.rect.y -= 3
       
        if e.type == gb.pygame.KEYDOWN:
            if e.key == gb.pygame.K_RIGHT:
                self.movingR = True
            if e.key == gb.pygame.K_LEFT:
                self.movingL =  True
            if e.key == gb.pygame.K_UP:
                self.movingU = True
            if e.key == gb.pygame.K_DOWN:
                self.movingD = True
    
        if e.type == gb.pygame.KEYUP:
            if e.key == gb.pygame.K_RIGHT:
                self.movingR = False
            if e.key == gb.pygame.K_LEFT:
                self.movingL = False
            if e.key == gb.pygame.K_UP:
                self.movingU = False
            if e.key == gb.pygame.K_DOWN:
                self.movingD = False






class Enemy(Entity):
    def update(self):
        pass
        
        
