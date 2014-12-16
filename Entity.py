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
        self.keys = 0
        self.sight = []
        self.hearts = 3
        self.maxhearts = 3
        self.immune = False
        self.immuneMax = 50
        self.immuneCounter = self.immuneMax 
    
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
        Sightdistance = 30
        onBlock = []
        for block in gb.maps.new_blocks:
            if self.rect.colliderect(block):
                onBlock.append(block)

        
        open_list = gb.maps.getAdjacents(onBlock, True)
        already_seen = []
        walls = []
        while (open_list):
            for block in open_list:
                if not block.is_wall:
                    already_seen.append(block)
                else:
                    walls.append(block)
            open_list = []
            open_list = gb.maps.getAdjacents(already_seen, True)
            Sightdistance -= 1
        
        for block in already_seen:
            self.sight.append(block)
        for block in walls:
            self.sight.append(block)
    
    def move(self, dx, dy):

        self.rect.x += dx
        self.rect.y += dy
        
        gb.maps.checkCollisions(self, "player", dx, dy)


    
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
    
    
    # MOVE THIS TO MAPS FUNCTION
    def objCollision(self):
    

        if self.hearts <= 0:
            gb.playing = False


    
        if self.immune:
            self.immuneCounter -= 1
            if self.immuneCounter == 0:
                self.immune = False
                self.immuneCounter = self.immuneMax

        for obj in gb.objects.all_objects:
            if self.rect.colliderect(obj):
                #CHESTS +1 KEY
                if obj.ID == 100:     
                    self.keys += 1
                    gb.objects.all_objects.remove(obj)
                # SPIKE BLOCKS
                if obj.ID == 102:
                    if not self.immune:
                        self.hearts -= 1
                        self.immune = True
                if obj.ID == 103:
                    if not self.immune:
                        self.hearts -= 1
                        self.immune = True








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
  
        
