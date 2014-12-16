from PodSixNet.Channel import Channel
from PodSixNet.Server import Server
from time import sleep


class ClientChannel(Channel):
    def __init__(self, *args, **kwargs):
        Channel.__init__(self, *args, **kwargs)

    def Network(self, data):
        pass

    def Network_move(self, data):
        #self._server.Move(data)
        print data

class GameServer(Server):
    channelClass = ClientChannel
	
    def __init__(self, *args, **kwargs):
        Server.__init__(self, *args, **kwargs)    
        self.queue = None
        self.currentIndex = 0
        self.games = []
    
    def Connected(self, channel, addr):
        print "new connection: ", channel
        if self.queue == None:
            self.currentIndex += 1
            self.queue = Game(channel, self.currentIndex)
        else:
            self.queue.player1 = channel
            self.queue.player0.Send({'action': 'startgame'})
            self.queue.player1.Send({'action': 'startgame'})
            self.games.append(self.queue)
            self.queue = None
 

class Game():
    def __init__(self, player0, currentIndex):
        self.player0 = player0
        self.player1 = None
        self.currentIndex = currentIndex


 
print "STARTING SERVER ON LOCALHOST"

mainServer = GameServer()

while True:
    mainServer.Pump()
    sleep(0.01)