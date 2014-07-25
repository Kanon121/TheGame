import Globals as gb
from Entity import Entity
from Entity import Enemy
import Map as maps
gb.pygame.init()
gb.window.CreateWindow(gb.screen_height, gb.screen_width)

player = Entity(100, 100, 'guy.png')
#baddie = Enemy(300, 300, 'mummy.png')
#gb.entities.append(baddie)
playing = True



while playing:
    time_passed = gb.clock.tick(60) 
    
    for e in gb.pygame.event.get():
        if e.type == gb.pygame.QUIT:
            playing = False
        if e.type == gb.pygame.KEYDOWN and e.key == gb.pygame.K_ESCAPE:
            playing = False 
        move = e
    key = gb.pygame.key.get_pressed()
    player.update(move)
   
    maps.render()
    for ents in gb.entities:
        ents.update()
        ents.render()

    
    player.render()

    gb.pygame.display.flip()
    gb.window.RenderWindow('black')
    
