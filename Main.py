import Globals as gb


for argv in gb.sys.argv:
    if argv == '-edit':
        editing = True
        playing = False
    
    else:
        playing = True
        editing = False


"""
baddie = gb.Enemy(300, 300, 'mummy.png')
baddie2 = gb.Enemy(500, 500, 'mummy.png')
gb.entities.append(baddie)
gb.entities.append(baddie2)
"""

mode = 'delete'
draggingL = False
draggingR = False


gb.maps.all_block_types = gb.maps.getAllBlockTypes(gb.maps.new_blocks)


selected = gb.maps.all_block_types[0]


mouseHover = True


def makeBlock():
    emptySpace = True
    posx, posy = gb.pygame.mouse.get_pos()
    posx += gb.cam.rect.x
    posy += gb.cam.rect.y
    roundX = int(50 * round(posx / 50))
    roundY = int(50 * round(posy / 50))
    newblock = gb.maps.inherent(selected, roundX, roundY)
    
    for block in gb.maps.new_blocks:
        if block.rect.collidepoint(posx, posy): 
            gb.maps.new_blocks.remove(block)
            gb.maps.new_blocks.append(newblock)
            emptySpace = False
            break
    if emptySpace:
        gb.maps.new_blocks.append(newblock)
        




while editing:
    ev = gb.pygame.event.get()
    for e in ev:
        if e.type == gb.pygame.QUIT:
            editing = False
            gb.maps.save()


        if e.type == gb.pygame.KEYDOWN and e.key == gb.pygame.K_t:
            mouseHover = not mouseHover
       
        if e.type == gb.pygame.KEYDOWN and e.key == gb.pygame.K_y:
            selected = gb.maps.cycleBlock(selected)
            
                
                
            
        if e.type == gb.pygame.MOUSEBUTTONDOWN:
            if e.button == 3:
                draggingL = True
                for block in gb.maps.new_blocks:
                    if block.rect.collidepoint(e.pos[0] + gb.cam.rect.x,
                        e.pos[1] + gb.cam.rect.y):
                        gb.maps.new_blocks.remove(block)
            
            if e.button == 1:                
                makeBlock()
                draggingR = True
            
            
            if e.button == 2:
                for block in gb.maps.new_blocks:
                    if block.rect.collidepoint(e.pos[0] + gb.cam.rect.x,
                        e.pos[1] + gb.cam.rect.y):
                        selected = block

        if e.type == gb.pygame.MOUSEBUTTONUP:
            if e.button == 3:
                draggingL = False
            if e.button == 1:
                draggingR = False


        if draggingL:
            posx, posy = gb.pygame.mouse.get_pos()
            
            for block in gb.maps.new_blocks:
                if block.rect.collidepoint(posx + gb.cam.rect.x,
                    posy + gb.cam.rect.y):
                    gb.maps.new_blocks.remove(block)

        if draggingR:
            makeBlock()            

    gb.maps.render(gb.cam)
    if mouseHover:
        posx, posy = gb.pygame.mouse.get_pos()
        gb.window.screen.blit(selected.image, (posx - 25 , posy - 25))
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





while playing:
    time_passed = gb.clock.tick(60)
    for e in gb.pygame.event.get():
        if e.type == gb.pygame.QUIT:
            playing = False
            gb.maps.save()
        if e.type == gb.pygame.KEYDOWN and e.key == gb.pygame.K_ESCAPE:
            playing = False 

    key = gb.pygame.key.get_pressed()

    if key[gb.pygame.K_LEFT]:
        gb.player.update("left")
    if key[gb.pygame.K_RIGHT]:
        gb.player.update("right")
    if key[gb.pygame.K_DOWN]:
        gb.player.update("down")
    if key[gb.pygame.K_UP]:
        gb.player.update("up")


    gb.maps.render(gb.cam)    

    gb.cam.update(False) 
    for ents in gb.entities:
        #ents.update(gb.find)
        ents.render(gb.cam)
        ents.see()
     
    gb.player.render(gb.cam)



    gb.player.see(gb.maps.new_blocks)

    gb.pygame.display.flip()
    gb.window.RenderWindow('black')
    
