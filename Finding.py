import Globals as gb

ADJACENTS = ((1,0), (-1,0), (0,1), (0,-1), (1,1), (1, -1), (-1, 1), (-1, -1))

class Finding():
    def __init__(self, start_block, end_block, blocks):
        self.start = start_block
        self.current = self.start
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

            if check not in self.walls and check not in self.closed_list:
                if check not in self.open_list:
                    self.open_list.append(check)
                    check.parent = self.current
                
            if self.current in self.open_list:
                self.open_list.remove(self.current)
            
            self.closed_list.append(self.current)


    def getCost(self, block):
        x = abs(block.tile_x - self.end.tile_x)
        y = abs(block.tile_y - self.end.tile_y)
        x,y = x * 10, y * 10
        
        block.hx = x + y

        Sx = block.tile_x
        Sy = block.tile_y
        if self.current.tile_x != Sx and self.current.tile_y != Sy:
            block.gx = block.parent.gx + 14
        if self.current.tile_x != Sx and self.current.tile_y == Sy:
            block.gx = block.parent.gx + 10
        if self.current.tile_x != Sy and self.current.tile_x == Sx:
            block.gx = block.parent.gx + 10

        block.fx = block.hx + block.gx

    

    def beginSearch(self):
        lowestFx = None
        fx = 10000
        for block in self.open_list:
            self.getCost(block)
            if block.fx < fx:
                lowestFx = block
                fx = lowestFx.fx
        self.open_list.remove(lowestFx)
        self.closed_list.append(lowestFx)
        self.current = lowestFx
        
        if self.end in self.closed_list:
            previous = self.end
            while self.start not in self.path:
                parent = previous.parent
                previous = parent
                self.path.append(parent)

        
