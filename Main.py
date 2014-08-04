import Globals as gb
from FOV import FOV

from Camera import Camera
#baddie = Enemy(300, 300, 'mummy.png')
#gb.entities.append(baddie)


playing = True

fov = FOV()
cam = Camera(0, 0, gb.screen_width, gb.screen_height)

while playing:
    time_passed = gb.clock.tick(60) 
    
    for e in gb.pygame.event.get():
        if e.type == gb.pygame.QUIT:
            playing = False
        if e.type == gb.pygame.KEYDOWN and e.key == gb.pygame.K_ESCAPE:
            playing = False 
        
    
        gb.player.update(e)
    
   
    gb.maps.render(fov, cam)    
    gb.player.move(cam)
    center = (gb.player.rect.x - cam.rect.x, gb.player.rect.y - cam.rect.y)
    fov.update(center) 
    cam.update() 
    for ents in gb.entities:
        ents.update()
        ents.render()
         
    
    gb.player.render(cam)

    gb.pygame.display.flip()
    gb.window.RenderWindow('black')
    
