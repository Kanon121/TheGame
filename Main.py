import Globals as gb


for argv in gb.sys.argv:
    if argv == '-edit':
        gb.edit.editing = True
        playing = False
    
    else:
        playing = True
        gb.edit.editing = False


"""
baddie = gb.Enemy(300, 300, 'mummy.png')
baddie2 = gb.Enemy(500, 500, 'mummy.png')
gb.entities.append(baddie)
gb.entities.append(baddie2)
"""




   




while gb.edit.editing:
    gb.edit.RunEditor()



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
    
