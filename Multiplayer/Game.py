import pygame
from Window import Window
from PodSixNet.Connection import ConnectionListener, connection
from time import sleep

class Connector(ConnectionListener):
    def __init__(self):
        self.Connect()
        self.running = True
    def update(self):
        connection.Pump()
        self.Pump()

    def Network(self, data):
        print data
    
    def Network_startgame(self, data):
        print "Starting!"

    def render(self):
        self.update()
        ev = pygame.event.get()
        for e in ev:
            if e.type == pygame.QUIT:
                self.running = False

            if e.type == pygame.KEYDOWN and e.key == pygame.K_p:
                self.Send({"action": "move"})
        
        
        pygame.display.flip()
        window.RenderWindow('black') 




        
connector = Connector()

window = Window()
screen_width = 800
screen_height = 800
pygame.init()
window.CreateWindow(screen_height, screen_width)
pygame.display.init()


while connector.running:
    connector.render()


