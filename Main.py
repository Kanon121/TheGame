import Globals as gb


"""
baddie = gb.Enemy(300, 300, 'mummy.png')
baddie2 = gb.Enemy(500, 500, 'mummy.png')
gb.entities.append(baddie)
gb.entities.append(baddie2)
"""
class Associate():
    def __init__(self, text, id, offset):
        self.surface = text
        self.rect = gb.pygame.Surface.get_rect(self.surface)
        self.ID = id
        self.rect.x = 30
        self.rect.y = 10 + offset
        GetID(self)
settingUp = True
if settingUp:

    typed = []
    files = []
    saves = []
    files.append(gb.os.listdir(gb.os.getcwd() + "/saves/"))
    checked = 0
    displayGames = []
    gb.pygame.font.init()
    myfont = gb.pygame.font.SysFont("monospace", 30)
    
    def GetID(text):
        text.ID = saves[text.ID]
    files = [file for sublist in files for file in sublist]
    for file in files:
        if file[-10:] == ".custommap":
            saves.append(file)

    for save in saves:
        displayGames.append(myfont.render(str(save), 1, (255, 255, 255)))

    while settingUp:
        offset = 0
        id = 0
        event = gb.pygame.event.poll()
        
        for text in displayGames:
            
            text = Associate(text, id, offset)
            id += 1
            offset += 30
            if event.type == gb.pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if text.rect.collidepoint(gb.pygame.mouse.get_pos()):
                        settingUp = False
                        gb.maps.save()
                        gb.mapName = text.ID
                        gb.LoadGame()   
                        



        offset = 0
        for text in displayGames:    
            gb.window.screen.blit(text, (30, 10 + offset))
            offset += 30

        if event.type == gb.pygame.KEYDOWN:
            keyHit = chr(event.key)
            typed.append(keyHit)
        

        gb.pygame.display.flip()
        gb.window.RenderWindow('black')


while gb.edit.editing:
    gb.edit.RunEditor()


while gb.playing:
    time_passed = gb.clock.tick(60)
    for e in gb.pygame.event.get():
        if e.type == gb.pygame.QUIT:
            gb.playing = False
            
        if e.type == gb.pygame.KEYDOWN and e.key == gb.pygame.K_ESCAPE:
            gb.maps.save()

    key = gb.pygame.key.get_pressed()

    if key[gb.pygame.K_a]:
        gb.player.update("left")
    if key[gb.pygame.K_d]:
        gb.player.update("right")
    if key[gb.pygame.K_s]:
        gb.player.update("down")
    if key[gb.pygame.K_w]:
        gb.player.update("up")

    gb.maps.render(gb.cam)    

    gb.cam.update(False) 
    for ents in gb.entities:
        ents.render(gb.cam)
        ents.see()
     
    gb.player.render(gb.cam)
    gb.player.see(gb.maps.new_blocks)

    gb.pygame.display.flip()
    gb.window.RenderWindow('black')
    
