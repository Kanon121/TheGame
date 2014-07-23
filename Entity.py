import Globals as gb
import os
class Entity(object):
    def __init__(self, x, y, image):
        self.setup(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def setup(self, image):
        img_file = os.path.join('img', image)
        self.image = gb.pygame.image.load(img_file)
    def render(self):
        gb.window.screen.blit(self.image, self.rect)
        
    def update(self, e):
        pass
class Enemy(Entity):
    def update(self):
        pass
        
