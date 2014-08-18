import Globals as gb

ADJACENTS = ((1,0), (-1,0), (0,1), (0,-1), (1,1), (1, -1), (-1, 1), (-1, -1))

class Finding():
    def __init__(self, start_pos, blocks):
        self.current = start_pos
        self.open_list = []
        self.closed_list = []
        self.neighbors = []
        self.walls = []
        self.parseWalls(blocks)
        self.gx = 0
        self.hx = 0
        self.fx = 0
    def parseWalls(self, blocks):
        for block in blocks:
            if block.is_wall == True:
                self.walls.append(block)
    def getNeighbors(self):
        for (i, j) in ADJACENTS:
            check = (self.current[0]+i, self.current[1]+j)
            if check not in (self.closed_list, self.walls):
                #SET PARENT
                self.neighbors.append(check)
    def beginSearch(self):
        for block in self.neighbors:
            if block not in self.open_list:
                self.open_list.append(block)
                




find = Finding((10,10), gb.maps.new_blocks)
find.getNeighbors()
print find.neighbors
