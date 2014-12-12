import Globals as gb
class Overlay():
    def __init__(self):
        self.font = gb.pygame.font.SysFont("monospace", 30)
        
    def render(self):
        keys = gb.player.keys
        keyText = self.font.render("Keys: "+str(keys), 1, (255,255,0))
        gb.window.screen.blit(keyText, (10, 750))
