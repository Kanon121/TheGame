import Globals as gb

ADJACENTS = ((1,0), (-1,0), (0,1), (0,-1), (1,1), (1, -1), (-1, 1), (-1, -1))

class Finding():
    def __init__(self, start_block, end_block, blocks):
        self.start = start_block
        self.current = start_block
        self.end = end_block
        self.open_list = [self.current]
        self.closed_list = []
        self.neighbors = []
        self.blocks = blocks
        self.walls = []
        self.tiles = []
        self.path = []
        self.found_end = False
        self.parseWalls(self.blocks)
        self.getNeighbors()
        self.beginSearch()
 
        
    def parseWalls(self, blocks):
        for block in blocks:
            if block.is_wall == True:
                self.walls.append(block)
            else:
                self.tiles.append(block)
    def getNeighbors(self):
        self.neighbors = []
        for (i, j) in ADJACENTS:
            check = (self.current.tile_x+i, self.current.tile_y+j)
            for block in self.blocks:
                if check == block.location:
                    check = block
            
            if check not in self.closed_list:   
                if check not in self.walls:
                    self.neighbors.append(check)

            

            
            for block in self.neighbors:
                block.parent = self.current
                #self.AssignNeighbors(check)
        
            self.closed_list.append(self.current) 

    """
    def AssignNeighbors(self, check):   
       

        for block in self.tiles:
            if check == (block.tile_x, block.tile_y):
                self.neighbors.append(block)
                block.parent = self.current
                self.neighbors.remove(check)
        for block in self.walls:
            if check == (block.tile_x, block.tile_y):
                self.neighbors.remove(check)
                self.closed_list.append(block)
    """

    def beginSearch(self):
        lowestFx = self.current
        lowestFxNum = 1000
        for block in self.neighbors:
            if block not in self.open_list:
                self.open_list.append(block)
            
            x = abs(self.end.tile_x - block.tile_x)
            y = abs(self.end.tile_y - block.tile_y)
            x = x * 10
            y = y * 10
            block.hx = x + y

            Sx = block.tile_x
            Sy = block.tile_y
            
            if self.current.tile_x != Sx and self.current.tile_y != Sy:
                block.gx = block.parent.gx + 14
            if self.current.tile_x != Sx and self.current.tile_y == Sy:
                block.gx = block.parent.gx + 10
            if self.current.tile_y != Sy and self.current.tile_x == Sx:
                block.gx = block.parent.gx + 10
            block.fx = block.gx + block.hx
        
        for block in self.open_list:
            if block.fx < lowestFxNum:
                lowestFxNum = block.fx
                lowestFx = block
        self.open_list.remove(lowestFx)
        self.current = lowestFx
        #print "neighbors " + str(len(self.neighbors))
        #print "open " + str(len(self.open_list))
        #print "closed " + str(len(self.closed_list))
        if self.end in self.closed_list:
            self.found_end = True
            
            
            previous = self.end
            while self.start not in self.path:
                parent = previous.parent
                previous = parent
                self.path.append(parent)
