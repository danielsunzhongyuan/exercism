NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

class Robot(object):
    def __init__(self, direction=NORTH, start_x=0, start_y=0):
        self._bearing = direction
        self._coordinates = [start_x, start_y]

    def simulate(self, orders):
        for action in list(orders):
            if "L" == action:
                self.turn_left()
            elif "R" == action:
                self.turn_right()
            elif "A" == action:
                self.advance()
            else:
                continue

    @property
    def coordinates(self):
        return (self._coordinates[0], self._coordinates[1])

    @coordinates.setter
    def coordinates(self, x, y):
        self._coordinates = (x, y)

    @property
    def bearing(self):
        return self._bearing

    @bearing.setter
    def bearing(self, direction):
        self._bearing = direction

    def turn_left(self):
        self._bearing = (self._bearing + 3) % 4
    
    def turn_right(self):
        self._bearing = (self._bearing + 1) % 4

    def advance(self):
        if self._bearing == NORTH:
            self._coordinates[1] += 1
        elif self._bearing == WEST:
            self._coordinates[0] -= 1
        elif self._bearing == EAST:
            self._coordinates[0] += 1
        elif self._bearing == SOUTH:
            self._coordinates[1] -= 1
        else:
            return

