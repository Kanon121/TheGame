import Globals as gb


for argv in gb.sys.argv:
    if argv == '-edit':
        editing = True
        playing = False
    
    else:
        playing = True
        editing = False



baddie = gb.Enemy(300, 300, 'mummy.png')
baddie2 = gb.Enemy(500, 500, 'mummy.png')
gb.entities.append(baddie)
gb.entities.append(baddie2)


mode = 'delete'
draggingL = False
draggingR = False
selected = False


def makeBlock():
    posx, posy = gb.pygame.mouse.get_pos()
    posx += gb.cam.rect.x
    posy += gb.cam.rect.y
    roundX = int(50 * round(posx / 50))
    roundY = int(50 * round(posy / 50))
    if selected:
        newblock = gb.maps.Blocks()
        newblock =  gb.maps.inherent(newblock, selected, roundX, roundY)
    for block in gb.maps.new_blocks:
        if block.rect.collidepoint(posx, posy): 
            gb.maps.new_blocks.remove(block)
            gb.maps.new_blocks.append(newblock)
            madeblock = True
        else:
            if not madeblock:
                madeblock = True
                gb.maps.new_blocks.append(newblock)
            

    
            
                





while editing:
    ev = gb.pygame.event.get()
    for e in ev:
        if e.type == gb.pygame.QUIT:
            editing = False
            gb.maps.save()
            
        if e.type == gb.pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                draggingL = True
                for block in gb.maps.new_blocks:
                    if block.rect.collidepoint(e.pos[0] + gb.cam.rect.x,
                        e.pos[1] + gb.cam.rect.y):
                        if mode == 'delete':
                            gb.maps.new_blocks.remove(block)
            if e.button == 3:                
                makeBlock()
                draggingR = True
            
            
            if e.button == 2:
                for block in gb.maps.new_blocks:
                    if block.rect.collidepoint(e.pos[0] + gb.cam.rect.x,
                        e.pos[1] + gb.cam.rect.y):
                        selected = block

        if e.type == gb.pygame.MOUSEBUTTONUP:
            if e.button == 1:
                draggingL = False
            if e.button == 3:
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
    gb.pygame.display.flip()
    gb.window.RenderWindow('black')
    gb.cam.update(True)

    key = gb.pygame.key.get_pressed()

    if key[gb.pygame.K_d]:
        mode = 'delete'
    if key[gb.pygame.K_c]:
        mode = 'copy'
    if key[gb.pygame.K_p]:
        mode = 'paste'
    if key[gb.pygame.K_LEFT]:
        gb.cam.rect.x -= 3
    if key[gb.pygame.K_RIGHT]:
        gb.cam.rect.x += 3
    if key[gb.pygame.K_DOWN]:
        gb.cam.rect.y += 3
    if key[gb.pygame.K_UP]:
        gb.cam.rect.y -= 3





while playing:
    time_passed = gb.clock.tick(60)
    for e in gb.pygame.event.get():
        if e.type == gb.pygame.QUIT:
            playing = False
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
    
