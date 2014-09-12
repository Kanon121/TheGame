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
        self.flipped = False
        self.speed = 3
        self.flippedImage = gb.pygame.transform.flip(self.image, True, False)
        self.onBlock = 0

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

        
    def see(self, blocks):
 
        end = (gb.find.end.rect.center[0] - gb.cam.rect.x, 
            gb.find.end.rect.center[1] -gb.cam.rect.y)
        
        
        start = (gb.player.rect.center[0] - gb.cam.rect.x, 
            gb.player.rect.center[1] - gb.cam.rect.y)

        line = gb.pygame.draw.line(gb.window.screen, (255, 255, 255), 
            start, end)
       
       
    def move(self, dx, dy):

        self.rect.x += dx
        self.rect.y += dy
        
        for block in gb.maps.new_blocks:
            if self.rect.colliderect(block):
                if block.is_wall:
                    if dx > 0:
                        self.rect.right = block.rect.left
                    if dx < 0:
                        self.rect.left = block.rect.right
                    if dy > 0:
                        self.rect.bottom = block.rect.top
                    if dy < 0:
                        self.rect.top = block.rect.bottom
                    
                
                #block.ID 2 is stairs down
                if block.ID == 2:
                   gb.maps.level.loadNextMap()



    
    def update(self, e):
        spx = self.speed
        spy = self.speed
        if e == "right":
            self.move(spx, 0)
        if e == "up":
            self.move(0, -spy)
        if e == "left":
            self.move(-spx, 0)
        if e == "down":
            self.move(0, spy)

class Enemy(Entity):


    def update(self):
        self.rect.x += 1
    
    
    
    def render(self, cam):

        gb.window.screen.blit(self.image, (self.rect.x - cam.rect.x, 
            self.rect.y - cam.rect.y))


    def see(self):
        end = (gb.player.rect.center[0] - gb.cam.rect.x, 
            gb.player.rect.center[1] -gb.cam.rect.y)
            
            
        start = (self.rect.center[0] - gb.cam.rect.x, 
            self.rect.center[1] - gb.cam.rect.y)

        line = gb.pygame.draw.line(gb.window.screen, (255, 0, 0), 
            start, end)


        
