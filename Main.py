import Globals as gb
from FOV import FOV

#baddie = gb.Enemy(300, 300, 'mummy.png')
#baddie2 = gb.Enemy(500, 500, 'mummy.png')
#gb.entities.append(baddie)
#gb.entities.append(baddie2)


playing = True

fov = FOV()


for block in gb.find.open_list:
    baddie = gb.Enemy(block.rect.x, block.rect.y, 'mummy.png')
    gb.entities.append(baddie)


while playing:
    time_passed = gb.clock.tick(60) 
    
    for e in gb.pygame.event.get():
        if e.type == gb.pygame.QUIT:
            playing = False
        if e.type == gb.pygame.KEYDOWN and e.key == gb.pygame.K_ESCAPE:
            playing = False 
        
    
        gb.player.update(e)
   
    gb.maps.render(fov, gb.cam)    
    gb.player.move(gb.cam)
    center = (gb.player.rect.x - gb.cam.rect.x, 
        gb.player.rect.y - gb.cam.rect.y)
    fov.update(center) 
    gb.cam.update() 
    for ents in gb.entities:
        #ents.update()
        ents.render(gb.cam)
     
      
    gb.player.render(gb.cam)
    
    gb.pygame.display.flip()
    gb.window.RenderWindow('black')
    
