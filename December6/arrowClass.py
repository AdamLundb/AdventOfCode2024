class arrow:
    def __init__(self, x, y):
        self.x_loc = x
        self.y_loc = y
        self.facing = "^"
        self.stepsMoved = 0
        self.locationsVisited = []
        self.LastLocationsVisited = []
        self.checkedObstacleLocation = []
        self.obstacle_that_caused_loop = []
        self.currentCoordinateWhereObstaclePlace = (-1, -1)
        self.x_start = x
        self.y_start = y
    def set_arrow_to_start(self):
        self.x_loc = self.x_start
        self.y_loc = self.y_start

    def get_current_location(self):
        return (self.x_loc, self.y_loc)

    def leave(self):
        self.facing = "outside map"

    def move(self):
        match self.facing:
            case "^":
                self.move_up()
            case ">":
                self.move_right()
            case "v":
                self.move_down()
            case "<":
                self.move_left()
    
    def turn(self):
        match self.facing:
            case "^":
                self.facing = ">"
            case ">":
                self.facing = "v"
            case "v":
                self.facing = "<"
            case "<":
                self.facing = "^"
    def check_if_location_visited(self, x, y):
        self.locationsVisited.append((x,y))
        for i in range(len(self.locationsVisited)):
            if(self.locationsVisited[i] == (x, y)):
                return
        self.stepsMoved += 1
    
    def move_up(self):
        self.y_loc -= 1
        self.check_if_location_visited(self.x_loc, self.y_loc)
    def move_down(self):
        self.y_loc += 1
        self.check_if_location_visited(self.x_loc, self.y_loc)
    def move_left(self):
        self.x_loc -= 1
        self.check_if_location_visited(self.x_loc, self.y_loc)
    def move_right(self):
        self.x_loc += 1
        self.check_if_location_visited(self.x_loc, self.y_loc)
    
    def next_step(self):
        match self.facing:
            case "^":
                return (self.x_loc, self.y_loc - 1)
            case ">":
                return (self.x_loc + 1, self.y_loc)
            case "v":
                return (self.x_loc, self.y_loc + 1)
            case "<":
                return (self.x_loc - 1, self.y_loc)