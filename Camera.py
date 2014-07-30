import Globals as gb
class Camera(object):
    def __init__(self):
        self.rect = gb.pygame.Rect(0, 0, 300, 300)
    
    def update(self, center):
        self.rect.center = center
        #gb.pygame.draw.rect(gb.window.screen, (255, 10, 10), self.rect)


