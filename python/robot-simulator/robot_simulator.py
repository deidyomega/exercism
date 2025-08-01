# Globals for the bearings
# Change the values as you see fit
EAST = 1
NORTH = 0
WEST = 3
SOUTH = 2

class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.x = x
        self.y = y
    
    def simulate(self, sim):
        actions = {
            "R": self.turn_right,
            "L": self.turn_left,
            "A": self.advance,
        }
        for item in sim:
            actions[item]()

    def turn_right(self):
        self.bearing = (self.bearing + 1) % 4
    
    def turn_left(self):
        self.bearing = (self.bearing - 1) % 4
    
    def advance(self):
        if self.bearing == NORTH:
            self.y += 1
        if self.bearing == SOUTH:
            self.y -= 1
        if self.bearing == EAST:
            self.x += 1
        if self.bearing == WEST:
            self.x -= 1

    @property
    def coordinates(self):
        return (self.x, self.y)

