import Globals as gb

ADJACENTS = ((1,0), (-1,0), (0,1), (0,-1), (1,1), (1, -1), (-1, 1), (-1, -1))

class Finding():
    def __init__(self, start_block, end_block, blocks):
        self.current = start_block
        self.end = end_block
        self.open_list = []
        self.closed_list = []
        self.neighbors = []
        self.walls = []
        self.tiles = []
        self.parseWalls(blocks)
        self.getNeighbors()
        self.beginSearch()
        self.hxCount = 0
    def parseWalls(self, blocks):
        for block in blocks:
            if block.is_wall == True:
                self.walls.append(block)
            else:
                self.tiles.append(block)
    def getNeighbors(self):
        for (i, j) in ADJACENTS:
            check = (self.current.tile_x+i, self.current.tile_y+j)
            if check not in (self.closed_list, self.walls):
                
                self.neighbors.append(check)
                self.AssignNeighbors(check)
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


    def beginSearch(self):        
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
            print min()
