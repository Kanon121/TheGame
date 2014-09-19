import Globals as gb
class Editor():
    def __init__(self):
        self.editing = True
        self.draggingL = False
        self.draggingR = False
        self.selected = gb.maps.all_block_types[0]
        self.mouseHover = True


    def makeBlock(self):
        emptySpace = True
        posx, posy = gb.pygame.mouse.get_pos()
        posx += gb.cam.rect.x
        posy += gb.cam.rect.y
        roundX = int(50 * round(posx / 50))
        roundY = int(50 * round(posy / 50))
        newblock = gb.maps.inherent(self.selected, roundX, roundY)
        
        for block in gb.maps.new_blocks:
            if block.rect.collidepoint(posx, posy): 
                gb.maps.new_blocks.remove(block)
                gb.maps.new_blocks.append(newblock)
                emptySpace = False
                break
        if emptySpace:
            gb.maps.new_blocks.append(newblock)
         






    def RunEditor(self):

        ev = gb.pygame.event.get()
        for e in ev:
            if e.type == gb.pygame.QUIT:
                self.editing = False
                issaving = raw_input('Are you saving?')
                gb.maps.save()


            if e.type == gb.pygame.KEYDOWN and e.key == gb.pygame.K_t:
                self.mouseHover = not self.mouseHover
           
            if e.type == gb.pygame.KEYDOWN and e.key == gb.pygame.K_y:
                self.selected = gb.maps.cycleBlock(self.selected)
                
                    
                    
                
            if e.type == gb.pygame.MOUSEBUTTONDOWN:
                if e.button == 3:
                    self.draggingL = True
                    for block in gb.maps.new_blocks:
                        if block.rect.collidepoint(e.pos[0] + gb.cam.rect.x,
                            e.pos[1] + gb.cam.rect.y):
                            gb.maps.new_blocks.remove(block)
                
                if e.button == 1:                
                    self.makeBlock()
                    self.draggingR = True
                
                
                if e.button == 2:
                    for block in gb.maps.new_blocks:
                        if block.rect.collidepoint(e.pos[0] + gb.cam.rect.x,
                            e.pos[1] + gb.cam.rect.y):
                            self.selected = block

            if e.type == gb.pygame.MOUSEBUTTONUP:
                if e.button == 3:
                    self.draggingL = False
                if e.button == 1:
                    self.draggingR = False


            if self.draggingL:
                posx, posy = gb.pygame.mouse.get_pos()
                
                for block in gb.maps.new_blocks:
                    if block.rect.collidepoint(posx + gb.cam.rect.x,
                        posy + gb.cam.rect.y):
                        gb.maps.new_blocks.remove(block)

            if self.draggingR:
                self.makeBlock()            

        gb.maps.render(gb.cam)
        if self.mouseHover:
            posx, posy = gb.pygame.mouse.get_pos()
            gb.window.screen.blit(self.selected.image, (posx - 25 , posy - 25))
            outLine = gb.pygame.draw.rect(gb.window.screen, (100, 200, 200),
                (posx - 25, posy - 25, 51, 51), 2)



        gb.pygame.display.flip()    
        gb.window.RenderWindow('black')    
        gb.cam.update(True)

    
    
    




        key = gb.pygame.key.get_pressed()

        
        if key[gb.pygame.K_a]:
            gb.cam.rect.x -= 3
        if key[gb.pygame.K_d]:
            gb.cam.rect.x += 3
        if key[gb.pygame.K_s]:
            gb.cam.rect.y += 3
        if key[gb.pygame.K_w]:
            gb.cam.rect.y -= 3


