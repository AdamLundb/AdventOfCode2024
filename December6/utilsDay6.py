import time

def find_arrow_location(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if(map[i][j] == "^"):
                return j, i

def check_surroundings(arrow, x, y, map):
    try:
        match arrow.facing:
            case "^":
                if(y - 1 < 0):
                    return "outside + leave"
                if(map[y - 1][x] == "#"):
                    return "turn"
                else:
                    return "move"
            case ">":
                if(map[y][x + 1] == "#"):
                    return "turn"
                else:
                    return "move"
            case "v":
                if(map[y + 1][x] == "#"):
                    return "turn"
                else:
                    return "move"
            case "<":
                if(x - 1 < 0):
                    return "outside + leave"
                if(map[y][x - 1] == "#"):
                    return "turn"
                else:
                    return "move"
    except IndexError:
        return "outside"

def print_map(map):
    for i in range(len(map)):
        ''.join(map[i])
        print(map[i])
        map[i] = list(map[i])

def update_map_arrow_move(arrow, map, setting):
    current_pos = arrow.get_current_location()
    next_pos = arrow.next_step()
    try:
        if(setting == "turn"):
            map[current_pos[1]][current_pos[0]] = arrow.facing
        if(setting == "move"):
            map[current_pos[1]][current_pos[0]] = '.'
            map[next_pos[1]][next_pos[0]] = arrow.facing
        print_map(map)
    except:
        print_map(map)
    
def determine_action(arrow, map):
    current_pos = (arrow.x_loc, arrow.y_loc)
    if(check_surroundings(arrow, current_pos[0], current_pos[1], map) == "turn"):
        arrow.turn()
        update_map_arrow_move(arrow, map, "turn")
    elif(check_surroundings(arrow, current_pos[0], current_pos[1], map) == "move"):
        update_map_arrow_move(arrow, map, "move")
        arrow.move()
    elif(check_surroundings(arrow, current_pos[0], current_pos[1], map) == "outside + leave"):
        arrow.stepsMoved += 1
        print(arrow.x_loc, arrow.y_loc)
        arrow.leave()
    else:
        arrow.leave()

def calculate_steps(arrow, map):
    while arrow.facing != "outside map":
        determine_action(arrow, map)
    return arrow.stepsMoved

def check_if_obstacle_has_been_placed(arrow, coordinate):
    for i in range(len(arrow.checkedObstacleLocation)):
        if(coordinate == arrow.checkedObstacleLocation[i]):
            return True
    return False

def check_if_visited_twice(arrow, coordinate):
    k = 0
    for i in range(len(arrow.locationsVisited)):
        if(coordinate == arrow.locationsVisited[i]):
            k += 1
        if(k == 2):
            return True
    return False

def place_obstacle(arrow, map):
    if(check_if_obstacle_has_been_placed(arrow, arrow.next_step()) == False):
        next_step = arrow.next_step()
        map[next_step[1]][next_step[0]] = '#'
        print_map(map)
        arrow.currentCoordinateWhereObstaclePlace = arrow.next_step()
        arrow.checkedObstacleLocation.append(arrow.next_step())
        arrow.locationsVisited.clear()

def reset_map(arrow, map):
    map[arrow.currentCoordinateWhereObstaclePlace[1]][arrow.currentCoordinateWhereObstaclePlace[0]] = '.'
    arrow.set_arrow_to_start()
    arrow.currentCoordinateWhereObstaclePlace = (-1,-1)


def check_possible_loops(arrow, map):
    while arrow.facing != "no more loops":
        coordinate = arrow.get_current_location()
        print(coordinate)
        print(check_if_obstacle_has_been_placed(arrow, arrow.next_step()), arrow.currentCoordinateWhereObstaclePlace)
        if(check_if_obstacle_has_been_placed(arrow, arrow.next_step()) == False and arrow.currentCoordinateWhereObstaclePlace == (-1, -1)):
            print("Placing obstacle")
            place_obstacle(arrow, map)
        if(arrow.LastLocationsVisited == arrow.locationsVisited and arrow.LastLocationsVisited != []):
            arrow.facing = "no more loops"
            break
        if(check_surroundings(arrow, coordinate[0], coordinate[1], map) == "outside + leave" or 
           check_surroundings(arrow, coordinate[0], coordinate[1], map) == "outside"):
            arrow.LastLocationsVisited = arrow.locationsVisited[:]
            reset_map(arrow, map)
        determine_action(arrow, map)
        if(check_if_visited_twice(arrow, coordinate) == True):
            arrow.obstacle_that_caused_loop.append(arrow.currentCoordinateWhereObstaclePlace)
            reset_map(arrow, map)
        time.sleep(1)
    return len(arrow.obstacle_that_caused_loop)