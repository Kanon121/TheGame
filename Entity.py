import Globals as gb
import os
class Entity(object):
    def __init__(self, x, y, image):
        self.setup(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.save_x = self.rect.x
        self.save_y = self.rect.y
        self.movingR = False
        self.movingL = False
        self.movingU = False
        self.movingD = False
        self.moving = False
        self.flipped = False
        self.flippedImage = gb.pygame.transform.flip(self.image, True, False)


    def setup(self, image):
        img_file = os.path.join('img', image)
        self.image = gb.pygame.image.load(img_file)
    
    def render(self, cam):
        if self.flipped == True:
            gb.window.screen.blit(self.flippedImage, (self.rect.x - cam.rect.x,
        self.rect.y - cam.rect.y))
        else:
            gb.window.screen.blit(self.image, (self.rect.x - cam.rect.x,
        self.rect.y - cam.rect.y))

        
    def move(self, cam):
  
        for block in gb.maps.new_blocks:
            if self.rect.colliderect(block):
                if block.is_wall == True:
                    self.rect.x = self.save_x
                    self.rect.y = self.save_y
                #block.ID 2 is stairs down
                if block.ID == 2:
                   gb.maps.level.loadNextMap()
                             
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
            if self.flipped == True:
                self.flipped = False
            self.save_x = self.rect.x
            self.rect.x -= 3
    


    
    
    def update(self, e):





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
        
        
