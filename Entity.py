import Globals as gb
import os
from Map import new_blocks as blocks
class Entity(object):
    def __init__(self, x, y, image):
        self.setup(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.save_x = 100
        self.save_y = 100
        self.movingR = False
        self.movingL = False
        self.movingU = False
        self.movingD = False
        self.moving = False
        self.flipped = False
        self.on_tile_x = 0
        self.on_tile_y = 0
        self.image = gb.pygame.transform.scale(self.image,(50, 50))
        self.flippedImage = gb.pygame.transform.flip(self.image, True, False)


    def setup(self, image):
        img_file = os.path.join('img', image)
        self.image = gb.pygame.image.load(img_file)
    
    def render(self):
        if self.flipped == True:
            gb.window.screen.blit(self.flippedImage, self.rect)
        else:
            gb.window.screen.blit(self.image, self.rect)

        
    def move(self):
        
        if self.movingR == True:
            if self.flipped == False:
                self.flipped = True
            self.save_x = self.rect.x
            self.rect.x += 3
        if self.movingU == True:
            self.save_y = self.rect.y
            self.rect.y -= 3
        if self.movingD == True:
            self.save_y = self.rect.y
            self.rect.y += 3
        if self.movingL == True:
            self.save_x = self.rect.x
            self.rect.x -= 3
    
    
    
    
    
    def update(self, e):

 
        for block in blocks:
            if self.rect.colliderect(block):
                self.on_tile_x = block.grid_x
                self.on_tile_y = block.grid_y
                   


        if e.type == gb.pygame.KEYDOWN:
            if e.key == gb.pygame.K_RIGHT:
                self.movingR = True
            if e.key == gb.pygame.K_UP:
                self.movingU = True
            if e.key == gb.pygame.K_LEFT:
                self.movingL = True
            if e.key == gb.pygame.K_DOWN:
                self.movingD = True
       
        if e.type == gb.pygame.KEYUP:
            if e.key == gb.pygame.K_RIGHT:
                self.movingR = False
            if e.key == gb.pygame.K_UP:
                self.movingU = False
            if e.key == gb.pygame.K_DOWN:
                self.movingD = False
            if e.key == gb.pygame.K_LEFT:
                self.movingL = False



class Enemy(Entity):
    def update(self):
        pass
        
        
